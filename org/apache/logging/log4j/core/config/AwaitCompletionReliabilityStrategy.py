def AwaitCompletionReliabilityStrategy():
'''public AwaitCompletionReliabilityStrategy(final LoggerConfig loggerConfig)
'''
pass
def log():
'''public void log(final Supplier<LoggerConfig> reconfigured, final String loggerName, final String fqcn, final Marker marker, final Level level, final Message data, final Throwable t)
public void log(final Supplier<LoggerConfig> reconfigured, final String loggerName, final String fqcn, final StackTraceElement location, final Marker marker, final Level level, final Message data, final Throwable t)
public void log(final Supplier<LoggerConfig> reconfigured, final LogEvent event)
'''
pass
def getActiveLoggerConfig():
'''public LoggerConfig getActiveLoggerConfig(final Supplier<LoggerConfig> next)
'''
pass
def afterLogEvent():
'''public void afterLogEvent()
'''
pass
def beforeStopAppenders():
'''public void beforeStopAppenders()
'''
pass
def beforeStopConfiguration():
'''public void beforeStopConfiguration(final Configuration configuration)
'''
pass
