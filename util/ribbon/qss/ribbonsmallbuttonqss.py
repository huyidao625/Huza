ribbonsmallbuttonqss="""QToolButton {
    text-align: left;
    border: 1px solid transparent;
    margin:2px;
}

QToolButton:hover {
    border: 1px solid rgba(120,160,255,60%);
    background-color: QLinearGradient(spread:pad, x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgba(150,180,200,30%),stop: 0.5 rgba(225,235,245,60%), stop: 1 rgba(225,235,245,30%));
}


QToolButton:pressed{
    border: 1px solid rgba(120,160,255,80%);
    background-color: QLinearGradient(spread:pad, x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 rgba(150,180,200,50%),stop: 0.5 rgba(225,235,245,80%), stop: 1 rgba(225,235,245,50%));
}

QToolButton:checked{
    border: 1px solid rgba(120,160,255,40%);
    background-color: rgba(0,0,0,10%)
}"""