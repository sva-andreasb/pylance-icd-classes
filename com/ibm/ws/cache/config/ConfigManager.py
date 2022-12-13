SIMPLE_FILE_SERVLET = "String  com.ibm.ws.webcontainer.servlet.SimpleFileServlet.class""
DEFAULT_EXTENSION_PROCESSOR_IMPL = "String  com.ibm.ws.webcontainer.extension.DefaultExtensionProcessorImpl.class""
def getInstance():
'''public static ConfigManager getInstance()
'''
pass
def addConfigChangeListener():
'''public synchronized void addConfigChangeListener(final ConfigChangeListener changeListener)
'''
pass
def removeConfigChangeListener():
'''public synchronized void removeConfigChangeListener(final ConfigChangeListener changeListener)
'''
pass
def fireChangedEvent():
'''public synchronized void fireChangedEvent()
'''
pass
def setReloadInterval():
'''public void setReloadInterval(final int reloadInterval)
'''
pass
def setPropertiesDirectory():
'''public static void setPropertiesDirectory(final String dirName)
'''
pass
def alarm():
'''public void alarm(final Object alarmContext)
'''
pass
def addLegacyCacheEntry():
'''public void addLegacyCacheEntry(final ConfigEntry ce)
'''
pass
def getJaxRpcConfigEntry():
'''public ConfigEntry getJaxRpcConfigEntry(final String name)
'''
pass
def getServletCacheEntry():
'''public ConfigEntry getServletCacheEntry(final Object s, final String uri, final String contextRoot)
'''
pass
def getPortletCacheEntry():
'''public ConfigEntry getPortletCacheEntry(final Object s, final String uri, final String contextRoot)
'''
pass
def getCacheEntry():
'''public ConfigEntry getCacheEntry(final Object s, final String name, final String contextRoot)
public ConfigEntry getCacheEntry(final Object s, final String name)
'''
pass
def getCacheProcessor():
'''public CacheProcessor getCacheProcessor(final ConfigEntry ce)
'''
pass
def returnCacheProcessor():
'''public void returnCacheProcessor(final CacheProcessor cp)
'''
pass
def loadConfig():
'''public boolean loadConfig(String fileName, final boolean isWarFile, final boolean isModule, final String appName, final HashMap appContext)
'''
pass
def unloadEJBJarConfig():
'''public void unloadEJBJarConfig(final String fileName)
'''
pass
def loadEJBJarConfig():
'''public boolean loadEJBJarConfig(final String fileName, final String appName, final HashMap appContext)
'''
pass
def getCacheInstances():
'''public ArrayList getCacheInstances()
'''
pass
def getEntries():
'''public ArrayList getEntries()
'''
pass
def getCacheEntries():
'''public ArrayList getCacheEntries(final String instanceName)
'''
pass
def resolveEntity():
'''public InputSource resolveEntity(final String publicId, final String systemId)
'''
pass
def CacheProcessorPool():
'''public CacheProcessorPool(final int size, final String className)
'''
pass
def add():
'''public boolean add(final CacheProcessor cp)
'''
pass
def addPool():
'''public void addPool(final int index, final String className)
'''
pass
