def init():
'''public void init()
public void init(final MXServer mxs)
'''
pass
def reload():
'''public void reload()
public void reload(final String key)
'''
pass
def getName():
'''public String getName()
'''
pass
def getSigoCache():
'''public Map<String, SigOptionInfo> getSigoCache(final String appName)
'''
pass
def isValidOption():
'''public boolean isValidOption(final String appName, final String optionName)
'''
pass
def isValidLicense():
'''public boolean isValidLicense(final String appName, final String optionName, final boolean checkSigoption)
'''
pass
def getSigoFlags():
'''public Map<String, String> getSigoFlags(final String appName, final String optionName)
'''
pass
def getSigoAppCache():
'''public SigOptionInfo getSigoAppCache(final String appName)
'''
pass
def getMaxAppsCache():
'''public Map<String, MaxAppsInfo> getMaxAppsCache()
public MaxAppsInfo getMaxAppsCache(final String appName)
'''
pass
def getMaxAppsForTb():
'''public Set<String> getMaxAppsForTb(final String mainTbName)
'''
pass
def getNonMobileMaxAppsForTb():
'''public List<String> getNonMobileMaxAppsForTb(final String mainTbName)
'''
pass
def getAuthAppCache():
'''public Set<String> getAuthAppCache()
'''
pass
def getMaxModuleCache():
'''public MaxModuleInfo getMaxModuleCache(final String moduleName)
'''
pass
def getModuleMenuCache():
'''public Map<String, Map<Integer, MaxMenuInfo>> getModuleMenuCache()
'''
pass
def isLoaded():
'''public boolean isLoaded()
'''
pass
