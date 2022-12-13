def init():
    '''public void init()
    public void init(final MXServer mxs)
    '''
def reload():
    '''public void reload()
    public void reload(final String key)
    '''
def getName():
    '''public String getName()
    '''
def getSigoCache():
    '''public Map<String, SigOptionInfo> getSigoCache(final String appName)
    '''
def isValidOption():
    '''public boolean isValidOption(final String appName, final String optionName)
    '''
def isValidLicense():
    '''public boolean isValidLicense(final String appName, final String optionName, final boolean checkSigoption)
    '''
def getSigoFlags():
    '''public Map<String, String> getSigoFlags(final String appName, final String optionName)
    '''
def getSigoAppCache():
    '''public SigOptionInfo getSigoAppCache(final String appName)
    '''
def getMaxAppsCache():
    '''public Map<String, MaxAppsInfo> getMaxAppsCache()
    public MaxAppsInfo getMaxAppsCache(final String appName)
    '''
def getMaxAppsForTb():
    '''public Set<String> getMaxAppsForTb(final String mainTbName)
    '''
def getNonMobileMaxAppsForTb():
    '''public List<String> getNonMobileMaxAppsForTb(final String mainTbName)
    '''
def getAuthAppCache():
    '''public Set<String> getAuthAppCache()
    '''
def getMaxModuleCache():
    '''public MaxModuleInfo getMaxModuleCache(final String moduleName)
    '''
def getModuleMenuCache():
    '''public Map<String, Map<Integer, MaxMenuInfo>> getModuleMenuCache()
    '''
def isLoaded():
    '''public boolean isLoaded()
    '''
