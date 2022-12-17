STICK = "int  0"
BAR = "int  1"
ARROW = "int  2"
MARKED = "int  3"
def ():
    '''returns IlvSingleHiLoRenderer\n\n
    ()\n
    (final IlvStyle ilvStyle, final IlvStyle ilvStyle2)\n
    (final IlvStyle ilvStyle, final IlvStyle fallStyle, final int type, final double widthPercent)\n
    '''
def getMinDataSetCount():
    '''returns int\n\n
    getMinDataSetCount()\n
    '''
def isFilled():
    '''returns boolean\n\n
    isFilled()\n
    '''
def getRiseStyle():
    '''returns IlvStyle\n\n
    getRiseStyle()\n
    '''
def setRiseStyle():
    '''returns None\n\n
    setRiseStyle(final IlvStyle style)\n
    '''
def getFallStyle():
    '''returns IlvStyle\n\n
    getFallStyle()\n
    '''
def setFallStyle():
    '''returns None\n\n
    setFallStyle(final IlvStyle b)\n
    '''
def getStyles():
    '''returns IlvStyle[]\n\n
    getStyles()\n
    '''
def setStyles():
    '''returns None\n\n
    setStyles(final IlvStyle[] array)\n
    '''
def applyStyles():
    '''returns None\n\n
    applyStyles(final boolean b)\n
    '''
def getWidthPercent():
    '''returns double\n\n
    getWidthPercent()\n
    '''
def setWidthPercent():
    '''returns None\n\n
    setWidthPercent(double c)\n
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
def setType():
    '''returns None\n\n
    setType(final int e)\n
    '''
def getBounds():
    '''returns Rectangle2D\n\n
    getBounds(final IlvDataSet set, int n, int n2, final Rectangle2D rectangle2D)\n
    getBounds(final IlvDataSet set, int n, int n2, final Rectangle2D rectangle2D, final boolean b)\n
    '''
def drawLegendSymbol():
    '''returns None\n\n
    drawLegendSymbol(final IlvLegendItem ilvLegendItem, final Graphics graphics, int n, int n2, final int a, final int b)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvStyle ilvStyle)\n
    '''
def distance():
    '''returns double\n\n
    distance(final IlvStyle ilvStyle, final double x, final double y, final boolean b)\n
    '''
def getMapArea():
    '''returns IlvIMapArea\n\n
    getMapArea(final IlvIMapDefinition ilvIMapDefinition, final IlvStyle ilvStyle, final IlvIMapAttributes ilvIMapAttributes)\n
    '''
