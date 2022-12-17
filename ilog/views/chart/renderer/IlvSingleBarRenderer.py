SHAPE_QUADRILATERAL = "int  1"
SHAPE_POLYGON = "int  2"
SHAPE_EXACT = "int  3"
def ():
    '''returns BarItem\n\n
    ()\n
    (final IlvStyle ilvStyle)\n
    (final IlvStyle ilvStyle, final double widthPercent)\n
    (final int n)\n
    '''
def getSpecWidthPercent():
    '''returns double\n\n
    getSpecWidthPercent()\n
    '''
def setWidthPercent():
    '''returns None\n\n
    setWidthPercent(final double c)\n
    '''
def getWidthPercent():
    '''returns double\n\n
    getWidthPercent()\n
    '''
def getWidth():
    '''returns double\n\n
    getWidth()\n
    '''
def isUseCategorySpacingAtBorders():
    '''returns boolean\n\n
    isUseCategorySpacingAtBorders()\n
    '''
def setUseCategorySpacingAtBorders():
    '''returns None\n\n
    setUseCategorySpacingAtBorders(final boolean d)\n
    '''
def getBarShape():
    '''returns int\n\n
    getBarShape()\n
    '''
def setBarShape():
    '''returns None\n\n
    setBarShape(final int n)\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final IlvChartRenderer parent)\n
    '''
def has3DSupport():
    '''returns boolean\n\n
    has3DSupport()\n
    '''
def getDepths():
    '''returns double[]\n\n
    getDepths()\n
    '''
def getZAnnotationText():
    '''returns String\n\n
    getZAnnotationText()\n
    '''
def computeDataLabelLocation():
    '''returns Point\n\n
    computeDataLabelLocation(IlvDisplayPoint ilvDisplayPoint, final Dimension dimension)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvStyle ilvStyle)\n
    '''
def needDrawIntoHitmap():
    '''returns boolean\n\n
    needDrawIntoHitmap(final Points points, final int n, final IlvStyle ilvStyle)\n
    '''
def drawIntoHitmap():
    '''returns None\n\n
    drawIntoHitmap(final IlvStyle ilvStyle, final Points points, final IlvDataSetPoint ilvDataSetPoint, final IlvChartHitmapDefinition ilvChartHitmapDefinition, final IlvChartHitmapAccumulator ilvChartHitmapAccumulator)\n
    '''
def getBounds():
    '''returns Rectangle2D\n\n
    getBounds(final IlvStyle ilvStyle, final boolean b, final Rectangle2D rectangle2D)\n
    '''
def distance():
    '''returns double\n\n
    distance(final IlvStyle ilvStyle, final double x, final double y, final boolean b)\n
    '''
def getMapArea():
    '''returns IlvIMapArea\n\n
    getMapArea(final IlvIMapDefinition ilvIMapDefinition, final IlvStyle ilvStyle, final IlvIMapAttributes ilvIMapAttributes)\n
    '''
