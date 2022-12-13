def getConfigurationSource():
    '''    public ConfigurationSource getConfigurationSource()
    '''
def getPluginPackages():
    '''    public List<String> getPluginPackages()
    '''
def getProperties():
    '''    public Map<String, String> getProperties()
    '''
def getScriptManager():
    '''    public ScriptManager getScriptManager()
    '''
def setScriptManager():
    '''    public void setScriptManager(final ScriptManager scriptManager)
    '''
def getPluginManager():
    '''    public PluginManager getPluginManager()
    '''
def setPluginManager():
    '''    public void setPluginManager(final PluginManager pluginManager)
    '''
def getWatchManager():
    '''    public WatchManager getWatchManager()
    '''
def getScheduler():
    '''    public ConfigurationScheduler getScheduler()
    '''
def getRootNode():
    '''    public Node getRootNode()
    '''
def getAsyncLoggerConfigDelegate():
    '''    public AsyncLoggerConfigDelegate getAsyncLoggerConfigDelegate()
    '''
def initialize():
    '''    public void initialize()
    '''
def start():
    '''    public void start()
    '''
def stop():
    '''    public boolean stop(final long timeout, final TimeUnit timeUnit)
    '''
def isShutdownHookEnabled():
    '''    public boolean isShutdownHookEnabled()
    '''
def getShutdownTimeoutMillis():
    '''    public long getShutdownTimeoutMillis()
    '''
def setup():
    '''    public void setup()
    '''
def getComponent():
    '''    public <T> T getComponent(final String componentName)
    '''
def addComponent():
    '''    public void addComponent(final String componentName, final Object obj)
    '''
def setName():
    '''    public void setName(final String name)
    '''
def getName():
    '''    public String getName()
    '''
def addListener():
    '''    public void addListener(final ConfigurationListener listener)
    '''
def removeListener():
    '''    public void removeListener(final ConfigurationListener listener)
    '''
def getAppender():
    '''    public <T extends Appender> T getAppender(final String appenderName)
    '''
def getAppenders():
    '''    public Map<String, Appender> getAppenders()
    '''
def addAppender():
    '''    public void addAppender(final Appender appender)
    '''
def getStrSubstitutor():
    '''    public StrSubstitutor getStrSubstitutor()
    '''
def getConfigurationStrSubstitutor():
    '''    public StrSubstitutor getConfigurationStrSubstitutor()
    '''
def setAdvertiser():
    '''    public void setAdvertiser(final Advertiser advertiser)
    '''
def getAdvertiser():
    '''    public Advertiser getAdvertiser()
    '''
def getReliabilityStrategy():
    '''    public ReliabilityStrategy getReliabilityStrategy(final LoggerConfig loggerConfig)
    '''
def addLoggerAppender():
    '''    public synchronized void addLoggerAppender(final Logger logger, final Appender appender)
    '''
def addLoggerFilter():
    '''    public synchronized void addLoggerFilter(final Logger logger, final Filter filter)
    '''
def setLoggerAdditive():
    '''    public synchronized void setLoggerAdditive(final Logger logger, final boolean additive)
    '''
def removeAppender():
    '''    public synchronized void removeAppender(final String appenderName)
    '''
def getCustomLevels():
    '''    public List<CustomLevelConfig> getCustomLevels()
    '''
def getLoggerConfig():
    '''    public LoggerConfig getLoggerConfig(final String loggerName)
    '''
def getLoggerContext():
    '''    public LoggerContext getLoggerContext()
    '''
def getRootLogger():
    '''    public LoggerConfig getRootLogger()
    '''
def getLoggers():
    '''    public Map<String, LoggerConfig> getLoggers()
    '''
def getLogger():
    '''    public LoggerConfig getLogger(final String loggerName)
    '''
def addLogger():
    '''    public synchronized void addLogger(final String loggerName, final LoggerConfig loggerConfig)
    '''
def removeLogger():
    '''    public synchronized void removeLogger(final String loggerName)
    '''
def createConfiguration():
    '''    public void createConfiguration(final Node node, final LogEvent event)
    '''
def createPluginObject():
    '''    public Object createPluginObject(final PluginType<?> type, final Node node)
    '''
def getNanoClock():
    '''    public NanoClock getNanoClock()
    '''
def setNanoClock():
    '''    public void setNanoClock(final NanoClock nanoClock)
    '''
