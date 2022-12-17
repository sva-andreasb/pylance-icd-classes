def ():
    '''returns DefaultLogBuilder\n\n
    (final Logger logger, final Level level)\n
    (final Logger logger)\n
    '''
def reset():
    '''returns LogBuilder\n\n
    reset(final Level level)\n
    '''
def withMarker():
    '''returns LogBuilder\n\n
    withMarker(final Marker marker)\n
    '''
def withThrowable():
    '''returns LogBuilder\n\n
    withThrowable(final Throwable throwable)\n
    '''
def withLocation():
    '''returns LogBuilder\n\n
    withLocation()\n
    withLocation(final StackTraceElement location)\n
    '''
def isInUse():
    '''returns boolean\n\n
    isInUse()\n
    '''
def log():
    '''returns None\n\n
    log(final Message message)\n
    log(final CharSequence message)\n
    log(final String message)\n
    log(final String message, final Object... params)\n
    log(final String message, final Supplier<?>... params)\n
    log(final Supplier<Message> messageSupplier)\n
    log(final Object message)\n
    log(final String message, final Object p0)\n
    log(final String message, final Object p0, final Object p1)\n
    log(final String message, final Object p0, final Object p1, final Object p2)\n
    log(final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    log(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    log(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    log(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    log(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    log(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    log(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    log()\n
    '''
