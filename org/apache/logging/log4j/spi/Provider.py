FACTORY_PRIORITY = "String  \"FactoryPriority\""
THREAD_CONTEXT_MAP = "String  \"ThreadContextMap\""
LOGGER_CONTEXT_FACTORY = "String  \"LoggerContextFactory\""
def Provider():
    '''    public Provider(final Properties props, final URL url, final ClassLoader classLoader)
    public Provider(final Integer priority, final String versions, final Class<? extends LoggerContextFactory> loggerContextFactoryClass)
    public Provider(final Integer priority, final String versions, final Class<? extends LoggerContextFactory> loggerContextFactoryClass, final Class<? extends ThreadContextMap> threadContextMapClass)
    '''
def getVersions():
    '''    public String getVersions()
    '''
def getPriority():
    '''    public Integer getPriority()
    '''
def getClassName():
    '''    public String getClassName()
    '''
def getThreadContextMap():
    '''    public String getThreadContextMap()
    '''
def getUrl():
    '''    public URL getUrl()
    '''
def toString():
    '''    public String toString()
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def hashCode():
    '''    public int hashCode()
    '''
