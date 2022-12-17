CLUSTERED = "int  1"
CANDLE = "int  2"
OPENCLOSE = "int  3"
def ():
    '''returns IlvHiLoChartRenderer\n\n
    ()\n
    (final int d, final int c, final double widthPercent)\n
    '''
def setType():
    '''returns None\n\n
    setType(final int c)\n
    '''
def getMode():
    '''returns int\n\n
    getMode()\n
    '''
def setMode():
    '''returns None\n\n
    setMode(final int d)\n
    '''
def getNames():
    '''returns String[]\n\n
    getNames()\n
    '''
def setNames():
    '''returns None\n\n
    setNames(final String[] a2)\n
    '''
def getName():
    '''returns String\n\n
    getName(final int n)\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final int n, final String s)\n
    setName(final String s)\n
    '''
def getOverlap():
    '''returns double\n\n
    getOverlap()\n
    '''
def setOverlap():
    '''returns None\n\n
    setOverlap(final double n)\n
    '''
def getSpecWidthPercent():
    '''returns double\n\n
    getSpecWidthPercent()\n
    '''
def setWidthPercent():
    '''returns None\n\n
    setWidthPercent(final double n)\n
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
    setUseCategorySpacingAtBorders(final boolean b)\n
    '''
def getHiLo():
    '''returns IlvSingleHiLoRenderer\n\n
    getHiLo(final IlvDataSet set)\n
    '''
def setStyles():
    '''returns None\n\n
    setStyles(final IlvStyle[] array)\n
    '''
def createLegendItems():
    '''returns IlvLegendItem[]\n\n
    createLegendItems()\n
    '''
def getLegendText():
    '''returns String\n\n
    getLegendText(final IlvLegendItem ilvLegendItem)\n
    '''
def drawLegendSymbol():
    '''returns None\n\n
    drawLegendSymbol(final IlvLegendItem ilvLegendItem, final Graphics graphics, int n, int n2, final int a, final int b)\n
    '''
