SIMPLE_FILE_SERVLET = "String  \"com.ibm.ws.webcontainer.servlet.SimpleFileServlet.class\""
DEFAULT_EXTENSION_PROCESSOR_IMPL = "String  \"com.ibm.ws.webcontainer.extension.DefaultExtensionProcessorImpl.class\""
def setReloadInterval():
    '''returns None\n\n
    setReloadInterval(final int reloadInterval)\n
    '''
def alarm():
    '''returns None\n\n
    alarm(final Object alarmContext)\n
    '''
def addLegacyCacheEntry():
    '''returns None\n\n
    addLegacyCacheEntry(final ConfigEntry ce)\n
    '''
def getJaxRpcConfigEntry():
    '''returns ConfigEntry\n\n
    getJaxRpcConfigEntry(final String name)\n
    '''
def getServletCacheEntry():
    '''returns ConfigEntry\n\n
    getServletCacheEntry(final Object s, final String uri, final String contextRoot)\n
    '''
def getPortletCacheEntry():
    '''returns ConfigEntry\n\n
    getPortletCacheEntry(final Object s, final String uri, final String contextRoot)\n
    '''
def getCacheEntry():
    '''returns ConfigEntry\n\n
    getCacheEntry(final Object s, final String name, final String contextRoot)\n
    getCacheEntry(final Object s, final String name)\n
    '''
def getCacheProcessor():
    '''returns CacheProcessor\n\n
    getCacheProcessor(final ConfigEntry ce)\n
    '''
def returnCacheProcessor():
    '''returns None\n\n
    returnCacheProcessor(final CacheProcessor cp)\n
    '''
def loadConfig():
    '''returns boolean\n\n
    loadConfig(String fileName, final boolean isWarFile, final boolean isModule, final String appName, final HashMap appContext)\n
    '''
def unloadEJBJarConfig():
    '''returns None\n\n
    unloadEJBJarConfig(final String fileName)\n
    '''
def loadEJBJarConfig():
    '''returns boolean\n\n
    loadEJBJarConfig(final String fileName, final String appName, final HashMap appContext)\n
    '''
def getCacheInstances():
    '''returns ArrayList\n\n
    getCacheInstances()\n
    '''
def getEntries():
    '''returns ArrayList\n\n
    getEntries()\n
    '''
def getCacheEntries():
    '''returns ArrayList\n\n
    getCacheEntries(final String instanceName)\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String publicId, final String systemId)\n
    '''
def ():
    '''returns CacheProcessorPool\n\n
    (final int size, final String className)\n
    '''
def add():
    '''returns boolean\n\n
    add(final CacheProcessor cp)\n
    '''
def addPool():
    '''returns None\n\n
    addPool(final int index, final String className)\n
    '''
