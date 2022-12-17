def ():
    '''returns LockingReliabilityStrategy\n\n
    (final LoggerConfig loggerConfig)\n
    '''
def log():
    '''returns None\n\n
    log(final Supplier<LoggerConfig> reconfigured, final String loggerName, final String fqcn, final Marker marker, final Level level, final Message data, final Throwable t)\n
    log(final Supplier<LoggerConfig> reconfigured, final String loggerName, final String fqcn, final StackTraceElement location, final Marker marker, final Level level, final Message data, final Throwable t)\n
    log(final Supplier<LoggerConfig> reconfigured, final LogEvent event)\n
    '''
def getActiveLoggerConfig():
    '''returns LoggerConfig\n\n
    getActiveLoggerConfig(final Supplier<LoggerConfig> next)\n
    '''
def afterLogEvent():
    '''returns None\n\n
    afterLogEvent()\n
    '''
def beforeStopAppenders():
    '''returns None\n\n
    beforeStopAppenders()\n
    '''
def beforeStopConfiguration():
    '''returns None\n\n
    beforeStopConfiguration(final Configuration configuration)\n
    '''
