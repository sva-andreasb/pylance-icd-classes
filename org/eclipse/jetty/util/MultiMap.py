def ():
    '''returns MultiMap\n\n
    ()\n
    (final Map<K, Object> map)\n
    (final MultiMap<K> map)\n
    (final int capacity)\n
    (final boolean concurrent)\n
    '''
def getValues():
    '''returns List<Object>\n\n
    getValues(final Object name)\n
    '''
def getValue():
    '''returns Object\n\n
    getValue(final Object name, final int i)\n
    '''
def getString():
    '''returns String\n\n
    getString(final Object name)\n
    '''
def get():
    '''returns Object\n\n
    get(final Object name)\n
    '''
def put():
    '''returns Object\n\n
    put(final K name, final Object value)\n
    '''
def putValues():
    '''returns Object\n\n
    putValues(final K name, final List<?> values)\n
    putValues(final K name, final String... values)\n
    '''
def add():
    '''returns None\n\n
    add(final K name, final Object value)\n
    '''
def addValues():
    '''returns None\n\n
    addValues(final K name, final List<?> values)\n
    addValues(final K name, final String[] values)\n
    '''
def removeValue():
    '''returns boolean\n\n
    removeValue(final K name, final Object value)\n
    '''
def putAll():
    '''returns None\n\n
    putAll(final Map<? extends K, ?> m)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def containsKey():
    '''returns boolean\n\n
    containsKey(final Object key)\n
    '''
def containsValue():
    '''returns boolean\n\n
    containsValue(final Object value)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def keySet():
    '''returns Set<K>\n\n
    keySet()\n
    '''
def remove():
    '''returns boolean\n\n
    remove(final Object key)\n
    remove(final Object key, final Object value)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def values():
    '''returns Collection<Object>\n\n
    values()\n
    '''
def putIfAbsent():
    '''returns Object\n\n
    putIfAbsent(final K key, final Object value)\n
    '''
def replace():
    '''returns Object\n\n
    replace(final K key, final Object oldValue, final Object newValue)\n
    replace(final K key, final Object value)\n
    '''
