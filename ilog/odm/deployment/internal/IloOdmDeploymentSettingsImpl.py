COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns PropertiesMap\n\n
    (final String name, final IloOdmDeployerBaseImpl application, final File odmdsFile)\n
    (final Properties props)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def write():
    '''returns None\n\n
    write(final OutputStream settingsStream)\n
    '''
def getScenarioRepositoryDatabase():
    '''returns IloOdmScenarioRepositoryDatabaseImpl\n\n
    getScenarioRepositoryDatabase()\n
    '''
def getApplication():
    '''returns IloOdmDeployerBaseImpl\n\n
    getApplication()\n
    '''
def setupServer():
    '''returns None\n\n
    setupServer(final IloOdmServerDesc odmeServerDesc, final boolean optimizationServerEnabled, final boolean dataServerEnabled)\n
    setupServer(final IloOdmServerDesc odmeServerDesc, final boolean optimizationServerEnabled, final IloCredential odmeSystemCreds)\n
    '''
def getServer():
    '''returns IloOdmServerDescImpl\n\n
    getServer()\n
    '''
def setServerURL():
    '''returns None\n\n
    setServerURL(final String url)\n
    '''
def isOptimizationServerEnabled():
    '''returns boolean\n\n
    isOptimizationServerEnabled()\n
    '''
def setOptimizationServerEnabled():
    '''returns None\n\n
    setOptimizationServerEnabled(final boolean optimizationServerEnabled)\n
    '''
def setOptimizationServerParameters():
    '''returns None\n\n
    setOptimizationServerParameters(final Map<String, String> parameters)\n
    '''
def isDataServerEnabled():
    '''returns boolean\n\n
    isDataServerEnabled()\n
    '''
def setDataServerEnabled():
    '''returns None\n\n
    setDataServerEnabled(final boolean dataServerEnabled)\n
    '''
def checkSettings():
    '''returns String\n\n
    checkSettings()\n
    '''
def install():
    '''returns None\n\n
    install()\n
    install(final IloCredential odmeAdminCreds, final X509TrustManager trustMgr)\n
    '''
def packageOdmApplication():
    '''returns None\n\n
    packageOdmApplication(final OutputStream odmApplicationStream, final OutputStreamProvider osProvider)\n
    packageOdmApplication(final File odmApplicationFile)\n
    '''
def copy():
    '''returns IloOdmDeploymentSettingsImpl\n\n
    copy(final String newSettingsName)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def getDefaultODMApplicationFile():
    '''returns File\n\n
    getDefaultODMApplicationFile()\n
    '''
def getClasspathEntries():
    '''returns String[]\n\n
    getClasspathEntries()\n
    '''
def setClasspathEntries():
    '''returns None\n\n
    setClasspathEntries(final String[] classpathEntries)\n
    '''
def setDeploymentProperties():
    '''returns None\n\n
    setDeploymentProperties(final Map<String, String> properties)\n
    '''
def getArchiveChecksum():
    '''returns String\n\n
    getArchiveChecksum()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def clone():
    '''returns IloOdmDeploymentSettingsImpl\n\n
    clone()\n
    '''
def getSystemCredentials():
    '''returns IloCredential\n\n
    getSystemCredentials()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def getKey():
    '''returns String\n\n
    getKey()\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    '''
def setValue():
    '''returns String\n\n
    setValue(final String value)\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
