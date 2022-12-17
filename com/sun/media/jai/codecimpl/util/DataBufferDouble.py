def ():
    '''returns DataBufferDouble\n\n
    (final int size)\n
    (final int size, final int numBanks)\n
    (final double[] dataArray, final int size)\n
    (final double[] dataArray, final int size, final int offset)\n
    (final double[][] dataArray, final int size)\n
    (final double[][] dataArray, final int size, final int[] offsets)\n
    '''
def getData():
    '''returns double[]\n\n
    getData()\n
    getData(final int bank)\n
    '''
def getBankData():
    '''returns double[][]\n\n
    getBankData()\n
    '''
def getElem():
    '''returns int\n\n
    getElem(final int i)\n
    getElem(final int bank, final int i)\n
    '''
def setElem():
    '''returns None\n\n
    setElem(final int i, final int val)\n
    setElem(final int bank, final int i, final int val)\n
    '''
def getElemFloat():
    '''returns float\n\n
    getElemFloat(final int i)\n
    getElemFloat(final int bank, final int i)\n
    '''
def setElemFloat():
    '''returns None\n\n
    setElemFloat(final int i, final float val)\n
    setElemFloat(final int bank, final int i, final float val)\n
    '''
def getElemDouble():
    '''returns double\n\n
    getElemDouble(final int i)\n
    getElemDouble(final int bank, final int i)\n
    '''
def setElemDouble():
    '''returns None\n\n
    setElemDouble(final int i, final double val)\n
    setElemDouble(final int bank, final int i, final double val)\n
    '''
