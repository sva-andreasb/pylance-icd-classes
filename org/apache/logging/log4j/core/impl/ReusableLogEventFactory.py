def ReusableLogEventFactory():
    '''public ReusableLogEventFactory()
    '''
def createEvent():
    '''public LogEvent createEvent(final String loggerName, final Marker marker, final String fqcn, final Level level, final Message message, final List<Property> properties, final Throwable t)
    public LogEvent createEvent(final String loggerName, final Marker marker, final String fqcn, final StackTraceElement location, final Level level, final Message message, final List<Property> properties, final Throwable t)
    '''
def release():
    '''public static void release(final LogEvent logEvent)
    '''
