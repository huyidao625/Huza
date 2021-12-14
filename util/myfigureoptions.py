# Copyright © 2009 Pierre Raybaut
# Licensed under the terms of the MIT License
# see the Matplotlib licenses directory for a copy of the license


"""Module that provides a GUI-based editor for Matplotlib's figure options."""

import re
from copy import deepcopy

from PyQt5 import QtGui, QtWidgets
from matplotlib import cbook, cm, colors as mcolors, markers, image as mimage

from util.my_formlayout import fedit

LINESTYLES = {'-': 'Solid',
              '--': 'Dashed',
              '-.': 'DashDot',
              ':': 'Dotted',
              'None': 'None',
              }

DRAWSTYLES = {
    'default': 'Default',
    'steps-pre': 'Steps (Pre)', 'steps': 'Steps (Pre)',
    'steps-mid': 'Steps (Mid)',
    'steps-post': 'Steps (Post)'}

MARKERS = markers.MarkerStyle.markers


def apply_axes(axes, data):
    sep = (None, None)  # separator

    # Get / General
    # Cast to builtin floats as they have nicer reprs.
    xmin, xmax = map(float, axes.get_xlim())
    ymin, ymax = map(float, axes.get_ylim())
    general = [('Title', axes.get_title()),
               sep,
               (None, "<b>X-Axis</b>"),
               ('Left', xmin), ('Right', xmax),
               ('Label', axes.get_xlabel()),
               ('Scale', [axes.get_xscale(), 'linear', 'log', 'logit']),
               sep,
               (None, "<b>Y-Axis</b>"),
               ('Bottom', ymin), ('Top', ymax),
               ('Label', axes.get_ylabel()),
               ('Scale', [axes.get_yscale(), 'linear', 'log', 'logit']),
               sep,
               ('(Re-)Generate automatic legend', True),
               ]

    # Save the unit data
    xconverter = axes.xaxis.converter
    yconverter = axes.yaxis.converter
    xunits = axes.xaxis.get_units()
    yunits = axes.yaxis.get_units()

    # Sorting for default labels (_lineXXX, _imageXXX).
    def cmp_key(label):
        match = re.match(r"(_line|_image)(\d+)", label)
        if match:
            return match.group(1), int(match.group(2))
        else:
            return label, 0

    # Get / Curves
    linedict = {}
    for line in axes.get_lines():
        label = line.get_label()
        if label == '_nolegend_':
            continue
        linedict[label] = line
    curves = []

    def prepare_data(d, init):
        """
        Prepare entry for FormLayout.

        *d* is a mapping of shorthands to style names (a single style may
        have multiple shorthands, in particular the shorthands `None`,
        `"None"`, `"none"` and `""` are synonyms); *init* is one shorthand
        of the initial style.

        This function returns an list suitable for initializing a
        FormLayout combobox, namely `[initial_name, (shorthand,
        style_name), (shorthand, style_name), ...]`.
        """
        if init not in d:
            d = {**d, init: str(init)}
        # Drop duplicate shorthands from dict (by overwriting them during
        # the dict comprehension).
        name2short = {name: short for short, name in d.items()}
        # Convert back to {shorthand: name}.
        short2name = {short: name for name, short in name2short.items()}
        # Find the kept shorthand for the style specified by init.
        canonical_init = name2short[d[init]]
        # Sort by representation and prepend the initial value.
        return ([canonical_init] +
                sorted(short2name.items(),
                       key=lambda short_and_name: short_and_name[1]))

    curvelabels = sorted(linedict, key=cmp_key)
    for label in curvelabels:
        line = linedict[label]
        color = mcolors.to_hex(
            mcolors.to_rgba(line.get_color(), line.get_alpha()),
            keep_alpha=True)
        ec = mcolors.to_hex(
            mcolors.to_rgba(line.get_markeredgecolor(), line.get_alpha()),
            keep_alpha=True)
        fc = mcolors.to_hex(
            mcolors.to_rgba(line.get_markerfacecolor(), line.get_alpha()),
            keep_alpha=True)
        curvedata = [
            ('Label', label),
            sep,
            (None, '<b>Line</b>'),
            ('Line style', prepare_data(LINESTYLES, line.get_linestyle())),
            ('Draw style', prepare_data(DRAWSTYLES, line.get_drawstyle())),
            ('Width', line.get_linewidth()),
            ('Color (RGBA)', color),
            sep,
            (None, '<b>Marker</b>'),
            ('Style', prepare_data(MARKERS, line.get_marker())),
            ('Size', line.get_markersize()),
            ('Face color (RGBA)', fc),
            ('Edge color (RGBA)', ec)]
        curves.append([curvedata, label, ""])
    # Is there a curve displayed?
    has_curve = bool(curves)

    # Get ScalarMappables.
    mappabledict = {}
    for mappable in [*axes.images, *axes.collections]:
        label = mappable.get_label()
        if label == '_nolegend_' or mappable.get_array() is None:
            continue
        mappabledict[label] = mappable
    mappablelabels = sorted(mappabledict, key=cmp_key)
    mappables = []
    cmaps = [(cmap, name) for name, cmap in sorted(cm._cmap_registry.items())]
    for label in mappablelabels:
        mappable = mappabledict[label]
        cmap = mappable.get_cmap()
        if cmap not in cm._cmap_registry.values():
            cmaps = [(cmap, cmap.name), *cmaps]
        low, high = mappable.get_clim()
        mappabledata = [
            ('Label', label),
            ('Colormap', [cmap.name] + cmaps),
            ('Min. value', low),
            ('Max. value', high),
        ]
        if hasattr(mappable, "get_interpolation"):  # Images.
            interpolations = [
                (name, name) for name in sorted(mimage.interpolations_names)]
            mappabledata.append((
                'Interpolation',
                [mappable.get_interpolation(), *interpolations]))
        mappables.append([mappabledata, label, ""])
    # Is there a scalarmappable displayed?
    has_sm = bool(mappables)

    datalist = [(general, "Axes", "")]
    if curves:
        datalist.append((curves, "Curves", ""))
    if mappables:
        datalist.append((mappables, "Images, etc.", ""))

    orig_xlim = axes.get_xlim()
    orig_ylim = axes.get_ylim()

    general = data.pop(0)
    curves = data.pop(0) if has_curve else []
    mappables = data.pop(0) if has_sm else []
    if data:
        raise ValueError("Unexpected field")

    # Set / General
    (title, xmin, xmax, xlabel, xscale, ymin, ymax, ylabel, yscale,
     generate_legend) = general

    if axes.get_xscale() != xscale:
        axes.set_xscale(xscale)
    if axes.get_yscale() != yscale:
        axes.set_yscale(yscale)

    axes.set_title(title)
    axes.set_xlim(xmin, xmax)
    axes.set_xlabel(xlabel)
    axes.set_ylim(ymin, ymax)
    axes.set_ylabel(ylabel)

    # Restore the unit data
    axes.xaxis.converter = xconverter
    axes.yaxis.converter = yconverter
    axes.xaxis.set_units(xunits)
    axes.yaxis.set_units(yunits)
    axes.xaxis._update_axisinfo()
    axes.yaxis._update_axisinfo()

    # Set / Curves
    for index, curve in enumerate(curves):
        line = linedict[curvelabels[index]]
        (label, linestyle, drawstyle, linewidth, color, marker, markersize,
         markerfacecolor, markeredgecolor) = curve
        line.set_label(label)
        line.set_linestyle(linestyle)
        line.set_drawstyle(drawstyle)
        line.set_linewidth(linewidth)
        rgba = mcolors.to_rgba(color)
        line.set_alpha(None)
        line.set_color(rgba)
        if marker != 'none':
            line.set_marker(marker)
            line.set_markersize(markersize)
            line.set_markerfacecolor(markerfacecolor)
            line.set_markeredgecolor(markeredgecolor)

    # Set ScalarMappables.
    for index, mappable_settings in enumerate(mappables):
        mappable = mappabledict[mappablelabels[index]]
        if len(mappable_settings) == 5:
            label, cmap, low, high, interpolation = mappable_settings
            mappable.set_interpolation(interpolation)
        elif len(mappable_settings) == 4:
            label, cmap, low, high = mappable_settings
        mappable.set_label(label)
        mappable.set_cmap(cm.get_cmap(cmap))
        mappable.set_clim(*sorted([low, high]))

    # re-generate legend, if checkbox is checked
    figure = axes.get_figure()
    if generate_legend:
        draggable = None
        ncol = 1
        if axes.legend_ is not None:
            old_legend = axes.get_legend()
            draggable = old_legend._draggable is not None
            ncol = old_legend._ncol
        new_legend = axes.legend(ncol=ncol, loc='upper right', shadow=True)
        if new_legend:
            new_legend.set_draggable(draggable)

        lined = {}
        for legline, origline in zip(new_legend.get_lines(), axes.get_lines()):
            legline.set_picker(True)
            legline.set_pickradius(6)
            lined[legline] = origline

        def on_pick(event):
            legline = event.artist
            origline = lined[legline]
            visible = not origline.get_visible()
            origline.set_visible(visible)
            legline.set_alpha(1.0 if visible else 0.2)
            figure.canvas.draw()

    # Redraw

    figure.canvas.draw()
    figure.canvas.mpl_connect('pick_event', on_pick)
    if not (axes.get_xlim() == orig_xlim and axes.get_ylim() == orig_ylim):
        figure.canvas.toolbar.push_current()


def figure_edit(axes, parent=None):
    """Edit matplotlib figure options"""
    sep = (None, None)  # separator

    # Get / General
    # Cast to builtin floats as they have nicer reprs.
    xmin, xmax = map(float, axes.get_xlim())
    ymin, ymax = map(float, axes.get_ylim())
    general = [('Title', axes.get_title()),
               ('Title Font Size', 12),
               sep,
               (None, "<b>X-Axis</b>"),
               ('Left', xmin), ('Right', xmax),
               ('Label', axes.get_xlabel()),
               ('Label Font Size', 10),
               ('Scale', [axes.get_xscale(), 'linear', 'log', 'logit']),
               sep,
               (None, "<b>Y-Axis</b>"),
               ('Bottom', ymin), ('Top', ymax),
               ('Label', axes.get_ylabel()),
               ('Label Font Size', 10),
               ('Scale', [axes.get_yscale(), 'linear', 'log', 'logit']),
               sep,
               ('(Re-)Generate automatic legend', True),
               ]

    # Save the unit data
    xconverter = axes.xaxis.converter
    yconverter = axes.yaxis.converter
    xunits = axes.xaxis.get_units()
    yunits = axes.yaxis.get_units()

    # Sorting for default labels (_lineXXX, _imageXXX).
    def cmp_key(label):
        match = re.match(r"(_line|_image)(\d+)", label)
        if match:
            return match.group(1), int(match.group(2))
        else:
            return label, 0

    # Get / Curves
    linedict = {}
    for line in axes.get_lines():
        label = line.get_label()
        if label == '_nolegend_':
            continue
        linedict[label] = line
    curves = []

    def prepare_data(d, init):
        """
        Prepare entry for FormLayout.

        *d* is a mapping of shorthands to style names (a single style may
        have multiple shorthands, in particular the shorthands `None`,
        `"None"`, `"none"` and `""` are synonyms); *init* is one shorthand
        of the initial style.

        This function returns an list suitable for initializing a
        FormLayout combobox, namely `[initial_name, (shorthand,
        style_name), (shorthand, style_name), ...]`.
        """
        if init not in d:
            d = {**d, init: str(init)}
        # Drop duplicate shorthands from dict (by overwriting them during
        # the dict comprehension).
        name2short = {name: short for short, name in d.items()}
        # Convert back to {shorthand: name}.
        short2name = {short: name for name, short in name2short.items()}
        # Find the kept shorthand for the style specified by init.
        canonical_init = name2short[d[init]]
        # Sort by representation and prepend the initial value.
        return ([canonical_init] +
                sorted(short2name.items(),
                       key=lambda short_and_name: short_and_name[1]))

    curvelabels = sorted(linedict, key=cmp_key)
    for label in curvelabels:
        line = linedict[label]
        color = mcolors.to_hex(
            mcolors.to_rgba(line.get_color(), line.get_alpha()),
            keep_alpha=True)
        ec = mcolors.to_hex(
            mcolors.to_rgba(line.get_markeredgecolor(), line.get_alpha()),
            keep_alpha=True)
        fc = mcolors.to_hex(
            mcolors.to_rgba(line.get_markerfacecolor(), line.get_alpha()),
            keep_alpha=True)
        curvedata = [
            ('Label', label),
            sep,
            (None, '<b>Line</b>'),
            ('Line style', prepare_data(LINESTYLES, line.get_linestyle())),
            ('Draw style', prepare_data(DRAWSTYLES, line.get_drawstyle())),
            ('Width', line.get_linewidth()),
            ('Color (RGBA)', color),
            sep,
            (None, '<b>Marker</b>'),
            ('Style', prepare_data(MARKERS, line.get_marker())),
            ('Size', line.get_markersize()),
            ('Face color (RGBA)', fc),
            ('Edge color (RGBA)', ec)]
        curves.append([curvedata, label, ""])
    # Is there a curve displayed?
    has_curve = bool(curves)

    # Get ScalarMappables.
    mappabledict = {}
    for mappable in [*axes.images, *axes.collections]:
        label = mappable.get_label()
        if label == '_nolegend_' or mappable.get_array() is None:
            continue
        mappabledict[label] = mappable
    mappablelabels = sorted(mappabledict, key=cmp_key)
    mappables = []
    cmaps = [(cmap, name) for name, cmap in sorted(cm._cmap_registry.items())]
    for label in mappablelabels:
        mappable = mappabledict[label]
        cmap = mappable.get_cmap()
        if cmap not in cm._cmap_registry.values():
            cmaps = [(cmap, cmap.name), *cmaps]
        low, high = mappable.get_clim()
        mappabledata = [
            ('Label', label),
            ('Colormap', [cmap.name] + cmaps),
            ('Min. value', low),
            ('Max. value', high),
        ]
        if hasattr(mappable, "get_interpolation"):  # Images.
            interpolations = [
                (name, name) for name in sorted(mimage.interpolations_names)]
            mappabledata.append((
                'Interpolation',
                [mappable.get_interpolation(), *interpolations]))
        mappables.append([mappabledata, label, ""])
    # Is there a scalarmappable displayed?
    has_sm = bool(mappables)

    datalist = [(general, "Axes", "")]
    if curves:
        datalist.append((curves, "Curves", ""))
    if mappables:
        datalist.append((mappables, "Images, etc.", ""))

    def apply_callback(data):
        """A callback to apply changes."""
        orig_xlim = axes.get_xlim()
        orig_ylim = axes.get_ylim()

        general = data.pop(0)
        curves = data.pop(0) if has_curve else []
        mappables = data.pop(0) if has_sm else []
        if data:
            raise ValueError("Unexpected field")

        # Set / General
        (title, title_font, xmin, xmax, xlabel, x_size, xscale, ymin, ymax, ylabel, y_size, yscale,
         generate_legend) = general

        if axes.get_xscale() != xscale:
            axes.set_xscale(xscale)
        if axes.get_yscale() != yscale:
            axes.set_yscale(yscale)

        axes.set_title(title, fontdict={'weight': 'normal', 'size': title_font})
        axes.set_xlim(xmin, xmax)
        axes.set_xlabel(xlabel, fontsize=x_size)
        axes.set_ylim(ymin, ymax)
        axes.set_ylabel(ylabel, fontsize=y_size)

        # Restore the unit data
        axes.xaxis.converter = xconverter
        axes.yaxis.converter = yconverter
        axes.xaxis.set_units(xunits)
        axes.yaxis.set_units(yunits)
        axes.xaxis._update_axisinfo()
        axes.yaxis._update_axisinfo()

        # Set / Curves
        for index, curve in enumerate(curves):
            line = linedict[curvelabels[index]]
            (label, linestyle, drawstyle, linewidth, color, marker, markersize,
             markerfacecolor, markeredgecolor) = curve
            line.set_label(label)
            line.set_linestyle(linestyle)
            line.set_drawstyle(drawstyle)
            line.set_linewidth(linewidth)
            rgba = mcolors.to_rgba(color)
            line.set_alpha(None)
            line.set_color(rgba)
            if marker != 'none':
                line.set_marker(marker)
                line.set_markersize(markersize)
                line.set_markerfacecolor(markerfacecolor)
                line.set_markeredgecolor(markeredgecolor)

        # Set ScalarMappables.
        for index, mappable_settings in enumerate(mappables):
            mappable = mappabledict[mappablelabels[index]]
            if len(mappable_settings) == 5:
                label, cmap, low, high, interpolation = mappable_settings
                mappable.set_interpolation(interpolation)
            elif len(mappable_settings) == 4:
                label, cmap, low, high = mappable_settings
            mappable.set_label(label)
            mappable.set_cmap(cm.get_cmap(cmap))
            mappable.set_clim(*sorted([low, high]))

        # re-generate legend, if checkbox is checked
        figure = axes.get_figure()
        if generate_legend:
            draggable = None
            ncol = 1
            if axes.legend_ is not None:
                old_legend = axes.get_legend()
                draggable = old_legend._draggable is not None
                ncol = old_legend._ncol
            new_legend = axes.legend(ncol=ncol, loc='upper right', shadow=True)
            if new_legend:
                new_legend.set_draggable(draggable)

            lined = {}
            for legline, origline in zip(new_legend.get_lines(), axes.get_lines()):
                legline.set_picker(True)
                legline.set_pickradius(6)
                lined[legline] = origline

            def on_pick(event):
                legline = event.artist
                origline = lined[legline]
                visible = not origline.get_visible()
                origline.set_visible(visible)
                legline.set_alpha(1.0 if visible else 0.2)
                figure.canvas.draw()

        # Redraw

        figure.canvas.draw()
        figure.canvas.mpl_connect('pick_event', on_pick)
        if not (axes.get_xlim() == orig_xlim and axes.get_ylim() == orig_ylim):
            figure.canvas.toolbar.push_current()

    data = fedit(
        datalist, title="Figure options", parent=parent,
        icon=QtGui.QIcon(
            str(cbook._get_data_path('images', 'qt4_editor_options.svg'))),
        apply=apply_callback)
    data_copy = deepcopy(data)
    if data is not None:
        apply_callback(data)
    return data_copy


def edit_parameters(canvas, parent):
    axes = [i for i in canvas.figure.get_axes() if len(i.lines) > 0]
    if not axes:
        QtWidgets.QMessageBox.warning(
            canvas.parent(), "Error", "There are no axes to edit.")
        return None, None
    elif len(axes) == 1:
        ax, = axes
        index = 0
    else:
        titles = [
            ax.get_label() or
            ax.get_title() or
            " - ".join(filter(None, [ax.get_xlabel(), ax.get_ylabel()])) or
            f"<anonymous {type(ax).__name__}>"
            for ax in axes]
        duplicate_titles = [
            title for title in titles if titles.count(title) > 1]
        for i, ax in enumerate(axes):
            if titles[i] in duplicate_titles:
                titles[i] += f" (id: {id(ax):#x})"  # Deduplicate titles.
        item, ok = QtWidgets.QInputDialog.getItem(
            canvas.parent(),
            'Customize', 'Select axes:', titles, 0, False)
        if not ok:
            return None, None
        ax = axes[titles.index(item)]
        index = titles.index(item)
    data = figure_edit(ax, parent)
    return index, data  # index , data
