def ():
    '''returns XWPFNumbering\n\n
    (final PackagePart part)\n
    ()\n
    '''
def setNumbering():
    '''returns None\n\n
    setNumbering(final CTNumbering numbering)\n
    '''
def numExist():
    '''returns boolean\n\n
    numExist(final BigInteger numID)\n
    '''
def addNum():
    '''returns None\n\n
    addNum(final XWPFNum num)\n
    addNum(final BigInteger abstractNumID)\n
    addNum(final BigInteger abstractNumID, final BigInteger numID)\n
    '''
def getNum():
    '''returns XWPFNum\n\n
    getNum(final BigInteger numID)\n
    '''
def getAbstractNum():
    '''returns XWPFAbstractNum\n\n
    getAbstractNum(final BigInteger abstractNumID)\n
    '''
def getIdOfAbstractNum():
    '''returns BigInteger\n\n
    getIdOfAbstractNum(final XWPFAbstractNum abstractNum)\n
    '''
def addAbstractNum():
    '''returns BigInteger\n\n
    addAbstractNum(final XWPFAbstractNum abstractNum)\n
    '''
def removeAbstractNum():
    '''returns boolean\n\n
    removeAbstractNum(final BigInteger abstractNumID)\n
    '''
def getAbstractNumID():
    '''returns BigInteger\n\n
    getAbstractNumID(final BigInteger numID)\n
    '''
