INTERNAL_HIGH = "int  1000"
NORMAL = "int  0"
INTERNAL_LOW = "int  -1000"
def getInteractorClassByName():
'''public static synchronized Class getInteractorClassByName(final String key)
'''
pass
def getShortName():
'''public static synchronized String getShortName(final Class clazz)
'''
pass
def create():
'''public static IlvChartInteractor create(final String s)
public static IlvChartInteractor create(final String s, final boolean b)
'''
pass
def getRegisteredInteractorsByName():
'''public static synchronized String[] getRegisteredInteractorsByName()
'''
pass
def getLocalizedName():
'''public static String getLocalizedName(final Class clazz, final Locale locale)
'''
pass
def IlvChartInteractor():
'''public IlvChartInteractor()
public IlvChartInteractor(final int h, final int i)
'''
pass
def getPriority():
'''public final int getPriority()
'''
pass
def setPriority():
'''public void setPriority(final int d)
'''
pass
def getXAxis():
'''public final IlvAxis getXAxis()
'''
pass
def getYAxis():
'''public final IlvAxis getYAxis()
'''
pass
def getCoordinateSystem():
'''public final IlvCoordinateSystem getCoordinateSystem()
'''
pass
def getChart():
'''public final IlvChart getChart()
'''
pass
def setChart():
'''public final void setChart(final IlvChart c)
'''
pass
def getAWTEventMask():
'''public final long getAWTEventMask()
'''
pass
def isAborted():
'''public final boolean isAborted()
'''
pass
def isInOperation():
'''public final boolean isInOperation()
'''
pass
def getYAxisIndex():
'''public final int getYAxisIndex()
'''
pass
def setYAxisIndex():
'''public void setYAxisIndex(final int h)
'''
pass
def getEventMask():
'''public final int getEventMask()
'''
pass
def getEventMaskEx():
'''public final int getEventMaskEx()
'''
pass
def setEventMask():
'''public void setEventMask(final int i)
'''
pass
def isConsumeEvents():
'''public boolean isConsumeEvents()
'''
pass
def setConsumeEvents():
'''public void setConsumeEvents(final boolean k)
'''
pass
def getGhostColor():
'''public Color getGhostColor()
'''
pass
def setGhostColor():
'''public void setGhostColor(final Color m)
'''
pass
def getXORColor():
'''public final Color getXORColor()
'''
pass
def setXORColor():
'''public void setXORColor(final Color l)
'''
pass
def isXORGhost():
'''public final boolean isXORGhost()
'''
pass
def setXORGhost():
'''public void setXORGhost(final boolean o)
'''
pass
def isHandling():
'''public boolean isHandling(final int x, final int y)
'''
pass
def getData():
'''public final IlvDoublePoint getData(final MouseEvent mouseEvent)
public final IlvDoublePoint getData(final int n, final int n2)
'''
pass
def toDisplay():
'''public final IlvDoublePoint toDisplay(final IlvDoublePoint ilvDoublePoint)
'''
pass
def processMouseEvent():
'''public void processMouseEvent(final MouseEvent mouseEvent)
'''
pass
def processMouseMotionEvent():
'''public void processMouseMotionEvent(final MouseEvent mouseEvent)
'''
pass
def processKeyEvent():
'''public void processKeyEvent(final KeyEvent keyEvent)
'''
pass
def handleExpose():
'''public void handleExpose(final Graphics graphics)
'''
pass
def interactionStarted():
'''public void interactionStarted(final IlvChartInteractor ilvChartInteractor, final MouseEvent mouseEvent)
'''
pass
def addChartInteractionListener():
'''public final void addChartInteractionListener(final ChartInteractionListener l)
'''
pass
def removeChartInteractionListener():
'''public final void removeChartInteractionListener(final ChartInteractionListener l)
'''
pass
def has3DSupport():
'''public boolean has3DSupport()
'''
pass
