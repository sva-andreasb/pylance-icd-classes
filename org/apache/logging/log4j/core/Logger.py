def getParent():
    '''returns Logger\n\n
    getParent()\n
    '''
def getContext():
    '''returns LoggerContext\n\n
    getContext()\n
    '''
def get():
    '''returns LoggerConfig\n\n
    get()\n
    '''
def logMessage():
    '''returns None\n\n
    logMessage(final String fqcn, final Level level, final Marker marker, final Message message, final Throwable t)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final Level level, final Marker marker, final String message, final Throwable t)\n
    isEnabled(final Level level, final Marker marker, final String message)\n
    isEnabled(final Level level, final Marker marker, final String message, final Object... params)\n
    isEnabled(final Level level, final Marker marker, final String message, final Object p0)\n
    isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1)\n
    isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2)\n
    isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    isEnabled(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    isEnabled(final Level level, final Marker marker, final CharSequence message, final Throwable t)\n
    isEnabled(final Level level, final Marker marker, final Object message, final Throwable t)\n
    isEnabled(final Level level, final Marker marker, final Message message, final Throwable t)\n
    '''
def addAppender():
    '''returns None\n\n
    addAppender(final Appender appender)\n
    '''
def removeAppender():
    '''returns None\n\n
    removeAppender(final Appender appender)\n
    '''
def getFilters():
    '''returns Iterator<Filter>\n\n
    getFilters()\n
    '''
def getLevel():
    '''returns Level\n\n
    getLevel()\n
    '''
def filterCount():
    '''returns int\n\n
    filterCount()\n
    '''
def addFilter():
    '''returns None\n\n
    addFilter(final Filter filter)\n
    '''
def isAdditive():
    '''returns boolean\n\n
    isAdditive()\n
    '''
def setAdditive():
    '''returns None\n\n
    setAdditive(final boolean additive)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def ():
    '''returns LoggerProxy\n\n
    (final Configuration config, final Logger logger)\n
    (final PrivateConfig pc, final Level level)\n
    (final PrivateConfig pc, final LoggerConfig lc)\n
    (final String name, final MessageFactory messageFactory)\n
    '''
def logEvent():
    '''returns None\n\n
    logEvent(final LogEvent event)\n
    '''
