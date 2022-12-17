def init():
    '''returns None\n\n
    init()\n
    init(final MXServer mxs)\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    reload(final String key)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def isValidOption():
    '''returns boolean\n\n
    isValidOption(final String appName, final String optionName)\n
    '''
def isValidLicense():
    '''returns boolean\n\n
    isValidLicense(final String appName, final String optionName, final boolean checkSigoption)\n
    '''
def getSigoAppCache():
    '''returns SigOptionInfo\n\n
    getSigoAppCache(final String appName)\n
    '''
def getMaxAppsForTb():
    '''returns Set<String>\n\n
    getMaxAppsForTb(final String mainTbName)\n
    '''
def getNonMobileMaxAppsForTb():
    '''returns List<String>\n\n
    getNonMobileMaxAppsForTb(final String mainTbName)\n
    '''
def getAuthAppCache():
    '''returns Set<String>\n\n
    getAuthAppCache()\n
    '''
def getMaxAppsCache():
    '''returns MaxAppsInfo\n\n
    getMaxAppsCache(final String appName)\n
    '''
def getMaxModuleCache():
    '''returns MaxModuleInfo\n\n
    getMaxModuleCache(final String moduleName)\n
    '''
def isLoaded():
    '''returns boolean\n\n
    isLoaded()\n
    '''
