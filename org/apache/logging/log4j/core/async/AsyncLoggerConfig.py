def start():
'''public void start()
'''
pass
def stop():
'''public boolean stop(final long timeout, final TimeUnit timeUnit)
'''
pass
def createRingBufferAdmin():
'''public RingBufferAdmin createRingBufferAdmin(final String contextName)
'''
pass
def createLogger():
'''public static LoggerConfig createLogger(final String additivity, final String levelName, final String loggerName, final String includeLocation, final AppenderRef[] refs, final Property[] properties, final Configuration config, final Filter filter)
public static LoggerConfig createLogger(@PluginAttribute(value = "additivity", defaultBoolean = true) final boolean additivity, @PluginAttribute("level") final Level level, @Required(message = "Loggers cannot be configured without a name") @PluginAttribute("name") final String loggerName, @PluginAttribute("includeLocation") final String includeLocation, @PluginElement("AppenderRef") final AppenderRef[] refs, @PluginElement("Properties") final Property[] properties, @PluginConfiguration final Configuration config, @PluginElement("Filter") final Filter filter)
public static LoggerConfig createLogger(final String additivity, final String levelName, final String includeLocation, final AppenderRef[] refs, final Property[] properties, final Configuration config, final Filter filter)
public static LoggerConfig createLogger(@PluginAttribute("additivity") final String additivity, @PluginAttribute("level") final Level level, @PluginAttribute("includeLocation") final String includeLocation, @PluginElement("AppenderRef") final AppenderRef[] refs, @PluginElement("Properties") final Property[] properties, @PluginConfiguration final Configuration config, @PluginElement("Filter") final Filter filter)
'''
pass
