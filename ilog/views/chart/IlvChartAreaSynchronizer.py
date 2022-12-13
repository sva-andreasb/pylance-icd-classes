HORIZONTAL = "int  0"
VERTICAL = "int  1"
def IlvChartAreaSynchronizer():
    '''public IlvChartAreaSynchronizer(final int d)
    '''
def getChart():
    '''public final IlvChart getChart()
    '''
def getTargetComponent():
    '''public final Component getTargetComponent()
    '''
def plug():
    '''public void plug(final IlvChart b, final Component c)
    '''
def unplug():
    '''public void unplug()
    '''
def synchronize():
    '''public static void synchronize(final IlvChart ilvChart, final Component component)
    public static void synchronize(final IlvChart ilvChart, final Component component, final IlvChartAreaSynchronizer value)
    '''
def unSynchronize():
    '''public static IlvChartAreaSynchronizer unSynchronize(final IlvChart ilvChart)
    '''
def beforeDraw():
    '''public void beforeDraw(final ChartDrawEvent chartDrawEvent)
    '''
def afterDraw():
    '''public void afterDraw(final ChartDrawEvent chartDrawEvent)
    '''
def chartAreaChanged():
    '''public void chartAreaChanged(final ChartAreaEvent chartAreaEvent)
    '''
def componentMoved():
    '''public void componentMoved(final ComponentEvent componentEvent)
    '''
def componentResized():
    '''public void componentResized(final ComponentEvent componentEvent)
    '''
