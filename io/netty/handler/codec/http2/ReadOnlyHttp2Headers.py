def get():
    '''returns CharSequence\n\n
    get(final CharSequence name)\n
    get(final CharSequence name, final CharSequence defaultValue)\n
    '''
def getAndRemove():
    '''returns CharSequence\n\n
    getAndRemove(final CharSequence name)\n
    getAndRemove(final CharSequence name, final CharSequence defaultValue)\n
    '''
def getAll():
    '''returns List<CharSequence>\n\n
    getAll(final CharSequence name)\n
    '''
def getAllAndRemove():
    '''returns List<CharSequence>\n\n
    getAllAndRemove(final CharSequence name)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final CharSequence name)\n
    getBoolean(final CharSequence name, final boolean defaultValue)\n
    '''
def getByte():
    '''returns byte\n\n
    getByte(final CharSequence name)\n
    getByte(final CharSequence name, final byte defaultValue)\n
    '''
def getChar():
    '''returns char\n\n
    getChar(final CharSequence name)\n
    getChar(final CharSequence name, final char defaultValue)\n
    '''
def getShort():
    '''returns short\n\n
    getShort(final CharSequence name)\n
    getShort(final CharSequence name, final short defaultValue)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final CharSequence name)\n
    getInt(final CharSequence name, final int defaultValue)\n
    '''
def getLong():
    '''returns long\n\n
    getLong(final CharSequence name)\n
    getLong(final CharSequence name, final long defaultValue)\n
    '''
def getFloat():
    '''returns float\n\n
    getFloat(final CharSequence name)\n
    getFloat(final CharSequence name, final float defaultValue)\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final CharSequence name)\n
    getDouble(final CharSequence name, final double defaultValue)\n
    '''
def getTimeMillis():
    '''returns long\n\n
    getTimeMillis(final CharSequence name)\n
    getTimeMillis(final CharSequence name, final long defaultValue)\n
    '''
def getBooleanAndRemove():
    '''returns boolean\n\n
    getBooleanAndRemove(final CharSequence name)\n
    getBooleanAndRemove(final CharSequence name, final boolean defaultValue)\n
    '''
def getByteAndRemove():
    '''returns byte\n\n
    getByteAndRemove(final CharSequence name)\n
    getByteAndRemove(final CharSequence name, final byte defaultValue)\n
    '''
def getCharAndRemove():
    '''returns char\n\n
    getCharAndRemove(final CharSequence name)\n
    getCharAndRemove(final CharSequence name, final char defaultValue)\n
    '''
def getShortAndRemove():
    '''returns short\n\n
    getShortAndRemove(final CharSequence name)\n
    getShortAndRemove(final CharSequence name, final short defaultValue)\n
    '''
def getIntAndRemove():
    '''returns int\n\n
    getIntAndRemove(final CharSequence name)\n
    getIntAndRemove(final CharSequence name, final int defaultValue)\n
    '''
def getLongAndRemove():
    '''returns long\n\n
    getLongAndRemove(final CharSequence name)\n
    getLongAndRemove(final CharSequence name, final long defaultValue)\n
    '''
def getFloatAndRemove():
    '''returns float\n\n
    getFloatAndRemove(final CharSequence name)\n
    getFloatAndRemove(final CharSequence name, final float defaultValue)\n
    '''
def getDoubleAndRemove():
    '''returns double\n\n
    getDoubleAndRemove(final CharSequence name)\n
    getDoubleAndRemove(final CharSequence name, final double defaultValue)\n
    '''
def getTimeMillisAndRemove():
    '''returns long\n\n
    getTimeMillisAndRemove(final CharSequence name)\n
    getTimeMillisAndRemove(final CharSequence name, final long defaultValue)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final CharSequence name)\n
    contains(final CharSequence name, final CharSequence value)\n
    contains(final CharSequence name, final CharSequence value, final boolean caseInsensitive)\n
    '''
def containsObject():
    '''returns boolean\n\n
    containsObject(final CharSequence name, final Object value)\n
    '''
def containsBoolean():
    '''returns boolean\n\n
    containsBoolean(final CharSequence name, final boolean value)\n
    '''
def containsByte():
    '''returns boolean\n\n
    containsByte(final CharSequence name, final byte value)\n
    '''
def containsChar():
    '''returns boolean\n\n
    containsChar(final CharSequence name, final char value)\n
    '''
def containsShort():
    '''returns boolean\n\n
    containsShort(final CharSequence name, final short value)\n
    '''
def containsInt():
    '''returns boolean\n\n
    containsInt(final CharSequence name, final int value)\n
    '''
def containsLong():
    '''returns boolean\n\n
    containsLong(final CharSequence name, final long value)\n
    '''
def containsFloat():
    '''returns boolean\n\n
    containsFloat(final CharSequence name, final float value)\n
    '''
def containsDouble():
    '''returns boolean\n\n
    containsDouble(final CharSequence name, final double value)\n
    '''
def containsTimeMillis():
    '''returns boolean\n\n
    containsTimeMillis(final CharSequence name, final long value)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def names():
    '''returns Set<CharSequence>\n\n
    names()\n
    '''
def add():
    '''returns Http2Headers\n\n
    add(final CharSequence name, final CharSequence value)\n
    add(final CharSequence name, final Iterable<? extends CharSequence> values)\n
    add(final CharSequence name, final CharSequence... values)\n
    add(final Headers<? extends CharSequence, ? extends CharSequence, ?> headers)\n
    '''
def addObject():
    '''returns Http2Headers\n\n
    addObject(final CharSequence name, final Object value)\n
    addObject(final CharSequence name, final Iterable<?> values)\n
    addObject(final CharSequence name, final Object... values)\n
    '''
def addBoolean():
    '''returns Http2Headers\n\n
    addBoolean(final CharSequence name, final boolean value)\n
    '''
def addByte():
    '''returns Http2Headers\n\n
    addByte(final CharSequence name, final byte value)\n
    '''
def addChar():
    '''returns Http2Headers\n\n
    addChar(final CharSequence name, final char value)\n
    '''
def addShort():
    '''returns Http2Headers\n\n
    addShort(final CharSequence name, final short value)\n
    '''
def addInt():
    '''returns Http2Headers\n\n
    addInt(final CharSequence name, final int value)\n
    '''
def addLong():
    '''returns Http2Headers\n\n
    addLong(final CharSequence name, final long value)\n
    '''
def addFloat():
    '''returns Http2Headers\n\n
    addFloat(final CharSequence name, final float value)\n
    '''
def addDouble():
    '''returns Http2Headers\n\n
    addDouble(final CharSequence name, final double value)\n
    '''
def addTimeMillis():
    '''returns Http2Headers\n\n
    addTimeMillis(final CharSequence name, final long value)\n
    '''
def set():
    '''returns Http2Headers\n\n
    set(final CharSequence name, final CharSequence value)\n
    set(final CharSequence name, final Iterable<? extends CharSequence> values)\n
    set(final CharSequence name, final CharSequence... values)\n
    set(final Headers<? extends CharSequence, ? extends CharSequence, ?> headers)\n
    '''
def setObject():
    '''returns Http2Headers\n\n
    setObject(final CharSequence name, final Object value)\n
    setObject(final CharSequence name, final Iterable<?> values)\n
    setObject(final CharSequence name, final Object... values)\n
    '''
def setBoolean():
    '''returns Http2Headers\n\n
    setBoolean(final CharSequence name, final boolean value)\n
    '''
def setByte():
    '''returns Http2Headers\n\n
    setByte(final CharSequence name, final byte value)\n
    '''
def setChar():
    '''returns Http2Headers\n\n
    setChar(final CharSequence name, final char value)\n
    '''
def setShort():
    '''returns Http2Headers\n\n
    setShort(final CharSequence name, final short value)\n
    '''
def setInt():
    '''returns Http2Headers\n\n
    setInt(final CharSequence name, final int value)\n
    '''
def setLong():
    '''returns Http2Headers\n\n
    setLong(final CharSequence name, final long value)\n
    '''
def setFloat():
    '''returns Http2Headers\n\n
    setFloat(final CharSequence name, final float value)\n
    '''
def setDouble():
    '''returns Http2Headers\n\n
    setDouble(final CharSequence name, final double value)\n
    '''
def setTimeMillis():
    '''returns Http2Headers\n\n
    setTimeMillis(final CharSequence name, final long value)\n
    '''
def setAll():
    '''returns Http2Headers\n\n
    setAll(final Headers<? extends CharSequence, ? extends CharSequence, ?> headers)\n
    '''
def remove():
    '''returns None\n\n
    remove(final CharSequence name)\n
    remove()\n
    remove()\n
    '''
def clear():
    '''returns Http2Headers\n\n
    clear()\n
    '''
def valueIterator():
    '''returns Iterator<CharSequence>\n\n
    valueIterator(final CharSequence name)\n
    '''
def method():
    '''returns CharSequence\n\n
    method(final CharSequence value)\n
    method()\n
    '''
def scheme():
    '''returns CharSequence\n\n
    scheme(final CharSequence value)\n
    scheme()\n
    '''
def authority():
    '''returns CharSequence\n\n
    authority(final CharSequence value)\n
    authority()\n
    '''
def path():
    '''returns CharSequence\n\n
    path(final CharSequence value)\n
    path()\n
    '''
def status():
    '''returns CharSequence\n\n
    status(final CharSequence value)\n
    status()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    '''
def next():
    '''returns CharSequence\n\n
    next()\n
    '''
def getKey():
    '''returns CharSequence\n\n
    getKey()\n
    '''
def getValue():
    '''returns CharSequence\n\n
    getValue()\n
    '''
def setValue():
    '''returns CharSequence\n\n
    setValue(final CharSequence value)\n
    '''
