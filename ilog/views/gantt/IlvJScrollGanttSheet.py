VERTICAL_SCROLLBAR_AS_NEEDED = "int  20"
VERTICAL_SCROLLBAR_NEVER = "int  21"
VERTICAL_SCROLLBAR_ALWAYS = "int  22"
HORIZONTAL = "int  0"
VERTICAL = "int  1"
def IlvJScrollGanttSheet():
    '''public IlvJScrollGanttSheet()
    public IlvJScrollGanttSheet(final IlvGanttSheet ilvGanttSheet, final IlvTimeScale ilvTimeScale, final IlvTimeScrollBar ilvTimeScrollBar)
    public IlvJScrollGanttSheet(final IlvGanttConfiguration ilvGanttConfiguration)
    public IlvJScrollGanttSheet(final IlvGanttConfiguration ganttConfiguration, final IlvGanttSheet ilvGanttSheet, IlvTimeScale defaultTimeScale, IlvTimeScrollBar defaultTimeScrollBar)
    '''
def verticalExtentChanged():
    '''public void verticalExtentChanged(final VerticalScrollEvent verticalScrollEvent)
    '''
def maxVerticalPositionChanged():
    '''public void maxVerticalPositionChanged(final VerticalScrollEvent verticalScrollEvent)
    '''
def verticalPositionChanged():
    '''public void verticalPositionChanged(final VerticalScrollEvent verticalScrollEvent)
    '''
def setGanttConfiguration():
    '''public void setGanttConfiguration(final IlvGanttConfiguration a)
    '''
def getVerticalScrollBar():
    '''public IlvVerticalScrollBar getVerticalScrollBar()
    '''
def setVerticalScrollBar():
    '''public void setVerticalScrollBar(final JScrollBar scrollBar)
    public void setVerticalScrollBar(final IlvVerticalScrollBar g)
    '''
def getVerticalScrollBarPolicy():
    '''public int getVerticalScrollBarPolicy()
    '''
def setVerticalScrollBarPolicy():
    '''public void setVerticalScrollBarPolicy(final int i)
    '''
def getTimeScrollBar():
    '''public IlvTimeScrollBar getTimeScrollBar()
    '''
def setTimeScrollBar():
    '''public void setTimeScrollBar(final IlvTimeScrollBar f)
    '''
def isTimeScrollBarVisible():
    '''public boolean isTimeScrollBarVisible()
    '''
def setTimeScrollBarVisible():
    '''public void setTimeScrollBarVisible(final boolean visible)
    '''
def getTimeScale():
    '''public IlvTimeScale getTimeScale()
    '''
def setTimeScale():
    '''public void setTimeScale(final IlvTimeScale b)
    '''
def getGanttSheet():
    '''public IlvGanttSheet getGanttSheet()
    '''
def doLayout():
    '''public void doLayout()
    '''
def processManagerViewKeyEvent():
    '''public void processManagerViewKeyEvent(final KeyEvent e)
    '''
def getMinVisibleTime():
    '''public Date getMinVisibleTime()
    '''
def setMinVisibleTime():
    '''public void setMinVisibleTime(final Date minVisibleTime)
    '''
def getMaxVisibleTime():
    '''public Date getMaxVisibleTime()
    '''
def setMaxVisibleTime():
    '''public void setMaxVisibleTime(final Date maxVisibleTime)
    '''
def getMinVisibleDuration():
    '''public IlvDuration getMinVisibleDuration()
    '''
def setMinVisibleDuration():
    '''public void setMinVisibleDuration(final IlvDuration minVisibleDuration)
    '''
def getVisibleTime():
    '''public Date getVisibleTime()
    '''
def setVisibleTime():
    '''public void setVisibleTime(final Date visibleTime)
    '''
def getVisibleDuration():
    '''public IlvDuration getVisibleDuration()
    '''
def setVisibleDuration():
    '''public void setVisibleDuration(final IlvDuration visibleDuration)
    '''
def getVisibleInterval():
    '''public IlvTimeInterval getVisibleInterval()
    '''
def setVisibleInterval():
    '''public void setVisibleInterval(final Date date, final IlvDuration ilvDuration)
    '''
def addTimeScrollListener():
    '''public void addTimeScrollListener(final TimeScrollListener timeScrollListener)
    '''
def removeTimeScrollListener():
    '''public void removeTimeScrollListener(final TimeScrollListener timeScrollListener)
    '''
def getMaxVerticalPosition():
    '''public int getMaxVerticalPosition()
    public int getMaxVerticalPosition()
    '''
def setMaxVerticalPosition():
    '''public void setMaxVerticalPosition(final int maxVerticalPosition)
    public void setMaxVerticalPosition(final int n)
    '''
def getVerticalPosition():
    '''public int getVerticalPosition()
    public int getVerticalPosition()
    '''
def setVerticalPosition():
    '''public void setVerticalPosition(final int verticalPosition)
    public void setVerticalPosition(int min)
    '''
def getVerticalExtent():
    '''public int getVerticalExtent()
    public int getVerticalExtent()
    '''
def setVerticalExtent():
    '''public void setVerticalExtent(final int verticalExtent)
    public void setVerticalExtent(final int n)
    '''
def addVerticalScrollListener():
    '''public void addVerticalScrollListener(final VerticalScrollListener verticalScrollListener)
    public void addVerticalScrollListener(final VerticalScrollListener verticalScrollListener)
    '''
def removeVerticalScrollListener():
    '''public void removeVerticalScrollListener(final VerticalScrollListener verticalScrollListener)
    public void removeVerticalScrollListener(final VerticalScrollListener verticalScrollListener)
    '''
def isMouseWheelEnabled():
    '''public boolean isMouseWheelEnabled()
    '''
def setMouseWheelEnabled():
    '''public void setMouseWheelEnabled(final boolean b)
    '''
def getMouseWheelPreferredOrientation():
    '''public int getMouseWheelPreferredOrientation()
    '''
def setMouseWheelPreferredOrientation():
    '''public void setMouseWheelPreferredOrientation(final int k)
    '''
def getBaseTextDirection():
    '''public final int getBaseTextDirection()
    '''
def setBaseTextDirection():
    '''public void setBaseTextDirection(final int l)
    '''
def getResolvedBaseTextDirection():
    '''public int getResolvedBaseTextDirection()
    '''
def GanttSheetVerticalScrollAdapter():
    '''public GanttSheetVerticalScrollAdapter(final IlvGanttSheet a)
    '''
def transformerChanged():
    '''public void transformerChanged(final TransformerChangedEvent transformerChangedEvent)
    '''
def componentResized():
    '''public void componentResized(final ComponentEvent componentEvent)
    '''
def MouseWheelAdapter():
    '''public MouseWheelAdapter()
    '''
def mouseWheelMoved():
    '''public void mouseWheelMoved(final MouseWheelEvent mouseWheelEvent)
    '''
