DEFAULT_EXPLODE_RATIO = "int  20"
def has3DSupport():
    '''returns boolean\n\n
    has3DSupport()\n
    '''
def ():
    '''returns IlvSinglePieRenderer\n\n
    ()\n
    (final IlvStyle ilvStyle)\n
    '''
def setSliceStyle():
    '''returns None\n\n
    setSliceStyle(final int n, final IlvStyle style)\n
    '''
def applyDataSetStyle():
    '''returns None\n\n
    applyDataSetStyle(final IlvDataSetStyle ilvDataSetStyle)\n
    '''
def setSliceColors():
    '''returns None\n\n
    setSliceColors(final Color[] array)\n
    '''
def setStrokeOn():
    '''returns None\n\n
    setStrokeOn(final boolean e)\n
    '''
def setExplodeRatio():
    '''returns None\n\n
    setExplodeRatio(final int n, final int i)\n
    setExplodeRatio(final int n)\n
    '''
def getSlicePercent():
    '''returns double\n\n
    getSlicePercent(final int n)\n
    '''
def getPartialSum():
    '''returns double\n\n
    getPartialSum(final int n)\n
    '''
def getPreferredMargins():
    '''returns Insets\n\n
    getPreferredMargins()\n
    '''
def computeDataLabelLocation():
    '''returns Point\n\n
    computeDataLabelLocation(IlvDisplayPoint ilvDisplayPoint, final Dimension dimension)\n
    '''
def computeDataLabel():
    '''returns String\n\n
    computeDataLabel(final IlvDataSetPoint ilvDataSetPoint)\n
    '''
def drawSelectionHandles():
    '''returns None\n\n
    drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle, IlvDataSet set, int index)\n
    '''
def getYRange():
    '''returns IlvDataInterval\n\n
    getYRange(final int n, IlvDataInterval ilvDataInterval)\n
    '''
def getLegendText():
    '''returns String\n\n
    getLegendText(final IlvLegendItem ilvLegendItem)\n
    '''
def createLegendItems():
    '''returns IlvLegendItem[]\n\n
    createLegendItems()\n
    '''
def drawLegendSymbol():
    '''returns None\n\n
    drawLegendSymbol(final IlvLegendItem ilvLegendItem, final Graphics graphics, final int n, final int n2, final int a, final int b)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvStyle ilvStyle)\n
    '''
def getBounds():
    '''returns Rectangle2D\n\n
    getBounds(final IlvStyle ilvStyle, final boolean b, final Rectangle2D rectangle2D)\n
    '''
def distance():
    '''returns double\n\n
    distance(final IlvStyle ilvStyle, final double n, final double n2, final boolean b)\n
    '''
def getMapArea():
    '''returns IlvIMapArea\n\n
    getMapArea(final IlvIMapDefinition ilvIMapDefinition, final IlvStyle ilvStyle, final IlvIMapAttributes ilvIMapAttributes)\n
    '''
def drawIntoHitmap():
    '''returns None\n\n
    drawIntoHitmap(final IlvStyle ilvStyle, final Points points, final IlvDataSetPoint ilvDataSetPoint, final IlvChartHitmapDefinition ilvChartHitmapDefinition, final IlvChartHitmapAccumulator ilvChartHitmapAccumulator)\n
    '''
def needDrawIntoHitmap():
    '''returns boolean\n\n
    needDrawIntoHitmap(final Points points, final int n, final IlvStyle ilvStyle)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def isXValuesSorted():
    '''returns boolean\n\n
    isXValuesSorted()\n
    '''
def getPreviousXData():
    '''returns double\n\n
    getPreviousXData(final int n)\n
    '''
def map():
    '''returns None\n\n
    map(final IlvDataSetPoint ilvDataSetPoint)\n
    '''
def mapsMonotonically():
    '''returns boolean\n\n
    mapsMonotonically()\n
    '''
def unmap():
    '''returns None\n\n
    unmap(final IlvDataSetPoint ilvDataSetPoint)\n
    unmap(final IlvDataSetPoint ilvDataSetPoint, final IlvDoublePoint ilvDoublePoint)\n
    '''
def getUndefValue():
    '''returns Double\n\n
    getUndefValue()\n
    '''
def getXData():
    '''returns double\n\n
    getXData(final int n)\n
    '''
def getYData():
    '''returns double\n\n
    getYData(final int n)\n
    '''
def dataSetContentsChanged():
    '''returns None\n\n
    dataSetContentsChanged(final DataSetContentsEvent dataSetContentsEvent)\n
    '''
