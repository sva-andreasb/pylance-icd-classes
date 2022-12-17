def ():
    '''returns SimpleLogger\n\n
    (final String name, final Level defaultLevel, final boolean showLogName, final boolean showShortLogName, final boolean showDateTime, final boolean showContextMap, final String dateTimeFormat, final MessageFactory messageFactory, final PropertiesUtil props, final PrintStream stream)\n
    '''
def getLevel():
    '''returns Level\n\n
    getLevel()\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final Level testLevel, final Marker marker, final Message msg, final Throwable t)\n
    isEnabled(final Level testLevel, final Marker marker, final CharSequence msg, final Throwable t)\n
    isEnabled(final Level testLevel, final Marker marker, final Object msg, final Throwable t)\n
    isEnabled(final Level testLevel, final Marker marker, final String msg)\n
    isEnabled(final Level testLevel, final Marker marker, final String msg, final Object... p1)\n
    isEnabled(final Level testLevel, final Marker marker, final String message, final Object p0)\n
    isEnabled(final Level testLevel, final Marker marker, final String message, final Object p0, final Object p1)\n
    isEnabled(final Level testLevel, final Marker marker, final String message, final Object p0, final Object p1, final Object p2)\n
    isEnabled(final Level testLevel, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    isEnabled(final Level testLevel, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    isEnabled(final Level testLevel, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    isEnabled(final Level testLevel, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    isEnabled(final Level testLevel, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    isEnabled(final Level testLevel, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    isEnabled(final Level testLevel, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    isEnabled(final Level testLevel, final Marker marker, final String msg, final Throwable t)\n
    '''
def logMessage():
    '''returns None\n\n
    logMessage(final String fqcn, final Level mgsLevel, final Marker marker, final Message msg, final Throwable throwable)\n
    '''
def setLevel():
    '''returns None\n\n
    setLevel(final Level level)\n
    '''
def setStream():
    '''returns None\n\n
    setStream(final PrintStream stream)\n
    '''
