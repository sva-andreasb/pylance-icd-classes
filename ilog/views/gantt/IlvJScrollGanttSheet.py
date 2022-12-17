VERTICAL_SCROLLBAR_AS_NEEDED = "int  20"
VERTICAL_SCROLLBAR_NEVER = "int  21"
VERTICAL_SCROLLBAR_ALWAYS = "int  22"
HORIZONTAL = "int  0"
VERTICAL = "int  1"
def ():
    '''returns MouseWheelAdapter\n\n
    ()\n
    (final IlvGanttSheet ilvGanttSheet, final IlvTimeScale ilvTimeScale, final IlvTimeScrollBar ilvTimeScrollBar)\n
    (final IlvGanttConfiguration ilvGanttConfiguration)\n
    (final IlvGanttConfiguration ganttConfiguration, final IlvGanttSheet ilvGanttSheet, IlvTimeScale defaultTimeScale, IlvTimeScrollBar defaultTimeScrollBar)\n
    (final IlvGanttSheet a)\n
    ()\n
    '''
def verticalExtentChanged():
    '''returns None\n\n
    verticalExtentChanged(final VerticalScrollEvent verticalScrollEvent)\n
    '''
def maxVerticalPositionChanged():
    '''returns None\n\n
    maxVerticalPositionChanged(final VerticalScrollEvent verticalScrollEvent)\n
    '''
def verticalPositionChanged():
    '''returns None\n\n
    verticalPositionChanged(final VerticalScrollEvent verticalScrollEvent)\n
    '''
def setGanttConfiguration():
    '''returns None\n\n
    setGanttConfiguration(final IlvGanttConfiguration a)\n
    '''
def getVerticalScrollBar():
    '''returns IlvVerticalScrollBar\n\n
    getVerticalScrollBar()\n
    '''
def setVerticalScrollBar():
    '''returns None\n\n
    setVerticalScrollBar(final JScrollBar scrollBar)\n
    setVerticalScrollBar(final IlvVerticalScrollBar g)\n
    '''
def getVerticalScrollBarPolicy():
    '''returns int\n\n
    getVerticalScrollBarPolicy()\n
    '''
def setVerticalScrollBarPolicy():
    '''returns None\n\n
    setVerticalScrollBarPolicy(final int i)\n
    '''
def getTimeScrollBar():
    '''returns IlvTimeScrollBar\n\n
    getTimeScrollBar()\n
    '''
def setTimeScrollBar():
    '''returns None\n\n
    setTimeScrollBar(final IlvTimeScrollBar f)\n
    '''
def isTimeScrollBarVisible():
    '''returns boolean\n\n
    isTimeScrollBarVisible()\n
    '''
def setTimeScrollBarVisible():
    '''returns None\n\n
    setTimeScrollBarVisible(final boolean visible)\n
    '''
def getTimeScale():
    '''returns IlvTimeScale\n\n
    getTimeScale()\n
    '''
def setTimeScale():
    '''returns None\n\n
    setTimeScale(final IlvTimeScale b)\n
    '''
def getGanttSheet():
    '''returns IlvGanttSheet\n\n
    getGanttSheet()\n
    '''
def doLayout():
    '''returns None\n\n
    doLayout()\n
    '''
def processManagerViewKeyEvent():
    '''returns None\n\n
    processManagerViewKeyEvent(final KeyEvent e)\n
    '''
def getMinVisibleTime():
    '''returns Date\n\n
    getMinVisibleTime()\n
    '''
def setMinVisibleTime():
    '''returns None\n\n
    setMinVisibleTime(final Date minVisibleTime)\n
    '''
def getMaxVisibleTime():
    '''returns Date\n\n
    getMaxVisibleTime()\n
    '''
def setMaxVisibleTime():
    '''returns None\n\n
    setMaxVisibleTime(final Date maxVisibleTime)\n
    '''
def getMinVisibleDuration():
    '''returns IlvDuration\n\n
    getMinVisibleDuration()\n
    '''
def setMinVisibleDuration():
    '''returns None\n\n
    setMinVisibleDuration(final IlvDuration minVisibleDuration)\n
    '''
def getVisibleTime():
    '''returns Date\n\n
    getVisibleTime()\n
    '''
def setVisibleTime():
    '''returns None\n\n
    setVisibleTime(final Date visibleTime)\n
    '''
def getVisibleDuration():
    '''returns IlvDuration\n\n
    getVisibleDuration()\n
    '''
def setVisibleDuration():
    '''returns None\n\n
    setVisibleDuration(final IlvDuration visibleDuration)\n
    '''
def getVisibleInterval():
    '''returns IlvTimeInterval\n\n
    getVisibleInterval()\n
    '''
def setVisibleInterval():
    '''returns None\n\n
    setVisibleInterval(final Date date, final IlvDuration ilvDuration)\n
    '''
def addTimeScrollListener():
    '''returns None\n\n
    addTimeScrollListener(final TimeScrollListener timeScrollListener)\n
    '''
def removeTimeScrollListener():
    '''returns None\n\n
    removeTimeScrollListener(final TimeScrollListener timeScrollListener)\n
    '''
def getMaxVerticalPosition():
    '''returns int\n\n
    getMaxVerticalPosition()\n
    getMaxVerticalPosition()\n
    '''
def setMaxVerticalPosition():
    '''returns None\n\n
    setMaxVerticalPosition(final int maxVerticalPosition)\n
    setMaxVerticalPosition(final int n)\n
    '''
def getVerticalPosition():
    '''returns int\n\n
    getVerticalPosition()\n
    getVerticalPosition()\n
    '''
def setVerticalPosition():
    '''returns None\n\n
    setVerticalPosition(final int verticalPosition)\n
    setVerticalPosition(int min)\n
    '''
def getVerticalExtent():
    '''returns int\n\n
    getVerticalExtent()\n
    getVerticalExtent()\n
    '''
def setVerticalExtent():
    '''returns None\n\n
    setVerticalExtent(final int verticalExtent)\n
    setVerticalExtent(final int n)\n
    '''
def addVerticalScrollListener():
    '''returns None\n\n
    addVerticalScrollListener(final VerticalScrollListener verticalScrollListener)\n
    addVerticalScrollListener(final VerticalScrollListener verticalScrollListener)\n
    '''
def removeVerticalScrollListener():
    '''returns None\n\n
    removeVerticalScrollListener(final VerticalScrollListener verticalScrollListener)\n
    removeVerticalScrollListener(final VerticalScrollListener verticalScrollListener)\n
    '''
def isMouseWheelEnabled():
    '''returns boolean\n\n
    isMouseWheelEnabled()\n
    '''
def setMouseWheelEnabled():
    '''returns None\n\n
    setMouseWheelEnabled(final boolean b)\n
    '''
def getMouseWheelPreferredOrientation():
    '''returns int\n\n
    getMouseWheelPreferredOrientation()\n
    '''
def setMouseWheelPreferredOrientation():
    '''returns None\n\n
    setMouseWheelPreferredOrientation(final int k)\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int l)\n
    '''
def getResolvedBaseTextDirection():
    '''returns int\n\n
    getResolvedBaseTextDirection()\n
    '''
def transformerChanged():
    '''returns None\n\n
    transformerChanged(final TransformerChangedEvent transformerChangedEvent)\n
    '''
def componentResized():
    '''returns None\n\n
    componentResized(final ComponentEvent componentEvent)\n
    '''
def mouseWheelMoved():
    '''returns None\n\n
    mouseWheelMoved(final MouseWheelEvent mouseWheelEvent)\n
    '''
