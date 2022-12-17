MAX_CHUNK_SIZE = "int  32512"
MODE_READONLY = "int  0"
MODE_READWRITE = "int  1"
def ():
    '''returns OracleBfile\n\n
    ()\n
    (final OracleConnection oracleConnection)\n
    (final OracleConnection physicalConnectionOf, final byte[] array)\n
    '''
def length():
    '''returns long\n\n
    length()\n
    '''
def getBytes():
    '''returns int\n\n
    getBytes(final long n, final int n2)\n
    getBytes(final long n, final int n2, final byte[] array)\n
    '''
def getBinaryStream():
    '''returns InputStream\n\n
    getBinaryStream()\n
    getBinaryStream(final long n)\n
    '''
def position():
    '''returns long\n\n
    position(final byte[] array, final long n)\n
    position(final BFILE bfile, final long n)\n
    position(final oracle.jdbc.OracleBfile oracleBfile, final long n)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getDirAlias():
    '''returns String\n\n
    getDirAlias()\n
    '''
def openFile():
    '''returns None\n\n
    openFile()\n
    '''
def isFileOpen():
    '''returns boolean\n\n
    isFileOpen()\n
    '''
def fileExists():
    '''returns boolean\n\n
    fileExists()\n
    '''
def closeFile():
    '''returns None\n\n
    closeFile()\n
    '''
def getLocator():
    '''returns byte[]\n\n
    getLocator()\n
    '''
def setLocator():
    '''returns None\n\n
    setLocator(final byte[] bytes)\n
    '''
def open():
    '''returns None\n\n
    open()\n
    open(final LargeObjectAccessMode largeObjectAccessMode)\n
    open(final int n)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def toJdbc():
    '''returns Object\n\n
    toJdbc()\n
    '''
def isConvertibleTo():
    '''returns boolean\n\n
    isConvertibleTo(final Class clazz)\n
    '''
def characterStreamValue():
    '''returns Reader\n\n
    characterStreamValue()\n
    '''
def asciiStreamValue():
    '''returns InputStream\n\n
    asciiStreamValue()\n
    '''
def binaryStreamValue():
    '''returns InputStream\n\n
    binaryStreamValue()\n
    '''
def makeJdbcArray():
    '''returns Object\n\n
    makeJdbcArray(final int n)\n
    '''
def getDBAccess():
    '''returns BfileDBAccess\n\n
    getDBAccess()\n
    '''
def getJavaSqlConnection():
    '''returns Connection\n\n
    getJavaSqlConnection()\n
    '''
def setBytes():
    '''returns None\n\n
    setBytes(final byte[] array)\n
    '''
def setACProxy():
    '''returns None\n\n
    setACProxy(final Object acProxy)\n
    '''
def getACProxy():
    '''returns Object\n\n
    getACProxy()\n
    '''
