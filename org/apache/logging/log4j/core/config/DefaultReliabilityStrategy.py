def DefaultReliabilityStrategy():
    '''public DefaultReliabilityStrategy(final LoggerConfig loggerConfig)
    '''
def log():
    '''public void log(final Supplier<LoggerConfig> reconfigured, final String loggerName, final String fqcn, final Marker marker, final Level level, final Message data, final Throwable t)
    public void log(final Supplier<LoggerConfig> reconfigured, final String loggerName, final String fqcn, final StackTraceElement location, final Marker marker, final Level level, final Message data, final Throwable t)
    public void log(final Supplier<LoggerConfig> reconfigured, final LogEvent event)
    '''
def getActiveLoggerConfig():
    '''public LoggerConfig getActiveLoggerConfig(final Supplier<LoggerConfig> next)
    '''
def afterLogEvent():
    '''public void afterLogEvent()
    '''
def beforeStopAppenders():
    '''public void beforeStopAppenders()
    '''
def beforeStopConfiguration():
    '''public void beforeStopConfiguration(final Configuration configuration)
    '''
