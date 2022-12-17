LINEAR_MODE = "int  0"
ROTATE_MODE = "int  1"
CYCLIC_MODE = "int  2"
def ():
    '''returns IlvCyclicDataSet\n\n
    (final String s, final int n, final boolean b)\n
    (final String s, final int a, final int b, final boolean b2)\n
    '''
def getDataCount():
    '''returns int\n\n
    getDataCount()\n
    '''
def getXData():
    '''returns double\n\n
    getXData(int index)\n
    '''
def getYData():
    '''returns double\n\n
    getYData(final int index)\n
    '''
def getDataLabel():
    '''returns String\n\n
    getDataLabel(final int index)\n
    '''
def setData():
    '''returns None\n\n
    setData(final int index, final double n, final double n2)\n
    setData(final double[] array, final double[] array2, int c)\n
    '''
def addData():
    '''returns None\n\n
    addData(final double n, final double n2, final String s)\n
    '''
def isXValuesSorted():
    '''returns boolean\n\n
    isXValuesSorted()\n
    '''
def getMinimumXDifference():
    '''returns double\n\n
    getMinimumXDifference()\n
    '''
def getData():
    '''returns IlvDataPoints\n\n
    getData()\n
    '''
def getDataBetween():
    '''returns IlvDataPoints\n\n
    getDataBetween(int n, final int n2)\n
    '''
def getDataInside():
    '''returns IlvDataPoints\n\n
    getDataInside(final IlvDataWindow ilvDataWindow, final int n, final boolean b)\n
    '''
def useXValues():
    '''returns None\n\n
    useXValues(final boolean b)\n
    '''
def setDataLabel():
    '''returns None\n\n
    setDataLabel(final int n, final String s)\n
    '''
def setDataLabels():
    '''returns None\n\n
    setDataLabels(final String[] array)\n
    '''
