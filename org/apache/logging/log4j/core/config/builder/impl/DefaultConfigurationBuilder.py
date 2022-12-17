def ():
    '''returns DefaultConfigurationBuilder\n\n
    ()\n
    (final Class<T> clazz)\n
    '''
def add():
    '''returns ConfigurationBuilder<T>\n\n
    add(final AppenderComponentBuilder builder)\n
    add(final CustomLevelComponentBuilder builder)\n
    add(final FilterComponentBuilder builder)\n
    add(final ScriptComponentBuilder builder)\n
    add(final ScriptFileComponentBuilder builder)\n
    add(final LoggerComponentBuilder builder)\n
    add(final RootLoggerComponentBuilder builder)\n
    '''
def addProperty():
    '''returns ConfigurationBuilder<T>\n\n
    addProperty(final String key, final String value)\n
    '''
def build():
    '''returns T\n\n
    build()\n
    build(final boolean initialize)\n
    '''
def writeXmlConfiguration():
    '''returns None\n\n
    writeXmlConfiguration(final OutputStream output)\n
    '''
def toXmlConfiguration():
    '''returns String\n\n
    toXmlConfiguration()\n
    '''
def newScript():
    '''returns ScriptComponentBuilder\n\n
    newScript(final String name, final String language, final String text)\n
    '''
def newScriptFile():
    '''returns ScriptFileComponentBuilder\n\n
    newScriptFile(final String path)\n
    newScriptFile(final String name, final String path)\n
    '''
def newAppender():
    '''returns AppenderComponentBuilder\n\n
    newAppender(final String name, final String type)\n
    '''
def newAppenderRef():
    '''returns AppenderRefComponentBuilder\n\n
    newAppenderRef(final String ref)\n
    '''
def newAsyncLogger():
    '''returns LoggerComponentBuilder\n\n
    newAsyncLogger(final String name)\n
    newAsyncLogger(final String name, final boolean includeLocation)\n
    newAsyncLogger(final String name, final Level level)\n
    newAsyncLogger(final String name, final Level level, final boolean includeLocation)\n
    newAsyncLogger(final String name, final String level)\n
    newAsyncLogger(final String name, final String level, final boolean includeLocation)\n
    '''
def newAsyncRootLogger():
    '''returns RootLoggerComponentBuilder\n\n
    newAsyncRootLogger()\n
    newAsyncRootLogger(final boolean includeLocation)\n
    newAsyncRootLogger(final Level level)\n
    newAsyncRootLogger(final Level level, final boolean includeLocation)\n
    newAsyncRootLogger(final String level)\n
    newAsyncRootLogger(final String level, final boolean includeLocation)\n
    '''
def newProperty():
    '''returns PropertyComponentBuilder\n\n
    newProperty(final String name, final String value)\n
    '''
def newKeyValuePair():
    '''returns KeyValuePairComponentBuilder\n\n
    newKeyValuePair(final String key, final String value)\n
    '''
def newCustomLevel():
    '''returns CustomLevelComponentBuilder\n\n
    newCustomLevel(final String name, final int level)\n
    '''
def newFilter():
    '''returns FilterComponentBuilder\n\n
    newFilter(final String type, final Filter.Result onMatch, final Filter.Result onMismatch)\n
    newFilter(final String type, final String onMatch, final String onMismatch)\n
    '''
def newLayout():
    '''returns LayoutComponentBuilder\n\n
    newLayout(final String type)\n
    '''
def newLogger():
    '''returns LoggerComponentBuilder\n\n
    newLogger(final String name)\n
    newLogger(final String name, final boolean includeLocation)\n
    newLogger(final String name, final Level level)\n
    newLogger(final String name, final Level level, final boolean includeLocation)\n
    newLogger(final String name, final String level)\n
    newLogger(final String name, final String level, final boolean includeLocation)\n
    '''
def newRootLogger():
    '''returns RootLoggerComponentBuilder\n\n
    newRootLogger()\n
    newRootLogger(final boolean includeLocation)\n
    newRootLogger(final Level level)\n
    newRootLogger(final Level level, final boolean includeLocation)\n
    newRootLogger(final String level)\n
    newRootLogger(final String level, final boolean includeLocation)\n
    '''
def setAdvertiser():
    '''returns ConfigurationBuilder<T>\n\n
    setAdvertiser(final String advertiser)\n
    '''
def setConfigurationName():
    '''returns ConfigurationBuilder<T>\n\n
    setConfigurationName(final String name)\n
    '''
def setConfigurationSource():
    '''returns ConfigurationBuilder<T>\n\n
    setConfigurationSource(final ConfigurationSource configurationSource)\n
    '''
def setMonitorInterval():
    '''returns ConfigurationBuilder<T>\n\n
    setMonitorInterval(final String intervalSeconds)\n
    '''
def setPackages():
    '''returns ConfigurationBuilder<T>\n\n
    setPackages(final String packages)\n
    '''
def setShutdownHook():
    '''returns ConfigurationBuilder<T>\n\n
    setShutdownHook(final String flag)\n
    '''
def setShutdownTimeout():
    '''returns ConfigurationBuilder<T>\n\n
    setShutdownTimeout(final long timeout, final TimeUnit timeUnit)\n
    '''
def setStatusLevel():
    '''returns ConfigurationBuilder<T>\n\n
    setStatusLevel(final Level level)\n
    '''
def setVerbosity():
    '''returns ConfigurationBuilder<T>\n\n
    setVerbosity(final String verbosity)\n
    '''
def setDestination():
    '''returns ConfigurationBuilder<T>\n\n
    setDestination(final String destination)\n
    '''
def setLoggerContext():
    '''returns None\n\n
    setLoggerContext(final LoggerContext loggerContext)\n
    '''
def addRootProperty():
    '''returns ConfigurationBuilder<T>\n\n
    addRootProperty(final String key, final String value)\n
    '''
