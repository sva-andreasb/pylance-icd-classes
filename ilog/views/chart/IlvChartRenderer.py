BAR = "int  0"
STACKED_BAR = "int  1"
STACKED100_BAR = "int  17"
STACKED_DIVERGING_BAR = "int  24"
SUPERIMPOSED_BAR = "int  2"
AREA = "int  3"
STACKED_AREA = "int  4"
STACKED100_AREA = "int  19"
POLYLINE = "int  5"
STACKED_POLYLINE = "int  11"
STACKED100_POLYLINE = "int  18"
SCATTER = "int  6"
STAIR = "int  7"
STACKED_STAIR = "int  14"
STACKED100_STAIR = "int  20"
SUMMED_STAIR = "int  15"
BUBBLE = "int  8"
HILO = "int  9"
HILO_ARROW = "int  21"
HILO_STICK = "int  22"
CANDLE = "int  12"
HLOC = "int  13"
PIE = "int  10"
TREEMAP = "int  23"
COMBO = "int  16"
DATA_LABEL = "int  1"
Y_VALUE_LABEL = "int  2"
XY_VALUES_LABEL = "int  3"
X_VALUE_LABEL = "int  4"
PERCENT_LABEL = "int  5"
CENTERED_LABEL_LAYOUT = "int  1"
OUTSIDE_LABEL_LAYOUT = "int  2"
DEFAULT_LABEL_LAYOUT = "int  1"
DEFAULT_LABELING = "int  2"
def create():
    '''    public static IlvChartRenderer create(final String str)
    '''
def getChart():
    '''    public final IlvChart getChart()
    '''
def getPlotRect():
    '''    public final Rectangle getPlotRect()
    '''
def getClipRect():
    '''    public Rectangle getClipRect()
    '''
def isVisible():
    '''    public boolean isVisible()
    '''
def setVisible():
    '''    public void setVisible(final boolean b)
    '''
def getYAxisIdx():
    '''    public final int getYAxisIdx()
    '''
def setYAxisIdx():
    '''    public void setYAxisIdx(final int g)
    '''
def getCoordinateSystem():
    '''    public final IlvCoordinateSystem getCoordinateSystem()
    '''
def toData():
    '''    public void toData(final IlvDoublePoints ilvDoublePoints)
    '''
def toDisplay():
    '''    public void toDisplay(final IlvDoublePoints ilvDoublePoints)
    public void toDisplay(final IlvDoublePoints ilvDoublePoints, final IlvChartProjector ilvChartProjector, final Rectangle rectangle, final IlvCoordinateSystem ilvCoordinateSystem)
    '''
def getName():
    '''    public String getName()
    '''
def setName():
    '''    public void setName(final String i)
    '''
def setXShift():
    '''    public void setXShift(final double l)
    '''
def getXShift():
    '''    public double getXShift()
    '''
def isViewable():
    '''    public boolean isViewable()
    '''
def getMinDataSetCount():
    '''    public int getMinDataSetCount()
    '''
def getDataSource():
    '''    public final IlvDataSource getDataSource()
    '''
def getDataSetIndex():
    '''    public int getDataSetIndex(final IlvDataSet set)
    '''
def setDataSource():
    '''    public void setDataSource(final IlvDataSource m)
    '''
def isDisplayingDataSet():
    '''    public final boolean isDisplayingDataSet(final IlvDataSet set)
    '''
def getVirtualDataSet():
    '''    public final IlvDataSet getVirtualDataSet(final IlvDataSet set)
    '''
def setDataPoint():
    '''    public void setDataPoint(final IlvDataSet set, final int n, final double n2, final double n3)
    '''
def getStyle():
    '''    public IlvStyle getStyle(final int n)
    '''
def setStyle():
    '''    public void setStyle(final int n, final IlvStyle ilvStyle)
    '''
def getDefaultColors():
    '''    public Color[] getDefaultColors()
    '''
def getBounds():
    '''    public Rectangle2D getBounds(final IlvDataSet set, final int n, final int n2, final Rectangle2D rectangle2D)
    '''
def drawSelectionHandles():
    '''    public void drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle, final IlvDataSet set)
    public void drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle, final IlvDataSet set, final int n)
    public void drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle, final IlvObjectModelWithColumns ilvObjectModelWithColumns, final Object o)
    '''
def has3DSupport():
    '''    public boolean has3DSupport()
    '''
def getDepths():
    '''    public double[] getDepths()
    '''
def getChildCount():
    '''    public int getChildCount()
    '''
def getChildIterator():
    '''    public Iterator<IlvChartRenderer> getChildIterator()
    '''
def getChildren():
    '''    public List<IlvChartRenderer> getChildren()
    '''
def getChild():
    '''    public IlvChartRenderer getChild(final int n)
    '''
def getParent():
    '''    public IlvChartRenderer getParent()
    '''
def setParent():
    '''    public void setParent(final IlvChartRenderer j)
    '''
def getDataSetMainRenderer():
    '''    public IlvChartRenderer getDataSetMainRenderer(final IlvDataSet set)
    '''
def getDataSetMainIndex():
    '''    public int getDataSetMainIndex(final IlvDataSet set)
    '''
def addImageMapAreas():
    '''    public void addImageMapAreas(final IlvIMapDefinition ilvIMapDefinition, final List<? super IlvIMapArea> list)
    '''
def drawIntoHitmap():
    '''    public void drawIntoHitmap(final IlvChartHitmapDefinition ilvChartHitmapDefinition, final IlvChartHitmapAccumulator ilvChartHitmapAccumulator)
    '''
def collectDisplayItems():
    '''    public void collectDisplayItems(final IlvChartDataPicker ilvChartDataPicker, final ArrayList<IlvDisplayPoint> list)
    '''
def getNearestPoint():
    '''    public static IlvDisplayPoint getNearestPoint(final Iterator<IlvChartRenderer> iterator, final IlvChartDataPicker ilvChartDataPicker)
    '''
def getNearestItem():
    '''    public static IlvDisplayPoint getNearestItem(final Iterator<IlvChartRenderer> iterator, final IlvChartDataPicker ilvChartDataPicker, final double[] array)
    '''
def getDisplayItems():
    '''    public static List<IlvDisplayPoint> getDisplayItems(final Iterator<IlvChartRenderer> iterator, final IlvChartDataPicker ilvChartDataPicker)
    '''
def getDisplayItem():
    '''    public static IlvDisplayPoint getDisplayItem(final Iterator<IlvChartRenderer> iterator, final IlvChartDataPicker ilvChartDataPicker)
    '''
def getLegendText():
    '''    public String getLegendText(final IlvLegendItem ilvLegendItem)
    '''
def getDefaultLegendTitle():
    '''    public String getDefaultLegendTitle()
    '''
def getLegendStyle():
    '''    public IlvStyle getLegendStyle()
    '''
def getPreferredMargins():
    '''    public Insets getPreferredMargins()
    '''
def triggerChange():
    '''    public void triggerChange(final int n)
    '''
def isVisibleInLegend():
    '''    public boolean isVisibleInLegend()
    '''
def setVisibleInLegend():
    '''    public void setVisibleInLegend(final boolean b)
    '''
def getDataLabeling():
    '''    public int getDataLabeling()
    '''
def getDataLabelling():
    '''    public int getDataLabelling()
    '''
def setDataLabeling():
    '''    public void setDataLabeling(final int value)
    '''
def setDataLabelling():
    '''    public void setDataLabelling(final int dataLabeling)
    '''
def getDataLabelLayout():
    '''    public int getDataLabelLayout()
    '''
def setDataLabelLayout():
    '''    public void setDataLabelLayout(final int value)
    '''
def getAnnotation():
    '''    public final IlvDataAnnotation getAnnotation()
    '''
def setAnnotation():
    '''    public void setAnnotation(final IlvDataAnnotation o)
    '''
def getRenderingHint():
    '''    public final IlvDataRenderingHint getRenderingHint()
    '''
def setRenderingHint():
    '''    public void setRenderingHint(final IlvDataRenderingHint p)
    '''
def computeDataLabel():
    '''    public String computeDataLabel(final IlvDataSetPoint ilvDataSetPoint)
    '''
def computeDataLabelLocation():
    '''    public Point computeDataLabelLocation(final IlvDisplayPoint ilvDisplayPoint, final Dimension dimension)
    '''
def applyStyles():
    '''    public void applyStyles(final boolean b)
    public static IlvDataSetStyle applyStyles(final IlvDataSet set, final IlvChartRenderer ilvChartRenderer, final IlvChartRenderer ilvChartRenderer2, final IlvStylingSupport ilvStylingSupport, final boolean b)
    '''
def createRenderer():
    '''    public static IlvChartRenderer createRenderer(final int i)
    '''
def dispose():
    '''    public void dispose()
    '''
def dataSourceChanged():
    '''    public void dataSourceChanged(final DataSourceEvent dataSourceEvent)
    '''
def startDataSourceChanges():
    '''    public void startDataSourceChanges()
    '''
def endDataSourceChanges():
    '''    public void endDataSourceChanges()
    '''
