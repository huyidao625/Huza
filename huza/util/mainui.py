from PyQt5.QtWidgets import QAction, QDockWidget, QWidget


def get_extra(mainui):
    return mainui.extra


def get_action(mainui, action_name: str) -> QAction:
    if action_name in mainui.actions:
        return mainui.actions.get(action_name)
    return None


def get_dock(mainui, dock_name: str) -> QDockWidget:
    if dock_name in mainui.docks:
        return mainui.docks.get(dock_name)
    return None


def get_dock_current_ui(mainui, dock_name: str):
    if dock_name in mainui.docks:
        return mainui.docks.get(dock_name).widget().ui()
    return None


def get_dock_ui(mainui, dock_name: str, uiname: str):
    if dock_name in mainui.dockviews:
        dockviews = mainui.dockviews.get(dock_name)
        if uiname in dockviews:
            return dockviews.get(uiname).ui()
    return None


def del_dock_ui(mainui, dock_name: str, uiname: str):
    if dock_name in mainui.dockviews:
        dockviews = mainui.dockviews.get(dock_name)
        if uiname in dockviews:
            w = dockviews[uiname]
            dock = mainui.docks.get(dock_name).widget()
            if dock == w:
                get_dock(mainui, dock_name).setWidget(QWidget())
            return dockviews.pop(uiname)
