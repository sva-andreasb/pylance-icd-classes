MAX_STATUS_ENTRIES = "String  \"log4j2.status.entries\""
DEFAULT_STATUS_LISTENER_LEVEL = "String  \"log4j2.StatusLogger.level\""
STATUS_DATE_FORMAT = "String  \"log4j2.StatusLogger.DateFormat\""
def setLevel():
    '''returns None\n\n
    setLevel(final Level level)\n
    '''
def registerListener():
    '''returns None\n\n
    registerListener(final StatusListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final StatusListener listener)\n
    '''
def updateListenerLevel():
    '''returns None\n\n
    updateListenerLevel(final Level status)\n
    '''
def getListeners():
    '''returns Iterable<StatusListener>\n\n
    getListeners()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getStatusData():
    '''returns List<StatusData>\n\n
    getStatusData()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getLevel():
    '''returns Level\n\n
    getLevel()\n
    '''
def logMessage():
    '''returns None\n\n
    logMessage(final String fqcn, final Level level, final Marker marker, final Message msg, final Throwable t)\n
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
    isEnabled(final Level level, final Marker marker)\n
    '''
def add():
    '''returns boolean\n\n
    add(final E object)\n
    '''
