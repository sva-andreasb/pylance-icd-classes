def AbstractLogger():
'''public AbstractLogger()
public AbstractLogger(final String name)
public AbstractLogger(final String name, final MessageFactory messageFactory)
'''
pass
def checkMessageFactory():
'''public static void checkMessageFactory(final ExtendedLogger logger, final MessageFactory messageFactory)
'''
pass
def catching():
'''public void catching(final Level level, final Throwable throwable)
public void catching(final Throwable throwable)
'''
pass
def debug():
'''public void debug(final Marker marker, final CharSequence message)
public void debug(final Marker marker, final CharSequence message, final Throwable throwable)
public void debug(final Marker marker, final Message message)
public void debug(final Marker marker, final Message message, final Throwable throwable)
public void debug(final Marker marker, final Object message)
public void debug(final Marker marker, final Object message, final Throwable throwable)
public void debug(final Marker marker, final String message)
public void debug(final Marker marker, final String message, final Object... params)
public void debug(final Marker marker, final String message, final Throwable throwable)
public void debug(final Message message)
public void debug(final Message message, final Throwable throwable)
public void debug(final CharSequence message)
public void debug(final CharSequence message, final Throwable throwable)
public void debug(final Object message)
public void debug(final Object message, final Throwable throwable)
public void debug(final String message)
public void debug(final String message, final Object... params)
public void debug(final String message, final Throwable throwable)
public void debug(final Supplier<?> messageSupplier)
public void debug(final Supplier<?> messageSupplier, final Throwable throwable)
public void debug(final Marker marker, final Supplier<?> messageSupplier)
public void debug(final Marker marker, final String message, final Supplier<?>... paramSuppliers)
public void debug(final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)
public void debug(final String message, final Supplier<?>... paramSuppliers)
public void debug(final Marker marker, final MessageSupplier messageSupplier)
public void debug(final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)
public void debug(final MessageSupplier messageSupplier)
public void debug(final MessageSupplier messageSupplier, final Throwable throwable)
public void debug(final Marker marker, final String message, final Object p0)
public void debug(final Marker marker, final String message, final Object p0, final Object p1)
public void debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2)
public void debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void debug(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
public void debug(final String message, final Object p0)
public void debug(final String message, final Object p0, final Object p1)
public void debug(final String message, final Object p0, final Object p1, final Object p2)
public void debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void debug(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
'''
pass
def entry():
'''public void entry()
public void entry(final Object... params)
'''
pass
def error():
'''public void error(final Marker marker, final Message message)
public void error(final Marker marker, final Message message, final Throwable throwable)
public void error(final Marker marker, final CharSequence message)
public void error(final Marker marker, final CharSequence message, final Throwable throwable)
public void error(final Marker marker, final Object message)
public void error(final Marker marker, final Object message, final Throwable throwable)
public void error(final Marker marker, final String message)
public void error(final Marker marker, final String message, final Object... params)
public void error(final Marker marker, final String message, final Throwable throwable)
public void error(final Message message)
public void error(final Message message, final Throwable throwable)
public void error(final CharSequence message)
public void error(final CharSequence message, final Throwable throwable)
public void error(final Object message)
public void error(final Object message, final Throwable throwable)
public void error(final String message)
public void error(final String message, final Object... params)
public void error(final String message, final Throwable throwable)
public void error(final Supplier<?> messageSupplier)
public void error(final Supplier<?> messageSupplier, final Throwable throwable)
public void error(final Marker marker, final Supplier<?> messageSupplier)
public void error(final Marker marker, final String message, final Supplier<?>... paramSuppliers)
public void error(final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)
public void error(final String message, final Supplier<?>... paramSuppliers)
public void error(final Marker marker, final MessageSupplier messageSupplier)
public void error(final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)
public void error(final MessageSupplier messageSupplier)
public void error(final MessageSupplier messageSupplier, final Throwable throwable)
public void error(final Marker marker, final String message, final Object p0)
public void error(final Marker marker, final String message, final Object p0, final Object p1)
public void error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2)
public void error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void error(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
public void error(final String message, final Object p0)
public void error(final String message, final Object p0, final Object p1)
public void error(final String message, final Object p0, final Object p1, final Object p2)
public void error(final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void error(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void error(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void error(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void error(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void error(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void error(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
'''
pass
def exit():
'''public void exit()
public <R> R exit(final R result)
'''
pass
def fatal():
'''public void fatal(final Marker marker, final Message message)
public void fatal(final Marker marker, final Message message, final Throwable throwable)
public void fatal(final Marker marker, final CharSequence message)
public void fatal(final Marker marker, final CharSequence message, final Throwable throwable)
public void fatal(final Marker marker, final Object message)
public void fatal(final Marker marker, final Object message, final Throwable throwable)
public void fatal(final Marker marker, final String message)
public void fatal(final Marker marker, final String message, final Object... params)
public void fatal(final Marker marker, final String message, final Throwable throwable)
public void fatal(final Message message)
public void fatal(final Message message, final Throwable throwable)
public void fatal(final CharSequence message)
public void fatal(final CharSequence message, final Throwable throwable)
public void fatal(final Object message)
public void fatal(final Object message, final Throwable throwable)
public void fatal(final String message)
public void fatal(final String message, final Object... params)
public void fatal(final String message, final Throwable throwable)
public void fatal(final Supplier<?> messageSupplier)
public void fatal(final Supplier<?> messageSupplier, final Throwable throwable)
public void fatal(final Marker marker, final Supplier<?> messageSupplier)
public void fatal(final Marker marker, final String message, final Supplier<?>... paramSuppliers)
public void fatal(final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)
public void fatal(final String message, final Supplier<?>... paramSuppliers)
public void fatal(final Marker marker, final MessageSupplier messageSupplier)
public void fatal(final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)
public void fatal(final MessageSupplier messageSupplier)
public void fatal(final MessageSupplier messageSupplier, final Throwable throwable)
public void fatal(final Marker marker, final String message, final Object p0)
public void fatal(final Marker marker, final String message, final Object p0, final Object p1)
public void fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2)
public void fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void fatal(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
public void fatal(final String message, final Object p0)
public void fatal(final String message, final Object p0, final Object p1)
public void fatal(final String message, final Object p0, final Object p1, final Object p2)
public void fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void fatal(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
'''
pass
def getMessageFactory():
'''public <MF extends MessageFactory> MF getMessageFactory()
'''
pass
def getName():
'''public String getName()
'''
pass
def info():
'''public void info(final Marker marker, final Message message)
public void info(final Marker marker, final Message message, final Throwable throwable)
public void info(final Marker marker, final CharSequence message)
public void info(final Marker marker, final CharSequence message, final Throwable throwable)
public void info(final Marker marker, final Object message)
public void info(final Marker marker, final Object message, final Throwable throwable)
public void info(final Marker marker, final String message)
public void info(final Marker marker, final String message, final Object... params)
public void info(final Marker marker, final String message, final Throwable throwable)
public void info(final Message message)
public void info(final Message message, final Throwable throwable)
public void info(final CharSequence message)
public void info(final CharSequence message, final Throwable throwable)
public void info(final Object message)
public void info(final Object message, final Throwable throwable)
public void info(final String message)
public void info(final String message, final Object... params)
public void info(final String message, final Throwable throwable)
public void info(final Supplier<?> messageSupplier)
public void info(final Supplier<?> messageSupplier, final Throwable throwable)
public void info(final Marker marker, final Supplier<?> messageSupplier)
public void info(final Marker marker, final String message, final Supplier<?>... paramSuppliers)
public void info(final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)
public void info(final String message, final Supplier<?>... paramSuppliers)
public void info(final Marker marker, final MessageSupplier messageSupplier)
public void info(final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)
public void info(final MessageSupplier messageSupplier)
public void info(final MessageSupplier messageSupplier, final Throwable throwable)
public void info(final Marker marker, final String message, final Object p0)
public void info(final Marker marker, final String message, final Object p0, final Object p1)
public void info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2)
public void info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void info(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
public void info(final String message, final Object p0)
public void info(final String message, final Object p0, final Object p1)
public void info(final String message, final Object p0, final Object p1, final Object p2)
public void info(final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void info(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void info(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void info(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void info(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void info(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void info(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
'''
pass
def isDebugEnabled():
'''public boolean isDebugEnabled()
public boolean isDebugEnabled(final Marker marker)
'''
pass
def isEnabled():
'''public boolean isEnabled(final Level level)
public boolean isEnabled(final Level level, final Marker marker)
'''
pass
def isErrorEnabled():
'''public boolean isErrorEnabled()
public boolean isErrorEnabled(final Marker marker)
'''
pass
def isFatalEnabled():
'''public boolean isFatalEnabled()
public boolean isFatalEnabled(final Marker marker)
'''
pass
def isInfoEnabled():
'''public boolean isInfoEnabled()
public boolean isInfoEnabled(final Marker marker)
'''
pass
def isTraceEnabled():
'''public boolean isTraceEnabled()
public boolean isTraceEnabled(final Marker marker)
'''
pass
def isWarnEnabled():
'''public boolean isWarnEnabled()
public boolean isWarnEnabled(final Marker marker)
'''
pass
def log():
'''public void log(final Level level, final Marker marker, final Message message)
public void log(final Level level, final Marker marker, final Message message, final Throwable throwable)
public void log(final Level level, final Marker marker, final CharSequence message)
public void log(final Level level, final Marker marker, final CharSequence message, final Throwable throwable)
public void log(final Level level, final Marker marker, final Object message)
public void log(final Level level, final Marker marker, final Object message, final Throwable throwable)
public void log(final Level level, final Marker marker, final String message)
public void log(final Level level, final Marker marker, final String message, final Object... params)
public void log(final Level level, final Marker marker, final String message, final Throwable throwable)
public void log(final Level level, final Message message)
public void log(final Level level, final Message message, final Throwable throwable)
public void log(final Level level, final CharSequence message)
public void log(final Level level, final CharSequence message, final Throwable throwable)
public void log(final Level level, final Object message)
public void log(final Level level, final Object message, final Throwable throwable)
public void log(final Level level, final String message)
public void log(final Level level, final String message, final Object... params)
public void log(final Level level, final String message, final Throwable throwable)
public void log(final Level level, final Supplier<?> messageSupplier)
public void log(final Level level, final Supplier<?> messageSupplier, final Throwable throwable)
public void log(final Level level, final Marker marker, final Supplier<?> messageSupplier)
public void log(final Level level, final Marker marker, final String message, final Supplier<?>... paramSuppliers)
public void log(final Level level, final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)
public void log(final Level level, final String message, final Supplier<?>... paramSuppliers)
public void log(final Level level, final Marker marker, final MessageSupplier messageSupplier)
public void log(final Level level, final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)
public void log(final Level level, final MessageSupplier messageSupplier)
public void log(final Level level, final MessageSupplier messageSupplier, final Throwable throwable)
public void log(final Level level, final Marker marker, final String message, final Object p0)
public void log(final Level level, final Marker marker, final String message, final Object p0, final Object p1)
public void log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2)
public void log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void log(final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
public void log(final Level level, final String message, final Object p0)
public void log(final Level level, final String message, final Object p0, final Object p1)
public void log(final Level level, final String message, final Object p0, final Object p1, final Object p2)
public void log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void log(final Level level, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
'''
pass
def logIfEnabled():
'''public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final Message message, final Throwable throwable)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final Object message, final Throwable throwable)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final CharSequence message, final Throwable throwable)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Supplier<?>... paramSuppliers)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object... params)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
public void logIfEnabled(final String fqcn, final Level level, final Marker marker, final String message, final Throwable throwable)
'''
pass
def logMessage():
'''public void logMessage(final Level level, final Marker marker, final String fqcn, final StackTraceElement location, final Message message, final Throwable throwable)
'''
pass
def printf():
'''public void printf(final Level level, final Marker marker, final String format, final Object... params)
public void printf(final Level level, final String format, final Object... params)
'''
pass
def getRecursionDepth():
'''public static int getRecursionDepth()
'''
pass
def throwing():
'''public <T extends Throwable> T throwing(final T throwable)
public <T extends Throwable> T throwing(final Level level, final T throwable)
'''
pass
def trace():
'''public void trace(final Marker marker, final Message message)
public void trace(final Marker marker, final Message message, final Throwable throwable)
public void trace(final Marker marker, final CharSequence message)
public void trace(final Marker marker, final CharSequence message, final Throwable throwable)
public void trace(final Marker marker, final Object message)
public void trace(final Marker marker, final Object message, final Throwable throwable)
public void trace(final Marker marker, final String message)
public void trace(final Marker marker, final String message, final Object... params)
public void trace(final Marker marker, final String message, final Throwable throwable)
public void trace(final Message message)
public void trace(final Message message, final Throwable throwable)
public void trace(final CharSequence message)
public void trace(final CharSequence message, final Throwable throwable)
public void trace(final Object message)
public void trace(final Object message, final Throwable throwable)
public void trace(final String message)
public void trace(final String message, final Object... params)
public void trace(final String message, final Throwable throwable)
public void trace(final Supplier<?> messageSupplier)
public void trace(final Supplier<?> messageSupplier, final Throwable throwable)
public void trace(final Marker marker, final Supplier<?> messageSupplier)
public void trace(final Marker marker, final String message, final Supplier<?>... paramSuppliers)
public void trace(final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)
public void trace(final String message, final Supplier<?>... paramSuppliers)
public void trace(final Marker marker, final MessageSupplier messageSupplier)
public void trace(final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)
public void trace(final MessageSupplier messageSupplier)
public void trace(final MessageSupplier messageSupplier, final Throwable throwable)
public void trace(final Marker marker, final String message, final Object p0)
public void trace(final Marker marker, final String message, final Object p0, final Object p1)
public void trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2)
public void trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void trace(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
public void trace(final String message, final Object p0)
public void trace(final String message, final Object p0, final Object p1)
public void trace(final String message, final Object p0, final Object p1, final Object p2)
public void trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void trace(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
'''
pass
def traceEntry():
'''public EntryMessage traceEntry()
public EntryMessage traceEntry(final String format, final Object... params)
public EntryMessage traceEntry(final Supplier<?>... paramSuppliers)
public EntryMessage traceEntry(final String format, final Supplier<?>... paramSuppliers)
public EntryMessage traceEntry(final Message message)
'''
pass
def traceExit():
'''public void traceExit()
public <R> R traceExit(final R result)
public <R> R traceExit(final String format, final R result)
public void traceExit(final EntryMessage message)
public <R> R traceExit(final EntryMessage message, final R result)
public <R> R traceExit(final Message message, final R result)
'''
pass
def warn():
'''public void warn(final Marker marker, final Message message)
public void warn(final Marker marker, final Message message, final Throwable throwable)
public void warn(final Marker marker, final CharSequence message)
public void warn(final Marker marker, final CharSequence message, final Throwable throwable)
public void warn(final Marker marker, final Object message)
public void warn(final Marker marker, final Object message, final Throwable throwable)
public void warn(final Marker marker, final String message)
public void warn(final Marker marker, final String message, final Object... params)
public void warn(final Marker marker, final String message, final Throwable throwable)
public void warn(final Message message)
public void warn(final Message message, final Throwable throwable)
public void warn(final CharSequence message)
public void warn(final CharSequence message, final Throwable throwable)
public void warn(final Object message)
public void warn(final Object message, final Throwable throwable)
public void warn(final String message)
public void warn(final String message, final Object... params)
public void warn(final String message, final Throwable throwable)
public void warn(final Supplier<?> messageSupplier)
public void warn(final Supplier<?> messageSupplier, final Throwable throwable)
public void warn(final Marker marker, final Supplier<?> messageSupplier)
public void warn(final Marker marker, final String message, final Supplier<?>... paramSuppliers)
public void warn(final Marker marker, final Supplier<?> messageSupplier, final Throwable throwable)
public void warn(final String message, final Supplier<?>... paramSuppliers)
public void warn(final Marker marker, final MessageSupplier messageSupplier)
public void warn(final Marker marker, final MessageSupplier messageSupplier, final Throwable throwable)
public void warn(final MessageSupplier messageSupplier)
public void warn(final MessageSupplier messageSupplier, final Throwable throwable)
public void warn(final Marker marker, final String message, final Object p0)
public void warn(final Marker marker, final String message, final Object p0, final Object p1)
public void warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2)
public void warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void warn(final Marker marker, final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
public void warn(final String message, final Object p0)
public void warn(final String message, final Object p0, final Object p1)
public void warn(final String message, final Object p0, final Object p1, final Object p2)
public void warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3)
public void warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4)
public void warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)
public void warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6)
public void warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7)
public void warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8)
public void warn(final String message, final Object p0, final Object p1, final Object p2, final Object p3, final Object p4, final Object p5, final Object p6, final Object p7, final Object p8, final Object p9)
'''
pass
def atTrace():
'''public LogBuilder atTrace()
'''
pass
def atDebug():
'''public LogBuilder atDebug()
'''
pass
def atInfo():
'''public LogBuilder atInfo()
'''
pass
def atWarn():
'''public LogBuilder atWarn()
'''
pass
def atError():
'''public LogBuilder atError()
'''
pass
def atFatal():
'''public LogBuilder atFatal()
'''
pass
def always():
'''public LogBuilder always()
'''
pass
def atLevel():
'''public LogBuilder atLevel(final Level level)
'''
pass