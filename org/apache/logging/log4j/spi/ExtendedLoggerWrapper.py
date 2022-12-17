def ():
    '''returns ExtendedLoggerWrapper\n\n
    (final ExtendedLogger logger, final String name, final MessageFactory messageFactory)\n
    '''
def getLevel():
    '''returns Level\n\n
    getLevel()\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final Level level, final Marker marker, final Message message, final Throwable t)\n
    isEnabled(final Level level, final Marker marker, final CharSequence message, final Throwable t)\n
    isEnabled(final Level level, final Marker marker, final Object message, final Throwable t)\n
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
    isEnabled(final Level level, final Marker marker, final String message, final Throwable t)\n
    '''
def logMessage():
    '''returns None\n\n
    logMessage(final String fqcn, final Level level, final Marker marker, final Message message, final Throwable t)\n
    '''
