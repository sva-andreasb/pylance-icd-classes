PROPERTY_CONFIG = "String  config""
def LoggerContext():
'''public LoggerContext(final String name)
public LoggerContext(final String name, final Object externalContext)
public LoggerContext(final String name, final Object externalContext, final URI configLocn)
public LoggerContext(final String name, final Object externalContext, final String configLocn)
'''
pass
def addShutdownListener():
'''public void addShutdownListener(final LoggerContextShutdownAware listener)
'''
pass
def getListeners():
'''public List<LoggerContextShutdownAware> getListeners()
'''
pass
def getContext():
'''public static LoggerContext getContext()
public static LoggerContext getContext(final boolean currentContext)
public static LoggerContext getContext(final ClassLoader loader, final boolean currentContext, final URI configLocation)
'''
pass
def start():
'''public void start()
public void start(final Configuration config)
'''
pass
def run():
'''public void run()
public void run()
'''
pass
def toString():
'''public String toString()
'''
pass
def close():
'''public void close()
'''
pass
def terminate():
'''public void terminate()
'''
pass
def stop():
'''public boolean stop(final long timeout, final TimeUnit timeUnit)
'''
pass
def getName():
'''public String getName()
'''
pass
def getRootLogger():
'''public Logger getRootLogger()
'''
pass
def setName():
'''public void setName(final String name)
'''
pass
def getObject():
'''public Object getObject(final String key)
'''
pass
def putObject():
'''public Object putObject(final String key, final Object value)
'''
pass
def putObjectIfAbsent():
'''public Object putObjectIfAbsent(final String key, final Object value)
'''
pass
def removeObject():
'''public Object removeObject(final String key)
public boolean removeObject(final String key, final Object value)
'''
pass
def setExternalContext():
'''public void setExternalContext(final Object context)
'''
pass
def getExternalContext():
'''public Object getExternalContext()
'''
pass
def getLogger():
'''public Logger getLogger(final String name)
public Logger getLogger(final String name, final MessageFactory messageFactory)
'''
pass
def getLoggers():
'''public Collection<Logger> getLoggers()
'''
pass
def hasLogger():
'''public boolean hasLogger(final String name)
public boolean hasLogger(final String name, final MessageFactory messageFactory)
public boolean hasLogger(final String name, final Class<? extends MessageFactory> messageFactoryClass)
'''
pass
def getConfiguration():
'''public Configuration getConfiguration()
'''
pass
def addFilter():
'''public void addFilter(final Filter filter)
'''
pass
def removeFilter():
'''public void removeFilter(final Filter filter)
'''
pass
def setConfiguration():
'''public Configuration setConfiguration(final Configuration config)
'''
pass
def addPropertyChangeListener():
'''public void addPropertyChangeListener(final PropertyChangeListener listener)
'''
pass
def removePropertyChangeListener():
'''public void removePropertyChangeListener(final PropertyChangeListener listener)
'''
pass
def getConfigLocation():
'''public URI getConfigLocation()
'''
pass
def setConfigLocation():
'''public void setConfigLocation(final URI configLocation)
'''
pass
def reconfigure():
'''public void reconfigure()
public void reconfigure(final Configuration configuration)
'''
pass
def updateLoggers():
'''public void updateLoggers()
public void updateLoggers(final Configuration config)
'''
pass
def onChange():
'''public synchronized void onChange(final Reconfigurable reconfigurable)
'''
pass
