MAX_CHUNK_SIZE = "int  32768"
DURATION_SESSION = "int  10"
DURATION_CALL = "int  12"
MODE_READONLY = "int  0"
MODE_READWRITE = "int  1"
TRACE = "boolean  false"
def ():
    '''returns OracleBlob\n\n
    ()\n
    (final OracleConnection oracleConnection)\n
    (final OracleConnection oracleConnection, final byte[] array, final boolean fromObject)\n
    (final OracleConnection physicalConnectionOf, final byte[] array)\n
    '''
def setFromobject():
    '''returns None\n\n
    setFromobject(final boolean fromObject)\n
    '''
def length():
    '''returns long\n\n
    length()\n
    '''
def getBytes():
    '''returns int\n\n
    getBytes(final long n, final int b)\n
    getBytes(final long n, int length, final byte[] array)\n
    '''
def getBinaryStream():
    '''returns InputStream\n\n
    getBinaryStream()\n
    getBinaryStream(final boolean b)\n
    getBinaryStream(final long n)\n
    getBinaryStream(final long n, final boolean b)\n
    getBinaryStream(final long n, final long n2)\n
    '''
def position():
    '''returns long\n\n
    position(final byte[] array, final long n)\n
    position(final Blob blob, final long n)\n
    '''
def putBytes():
    '''returns int\n\n
    putBytes(final long n, final byte[] array)\n
    putBytes(final long n, final byte[] array, final int n2)\n
    '''
def getBinaryOutputStream():
    '''returns OutputStream\n\n
    getBinaryOutputStream()\n
    getBinaryOutputStream(final long n)\n
    '''
def getLocator():
    '''returns byte[]\n\n
    getLocator()\n
    '''
def setLocator():
    '''returns None\n\n
    setLocator(final byte[] bytes)\n
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
def setBytes():
    '''returns None\n\n
    setBytes(final long n, final byte[] array)\n
    setBytes(final long n, final byte[] array, final int n2, final int n3)\n
    setBytes(final byte[] array)\n
    '''
def setBinaryStream():
    '''returns OutputStream\n\n
    setBinaryStream(final long n)\n
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
    characterStreamValue(final boolean b)\n
    '''
def asciiStreamValue():
    '''returns InputStream\n\n
    asciiStreamValue()\n
    asciiStreamValue(final boolean b)\n
    '''
def binaryStreamValue():
    '''returns InputStream\n\n
    binaryStreamValue()\n
    binaryStreamValue(final boolean b)\n
    '''
def makeJdbcArray():
    '''returns Object\n\n
    makeJdbcArray(final int n)\n
    '''
def getDBAccess():
    '''returns BlobDBAccess\n\n
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
    toSQLXML(final int n)\n
    '''
