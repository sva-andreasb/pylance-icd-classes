JAR = "String  \"JAR\""
WAR = "String  \"WAR\""
RAR = "String  \"RAR\""
EJB3JAR = "String  \"EJB3JAR\""
WEB25WAR = "String  \"WEB25WAR\""
DD = "String  \"DD\""
BND = "String  \"BND\""
EXT = "String  \"EXT\""
JAR_DD = "String  \"JAR_DD\""
JAR_BND = "String  \"JAR_BND\""
JAR_EXT = "String  \"JAR_EXT\""
EJB3JAR_DD = "String  \"EJB3JAR_DD\""
EJB3JAR_BND = "String  \"EJB3JAR_BND\""
WAR_DD = "String  \"WAR_DD\""
WAR_BND = "String  \"WAR_BND\""
WAR_EXT = "String  \"WAR_EXT\""
WEB25WAR_DD = "String  \"WEB25WAR_DD\""
RAR_DD = "String  \"RAR_DD\""
RAR_BND = "String  \"RAR_BND\""
DEPL_RES = "String  \"edit.deplresource\""
def ():
    '''returns AppDeploymentInfo\n\n
    ()\n
    (final Hashtable prefs)\n
    '''
def getAppOptions():
    '''returns Hashtable\n\n
    getAppOptions()\n
    '''
def setAppOptions():
    '''returns None\n\n
    setAppOptions(final Hashtable h)\n
    '''
def getApplication():
    '''returns Application\n\n
    getApplication()\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final Application a)\n
    '''
def getApplicationBindings():
    '''returns ApplicationBinding\n\n
    getApplicationBindings()\n
    '''
def setApplicationBindings():
    '''returns None\n\n
    setApplicationBindings(final ApplicationBinding a)\n
    '''
def getApplicationExtensions():
    '''returns ApplicationExtension\n\n
    getApplicationExtensions()\n
    '''
def setApplicationExtensions():
    '''returns None\n\n
    setApplicationExtensions(final ApplicationExtension a)\n
    '''
def getModuleConfig():
    '''returns Vector\n\n
    getModuleConfig(final String configType)\n
    '''
def setModuleConfig():
    '''returns None\n\n
    setModuleConfig(final String configType, final Vector val)\n
    '''
def getAllURIStrings():
    '''returns Vector\n\n
    getAllURIStrings()\n
    '''
def printAppInfo():
    '''returns None\n\n
    printAppInfo(final PrintStream out)\n
    '''
def saveAsFile():
    '''returns None\n\n
    saveAsFile(final String moduleUri, final String fileUriInModule, final InputStream inputStream)\n
    '''
def getJ2EEAppVersion():
    '''returns String\n\n
    getJ2EEAppVersion()\n
    '''
def getAppDeploymentResource():
    '''returns Resource\n\n
    getAppDeploymentResource(final boolean processEmbeddedCfg)\n
    '''
