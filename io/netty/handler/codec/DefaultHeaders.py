def ():
    '''returns DefaultHeaders\n\n
    (final ValueConverter<V> valueConverter)\n
    (final ValueConverter<V> valueConverter, final NameValidator<K> nameValidator)\n
    (final HashingStrategy<K> nameHashingStrategy, final ValueConverter<V> valueConverter)\n
    (final HashingStrategy<K> nameHashingStrategy, final ValueConverter<V> valueConverter, final NameValidator<K> nameValidator)\n
    (final HashingStrategy<K> nameHashingStrategy, final ValueConverter<V> valueConverter, final NameValidator<K> nameValidator, final int arraySizeHint)\n
    '''
def get():
    '''returns V\n\n
    get(final K name)\n
    get(final K name, final V defaultValue)\n
    '''
def getAndRemove():
    '''returns V\n\n
    getAndRemove(final K name)\n
    getAndRemove(final K name, final V defaultValue)\n
    '''
def getAll():
    '''returns List<V>\n\n
    getAll(final K name)\n
    '''
def valueIterator():
    '''returns Iterator<V>\n\n
    valueIterator(final K name)\n
    '''
def getAllAndRemove():
    '''returns List<V>\n\n
    getAllAndRemove(final K name)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final K name)\n
    contains(final K name, final V value)\n
    '''
def containsObject():
    '''returns boolean\n\n
    containsObject(final K name, final Object value)\n
    '''
def containsBoolean():
    '''returns boolean\n\n
    containsBoolean(final K name, final boolean value)\n
    '''
def containsByte():
    '''returns boolean\n\n
    containsByte(final K name, final byte value)\n
    '''
def containsChar():
    '''returns boolean\n\n
    containsChar(final K name, final char value)\n
    '''
def containsShort():
    '''returns boolean\n\n
    containsShort(final K name, final short value)\n
    '''
def containsInt():
    '''returns boolean\n\n
    containsInt(final K name, final int value)\n
    '''
def containsLong():
    '''returns boolean\n\n
    containsLong(final K name, final long value)\n
    '''
def containsFloat():
    '''returns boolean\n\n
    containsFloat(final K name, final float value)\n
    '''
def containsDouble():
    '''returns boolean\n\n
    containsDouble(final K name, final double value)\n
    '''
def containsTimeMillis():
    '''returns boolean\n\n
    containsTimeMillis(final K name, final long value)\n
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
    '''returns Set<K>\n\n
    names()\n
    '''
def add():
    '''returns T\n\n
    add(final K name, final V value)\n
    add(final K name, final Iterable<? extends V> values)\n
    add(final K name, final V... values)\n
    add(final Headers<? extends K, ? extends V, ?> headers)\n
    '''
def addObject():
    '''returns T\n\n
    addObject(final K name, final Object value)\n
    addObject(final K name, final Iterable<?> values)\n
    addObject(final K name, final Object... values)\n
    '''
def addInt():
    '''returns T\n\n
    addInt(final K name, final int value)\n
    '''
def addLong():
    '''returns T\n\n
    addLong(final K name, final long value)\n
    '''
def addDouble():
    '''returns T\n\n
    addDouble(final K name, final double value)\n
    '''
def addTimeMillis():
    '''returns T\n\n
    addTimeMillis(final K name, final long value)\n
    '''
def addChar():
    '''returns T\n\n
    addChar(final K name, final char value)\n
    '''
def addBoolean():
    '''returns T\n\n
    addBoolean(final K name, final boolean value)\n
    '''
def addFloat():
    '''returns T\n\n
    addFloat(final K name, final float value)\n
    '''
def addByte():
    '''returns T\n\n
    addByte(final K name, final byte value)\n
    '''
def addShort():
    '''returns T\n\n
    addShort(final K name, final short value)\n
    '''
def set():
    '''returns T\n\n
    set(final K name, final V value)\n
    set(final K name, final Iterable<? extends V> values)\n
    set(final K name, final V... values)\n
    set(final Headers<? extends K, ? extends V, ?> headers)\n
    '''
def setObject():
    '''returns T\n\n
    setObject(final K name, final Object value)\n
    setObject(final K name, final Iterable<?> values)\n
    setObject(final K name, final Object... values)\n
    '''
def setInt():
    '''returns T\n\n
    setInt(final K name, final int value)\n
    '''
def setLong():
    '''returns T\n\n
    setLong(final K name, final long value)\n
    '''
def setDouble():
    '''returns T\n\n
    setDouble(final K name, final double value)\n
    '''
def setTimeMillis():
    '''returns T\n\n
    setTimeMillis(final K name, final long value)\n
    '''
def setFloat():
    '''returns T\n\n
    setFloat(final K name, final float value)\n
    '''
def setChar():
    '''returns T\n\n
    setChar(final K name, final char value)\n
    '''
def setBoolean():
    '''returns T\n\n
    setBoolean(final K name, final boolean value)\n
    '''
def setByte():
    '''returns T\n\n
    setByte(final K name, final byte value)\n
    '''
def setShort():
    '''returns T\n\n
    setShort(final K name, final short value)\n
    '''
def setAll():
    '''returns T\n\n
    setAll(final Headers<? extends K, ? extends V, ?> headers)\n
    '''
def remove():
    '''returns None\n\n
    remove(final K name)\n
    remove()\n
    remove()\n
    '''
def clear():
    '''returns T\n\n
    clear()\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final K name)\n
    getBoolean(final K name, final boolean defaultValue)\n
    '''
def getByte():
    '''returns byte\n\n
    getByte(final K name)\n
    getByte(final K name, final byte defaultValue)\n
    '''
def getChar():
    '''returns char\n\n
    getChar(final K name)\n
    getChar(final K name, final char defaultValue)\n
    '''
def getShort():
    '''returns short\n\n
    getShort(final K name)\n
    getShort(final K name, final short defaultValue)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final K name)\n
    getInt(final K name, final int defaultValue)\n
    '''
def getLong():
    '''returns long\n\n
    getLong(final K name)\n
    getLong(final K name, final long defaultValue)\n
    '''
def getFloat():
    '''returns float\n\n
    getFloat(final K name)\n
    getFloat(final K name, final float defaultValue)\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final K name)\n
    getDouble(final K name, final double defaultValue)\n
    '''
def getTimeMillis():
    '''returns long\n\n
    getTimeMillis(final K name)\n
    getTimeMillis(final K name, final long defaultValue)\n
    '''
def getBooleanAndRemove():
    '''returns boolean\n\n
    getBooleanAndRemove(final K name)\n
    getBooleanAndRemove(final K name, final boolean defaultValue)\n
    '''
def getByteAndRemove():
    '''returns byte\n\n
    getByteAndRemove(final K name)\n
    getByteAndRemove(final K name, final byte defaultValue)\n
    '''
def getCharAndRemove():
    '''returns char\n\n
    getCharAndRemove(final K name)\n
    getCharAndRemove(final K name, final char defaultValue)\n
    '''
def getShortAndRemove():
    '''returns short\n\n
    getShortAndRemove(final K name)\n
    getShortAndRemove(final K name, final short defaultValue)\n
    '''
def getIntAndRemove():
    '''returns int\n\n
    getIntAndRemove(final K name)\n
    getIntAndRemove(final K name, final int defaultValue)\n
    '''
def getLongAndRemove():
    '''returns long\n\n
    getLongAndRemove(final K name)\n
    getLongAndRemove(final K name, final long defaultValue)\n
    '''
def getFloatAndRemove():
    '''returns float\n\n
    getFloatAndRemove(final K name)\n
    getFloatAndRemove(final K name, final float defaultValue)\n
    '''
def getDoubleAndRemove():
    '''returns double\n\n
    getDoubleAndRemove(final K name)\n
    getDoubleAndRemove(final K name, final double defaultValue)\n
    '''
def getTimeMillisAndRemove():
    '''returns long\n\n
    getTimeMillisAndRemove(final K name)\n
    getTimeMillisAndRemove(final K name, final long defaultValue)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def validateName():
    '''returns None\n\n
    validateName(final Object name)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    '''
def next():
    '''returns V\n\n
    next()\n
    '''
