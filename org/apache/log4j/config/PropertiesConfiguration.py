DEFAULT_DELAY = "long  60000L"
DEBUG_KEY = "String  \"log4j.debug\""
def PropertiesConfiguration():
    '''    public PropertiesConfiguration(final LoggerContext loggerContext, final ConfigurationSource source, final int monitorIntervalSeconds)
    '''
def doConfigure():
    '''    public void doConfigure()
    '''
def reconfigure():
    '''    public Configuration reconfigure()
    '''
def parseAppender():
    '''    public Appender parseAppender(final Properties props, final String appenderName)
    '''
def parseLayout():
    '''    public Layout parseLayout(final String layoutPrefix, final String appenderName, final Properties props)
    '''
def parseErrorHandler():
    '''    public ErrorHandler parseErrorHandler(final Properties props, final String errorHandlerPrefix, final String errorHandlerClass, final Appender appender)
    '''
def addProperties():
    '''    public void addProperties(final Object obj, final String[] keys, final Properties props, final String prefix)
    '''
def toString():
    '''    public String toString()
    '''
