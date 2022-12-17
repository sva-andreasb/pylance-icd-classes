def ():
    '''returns AsyncLogger\n\n
    (final LoggerContext context, final String name, final MessageFactory messageFactory, final AsyncLoggerDisruptor loggerDisruptor)\n
    '''
def logMessage():
    '''returns None\n\n
    logMessage(final String fqcn, final Level level, final Marker marker, final Message message, final Throwable thrown)\n
    '''
def log():
    '''returns None\n\n
    log(final Level level, final Marker marker, final String fqcn, final StackTraceElement location, final Message message, final Throwable throwable)\n
    '''
def translateTo():
    '''returns None\n\n
    translateTo(final RingBufferLogEvent event, final long sequence, final Object... args)\n
    '''
def actualAsyncLog():
    '''returns None\n\n
    actualAsyncLog(final RingBufferLogEvent event)\n
    '''
