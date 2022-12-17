def ():
    '''returns ReadOnlyHttpHeaders\n\n
    (final boolean validateHeaders, final CharSequence... nameValuePairs)\n
    '''
def get():
    '''returns String\n\n
    get(final String name)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final CharSequence name)\n
    getInt(final CharSequence name, final int defaultValue)\n
    '''
def getShort():
    '''returns short\n\n
    getShort(final CharSequence name)\n
    getShort(final CharSequence name, final short defaultValue)\n
    '''
def getTimeMillis():
    '''returns long\n\n
    getTimeMillis(final CharSequence name)\n
    getTimeMillis(final CharSequence name, final long defaultValue)\n
    '''
def getAll():
    '''returns List<String>\n\n
    getAll(final String name)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final String name)\n
    contains(final String name, final String value, final boolean ignoreCase)\n
    '''
def containsValue():
    '''returns boolean\n\n
    containsValue(final CharSequence name, final CharSequence value, final boolean ignoreCase)\n
    '''
def valueStringIterator():
    '''returns Iterator<String>\n\n
    valueStringIterator(final CharSequence name)\n
    '''
def valueCharSequenceIterator():
    '''returns Iterator<CharSequence>\n\n
    valueCharSequenceIterator(final CharSequence name)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def names():
    '''returns Set<String>\n\n
    names()\n
    '''
def add():
    '''returns HttpHeaders\n\n
    add(final String name, final Object value)\n
    add(final String name, final Iterable<?> values)\n
    '''
def addInt():
    '''returns HttpHeaders\n\n
    addInt(final CharSequence name, final int value)\n
    '''
def addShort():
    '''returns HttpHeaders\n\n
    addShort(final CharSequence name, final short value)\n
    '''
def set():
    '''returns HttpHeaders\n\n
    set(final String name, final Object value)\n
    set(final String name, final Iterable<?> values)\n
    '''
def setInt():
    '''returns HttpHeaders\n\n
    setInt(final CharSequence name, final int value)\n
    '''
def setShort():
    '''returns HttpHeaders\n\n
    setShort(final CharSequence name, final short value)\n
    '''
def remove():
    '''returns None\n\n
    remove(final String name)\n
    remove()\n
    remove()\n
    remove()\n
    remove()\n
    '''
def clear():
    '''returns HttpHeaders\n\n
    clear()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    hasNext()\n
    hasNext()\n
    '''
def getKey():
    '''returns String\n\n
    getKey()\n
    getKey()\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    getValue()\n
    '''
def setValue():
    '''returns String\n\n
    setValue(final CharSequence value)\n
    setValue(final String value)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def next():
    '''returns CharSequence\n\n
    next()\n
    next()\n
    '''
