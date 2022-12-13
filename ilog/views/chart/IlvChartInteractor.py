INTERNAL_HIGH = "int  1000"
NORMAL = "int  0"
INTERNAL_LOW = "int  -1000"
def getInteractorClassByName():
    '''    public static synchronized Class getInteractorClassByName(final String key)
    '''
def getShortName():
    '''    public static synchronized String getShortName(final Class clazz)
    '''
def create():
    '''    public static IlvChartInteractor create(final String s)
    public static IlvChartInteractor create(final String s, final boolean b)
    '''
def getRegisteredInteractorsByName():
    '''    public static synchronized String[] getRegisteredInteractorsByName()
    '''
def getLocalizedName():
    '''    public static String getLocalizedName(final Class clazz, final Locale locale)
    '''
def IlvChartInteractor():
    '''    public IlvChartInteractor()
    public IlvChartInteractor(final int h, final int i)
    '''
def getPriority():
    '''    public final int getPriority()
    '''
def setPriority():
    '''    public void setPriority(final int d)
    '''
def getXAxis():
    '''    public final IlvAxis getXAxis()
    '''
def getYAxis():
    '''    public final IlvAxis getYAxis()
    '''
def getCoordinateSystem():
    '''    public final IlvCoordinateSystem getCoordinateSystem()
    '''
def getChart():
    '''    public final IlvChart getChart()
    '''
def setChart():
    '''    public final void setChart(final IlvChart c)
    '''
def getAWTEventMask():
    '''    public final long getAWTEventMask()
    '''
def isAborted():
    '''    public final boolean isAborted()
    '''
def isInOperation():
    '''    public final boolean isInOperation()
    '''
def getYAxisIndex():
    '''    public final int getYAxisIndex()
    '''
def setYAxisIndex():
    '''    public void setYAxisIndex(final int h)
    '''
def getEventMask():
    '''    public final int getEventMask()
    '''
def getEventMaskEx():
    '''    public final int getEventMaskEx()
    '''
def setEventMask():
    '''    public void setEventMask(final int i)
    '''
def isConsumeEvents():
    '''    public boolean isConsumeEvents()
    '''
def setConsumeEvents():
    '''    public void setConsumeEvents(final boolean k)
    '''
def getGhostColor():
    '''    public Color getGhostColor()
    '''
def setGhostColor():
    '''    public void setGhostColor(final Color m)
    '''
def getXORColor():
    '''    public final Color getXORColor()
    '''
def setXORColor():
    '''    public void setXORColor(final Color l)
    '''
def isXORGhost():
    '''    public final boolean isXORGhost()
    '''
def setXORGhost():
    '''    public void setXORGhost(final boolean o)
    '''
def isHandling():
    '''    public boolean isHandling(final int x, final int y)
    '''
def getData():
    '''    public final IlvDoublePoint getData(final MouseEvent mouseEvent)
    public final IlvDoublePoint getData(final int n, final int n2)
    '''
def toDisplay():
    '''    public final IlvDoublePoint toDisplay(final IlvDoublePoint ilvDoublePoint)
    '''
def processMouseEvent():
    '''    public void processMouseEvent(final MouseEvent mouseEvent)
    '''
def processMouseMotionEvent():
    '''    public void processMouseMotionEvent(final MouseEvent mouseEvent)
    '''
def processKeyEvent():
    '''    public void processKeyEvent(final KeyEvent keyEvent)
    '''
def handleExpose():
    '''    public void handleExpose(final Graphics graphics)
    '''
def interactionStarted():
    '''    public void interactionStarted(final IlvChartInteractor ilvChartInteractor, final MouseEvent mouseEvent)
    '''
def addChartInteractionListener():
    '''    public final void addChartInteractionListener(final ChartInteractionListener l)
    '''
def removeChartInteractionListener():
    '''    public final void removeChartInteractionListener(final ChartInteractionListener l)
    '''
def has3DSupport():
    '''    public boolean has3DSupport()
    '''
