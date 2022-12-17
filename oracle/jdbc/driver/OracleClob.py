MAX_CHUNK_SIZE = "int  32768"
DURATION_SESSION = "int  10"
DURATION_CALL = "int  12"
OLD_WRONG_DURATION_SESSION = "int  1"
OLD_WRONG_DURATION_CALL = "int  2"
MODE_READONLY = "int  0"
MODE_READWRITE = "int  1"
def ():
    '''returns OracleClob\n\n
    ()\n
    (final OracleConnection oracleConnection)\n
    (final OracleConnection oracleConnection, final byte[] array, final boolean fromObject)\n
    (final OracleConnection physicalConnectionOf, final byte[] array)\n
    (final OracleConnection oracleConnection, final byte[] array, final short csform)\n
    '''
def setCsform():
    '''returns None\n\n
    setCsform(final short csform)\n
    '''
def getCsform():
    '''returns short\n\n
    getCsform()\n
    '''
def setFromobject():
    '''returns None\n\n
    setFromobject(final boolean fromObject)\n
    '''
def isNCLOB():
    '''returns boolean\n\n
    isNCLOB()\n
    '''
def length():
    '''returns long\n\n
    length()\n
    '''
def getSubString():
    '''returns String\n\n
    getSubString(final long n, final int count)\n
    '''
def getCharacterStream():
    '''returns Reader\n\n
    getCharacterStream()\n
    getCharacterStream(long n)\n
    getCharacterStream(long n, final long n2)\n
    '''
def getAsciiStream():
    '''returns InputStream\n\n
    getAsciiStream()\n
    getAsciiStream(final boolean b)\n
    getAsciiStream(long n)\n
    '''
def position():
    '''returns long\n\n
    position(final String s, final long n)\n
    position(final Clob clob, final long n)\n
    '''
def getChars():
    '''returns int\n\n
    getChars(final long n, final int n2, final char[] array)\n
    '''
def getCharacterOutputStream():
    '''returns Writer\n\n
    getCharacterOutputStream()\n
    getCharacterOutputStream(final long n)\n
    '''
def getAsciiOutputStream():
    '''returns OutputStream\n\n
    getAsciiOutputStream()\n
    getAsciiOutputStream(final long n)\n
    '''
def getLocator():
    '''returns byte[]\n\n
    getLocator()\n
    '''
def setLocator():
    '''returns None\n\n
    setLocator(final byte[] bytes)\n
    '''
def putChars():
    '''returns int\n\n
    putChars(final long n, final char[] array)\n
    putChars(final long n, final char[] array, final int n2)\n
    putChars(final long n, final char[] array, final int n2, final int n3)\n
    '''
def putString():
    '''returns int\n\n
    putString(final long n, final String s)\n
    '''
def getChunkSize():
    '''returns int\n\n
    getChunkSize()\n
    '''
def getBufferSize():
    '''returns int\n\n
    getBufferSize()\n
    '''
def isEmptyLob():
    '''returns boolean\n\n
    isEmptyLob()\n
    '''
def isSecureFile():
    '''returns boolean\n\n
    isSecureFile()\n
    '''
def trim():
    '''returns None\n\n
    trim(final long n)\n
    '''
def freeTemporary():
    '''returns None\n\n
    freeTemporary()\n
    '''
def isTemporary():
    '''returns boolean\n\n
    isTemporary()\n
    '''
def getDuration():
    '''returns short\n\n
    getDuration()\n
    '''
def open():
    '''returns None\n\n
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
def setString():
    '''returns int\n\n
    setString(final long n, final String s)\n
    setString(final long n, final String s, final int n2, final int n3)\n
    '''
def setAsciiStream():
    '''returns OutputStream\n\n
    setAsciiStream(final long n)\n
    '''
def setCharacterStream():
    '''returns Writer\n\n
    setCharacterStream(final long n)\n
    '''
def truncate():
    '''returns None\n\n
    truncate(final long n)\n
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
def stringValue():
    '''returns String\n\n
    stringValue()\n
    '''
def makeJdbcArray():
    '''returns Object\n\n
    makeJdbcArray(final int n)\n
    '''
def getDBAccess():
    '''returns ClobDBAccess\n\n
    getDBAccess()\n
    '''
def getJavaSqlConnection():
    '''returns Connection\n\n
    getJavaSqlConnection()\n
    '''
def canReadBasicLobDataInLocator():
    '''returns boolean\n\n
    canReadBasicLobDataInLocator()\n
    '''
def free():
    '''returns None\n\n
    free()\n
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
def toSQLXML():
    '''returns SQLXML\n\n
    toSQLXML()\n
    toSQLXML(final String s)\n
    '''
