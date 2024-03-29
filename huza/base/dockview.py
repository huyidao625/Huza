from huza.icons.iconcore import IconListHandler
from huza.mainwindow import MainWindow_Form
from huza.util.mainui import *


class DockView(object):
    def __init__(self, mainui: MainWindow_Form):
        self.mainui = mainui
        self.extra = get_extra(mainui)
        self.iconlist = self.get_icon_list()  # IconListHandler

    def set_dock_view(self, name, displayname, dockname, formclass, showthisview=True):
        return self.mainui.set_dock_view(name, displayname, dockname, formclass, showthisview)

    def get_icon_list(self) -> IconListHandler:
        return self.mainui.icon_list

    def emit(self, signal, data):
        self.form.signal.emit(signal, data)

    def bind_signal(self, form: QWidget):
        form.signal.connect(self.form.signal)

    def get_extra(self):
        return get_extra(self.mainui)

    def get_action(self, action_name):
        return get_action(self.mainui, action_name)

    def get_dock(self, dock_name):
        return get_dock(self.mainui, dock_name)

    def get_all_dock(self):
        return get_all_dock(self.mainui)

    def get_all_action(self):
        return get_all_action(self.mainui)

    def get_all_dockview(self):
        return get_all_dockview(self.mainui)

    def get_dock_current_ui(self, dock_name):
        return get_dock_current_ui(self.mainui, dock_name)

    def get_dock_ui(self, dock_name, ui_name):
        return get_dock_ui(self.mainui, dock_name, ui_name)

    def get_ui(self, ui_name):
        return get_ui(self.mainui, ui_name)
