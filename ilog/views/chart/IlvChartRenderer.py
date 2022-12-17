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
def getClipRect():
    '''returns Rectangle\n\n
    getClipRect()\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible()\n
    '''
def setVisible():
    '''returns None\n\n
    setVisible(final boolean b)\n
    '''
def setYAxisIdx():
    '''returns None\n\n
    setYAxisIdx(final int g)\n
    '''
def toData():
    '''returns None\n\n
    toData(final IlvDoublePoints ilvDoublePoints)\n
    '''
def toDisplay():
    '''returns None\n\n
    toDisplay(final IlvDoublePoints ilvDoublePoints)\n
    toDisplay(final IlvDoublePoints ilvDoublePoints, final IlvChartProjector ilvChartProjector, final Rectangle rectangle, final IlvCoordinateSystem ilvCoordinateSystem)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String i)\n
    '''
def setXShift():
    '''returns None\n\n
    setXShift(final double l)\n
    '''
def getXShift():
    '''returns double\n\n
    getXShift()\n
    '''
def isViewable():
    '''returns boolean\n\n
    isViewable()\n
    '''
def getMinDataSetCount():
    '''returns int\n\n
    getMinDataSetCount()\n
    '''
def getDataSetIndex():
    '''returns int\n\n
    getDataSetIndex(final IlvDataSet set)\n
    '''
def setDataSource():
    '''returns None\n\n
    setDataSource(final IlvDataSource m)\n
    '''
def setDataPoint():
    '''returns None\n\n
    setDataPoint(final IlvDataSet set, final int n, final double n2, final double n3)\n
    '''
def getStyle():
    '''returns IlvStyle\n\n
    getStyle(final int n)\n
    '''
def setStyle():
    '''returns None\n\n
    setStyle(final int n, final IlvStyle ilvStyle)\n
    '''
def getDefaultColors():
    '''returns Color[]\n\n
    getDefaultColors()\n
    '''
def getBounds():
    '''returns Rectangle2D\n\n
    getBounds(final IlvDataSet set, final int n, final int n2, final Rectangle2D rectangle2D)\n
    '''
def drawSelectionHandles():
    '''returns None\n\n
    drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle, final IlvDataSet set)\n
    drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle, final IlvDataSet set, final int n)\n
    drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle, final IlvObjectModelWithColumns ilvObjectModelWithColumns, final Object o)\n
    '''
def has3DSupport():
    '''returns boolean\n\n
    has3DSupport()\n
    '''
def getDepths():
    '''returns double[]\n\n
    getDepths()\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount()\n
    '''
def getChildIterator():
    '''returns Iterator<IlvChartRenderer>\n\n
    getChildIterator()\n
    '''
def getChildren():
    '''returns List<IlvChartRenderer>\n\n
    getChildren()\n
    '''
def getChild():
    '''returns IlvChartRenderer\n\n
    getChild(final int n)\n
    '''
def getParent():
    '''returns IlvChartRenderer\n\n
    getParent()\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final IlvChartRenderer j)\n
    '''
def getDataSetMainRenderer():
    '''returns IlvChartRenderer\n\n
    getDataSetMainRenderer(final IlvDataSet set)\n
    '''
def getDataSetMainIndex():
    '''returns int\n\n
    getDataSetMainIndex(final IlvDataSet set)\n
    '''
def addImageMapAreas():
    '''returns None\n\n
    addImageMapAreas(final IlvIMapDefinition ilvIMapDefinition, final List<? super IlvIMapArea> list)\n
    '''
def drawIntoHitmap():
    '''returns None\n\n
    drawIntoHitmap(final IlvChartHitmapDefinition ilvChartHitmapDefinition, final IlvChartHitmapAccumulator ilvChartHitmapAccumulator)\n
    '''
def collectDisplayItems():
    '''returns None\n\n
    collectDisplayItems(final IlvChartDataPicker ilvChartDataPicker, final ArrayList<IlvDisplayPoint> list)\n
    '''
def getLegendText():
    '''returns String\n\n
    getLegendText(final IlvLegendItem ilvLegendItem)\n
    '''
def getDefaultLegendTitle():
    '''returns String\n\n
    getDefaultLegendTitle()\n
    '''
def getLegendStyle():
    '''returns IlvStyle\n\n
    getLegendStyle()\n
    '''
def getPreferredMargins():
    '''returns Insets\n\n
    getPreferredMargins()\n
    '''
def triggerChange():
    '''returns None\n\n
    triggerChange(final int n)\n
    '''
def isVisibleInLegend():
    '''returns boolean\n\n
    isVisibleInLegend()\n
    '''
def setVisibleInLegend():
    '''returns None\n\n
    setVisibleInLegend(final boolean b)\n
    '''
def getDataLabeling():
    '''returns int\n\n
    getDataLabeling()\n
    '''
def getDataLabelling():
    '''returns int\n\n
    getDataLabelling()\n
    '''
def setDataLabeling():
    '''returns None\n\n
    setDataLabeling(final int value)\n
    '''
def setDataLabelling():
    '''returns None\n\n
    setDataLabelling(final int dataLabeling)\n
    '''
def getDataLabelLayout():
    '''returns int\n\n
    getDataLabelLayout()\n
    '''
def setDataLabelLayout():
    '''returns None\n\n
    setDataLabelLayout(final int value)\n
    '''
def setAnnotation():
    '''returns None\n\n
    setAnnotation(final IlvDataAnnotation o)\n
    '''
def setRenderingHint():
    '''returns None\n\n
    setRenderingHint(final IlvDataRenderingHint p)\n
    '''
def computeDataLabel():
    '''returns String\n\n
    computeDataLabel(final IlvDataSetPoint ilvDataSetPoint)\n
    '''
def computeDataLabelLocation():
    '''returns Point\n\n
    computeDataLabelLocation(final IlvDisplayPoint ilvDisplayPoint, final Dimension dimension)\n
    '''
def applyStyles():
    '''returns None\n\n
    applyStyles(final boolean b)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def dataSourceChanged():
    '''returns None\n\n
    dataSourceChanged(final DataSourceEvent dataSourceEvent)\n
    '''
def startDataSourceChanges():
    '''returns None\n\n
    startDataSourceChanges()\n
    '''
def endDataSourceChanges():
    '''returns None\n\n
    endDataSourceChanges()\n
    '''
