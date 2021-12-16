from huza.ribbon.RibbonButton import RibbonButton


def init_ribbon(self):
    heat_tab = self._ribbon.add_ribbon_tab("开始计算")
    heat_find_pane = heat_tab.add_ribbon_pane("数值模拟")
    heat_find_pane.add_ribbon_widget(RibbonButton(self.form, self.actions["szmn"], True))
    heat_find_pane.add_ribbon_widget(RibbonButton(self.form, self.actions["importmesh"], True))
    exit_panel = heat_tab.add_ribbon_pane("关闭")
    exit_panel.add_ribbon_widget(RibbonButton(self.form, self.actions["exit"], True))



    view_tab = self._ribbon.add_ribbon_tab("视图")
    view_pane = view_tab.add_ribbon_pane("视图选择")
    view_pane.add_ribbon_widget(RibbonButton(self.form, self.actions["showpara"], True))
    view_pane.add_ribbon_widget(RibbonButton(self.form, self.actions["showsetup"], True))
    view_pane.add_ribbon_widget(RibbonButton(self.form, self.actions["showinfo"], True))

    help_tab = self._ribbon.add_ribbon_tab("帮助")

    help_pane = help_tab.add_ribbon_pane("帮助选项")
    help_pane.add_ribbon_widget(RibbonButton(self.form, self.actions["help-about"], True))
    help_pane.add_ribbon_widget(RibbonButton(self.form, self.actions["help-doc"], True))
    help_pane.add_ribbon_widget(RibbonButton(self.form, self.actions["help-version"], True))