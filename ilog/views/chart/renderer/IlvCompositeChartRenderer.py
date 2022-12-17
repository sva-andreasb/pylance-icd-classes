def isViewable():
    '''returns boolean\n\n
    isViewable()\n
    '''
def setStyles():
    '''returns None\n\n
    setStyles(final IlvStyle[] b)\n
    '''
def getStyles():
    '''returns IlvStyle[]\n\n
    getStyles()\n
    '''
def getStyle():
    '''returns IlvStyle\n\n
    getStyle(final IlvDataSet set, final int n)\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount()\n
    '''
def getChild():
    '''returns IlvChartRenderer\n\n
    getChild(final int index)\n
    getChild(final IlvDataSet set)\n
    '''
def getChildren():
    '''returns List<IlvChartRenderer>\n\n
    getChildren()\n
    '''
def getChildIterator():
    '''returns Iterator<IlvChartRenderer>\n\n
    getChildIterator()\n
    '''
def setDisplayPoint():
    '''returns None\n\n
    setDisplayPoint(final IlvDataSet set, final int n, final double n2, final double n3)\n
    '''
def setDataPoint():
    '''returns None\n\n
    setDataPoint(final IlvDataSet set, final int n, final double n2, final double n3)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics)\n
    draw(final Graphics graphics, final IlvDataSet set, final int n, final int n2)\n
    '''
def drawAnnotations():
    '''returns None\n\n
    drawAnnotations(final Graphics graphics)\n
    '''
def getBounds():
    '''returns Rectangle2D\n\n
    getBounds(Rectangle2D rectangle2D, final boolean b)\n
    getBounds(final IlvDataSet set, final int n, final int n2, Rectangle2D rectangle2D, final boolean b)\n
    '''
def drawSelectionHandles():
    '''returns None\n\n
    drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle)\n
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
    '''
def collectDisplayItems():
    '''returns None\n\n
    collectDisplayItems(final IlvChartDataPicker ilvChartDataPicker, final ArrayList<IlvDisplayPoint> list)\n
    '''
def getDisplayPoint():
    '''returns IlvDisplayPoint\n\n
    getDisplayPoint(final IlvDataSet set, final int n)\n
    '''
def getXRange():
    '''returns IlvDataInterval\n\n
    getXRange(IlvDataInterval ilvDataInterval)\n
    '''
def getYRange():
    '''returns IlvDataInterval\n\n
    getYRange(IlvDataInterval ilvDataInterval)\n
    getYRange(final IlvDataInterval ilvDataInterval, IlvDataInterval ilvDataInterval2)\n
    '''
def drawLegendSymbol():
    '''returns None\n\n
    drawLegendSymbol(final IlvLegendItem ilvLegendItem, final Graphics graphics, final int n, final int n2, final int n3, final int n4)\n
    '''
def createLegendItems():
    '''returns IlvLegendItem[]\n\n
    createLegendItems()\n
    '''
def getLegendText():
    '''returns String\n\n
    getLegendText(final IlvLegendItem ilvLegendItem)\n
    '''
def addImageMapAreas():
    '''returns None\n\n
    addImageMapAreas(final IlvIMapDefinition ilvIMapDefinition, final List<? super IlvIMapArea> list)\n
    '''
def drawIntoHitmap():
    '''returns None\n\n
    drawIntoHitmap(final IlvChartHitmapDefinition ilvChartHitmapDefinition, final IlvChartHitmapAccumulator ilvChartHitmapAccumulator)\n
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
def holdsAnnotations():
    '''returns boolean\n\n
    holdsAnnotations()\n
    '''
def setRenderingHint():
    '''returns None\n\n
    setRenderingHint(final IlvDataSet set, final int n, final IlvDataRenderingHint ilvDataRenderingHint)\n
    setRenderingHint(final IlvDataSet set, final IlvDataRenderingHint ilvDataRenderingHint)\n
    '''
def getRenderingHint():
    '''returns IlvDataRenderingHint\n\n
    getRenderingHint(final IlvDataSet set, final int n)\n
    getRenderingHint(final IlvDataSet set)\n
    '''
