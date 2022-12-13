SIMPLE_FILE_SERVLET = "String  \"com.ibm.ws.webcontainer.servlet.SimpleFileServlet.class\""
DEFAULT_EXTENSION_PROCESSOR_IMPL = "String  \"com.ibm.ws.webcontainer.extension.DefaultExtensionProcessorImpl.class\""
def getInstance():
    '''public static ConfigManager getInstance()
    '''
def addConfigChangeListener():
    '''public synchronized void addConfigChangeListener(final ConfigChangeListener changeListener)
    '''
def removeConfigChangeListener():
    '''public synchronized void removeConfigChangeListener(final ConfigChangeListener changeListener)
    '''
def fireChangedEvent():
    '''public synchronized void fireChangedEvent()
    '''
def setReloadInterval():
    '''public void setReloadInterval(final int reloadInterval)
    '''
def setPropertiesDirectory():
    '''public static void setPropertiesDirectory(final String dirName)
    '''
def alarm():
    '''public void alarm(final Object alarmContext)
    '''
def addLegacyCacheEntry():
    '''public void addLegacyCacheEntry(final ConfigEntry ce)
    '''
def getJaxRpcConfigEntry():
    '''public ConfigEntry getJaxRpcConfigEntry(final String name)
    '''
def getServletCacheEntry():
    '''public ConfigEntry getServletCacheEntry(final Object s, final String uri, final String contextRoot)
    '''
def getPortletCacheEntry():
    '''public ConfigEntry getPortletCacheEntry(final Object s, final String uri, final String contextRoot)
    '''
def getCacheEntry():
    '''public ConfigEntry getCacheEntry(final Object s, final String name, final String contextRoot)
    public ConfigEntry getCacheEntry(final Object s, final String name)
    '''
def getCacheProcessor():
    '''public CacheProcessor getCacheProcessor(final ConfigEntry ce)
    '''
def returnCacheProcessor():
    '''public void returnCacheProcessor(final CacheProcessor cp)
    '''
def loadConfig():
    '''public boolean loadConfig(String fileName, final boolean isWarFile, final boolean isModule, final String appName, final HashMap appContext)
    '''
def unloadEJBJarConfig():
    '''public void unloadEJBJarConfig(final String fileName)
    '''
def loadEJBJarConfig():
    '''public boolean loadEJBJarConfig(final String fileName, final String appName, final HashMap appContext)
    '''
def getCacheInstances():
    '''public ArrayList getCacheInstances()
    '''
def getEntries():
    '''public ArrayList getEntries()
    '''
def getCacheEntries():
    '''public ArrayList getCacheEntries(final String instanceName)
    '''
def resolveEntity():
    '''public InputSource resolveEntity(final String publicId, final String systemId)
    '''
def CacheProcessorPool():
    '''public CacheProcessorPool(final int size, final String className)
    '''
def add():
    '''public boolean add(final CacheProcessor cp)
    '''
def addPool():
    '''public void addPool(final int index, final String className)
    '''
