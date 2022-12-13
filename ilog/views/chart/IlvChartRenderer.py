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
'''public static IlvChartRenderer create(final String str)
'''
pass
def getChart():
'''public final IlvChart getChart()
'''
pass
def getPlotRect():
'''public final Rectangle getPlotRect()
'''
pass
def getClipRect():
'''public Rectangle getClipRect()
'''
pass
def isVisible():
'''public boolean isVisible()
'''
pass
def setVisible():
'''public void setVisible(final boolean b)
'''
pass
def getYAxisIdx():
'''public final int getYAxisIdx()
'''
pass
def setYAxisIdx():
'''public void setYAxisIdx(final int g)
'''
pass
def getCoordinateSystem():
'''public final IlvCoordinateSystem getCoordinateSystem()
'''
pass
def toData():
'''public void toData(final IlvDoublePoints ilvDoublePoints)
'''
pass
def toDisplay():
'''public void toDisplay(final IlvDoublePoints ilvDoublePoints)
public void toDisplay(final IlvDoublePoints ilvDoublePoints, final IlvChartProjector ilvChartProjector, final Rectangle rectangle, final IlvCoordinateSystem ilvCoordinateSystem)
'''
pass
def getName():
'''public String getName()
'''
pass
def setName():
'''public void setName(final String i)
'''
pass
def setXShift():
'''public void setXShift(final double l)
'''
pass
def getXShift():
'''public double getXShift()
'''
pass
def isViewable():
'''public boolean isViewable()
'''
pass
def getMinDataSetCount():
'''public int getMinDataSetCount()
'''
pass
def getDataSource():
'''public final IlvDataSource getDataSource()
'''
pass
def getDataSetIndex():
'''public int getDataSetIndex(final IlvDataSet set)
'''
pass
def setDataSource():
'''public void setDataSource(final IlvDataSource m)
'''
pass
def isDisplayingDataSet():
'''public final boolean isDisplayingDataSet(final IlvDataSet set)
'''
pass
def getVirtualDataSet():
'''public final IlvDataSet getVirtualDataSet(final IlvDataSet set)
'''
pass
def setDataPoint():
'''public void setDataPoint(final IlvDataSet set, final int n, final double n2, final double n3)
'''
pass
def getStyle():
'''public IlvStyle getStyle(final int n)
'''
pass
def setStyle():
'''public void setStyle(final int n, final IlvStyle ilvStyle)
'''
pass
def getDefaultColors():
'''public Color[] getDefaultColors()
'''
pass
def getBounds():
'''public Rectangle2D getBounds(final IlvDataSet set, final int n, final int n2, final Rectangle2D rectangle2D)
'''
pass
def drawSelectionHandles():
'''public void drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle, final IlvDataSet set)
public void drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle, final IlvDataSet set, final int n)
public void drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle, final IlvObjectModelWithColumns ilvObjectModelWithColumns, final Object o)
'''
pass
def has3DSupport():
'''public boolean has3DSupport()
'''
pass
def getDepths():
'''public double[] getDepths()
'''
pass
def getChildCount():
'''public int getChildCount()
'''
pass
def getChildIterator():
'''public Iterator<IlvChartRenderer> getChildIterator()
'''
pass
def getChildren():
'''public List<IlvChartRenderer> getChildren()
'''
pass
def getChild():
'''public IlvChartRenderer getChild(final int n)
'''
pass
def getParent():
'''public IlvChartRenderer getParent()
'''
pass
def setParent():
'''public void setParent(final IlvChartRenderer j)
'''
pass
def getDataSetMainRenderer():
'''public IlvChartRenderer getDataSetMainRenderer(final IlvDataSet set)
'''
pass
def getDataSetMainIndex():
'''public int getDataSetMainIndex(final IlvDataSet set)
'''
pass
def addImageMapAreas():
'''public void addImageMapAreas(final IlvIMapDefinition ilvIMapDefinition, final List<? super IlvIMapArea> list)
'''
pass
def drawIntoHitmap():
'''public void drawIntoHitmap(final IlvChartHitmapDefinition ilvChartHitmapDefinition, final IlvChartHitmapAccumulator ilvChartHitmapAccumulator)
'''
pass
def collectDisplayItems():
'''public void collectDisplayItems(final IlvChartDataPicker ilvChartDataPicker, final ArrayList<IlvDisplayPoint> list)
'''
pass
def getNearestPoint():
'''public static IlvDisplayPoint getNearestPoint(final Iterator<IlvChartRenderer> iterator, final IlvChartDataPicker ilvChartDataPicker)
'''
pass
def getNearestItem():
'''public static IlvDisplayPoint getNearestItem(final Iterator<IlvChartRenderer> iterator, final IlvChartDataPicker ilvChartDataPicker, final double[] array)
'''
pass
def getDisplayItems():
'''public static List<IlvDisplayPoint> getDisplayItems(final Iterator<IlvChartRenderer> iterator, final IlvChartDataPicker ilvChartDataPicker)
'''
pass
def getDisplayItem():
'''public static IlvDisplayPoint getDisplayItem(final Iterator<IlvChartRenderer> iterator, final IlvChartDataPicker ilvChartDataPicker)
'''
pass
def getLegendText():
'''public String getLegendText(final IlvLegendItem ilvLegendItem)
'''
pass
def getDefaultLegendTitle():
'''public String getDefaultLegendTitle()
'''
pass
def getLegendStyle():
'''public IlvStyle getLegendStyle()
'''
pass
def getPreferredMargins():
'''public Insets getPreferredMargins()
'''
pass
def triggerChange():
'''public void triggerChange(final int n)
'''
pass
def isVisibleInLegend():
'''public boolean isVisibleInLegend()
'''
pass
def setVisibleInLegend():
'''public void setVisibleInLegend(final boolean b)
'''
pass
def getDataLabeling():
'''public int getDataLabeling()
'''
pass
def getDataLabelling():
'''public int getDataLabelling()
'''
pass
def setDataLabeling():
'''public void setDataLabeling(final int value)
'''
pass
def setDataLabelling():
'''public void setDataLabelling(final int dataLabeling)
'''
pass
def getDataLabelLayout():
'''public int getDataLabelLayout()
'''
pass
def setDataLabelLayout():
'''public void setDataLabelLayout(final int value)
'''
pass
def getAnnotation():
'''public final IlvDataAnnotation getAnnotation()
'''
pass
def setAnnotation():
'''public void setAnnotation(final IlvDataAnnotation o)
'''
pass
def getRenderingHint():
'''public final IlvDataRenderingHint getRenderingHint()
'''
pass
def setRenderingHint():
'''public void setRenderingHint(final IlvDataRenderingHint p)
'''
pass
def computeDataLabel():
'''public String computeDataLabel(final IlvDataSetPoint ilvDataSetPoint)
'''
pass
def computeDataLabelLocation():
'''public Point computeDataLabelLocation(final IlvDisplayPoint ilvDisplayPoint, final Dimension dimension)
'''
pass
def applyStyles():
'''public void applyStyles(final boolean b)
public static IlvDataSetStyle applyStyles(final IlvDataSet set, final IlvChartRenderer ilvChartRenderer, final IlvChartRenderer ilvChartRenderer2, final IlvStylingSupport ilvStylingSupport, final boolean b)
'''
pass
def createRenderer():
'''public static IlvChartRenderer createRenderer(final int i)
'''
pass
def dispose():
'''public void dispose()
'''
pass
def dataSourceChanged():
'''public void dataSourceChanged(final DataSourceEvent dataSourceEvent)
'''
pass
def startDataSourceChanges():
'''public void startDataSourceChanges()
'''
pass
def endDataSourceChanges():
'''public void endDataSourceChanges()
'''
pass
