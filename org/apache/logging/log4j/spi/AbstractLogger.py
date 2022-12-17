def ():
    '''returns AbstractLogger\n\n
    ()\n
    (final String name)\n
    (final String name, final MessageFactory messageFactory)\n
    '''
def catching():
    '''returns None\n\n
    catching(final Level level, final Throwable throwable)\n
    catching(final Throwable throwable)\n
    '''
def debug():
    '''returns None\n\n
    debug(final Marker marker, final CharSequence message)\n
    debug(final Marker marker, final CharSequence message, final Throwable throwable)\n
    debug(final Marker marker, final Message message)\n
    debug(final Marker marker, final Message message, final Throwable throwable)\n
    debug(final Marker marker, final Object message)\n
    debug(final Marker marker, final Object message, final Throwable throwable)\n
    debug(final Marker marker, final String message)\n
    debug(final Marker marker, final String message, final Object... params)\n
    debug(final Marker marker, final String message, final Throwable throwable)\n
    debug(final Message message)\n
    debug(final Message message, final Throwable throwable)\n
    debug(final CharSequence message)\n
    debug(final CharSequence message, final Throwable throwable)\n
    debug(final Object message)\n
    debug(final Object message, final Throwable throwable)\n
    debug(final String message)\n
    debug(final String message, final Object... params)\n
    debug(final String message, final Throwable throwable)\n
    debug(final Supplier<?> messageSupplier)\n
    debug(final Supplier<?> messageSupplier, final Throwable throwable)\n
    debug(final Marker marker, final Supplier<?> messageSupplier)\n
    debug(final Marker marker, final String message, final Supplier<?>... paramSuppliers)\n
    debug(final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)\n
    debug(final String message, final Supplier<?>... paramSuppliers)\n
    debug(final Marker marker, final MessageSupplier messageSupplier)\n
    debug(final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)\n
    debug(final MessageSupplier messageSupplier)\n
    debug(final MessageSupplier messageSupplier, final Throwable throwable)\n
    debug(final Marker marker, final String message, final Object p0)\n
    debug(final Marker marker, final String message, final Object p0, final Object p1)\n
    debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2)\n
    debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    debug(final String message, final Object p0)\n
    debug(final String message, final Object p0, final Object p1)\n
    debug(final String message, final Object p0, final Object p1, final Object p2)\n
    debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    '''
def entry():
    '''returns None\n\n
    entry()\n
    entry(final Object... params)\n
    '''
def error():
    '''returns None\n\n
    error(final Marker marker, final Message message)\n
    error(final Marker marker, final Message message, final Throwable throwable)\n
    error(final Marker marker, final CharSequence message)\n
    error(final Marker marker, final CharSequence message, final Throwable throwable)\n
    error(final Marker marker, final Object message)\n
    error(final Marker marker, final Object message, final Throwable throwable)\n
    error(final Marker marker, final String message)\n
    error(final Marker marker, final String message, final Object... params)\n
    error(final Marker marker, final String message, final Throwable throwable)\n
    error(final Message message)\n
    error(final Message message, final Throwable throwable)\n
    error(final CharSequence message)\n
    error(final CharSequence message, final Throwable throwable)\n
    error(final Object message)\n
    error(final Object message, final Throwable throwable)\n
    error(final String message)\n
    error(final String message, final Object... params)\n
    error(final String message, final Throwable throwable)\n
    error(final Supplier<?> messageSupplier)\n
    error(final Supplier<?> messageSupplier, final Throwable throwable)\n
    error(final Marker marker, final Supplier<?> messageSupplier)\n
    error(final Marker marker, final String message, final Supplier<?>... paramSuppliers)\n
    error(final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)\n
    error(final String message, final Supplier<?>... paramSuppliers)\n
    error(final Marker marker, final MessageSupplier messageSupplier)\n
    error(final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)\n
    error(final MessageSupplier messageSupplier)\n
    error(final MessageSupplier messageSupplier, final Throwable throwable)\n
    error(final Marker marker, final String message, final Object p0)\n
    error(final Marker marker, final String message, final Object p0, final Object p1)\n
    error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2)\n
    error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    error(final String message, final Object p0)\n
    error(final String message, final Object p0, final Object p1)\n
    error(final String message, final Object p0, final Object p1, final Object p2)\n
    error(final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    error(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    error(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    error(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    error(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    error(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    error(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    '''
def exit():
    '''returns None\n\n
    exit()\n
    '''
def fatal():
    '''returns None\n\n
    fatal(final Marker marker, final Message message)\n
    fatal(final Marker marker, final Message message, final Throwable throwable)\n
    fatal(final Marker marker, final CharSequence message)\n
    fatal(final Marker marker, final CharSequence message, final Throwable throwable)\n
    fatal(final Marker marker, final Object message)\n
    fatal(final Marker marker, final Object message, final Throwable throwable)\n
    fatal(final Marker marker, final String message)\n
    fatal(final Marker marker, final String message, final Object... params)\n
    fatal(final Marker marker, final String message, final Throwable throwable)\n
    fatal(final Message message)\n
    fatal(final Message message, final Throwable throwable)\n
    fatal(final CharSequence message)\n
    fatal(final CharSequence message, final Throwable throwable)\n
    fatal(final Object message)\n
    fatal(final Object message, final Throwable throwable)\n
    fatal(final String message)\n
    fatal(final String message, final Object... params)\n
    fatal(final String message, final Throwable throwable)\n
    fatal(final Supplier<?> messageSupplier)\n
    fatal(final Supplier<?> messageSupplier, final Throwable throwable)\n
    fatal(final Marker marker, final Supplier<?> messageSupplier)\n
    fatal(final Marker marker, final String message, final Supplier<?>... paramSuppliers)\n
    fatal(final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)\n
    fatal(final String message, final Supplier<?>... paramSuppliers)\n
    fatal(final Marker marker, final MessageSupplier messageSupplier)\n
    fatal(final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)\n
    fatal(final MessageSupplier messageSupplier)\n
    fatal(final MessageSupplier messageSupplier, final Throwable throwable)\n
    fatal(final Marker marker, final String message, final Object p0)\n
    fatal(final Marker marker, final String message, final Object p0, final Object p1)\n
    fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2)\n
    fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    fatal(final String message, final Object p0)\n
    fatal(final String message, final Object p0, final Object p1)\n
    fatal(final String message, final Object p0, final Object p1, final Object p2)\n
    fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def info():
    '''returns None\n\n
    info(final Marker marker, final Message message)\n
    info(final Marker marker, final Message message, final Throwable throwable)\n
    info(final Marker marker, final CharSequence message)\n
    info(final Marker marker, final CharSequence message, final Throwable throwable)\n
    info(final Marker marker, final Object message)\n
    info(final Marker marker, final Object message, final Throwable throwable)\n
    info(final Marker marker, final String message)\n
    info(final Marker marker, final String message, final Object... params)\n
    info(final Marker marker, final String message, final Throwable throwable)\n
    info(final Message message)\n
    info(final Message message, final Throwable throwable)\n
    info(final CharSequence message)\n
    info(final CharSequence message, final Throwable throwable)\n
    info(final Object message)\n
    info(final Object message, final Throwable throwable)\n
    info(final String message)\n
    info(final String message, final Object... params)\n
    info(final String message, final Throwable throwable)\n
    info(final Supplier<?> messageSupplier)\n
    info(final Supplier<?> messageSupplier, final Throwable throwable)\n
    info(final Marker marker, final Supplier<?> messageSupplier)\n
    info(final Marker marker, final String message, final Supplier<?>... paramSuppliers)\n
    info(final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)\n
    info(final String message, final Supplier<?>... paramSuppliers)\n
    info(final Marker marker, final MessageSupplier messageSupplier)\n
    info(final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)\n
    info(final MessageSupplier messageSupplier)\n
    info(final MessageSupplier messageSupplier, final Throwable throwable)\n
    info(final Marker marker, final String message, final Object p0)\n
    info(final Marker marker, final String message, final Object p0, final Object p1)\n
    info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2)\n
    info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    info(final String message, final Object p0)\n
    info(final String message, final Object p0, final Object p1)\n
    info(final String message, final Object p0, final Object p1, final Object p2)\n
    info(final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    info(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    info(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    info(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    info(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    info(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    info(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    '''
def isDebugEnabled():
    '''returns boolean\n\n
    isDebugEnabled()\n
    isDebugEnabled(final Marker marker)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final Level level)\n
    isEnabled(final Level level, final Marker marker)\n
    '''
def isErrorEnabled():
    '''returns boolean\n\n
    isErrorEnabled()\n
    isErrorEnabled(final Marker marker)\n
    '''
def isFatalEnabled():
    '''returns boolean\n\n
    isFatalEnabled()\n
    isFatalEnabled(final Marker marker)\n
    '''
def isInfoEnabled():
    '''returns boolean\n\n
    isInfoEnabled()\n
    isInfoEnabled(final Marker marker)\n
    '''
def isTraceEnabled():
    '''returns boolean\n\n
    isTraceEnabled()\n
    isTraceEnabled(final Marker marker)\n
    '''
def isWarnEnabled():
    '''returns boolean\n\n
    isWarnEnabled()\n
    isWarnEnabled(final Marker marker)\n
    '''
def log():
    '''returns None\n\n
    log(final Level level, final Marker marker, final Message message)\n
    log(final Level level, final Marker marker, final Message message, final Throwable throwable)\n
    log(final Level level, final Marker marker, final CharSequence message)\n
    log(final Level level, final Marker marker, final CharSequence message, final Throwable throwable)\n
    log(final Level level, final Marker marker, final Object message)\n
    log(final Level level, final Marker marker, final Object message, final Throwable throwable)\n
    log(final Level level, final Marker marker, final String message)\n
    log(final Level level, final Marker marker, final String message, final Object... params)\n
    log(final Level level, final Marker marker, final String message, final Throwable throwable)\n
    log(final Level level, final Message message)\n
    log(final Level level, final Message message, final Throwable throwable)\n
    log(final Level level, final CharSequence message)\n
    log(final Level level, final CharSequence message, final Throwable throwable)\n
    log(final Level level, final Object message)\n
    log(final Level level, final Object message, final Throwable throwable)\n
    log(final Level level, final String message)\n
    log(final Level level, final String message, final Object... params)\n
    log(final Level level, final String message, final Throwable throwable)\n
    log(final Level level, final Supplier<?> messageSupplier)\n
    log(final Level level, final Supplier<?> messageSupplier, final Throwable throwable)\n
    log(final Level level, final Marker marker, final Supplier<?> messageSupplier)\n
    log(final Level level, final Marker marker, final String message, final Supplier<?>... paramSuppliers)\n
    log(final Level level, final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)\n
    log(final Level level, final String message, final Supplier<?>... paramSuppliers)\n
    log(final Level level, final Marker marker, final MessageSupplier messageSupplier)\n
    log(final Level level, final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)\n
    log(final Level level, final MessageSupplier messageSupplier)\n
    log(final Level level, final MessageSupplier messageSupplier, final Throwable throwable)\n
    log(final Level level, final Marker marker, final String message, final Object p0)\n
    log(final Level level, final Marker marker, final String message, final Object p0, final Object p1)\n
    log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2)\n
    log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    log(final Level level, final String message, final Object p0)\n
    log(final Level level, final String message, final Object p0, final Object p1)\n
    log(final Level level, final String message, final Object p0, final Object p1, final Object p2)\n
    log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    '''
def logIfEnabled():
    '''returns None\n\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final Message message, final Throwable throwable)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final Object message, final Throwable throwable)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final CharSequence message, final Throwable throwable)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Supplier<?>... paramSuppliers)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object... params)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Throwable throwable)\n
    '''
def logMessage():
    '''returns None\n\n
    logMessage(final Level level, final Marker marker, final String fqcn, final StackTraceElement location, final Message message, final Throwable throwable)\n
    '''
def printf():
    '''returns None\n\n
    printf(final Level level, final Marker marker, final String format, final Object... params)\n
    printf(final Level level, final String format, final Object... params)\n
    '''
def trace():
    '''returns None\n\n
    trace(final Marker marker, final Message message)\n
    trace(final Marker marker, final Message message, final Throwable throwable)\n
    trace(final Marker marker, final CharSequence message)\n
    trace(final Marker marker, final CharSequence message, final Throwable throwable)\n
    trace(final Marker marker, final Object message)\n
    trace(final Marker marker, final Object message, final Throwable throwable)\n
    trace(final Marker marker, final String message)\n
    trace(final Marker marker, final String message, final Object... params)\n
    trace(final Marker marker, final String message, final Throwable throwable)\n
    trace(final Message message)\n
    trace(final Message message, final Throwable throwable)\n
    trace(final CharSequence message)\n
    trace(final CharSequence message, final Throwable throwable)\n
    trace(final Object message)\n
    trace(final Object message, final Throwable throwable)\n
    trace(final String message)\n
    trace(final String message, final Object... params)\n
    trace(final String message, final Throwable throwable)\n
    trace(final Supplier<?> messageSupplier)\n
    trace(final Supplier<?> messageSupplier, final Throwable throwable)\n
    trace(final Marker marker, final Supplier<?> messageSupplier)\n
    trace(final Marker marker, final String message, final Supplier<?>... paramSuppliers)\n
    trace(final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)\n
    trace(final String message, final Supplier<?>... paramSuppliers)\n
    trace(final Marker marker, final MessageSupplier messageSupplier)\n
    trace(final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)\n
    trace(final MessageSupplier messageSupplier)\n
    trace(final MessageSupplier messageSupplier, final Throwable throwable)\n
    trace(final Marker marker, final String message, final Object p0)\n
    trace(final Marker marker, final String message, final Object p0, final Object p1)\n
    trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2)\n
    trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    trace(final String message, final Object p0)\n
    trace(final String message, final Object p0, final Object p1)\n
    trace(final String message, final Object p0, final Object p1, final Object p2)\n
    trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    '''
def traceEntry():
    '''returns EntryMessage\n\n
    traceEntry()\n
    traceEntry(final String format, final Object... params)\n
    traceEntry(final Supplier<?>... paramSuppliers)\n
    traceEntry(final String format, final Supplier<?>... paramSuppliers)\n
    traceEntry(final Message message)\n
    '''
def traceExit():
    '''returns None\n\n
    traceExit()\n
    traceExit(final EntryMessage message)\n
    '''
def warn():
    '''returns None\n\n
    warn(final Marker marker, final Message message)\n
    warn(final Marker marker, final Message message, final Throwable throwable)\n
    warn(final Marker marker, final CharSequence message)\n
    warn(final Marker marker, final CharSequence message, final Throwable throwable)\n
    warn(final Marker marker, final Object message)\n
    warn(final Marker marker, final Object message, final Throwable throwable)\n
    warn(final Marker marker, final String message)\n
    warn(final Marker marker, final String message, final Object... params)\n
    warn(final Marker marker, final String message, final Throwable throwable)\n
    warn(final Message message)\n
    warn(final Message message, final Throwable throwable)\n
    warn(final CharSequence message)\n
    warn(final CharSequence message, final Throwable throwable)\n
    warn(final Object message)\n
    warn(final Object message, final Throwable throwable)\n
    warn(final String message)\n
    warn(final String message, final Object... params)\n
    warn(final String message, final Throwable throwable)\n
    warn(final Supplier<?> messageSupplier)\n
    warn(final Supplier<?> messageSupplier, final Throwable throwable)\n
    warn(final Marker marker, final Supplier<?> messageSupplier)\n
    warn(final Marker marker, final String message, final Supplier<?>... paramSuppliers)\n
    warn(final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)\n
    warn(final String message, final Supplier<?>... paramSuppliers)\n
    warn(final Marker marker, final MessageSupplier messageSupplier)\n
    warn(final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)\n
    warn(final MessageSupplier messageSupplier)\n
    warn(final MessageSupplier messageSupplier, final Throwable throwable)\n
    warn(final Marker marker, final String message, final Object p0)\n
    warn(final Marker marker, final String message, final Object p0, final Object p1)\n
    warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2)\n
    warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    warn(final String message, final Object p0)\n
    warn(final String message, final Object p0, final Object p1)\n
    warn(final String message, final Object p0, final Object p1, final Object p2)\n
    warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3)\n
    warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)\n
    warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)\n
    warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)\n
    warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)\n
    warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)\n
    '''
def atTrace():
    '''returns LogBuilder\n\n
    atTrace()\n
    '''
def atDebug():
    '''returns LogBuilder\n\n
    atDebug()\n
    '''
def atInfo():
    '''returns LogBuilder\n\n
    atInfo()\n
    '''
def atWarn():
    '''returns LogBuilder\n\n
    atWarn()\n
    '''
def atError():
    '''returns LogBuilder\n\n
    atError()\n
    '''
def atFatal():
    '''returns LogBuilder\n\n
    atFatal()\n
    '''
def always():
    '''returns LogBuilder\n\n
    always()\n
    '''
def atLevel():
    '''returns LogBuilder\n\n
    atLevel(final Level level)\n
    '''
