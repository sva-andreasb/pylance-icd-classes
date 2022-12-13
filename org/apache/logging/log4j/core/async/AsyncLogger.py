def AsyncLogger():
    '''public AsyncLogger(final LoggerContext context, final String name, final MessageFactory messageFactory, final AsyncLoggerDisruptor loggerDisruptor)
    '''
def logMessage():
    '''public void logMessage(final String fqcn, final Level level, final Marker marker, final Message message, final Throwable thrown)
    '''
def log():
    '''public void log(final Level level, final Marker marker, final String fqcn, final StackTraceElement location, final Message message, final Throwable throwable)
    '''
def translateTo():
    '''public void translateTo(final RingBufferLogEvent event, final long sequence, final Object... args)
    '''
def actualAsyncLog():
    '''public void actualAsyncLog(final RingBufferLogEvent event)
    '''
