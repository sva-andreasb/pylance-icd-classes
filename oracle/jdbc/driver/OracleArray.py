ACCESS_FORWARD = "int  1"
ACCESS_REVERSE = "int  2"
ACCESS_UNKNOWN = "int  3"
def ():
    '''returns OracleArray\n\n
    (final ArrayDescriptor descriptor, final Connection connection, final Object o)\n
    (final ArrayDescriptor descriptor, final byte[] array, final Connection connection)\n
    '''
def getBaseTypeName():
    '''returns String\n\n
    getBaseTypeName()\n
    '''
def getBaseType():
    '''returns int\n\n
    getBaseType()\n
    '''
def getArray():
    '''returns Object\n\n
    getArray()\n
    getArray(final Map map)\n
    getArray(final long n, final int n2)\n
    getArray(final long n, final int n2, final Map map)\n
    '''
def getResultSet():
    '''returns ResultSet\n\n
    getResultSet()\n
    getResultSet(final Map map)\n
    getResultSet(final long n, final int n2)\n
    getResultSet(final long n, final int n2, final Map map)\n
    '''
def getOracleArray():
    '''returns Datum[]\n\n
    getOracleArray()\n
    getOracleArray(final long n, final int n2)\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def getSQLTypeName():
    '''returns String\n\n
    getSQLTypeName()\n
    '''
def getMap():
    '''returns Map\n\n
    getMap()\n
    '''
def getOracleMetaData():
    '''returns OracleTypeMetaData\n\n
    getOracleMetaData()\n
    '''
def getDescriptor():
    '''returns ArrayDescriptor\n\n
    getDescriptor()\n
    '''
def toBytes():
    '''returns byte[]\n\n
    toBytes()\n
    '''
def setDatumArray():
    '''returns None\n\n
    setDatumArray(final Datum[] datumArray)\n
    '''
def setObjArray():
    '''returns None\n\n
    setObjArray(final Object objArray)\n
    '''
def setJavaMap():
    '''returns None\n\n
    setJavaMap(final Map<?, ?> javaMap)\n
    '''
def setLocator():
    '''returns None\n\n
    setLocator(final byte[] locator)\n
    '''
def setPrefixSegment():
    '''returns None\n\n
    setPrefixSegment(final byte[] prefixSegment)\n
    '''
def setPrefixFlag():
    '''returns None\n\n
    setPrefixFlag(final byte prefixFlag)\n
    '''
def getLocator():
    '''returns byte[]\n\n
    getLocator()\n
    '''
def setLength():
    '''returns None\n\n
    setLength(final int numElems)\n
    '''
def hasDataSeg():
    '''returns boolean\n\n
    hasDataSeg()\n
    '''
def isInline():
    '''returns boolean\n\n
    isInline()\n
    '''
def toJdbc():
    '''returns Object\n\n
    toJdbc()\n
    toJdbc(final Map map)\n
    '''
def isConvertibleTo():
    '''returns boolean\n\n
    isConvertibleTo(final Class clazz)\n
    '''
def makeJdbcArray():
    '''returns Object\n\n
    makeJdbcArray(final int n)\n
    '''
def getIntArray():
    '''returns int[]\n\n
    getIntArray()\n
    getIntArray(final long n, final int n2)\n
    '''
def getDoubleArray():
    '''returns double[]\n\n
    getDoubleArray()\n
    getDoubleArray(final long n, final int n2)\n
    '''
def getShortArray():
    '''returns short[]\n\n
    getShortArray()\n
    getShortArray(final long n, final int n2)\n
    '''
def getLongArray():
    '''returns long[]\n\n
    getLongArray()\n
    getLongArray(final long n, final int n2)\n
    '''
def getFloatArray():
    '''returns float[]\n\n
    getFloatArray()\n
    getFloatArray(final long n, final int n2)\n
    '''
def setAutoBuffering():
    '''returns None\n\n
    setAutoBuffering(final boolean enableBuffering)\n
    '''
def getAutoBuffering():
    '''returns boolean\n\n
    getAutoBuffering()\n
    '''
def setAutoIndexing():
    '''returns None\n\n
    setAutoIndexing(final boolean enableIndexing, final int accessDirection)\n
    setAutoIndexing(final boolean enableIndexing)\n
    '''
def getAutoIndexing():
    '''returns boolean\n\n
    getAutoIndexing()\n
    '''
def getAccessDirection():
    '''returns int\n\n
    getAccessDirection()\n
    '''
def setLastIndexOffset():
    '''returns None\n\n
    setLastIndexOffset(final long lastIndex, final long lastOffset)\n
    '''
def setIndexOffset():
    '''returns None\n\n
    setIndexOffset(final long n, final long n2)\n
    '''
def getLastIndex():
    '''returns long\n\n
    getLastIndex()\n
    '''
def getLastOffset():
    '''returns long\n\n
    getLastOffset()\n
    '''
def getOffset():
    '''returns long\n\n
    getOffset(final long n)\n
    '''
def setImage():
    '''returns None\n\n
    setImage(final byte[] shareBytes, final long imageOffset, final long imageLength)\n
    '''
def setImageLength():
    '''returns None\n\n
    setImageLength(final long imageLength)\n
    '''
def getImageOffset():
    '''returns long\n\n
    getImageOffset()\n
    '''
def getImageLength():
    '''returns long\n\n
    getImageLength()\n
    '''
def stringValue():
    '''returns String\n\n
    stringValue()\n
    '''
def free():
    '''returns None\n\n
    free()\n
    '''
def isFreed():
    '''returns boolean\n\n
    isFreed()\n
    '''
def getNumElems():
    '''returns int\n\n
    getNumElems()\n
    '''
def getDatumArray():
    '''returns Datum[]\n\n
    getDatumArray()\n
    '''
def getObjArray():
    '''returns Object\n\n
    getObjArray()\n
    '''
def setNullObjArray():
    '''returns None\n\n
    setNullObjArray()\n
    '''
def setACProxy():
    '''returns None\n\n
    setACProxy(final Object acProxy)\n
    '''
def getACProxy():
    '''returns Object\n\n
    getACProxy()\n
    '''
