__COOKIE_DELIM = "String  \"\\"\\\n\r\t\f\b%+ ;=\""
__separators = "String  \", \t\""
def ():
    '''returns HttpFields\n\n
    ()\n
    (final int maxCookieVersion)\n
    '''
def getFieldNames():
    '''returns Enumeration<String>\n\n
    getFieldNames()\n
    '''
def nextElement():
    '''returns String\n\n
    nextElement()\n
    nextElement()\n
    nextElement()\n
    nextElement()\n
    '''
def hasMoreElements():
    '''returns boolean\n\n
    hasMoreElements()\n
    hasMoreElements()\n
    hasMoreElements()\n
    hasMoreElements()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getField():
    '''returns Field\n\n
    getField(final int i)\n
    '''
def containsKey():
    '''returns boolean\n\n
    containsKey(final Buffer name)\n
    containsKey(final String name)\n
    '''
def getStringField():
    '''returns String\n\n
    getStringField(final String name)\n
    getStringField(final Buffer name)\n
    '''
def get():
    '''returns Buffer\n\n
    get(final Buffer name)\n
    '''
def getValues():
    '''returns Enumeration<String>\n\n
    getValues(final String name)\n
    getValues(final Buffer name)\n
    getValues(final String name, final String separators)\n
    '''
def put():
    '''returns None\n\n
    put(final String name, final String value)\n
    put(final Buffer name, final String value)\n
    put(Buffer name, Buffer value)\n
    put(final String name, final List<?> list)\n
    '''
def add():
    '''returns None\n\n
    add(final String name, final String value)\n
    add(Buffer name, Buffer value)\n
    add(final HttpFields fields)\n
    '''
def remove():
    '''returns None\n\n
    remove(final String name)\n
    remove(Buffer name)\n
    '''
def getLongField():
    '''returns long\n\n
    getLongField(final String name)\n
    getLongField(final Buffer name)\n
    '''
def getDateField():
    '''returns long\n\n
    getDateField(final String name)\n
    '''
def putLongField():
    '''returns None\n\n
    putLongField(final Buffer name, final long value)\n
    putLongField(final String name, final long value)\n
    '''
def addLongField():
    '''returns None\n\n
    addLongField(final String name, final long value)\n
    addLongField(final Buffer name, final long value)\n
    '''
def putDateField():
    '''returns None\n\n
    putDateField(final Buffer name, final long date)\n
    putDateField(final String name, final long date)\n
    '''
def addDateField():
    '''returns None\n\n
    addDateField(final String name, final long date)\n
    '''
def addSetCookie():
    '''returns None\n\n
    addSetCookie(final HttpCookie cookie)\n
    addSetCookie(final String name, final String value, final String domain, final String path, final long maxAge, final String comment, final boolean isSecure, final boolean isHttpOnly, int version)\n
    '''
def putTo():
    '''returns None\n\n
    putTo(final Buffer buffer)\n
    putTo(final Buffer buffer)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def formatDate():
    '''returns String\n\n
    formatDate(final long date)\n
    '''
def formatCookieDate():
    '''returns None\n\n
    formatCookieDate(final StringBuilder buf, final long date)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getNameOrdinal():
    '''returns int\n\n
    getNameOrdinal()\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    '''
def getValueBuffer():
    '''returns Buffer\n\n
    getValueBuffer()\n
    '''
def getValueOrdinal():
    '''returns int\n\n
    getValueOrdinal()\n
    '''
def getIntValue():
    '''returns int\n\n
    getIntValue()\n
    '''
def getLongValue():
    '''returns long\n\n
    getLongValue()\n
    '''
