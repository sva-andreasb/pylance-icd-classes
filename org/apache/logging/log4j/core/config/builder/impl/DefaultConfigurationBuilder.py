def formatXml():
'''public static void formatXml(final Source source, final Result result)
'''
pass
def DefaultConfigurationBuilder():
'''public DefaultConfigurationBuilder()
public DefaultConfigurationBuilder(final Class<T> clazz)
'''
pass
def add():
'''public ConfigurationBuilder<T> add(final AppenderComponentBuilder builder)
public ConfigurationBuilder<T> add(final CustomLevelComponentBuilder builder)
public ConfigurationBuilder<T> add(final FilterComponentBuilder builder)
public ConfigurationBuilder<T> add(final ScriptComponentBuilder builder)
public ConfigurationBuilder<T> add(final ScriptFileComponentBuilder builder)
public ConfigurationBuilder<T> add(final LoggerComponentBuilder builder)
public ConfigurationBuilder<T> add(final RootLoggerComponentBuilder builder)
'''
pass
def addProperty():
'''public ConfigurationBuilder<T> addProperty(final String key, final String value)
'''
pass
def build():
'''public T build()
public T build(final boolean initialize)
'''
pass
def writeXmlConfiguration():
'''public void writeXmlConfiguration(final OutputStream output)
'''
pass
def toXmlConfiguration():
'''public String toXmlConfiguration()
'''
pass
def newScript():
'''public ScriptComponentBuilder newScript(final String name, final String language, final String text)
'''
pass
def newScriptFile():
'''public ScriptFileComponentBuilder newScriptFile(final String path)
public ScriptFileComponentBuilder newScriptFile(final String name, final String path)
'''
pass
def newAppender():
'''public AppenderComponentBuilder newAppender(final String name, final String type)
'''
pass
def newAppenderRef():
'''public AppenderRefComponentBuilder newAppenderRef(final String ref)
'''
pass
def newAsyncLogger():
'''public LoggerComponentBuilder newAsyncLogger(final String name)
public LoggerComponentBuilder newAsyncLogger(final String name, final boolean includeLocation)
public LoggerComponentBuilder newAsyncLogger(final String name, final Level level)
public LoggerComponentBuilder newAsyncLogger(final String name, final Level level, final boolean includeLocation)
public LoggerComponentBuilder newAsyncLogger(final String name, final String level)
public LoggerComponentBuilder newAsyncLogger(final String name, final String level, final boolean includeLocation)
'''
pass
def newAsyncRootLogger():
'''public RootLoggerComponentBuilder newAsyncRootLogger()
public RootLoggerComponentBuilder newAsyncRootLogger(final boolean includeLocation)
public RootLoggerComponentBuilder newAsyncRootLogger(final Level level)
public RootLoggerComponentBuilder newAsyncRootLogger(final Level level, final boolean includeLocation)
public RootLoggerComponentBuilder newAsyncRootLogger(final String level)
public RootLoggerComponentBuilder newAsyncRootLogger(final String level, final boolean includeLocation)
'''
pass
def newComponent():
'''public <B extends ComponentBuilder<B>> ComponentBuilder<B> newComponent(final String type)
public <B extends ComponentBuilder<B>> ComponentBuilder<B> newComponent(final String name, final String type)
public <B extends ComponentBuilder<B>> ComponentBuilder<B> newComponent(final String name, final String type, final String value)
'''
pass
def newProperty():
'''public PropertyComponentBuilder newProperty(final String name, final String value)
'''
pass
def newKeyValuePair():
'''public KeyValuePairComponentBuilder newKeyValuePair(final String key, final String value)
'''
pass
def newCustomLevel():
'''public CustomLevelComponentBuilder newCustomLevel(final String name, final int level)
'''
pass
def newFilter():
'''public FilterComponentBuilder newFilter(final String type, final Filter.Result onMatch, final Filter.Result onMismatch)
public FilterComponentBuilder newFilter(final String type, final String onMatch, final String onMismatch)
'''
pass
def newLayout():
'''public LayoutComponentBuilder newLayout(final String type)
'''
pass
def newLogger():
'''public LoggerComponentBuilder newLogger(final String name)
public LoggerComponentBuilder newLogger(final String name, final boolean includeLocation)
public LoggerComponentBuilder newLogger(final String name, final Level level)
public LoggerComponentBuilder newLogger(final String name, final Level level, final boolean includeLocation)
public LoggerComponentBuilder newLogger(final String name, final String level)
public LoggerComponentBuilder newLogger(final String name, final String level, final boolean includeLocation)
'''
pass
def newRootLogger():
'''public RootLoggerComponentBuilder newRootLogger()
public RootLoggerComponentBuilder newRootLogger(final boolean includeLocation)
public RootLoggerComponentBuilder newRootLogger(final Level level)
public RootLoggerComponentBuilder newRootLogger(final Level level, final boolean includeLocation)
public RootLoggerComponentBuilder newRootLogger(final String level)
public RootLoggerComponentBuilder newRootLogger(final String level, final boolean includeLocation)
'''
pass
def setAdvertiser():
'''public ConfigurationBuilder<T> setAdvertiser(final String advertiser)
'''
pass
def setConfigurationName():
'''public ConfigurationBuilder<T> setConfigurationName(final String name)
'''
pass
def setConfigurationSource():
'''public ConfigurationBuilder<T> setConfigurationSource(final ConfigurationSource configurationSource)
'''
pass
def setMonitorInterval():
'''public ConfigurationBuilder<T> setMonitorInterval(final String intervalSeconds)
'''
pass
def setPackages():
'''public ConfigurationBuilder<T> setPackages(final String packages)
'''
pass
def setShutdownHook():
'''public ConfigurationBuilder<T> setShutdownHook(final String flag)
'''
pass
def setShutdownTimeout():
'''public ConfigurationBuilder<T> setShutdownTimeout(final long timeout, final TimeUnit timeUnit)
'''
pass
def setStatusLevel():
'''public ConfigurationBuilder<T> setStatusLevel(final Level level)
'''
pass
def setVerbosity():
'''public ConfigurationBuilder<T> setVerbosity(final String verbosity)
'''
pass
def setDestination():
'''public ConfigurationBuilder<T> setDestination(final String destination)
'''
pass
def setLoggerContext():
'''public void setLoggerContext(final LoggerContext loggerContext)
'''
pass
def addRootProperty():
'''public ConfigurationBuilder<T> addRootProperty(final String key, final String value)
'''
pass
