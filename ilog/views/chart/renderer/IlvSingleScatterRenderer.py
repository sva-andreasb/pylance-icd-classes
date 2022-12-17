def ():
    '''returns IlvSingleScatterRenderer\n\n
    ()\n
    (final IlvStyle ilvStyle)\n
    (final IlvMarker c, final int d, final IlvStyle ilvStyle)\n
    '''
def setMarker():
    '''returns None\n\n
    setMarker(final IlvMarker c)\n
    '''
def setMarkerSize():
    '''returns None\n\n
    setMarkerSize(final int d)\n
    '''
def getMaxSize():
    '''returns int\n\n
    getMaxSize()\n
    '''
def getClipRect():
    '''returns Rectangle\n\n
    getClipRect()\n
    '''
def getPreferredMargins():
    '''returns Insets\n\n
    getPreferredMargins()\n
    '''
def computeDataLabelLocation():
    '''returns Point\n\n
    computeDataLabelLocation(final IlvDisplayPoint ilvDisplayPoint, final Dimension dimension)\n
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
    getBounds(final IlvStyle ilvStyle, final boolean b, Rectangle2D rectangle2D)\n
    '''
def distance():
    '''returns double\n\n
    distance(final IlvStyle ilvStyle, final double x, final double y, final boolean b)\n
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
