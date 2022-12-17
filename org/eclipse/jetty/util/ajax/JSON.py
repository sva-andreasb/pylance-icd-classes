def ():
    '''returns Literal\n\n
    ()\n
    (final String s)\n
    (final Reader r)\n
    (final String json)\n
    '''
def getStringBufferSize():
    '''returns int\n\n
    getStringBufferSize()\n
    '''
def setStringBufferSize():
    '''returns None\n\n
    setStringBufferSize(final int stringBufferSize)\n
    '''
def toJSON():
    '''returns None\n\n
    toJSON(final Object object)\n
    toJSON(final Output out)\n
    '''
def fromJSON():
    '''returns None\n\n
    fromJSON(final String json)\n
    fromJSON(final Map object)\n
    '''
def append():
    '''returns None\n\n
    append(final StringBuffer buffer, final Object object)\n
    append(final Appendable buffer, final Object object)\n
    '''
def appendNull():
    '''returns None\n\n
    appendNull(final StringBuffer buffer)\n
    appendNull(final Appendable buffer)\n
    '''
def appendJSON():
    '''returns None\n\n
    appendJSON(final StringBuffer buffer, final Convertor convertor, final Object object)\n
    appendJSON(final Appendable buffer, final Convertor convertor, final Object object)\n
    appendJSON(final StringBuffer buffer, final Convertible converter)\n
    appendJSON(final Appendable buffer, final Convertible converter)\n
    appendJSON(final StringBuffer buffer, final Generator generator)\n
    appendJSON(final Appendable buffer, final Generator generator)\n
    '''
def appendMap():
    '''returns None\n\n
    appendMap(final StringBuffer buffer, final Map<?, ?> map)\n
    appendMap(final Appendable buffer, final Map<?, ?> map)\n
    '''
def appendArray():
    '''returns None\n\n
    appendArray(final StringBuffer buffer, final Collection collection)\n
    appendArray(final Appendable buffer, final Collection collection)\n
    appendArray(final StringBuffer buffer, final Object array)\n
    appendArray(final Appendable buffer, final Object array)\n
    '''
def appendBoolean():
    '''returns None\n\n
    appendBoolean(final StringBuffer buffer, final Boolean b)\n
    appendBoolean(final Appendable buffer, final Boolean b)\n
    '''
def appendNumber():
    '''returns None\n\n
    appendNumber(final StringBuffer buffer, final Number number)\n
    appendNumber(final Appendable buffer, final Number number)\n
    '''
def appendString():
    '''returns None\n\n
    appendString(final StringBuffer buffer, final String string)\n
    appendString(final Appendable buffer, final String string)\n
    '''
def addConvertor():
    '''returns None\n\n
    addConvertor(final Class forClass, final Convertor convertor)\n
    '''
def addConvertorFor():
    '''returns None\n\n
    addConvertorFor(final String name, final Convertor convertor)\n
    '''
def getConvertorFor():
    '''returns Convertor\n\n
    getConvertorFor(final String name)\n
    '''
def parse():
    '''returns Object\n\n
    parse(final Source source, final boolean stripOuterComment)\n
    parse(final Source source)\n
    '''
def parseNumber():
    '''returns Number\n\n
    parseNumber(final Source source)\n
    '''
def complete():
    '''returns None\n\n
    complete()\n
    '''
def add():
    '''returns None\n\n
    add(final Object obj)\n
    add(final String name, final Object value)\n
    add(final String name, final double value)\n
    add(final String name, final long value)\n
    add(final String name, final boolean value)\n
    '''
def addClass():
    '''returns None\n\n
    addClass(final Class type)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    '''
def next():
    '''returns char\n\n
    next()\n
    next()\n
    '''
def peek():
    '''returns char\n\n
    peek()\n
    peek()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def scratchBuffer():
    '''returns char[]\n\n
    scratchBuffer()\n
    scratchBuffer()\n
    '''
def setReader():
    '''returns None\n\n
    setReader(final Reader reader)\n
    '''
def addJSON():
    '''returns None\n\n
    addJSON(final Appendable buffer)\n
    '''
