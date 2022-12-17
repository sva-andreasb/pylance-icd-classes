def ():
    '''returns StructuredDataMessage\n\n
    (final String id, final String msg, final String type)\n
    (final String id, final String msg, final String type, final int maxLength)\n
    (final String id, final String msg, final String type, final Map<String, String> data)\n
    (final String id, final String msg, final String type, final Map<String, String> data, final int maxLength)\n
    (final StructuredDataId id, final String msg, final String type)\n
    (final StructuredDataId id, final String msg, final String type, final int maxLength)\n
    (final StructuredDataId id, final String msg, final String type, final Map<String, String> data)\n
    (final StructuredDataId id, final String msg, final String type, final Map<String, String> data, final int maxLength)\n
    '''
def getFormats():
    '''returns String[]\n\n
    getFormats()\n
    '''
def getId():
    '''returns StructuredDataId\n\n
    getId()\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
def formatTo():
    '''returns None\n\n
    formatTo(final StringBuilder buffer)\n
    formatTo(final String[] formats, final StringBuilder buffer)\n
    '''
def getFormat():
    '''returns String\n\n
    getFormat()\n
    '''
def asString():
    '''returns String\n\n
    asString()\n
    asString(final String format)\n
    '''
def getFormattedMessage():
    '''returns String\n\n
    getFormattedMessage()\n
    getFormattedMessage(final String[] formats)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def newInstance():
    '''returns StructuredDataMessage\n\n
    newInstance(final Map<String, String> map)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
