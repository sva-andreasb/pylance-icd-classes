ROOT = "String  \"root\""
def ():
    '''returns LoggerConfig\n\n
    ()\n
    (final String name, final Level level, final boolean additive)\n
    '''
def getFilter():
    '''returns Filter\n\n
    getFilter()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final LoggerConfig parent)\n
    '''
def getParent():
    '''returns LoggerConfig\n\n
    getParent()\n
    '''
def addAppender():
    '''returns None\n\n
    addAppender(final Appender appender, final Level level, final Filter filter)\n
    '''
def removeAppender():
    '''returns None\n\n
    removeAppender(final String name)\n
    '''
def getAppenderRefs():
    '''returns List<AppenderRef>\n\n
    getAppenderRefs()\n
    '''
def setLevel():
    '''returns None\n\n
    setLevel(final Level level)\n
    '''
def getLevel():
    '''returns Level\n\n
    getLevel()\n
    '''
def getLogEventFactory():
    '''returns LogEventFactory\n\n
    getLogEventFactory()\n
    '''
def setLogEventFactory():
    '''returns None\n\n
    setLogEventFactory(final LogEventFactory logEventFactory)\n
    '''
def isAdditive():
    '''returns boolean\n\n
    isAdditive()\n
    '''
def setAdditive():
    '''returns None\n\n
    setAdditive(final boolean additive)\n
    '''
def isIncludeLocation():
    '''returns boolean\n\n
    isIncludeLocation()\n
    '''
def getPropertyList():
    '''returns List<Property>\n\n
    getPropertyList()\n
    '''
def isPropertiesRequireLookup():
    '''returns boolean\n\n
    isPropertiesRequireLookup()\n
    '''
def log():
    '''returns None\n\n
    log(final String loggerName, final String fqcn, final Marker marker, final Level level, final Message data, final Throwable t)\n
    log(final String loggerName, final String fqcn, final StackTraceElement location, final Marker marker, final Level level, final Message data, final Throwable t)\n
    log(final LogEvent event)\n
    '''
def getReliabilityStrategy():
    '''returns ReliabilityStrategy\n\n
    getReliabilityStrategy()\n
    '''
def requiresLocation():
    '''returns boolean\n\n
    requiresLocation()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
