def getConfigurationSource():
    '''returns ConfigurationSource\n\n
    getConfigurationSource()\n
    '''
def getPluginPackages():
    '''returns List<String>\n\n
    getPluginPackages()\n
    '''
def getScriptManager():
    '''returns ScriptManager\n\n
    getScriptManager()\n
    '''
def setScriptManager():
    '''returns None\n\n
    setScriptManager(final ScriptManager scriptManager)\n
    '''
def getPluginManager():
    '''returns PluginManager\n\n
    getPluginManager()\n
    '''
def setPluginManager():
    '''returns None\n\n
    setPluginManager(final PluginManager pluginManager)\n
    '''
def getWatchManager():
    '''returns WatchManager\n\n
    getWatchManager()\n
    '''
def getScheduler():
    '''returns ConfigurationScheduler\n\n
    getScheduler()\n
    '''
def getRootNode():
    '''returns Node\n\n
    getRootNode()\n
    '''
def getAsyncLoggerConfigDelegate():
    '''returns AsyncLoggerConfigDelegate\n\n
    getAsyncLoggerConfigDelegate()\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def stop():
    '''returns boolean\n\n
    stop(final long timeout, final TimeUnit timeUnit)\n
    '''
def isShutdownHookEnabled():
    '''returns boolean\n\n
    isShutdownHookEnabled()\n
    '''
def getShutdownTimeoutMillis():
    '''returns long\n\n
    getShutdownTimeoutMillis()\n
    '''
def setup():
    '''returns None\n\n
    setup()\n
    '''
def addComponent():
    '''returns None\n\n
    addComponent(final String componentName, final Object obj)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final ConfigurationListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final ConfigurationListener listener)\n
    '''
def addAppender():
    '''returns None\n\n
    addAppender(final Appender appender)\n
    '''
def getStrSubstitutor():
    '''returns StrSubstitutor\n\n
    getStrSubstitutor()\n
    '''
def getConfigurationStrSubstitutor():
    '''returns StrSubstitutor\n\n
    getConfigurationStrSubstitutor()\n
    '''
def setAdvertiser():
    '''returns None\n\n
    setAdvertiser(final Advertiser advertiser)\n
    '''
def getAdvertiser():
    '''returns Advertiser\n\n
    getAdvertiser()\n
    '''
def getReliabilityStrategy():
    '''returns ReliabilityStrategy\n\n
    getReliabilityStrategy(final LoggerConfig loggerConfig)\n
    '''
def getCustomLevels():
    '''returns List<CustomLevelConfig>\n\n
    getCustomLevels()\n
    '''
def getLoggerConfig():
    '''returns LoggerConfig\n\n
    getLoggerConfig(final String loggerName)\n
    '''
def getLoggerContext():
    '''returns LoggerContext\n\n
    getLoggerContext()\n
    '''
def getRootLogger():
    '''returns LoggerConfig\n\n
    getRootLogger()\n
    '''
def getLogger():
    '''returns LoggerConfig\n\n
    getLogger(final String loggerName)\n
    '''
def createConfiguration():
    '''returns None\n\n
    createConfiguration(final Node node, final LogEvent event)\n
    '''
def createPluginObject():
    '''returns Object\n\n
    createPluginObject(final PluginType<?> type, final Node node)\n
    '''
def getNanoClock():
    '''returns NanoClock\n\n
    getNanoClock()\n
    '''
def setNanoClock():
    '''returns None\n\n
    setNanoClock(final NanoClock nanoClock)\n
    '''
