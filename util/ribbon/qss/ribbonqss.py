ribbonqss="""QToolBar {
    padding: 0px;
}

QTabWidget::pane {
	border-radius: 0px;
	margin:0px;
	padding: 0px;
    background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #efefef, stop: 0.5 #e5e5e5, stop: 1.0 #fdfdfd);
    border-bottom: 1px solid rgba(0,0,0,20%);
    border-top: 1px solid rgba(0,0,0,20%);
    top: -1;
}
QTabWidget{

}

QTabWidget::tab-bar {
    left: 2px;
}

QTabBar::tab {
    padding-top: 4px;
    padding-bottom: 4px;
    padding-left: 12px;
    padding-right: 12px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    margin-right:5px;
    color:#2A2A2A;
 }

QTabBar::tab:hover {
    background: rgba(255, 119, 0, 20%);
}

QTabBar::tab:selected{
    background: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #fdfdfd, stop: 1.0 #efefef);
    color: #2A2A2A;

    border: 1px solid rgba(0,0,0,20%);
    border-bottom-color: #f9f9f9;
}"""