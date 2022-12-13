PROPERTY_CONFIG = "String  \"config\""
def LoggerContext():
    '''public LoggerContext(final String name)
    public LoggerContext(final String name, final Object externalContext)
    public LoggerContext(final String name, final Object externalContext, final URI configLocn)
    public LoggerContext(final String name, final Object externalContext, final String configLocn)
    '''
def addShutdownListener():
    '''public void addShutdownListener(final LoggerContextShutdownAware listener)
    '''
def getListeners():
    '''public List<LoggerContextShutdownAware> getListeners()
    '''
def getContext():
    '''public static LoggerContext getContext()
    public static LoggerContext getContext(final boolean currentContext)
    public static LoggerContext getContext(final ClassLoader loader, final boolean currentContext, final URI configLocation)
    '''
def start():
    '''public void start()
    public void start(final Configuration config)
    '''
def run():
    '''public void run()
    public void run()
    '''
def toString():
    '''public String toString()
    '''
def close():
    '''public void close()
    '''
def terminate():
    '''public void terminate()
    '''
def stop():
    '''public boolean stop(final long timeout, final TimeUnit timeUnit)
    '''
def getName():
    '''public String getName()
    '''
def getRootLogger():
    '''public Logger getRootLogger()
    '''
def setName():
    '''public void setName(final String name)
    '''
def getObject():
    '''public Object getObject(final String key)
    '''
def putObject():
    '''public Object putObject(final String key, final Object value)
    '''
def putObjectIfAbsent():
    '''public Object putObjectIfAbsent(final String key, final Object value)
    '''
def removeObject():
    '''public Object removeObject(final String key)
    public boolean removeObject(final String key, final Object value)
    '''
def setExternalContext():
    '''public void setExternalContext(final Object context)
    '''
def getExternalContext():
    '''public Object getExternalContext()
    '''
def getLogger():
    '''public Logger getLogger(final String name)
    public Logger getLogger(final String name, final MessageFactory messageFactory)
    '''
def getLoggers():
    '''public Collection<Logger> getLoggers()
    '''
def hasLogger():
    '''public boolean hasLogger(final String name)
    public boolean hasLogger(final String name, final MessageFactory messageFactory)
    public boolean hasLogger(final String name, final Class<? extends MessageFactory> messageFactoryClass)
    '''
def getConfiguration():
    '''public Configuration getConfiguration()
    '''
def addFilter():
    '''public void addFilter(final Filter filter)
    '''
def removeFilter():
    '''public void removeFilter(final Filter filter)
    '''
def setConfiguration():
    '''public Configuration setConfiguration(final Configuration config)
    '''
def addPropertyChangeListener():
    '''public void addPropertyChangeListener(final PropertyChangeListener listener)
    '''
def removePropertyChangeListener():
    '''public void removePropertyChangeListener(final PropertyChangeListener listener)
    '''
def getConfigLocation():
    '''public URI getConfigLocation()
    '''
def setConfigLocation():
    '''public void setConfigLocation(final URI configLocation)
    '''
def reconfigure():
    '''public void reconfigure()
    public void reconfigure(final Configuration configuration)
    '''
def updateLoggers():
    '''public void updateLoggers()
    public void updateLoggers(final Configuration config)
    '''
def onChange():
    '''public synchronized void onChange(final Reconfigurable reconfigurable)
    '''
