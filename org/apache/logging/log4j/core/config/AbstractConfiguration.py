def getConfigurationSource():
'''public ConfigurationSource getConfigurationSource()
'''
pass
def getPluginPackages():
'''public List<String> getPluginPackages()
'''
pass
def getProperties():
'''public Map<String, String> getProperties()
'''
pass
def getScriptManager():
'''public ScriptManager getScriptManager()
'''
pass
def setScriptManager():
'''public void setScriptManager(final ScriptManager scriptManager)
'''
pass
def getPluginManager():
'''public PluginManager getPluginManager()
'''
pass
def setPluginManager():
'''public void setPluginManager(final PluginManager pluginManager)
'''
pass
def getWatchManager():
'''public WatchManager getWatchManager()
'''
pass
def getScheduler():
'''public ConfigurationScheduler getScheduler()
'''
pass
def getRootNode():
'''public Node getRootNode()
'''
pass
def getAsyncLoggerConfigDelegate():
'''public AsyncLoggerConfigDelegate getAsyncLoggerConfigDelegate()
'''
pass
def initialize():
'''public void initialize()
'''
pass
def start():
'''public void start()
'''
pass
def stop():
'''public boolean stop(final long timeout, final TimeUnit timeUnit)
'''
pass
def isShutdownHookEnabled():
'''public boolean isShutdownHookEnabled()
'''
pass
def getShutdownTimeoutMillis():
'''public long getShutdownTimeoutMillis()
'''
pass
def setup():
'''public void setup()
'''
pass
def getComponent():
'''public <T> T getComponent(final String componentName)
'''
pass
def addComponent():
'''public void addComponent(final String componentName, final Object obj)
'''
pass
def setName():
'''public void setName(final String name)
'''
pass
def getName():
'''public String getName()
'''
pass
def addListener():
'''public void addListener(final ConfigurationListener listener)
'''
pass
def removeListener():
'''public void removeListener(final ConfigurationListener listener)
'''
pass
def getAppender():
'''public <T extends Appender> T getAppender(final String appenderName)
'''
pass
def getAppenders():
'''public Map<String, Appender> getAppenders()
'''
pass
def addAppender():
'''public void addAppender(final Appender appender)
'''
pass
def getStrSubstitutor():
'''public StrSubstitutor getStrSubstitutor()
'''
pass
def getConfigurationStrSubstitutor():
'''public StrSubstitutor getConfigurationStrSubstitutor()
'''
pass
def setAdvertiser():
'''public void setAdvertiser(final Advertiser advertiser)
'''
pass
def getAdvertiser():
'''public Advertiser getAdvertiser()
'''
pass
def getReliabilityStrategy():
'''public ReliabilityStrategy getReliabilityStrategy(final LoggerConfig loggerConfig)
'''
pass
def addLoggerAppender():
'''public synchronized void addLoggerAppender(final Logger logger, final Appender appender)
'''
pass
def addLoggerFilter():
'''public synchronized void addLoggerFilter(final Logger logger, final Filter filter)
'''
pass
def setLoggerAdditive():
'''public synchronized void setLoggerAdditive(final Logger logger, final boolean additive)
'''
pass
def removeAppender():
'''public synchronized void removeAppender(final String appenderName)
'''
pass
def getCustomLevels():
'''public List<CustomLevelConfig> getCustomLevels()
'''
pass
def getLoggerConfig():
'''public LoggerConfig getLoggerConfig(final String loggerName)
'''
pass
def getLoggerContext():
'''public LoggerContext getLoggerContext()
'''
pass
def getRootLogger():
'''public LoggerConfig getRootLogger()
'''
pass
def getLoggers():
'''public Map<String, LoggerConfig> getLoggers()
'''
pass
def getLogger():
'''public LoggerConfig getLogger(final String loggerName)
'''
pass
def addLogger():
'''public synchronized void addLogger(final String loggerName, final LoggerConfig loggerConfig)
'''
pass
def removeLogger():
'''public synchronized void removeLogger(final String loggerName)
'''
pass
def createConfiguration():
'''public void createConfiguration(final Node node, final LogEvent event)
'''
pass
def createPluginObject():
'''public Object createPluginObject(final PluginType<?> type, final Node node)
'''
pass
def getNanoClock():
'''public NanoClock getNanoClock()
'''
pass
def setNanoClock():
'''public void setNanoClock(final NanoClock nanoClock)
'''
pass
