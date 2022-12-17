def ():
    '''returns Reference\n\n
    (final String msg)\n
    (final String msg, final Throwable rootCause)\n
    (final String msg, final JsonLocation loc)\n
    (final String msg, final JsonLocation loc, final Throwable rootCause)\n
    (final Closeable processor, final String msg)\n
    (final Closeable processor, final String msg, final Throwable problem)\n
    (final Closeable processor, final String msg, final JsonLocation loc)\n
    (final Object from)\n
    (final Object from, final String fieldName)\n
    (final Object from, final int index)\n
    '''
def getPath():
    '''returns List<Reference>\n\n
    getPath()\n
    '''
def getPathReference():
    '''returns StringBuilder\n\n
    getPathReference()\n
    getPathReference(final StringBuilder sb)\n
    '''
def prependPath():
    '''returns None\n\n
    prependPath(final Object referrer, final String fieldName)\n
    prependPath(final Object referrer, final int index)\n
    prependPath(final Reference r)\n
    '''
def getProcessor():
    '''returns Object\n\n
    getProcessor()\n
    '''
def getLocalizedMessage():
    '''returns String\n\n
    getLocalizedMessage()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getFrom():
    '''returns Object\n\n
    getFrom()\n
    '''
def getFieldName():
    '''returns String\n\n
    getFieldName()\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex()\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
