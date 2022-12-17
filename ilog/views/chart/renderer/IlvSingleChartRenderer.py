def isFilled():
    '''returns boolean\n\n
    isFilled()\n
    '''
def setStyle():
    '''returns None\n\n
    setStyle(final IlvStyle ilvStyle)\n
    '''
def getStyle():
    '''returns IlvStyle\n\n
    getStyle()\n
    getStyle(final IlvDataSet set, final int n)\n
    getStyle()\n
    '''
def setStyles():
    '''returns None\n\n
    setStyles(final IlvStyle[] array)\n
    '''
def getStyles():
    '''returns IlvStyle[]\n\n
    getStyles()\n
    '''
def toDisplay():
    '''returns None\n\n
    toDisplay(final IlvDoublePoints ilvDoublePoints)\n
    toDisplay(final IlvDoublePoints ilvDoublePoints, final IlvChartProjector ilvChartProjector, final Rectangle rectangle, final IlvCoordinateSystem ilvCoordinateSystem)\n
    '''
def getZAnnotationText():
    '''returns String\n\n
    getZAnnotationText()\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics)\n
    draw(final Graphics graphics, final IlvDataSet set, final int n, final int n2)\n
    draw(final Graphics graphics, final IlvStyle ilvStyle)\n
    '''
def getBounds():
    '''returns Rectangle2D\n\n
    getBounds(Rectangle2D rectangle2D, final boolean b)\n
    getBounds(final IlvDataSet dataSet, final int n, final int n2, Rectangle2D rectangle2D, final boolean b)\n
    getBounds()\n
    getBounds(final IlvStyle ilvStyle, final boolean b, final Rectangle2D rectangle2D)\n
    '''
def drawSelectionHandles():
    '''returns None\n\n
    drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle)\n
    drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle, final IlvDataSet set)\n
    '''
def getNearestPoint():
    '''returns IlvDisplayPoint\n\n
    getNearestPoint(final IlvChartDataPicker ilvChartDataPicker)\n
    '''
def getNearestItem():
    '''returns IlvDisplayPoint\n\n
    getNearestItem(final IlvChartDataPicker ilvChartDataPicker, final double[] array)\n
    '''
def getDisplayItem():
    '''returns IlvDisplayPoint\n\n
    getDisplayItem(final IlvChartDataPicker ilvChartDataPicker)\n
    getDisplayItem()\n
    '''
def getDisplayPoint():
    '''returns IlvDisplayPoint\n\n
    getDisplayPoint(final IlvDataSet set, final int n)\n
    '''
def setDisplayPoint():
    '''returns None\n\n
    setDisplayPoint(final IlvDataSet set, final int n, final double n2, final double n3)\n
    '''
def setDataPoint():
    '''returns None\n\n
    setDataPoint(final IlvDataSet set, final int n, final double n2, final double n3)\n
    '''
def addImageMapAreas():
    '''returns None\n\n
    addImageMapAreas(final IlvIMapDefinition ilvIMapDefinition, final List<? super IlvIMapArea> list)\n
    '''
def drawIntoHitmap():
    '''returns None\n\n
    drawIntoHitmap(final IlvChartHitmapDefinition ilvChartHitmapDefinition, final IlvChartHitmapAccumulator ilvChartHitmapAccumulator)\n
    drawIntoHitmap(final IlvStyle ilvStyle, final Points points, final IlvDataSetPoint ilvDataSetPoint, final IlvChartHitmapDefinition ilvChartHitmapDefinition, final IlvChartHitmapAccumulator ilvChartHitmapAccumulator)\n
    '''
def dataSetContentsChanged():
    '''returns None\n\n
    dataSetContentsChanged(final DataSetContentsEvent a)\n
    dataSetContentsChanged(final DataSetContentsEvent dataSetContentsEvent)\n
    '''
def dataSetPropertyChanged():
    '''returns None\n\n
    dataSetPropertyChanged(final DataSetPropertyEvent dataSetPropertyEvent)\n
    dataSetPropertyChanged(final DataSetPropertyEvent dataSetPropertyEvent)\n
    '''
def getXRange():
    '''returns IlvDataInterval\n\n
    getXRange(final IlvDataInterval ilvDataInterval)\n
    '''
def getYRange():
    '''returns IlvDataInterval\n\n
    getYRange(IlvDataInterval ilvDataInterval)\n
    getYRange(final IlvDataInterval ilvDataInterval, IlvDataInterval ilvDataInterval2)\n
    '''
def getPreferredMargins():
    '''returns Insets\n\n
    getPreferredMargins()\n
    '''
def drawLegendSymbol():
    '''returns None\n\n
    drawLegendSymbol(final IlvLegendItem ilvLegendItem, final Graphics graphics, final int n, final int n2, final int a, final int b)\n
    '''
def createLegendItems():
    '''returns IlvLegendItem[]\n\n
    createLegendItems()\n
    '''
def getLegendText():
    '''returns String\n\n
    getLegendText(final IlvLegendItem ilvLegendItem)\n
    '''
def getDefaultLegendText():
    '''returns String\n\n
    getDefaultLegendText()\n
    '''
def drawAnnotations():
    '''returns None\n\n
    drawAnnotations(final Graphics graphics)\n
    '''
def setAnnotation():
    '''returns None\n\n
    setAnnotation(final IlvDataSet set, final int n, final IlvDataAnnotation ilvDataAnnotation)\n
    setAnnotation(final IlvDataSet set, final IlvDataAnnotation ilvDataAnnotation)\n
    '''
def getAnnotation():
    '''returns IlvDataAnnotation\n\n
    getAnnotation(final IlvDataSet set, final int n)\n
    '''
def setRenderingHint():
    '''returns None\n\n
    setRenderingHint(final IlvDataSet set, final int n, final IlvDataRenderingHint ilvDataRenderingHint)\n
    setRenderingHint(final IlvDataSet set, final IlvDataRenderingHint renderingHint)\n
    '''
def getRenderingHint():
    '''returns IlvDataRenderingHint\n\n
    getRenderingHint(final IlvDataSet set, final int n)\n
    getRenderingHint(final IlvDataSet set)\n
    '''
def getDisplayStyle():
    '''returns IlvStyle\n\n
    getDisplayStyle(final int n)\n
    '''
def holdsAnnotations():
    '''returns boolean\n\n
    holdsAnnotations()\n
    '''
def applyStyles():
    '''returns None\n\n
    applyStyles(final boolean b)\n
    '''
def applyDataSetStyle():
    '''returns None\n\n
    applyDataSetStyle(final IlvDataSetStyle ilvDataSetStyle)\n
    '''
def ():
    '''returns DefaultItem\n\n
    (final Points c)\n
    (final IlvDataPoints a, final boolean c)\n
    (final IlvChartHitmapDefinition a, final IlvChartHitmapAccumulator b)\n
    (final IlvChartDataPicker ilvChartDataPicker, final boolean a)\n
    (final IlvChartDataPicker a)\n
    ()\n
    (final int n)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns None\n\n
    next()\n
    '''
def getCurrentIdx():
    '''returns int\n\n
    getCurrentIdx()\n
    '''
def getPoints():
    '''returns Points\n\n
    getPoints()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def startProcessItems():
    '''returns None\n\n
    startProcessItems()\n
    startProcessItems()\n
    startProcessItems()\n
    startProcessItems()\n
    startProcessItems()\n
    '''
def endProcessItems():
    '''returns None\n\n
    endProcessItems()\n
    endProcessItems()\n
    endProcessItems()\n
    endProcessItems()\n
    endProcessItems()\n
    '''
def processItem():
    '''returns None\n\n
    processItem(final Points points, final int n, final Item item, final IlvStyle ilvStyle)\n
    processItem(final Points points, final int n, final Item item, final IlvStyle ilvStyle)\n
    processItem(final Points points, final int n, final Item item, final IlvStyle ilvStyle)\n
    processItem(final Points points, final int n, final Item item, final IlvStyle ilvStyle)\n
    processItem(final Points points, final int n, final Item item, final IlvStyle ilvStyle)\n
    '''
def setGraphics():
    '''returns None\n\n
    setGraphics(final Graphics a)\n
    '''
def getDistance():
    '''returns double\n\n
    getDistance()\n
    '''
def distance():
    '''returns double\n\n
    distance(final IlvStyle ilvStyle, final double n, final double n2, final boolean b)\n
    '''
def getMapArea():
    '''returns IlvIMapArea\n\n
    getMapArea(final IlvIMapDefinition ilvIMapDefinition, final IlvStyle ilvStyle, final IlvIMapAttributes ilvIMapAttributes)\n
    '''
def needDrawIntoHitmap():
    '''returns boolean\n\n
    needDrawIntoHitmap(final Points points, final int n, final IlvStyle ilvStyle)\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
