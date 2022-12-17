DEFAULT_DELAY = "long  60000L"
DEBUG_KEY = "String  \"log4j.debug\""
def ():
    '''returns PropertiesConfiguration\n\n
    (final LoggerContext loggerContext, final ConfigurationSource source, final int monitorIntervalSeconds)\n
    '''
def doConfigure():
    '''returns None\n\n
    doConfigure()\n
    '''
def reconfigure():
    '''returns Configuration\n\n
    reconfigure()\n
    '''
def parseAppender():
    '''returns Appender\n\n
    parseAppender(final Properties props, final String appenderName)\n
    '''
def parseLayout():
    '''returns Layout\n\n
    parseLayout(final String layoutPrefix, final String appenderName, final Properties props)\n
    '''
def parseErrorHandler():
    '''returns ErrorHandler\n\n
    parseErrorHandler(final Properties props, final String errorHandlerPrefix, final String errorHandlerClass, final Appender appender)\n
    '''
def addProperties():
    '''returns None\n\n
    addProperties(final Object obj, final String[] keys, final Properties props, final String prefix)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
