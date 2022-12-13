COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def IloOdmDeploymentSettingsImpl():
    '''public IloOdmDeploymentSettingsImpl(final String name, final IloOdmDeployerBaseImpl application, final File odmdsFile)
    '''
def getName():
    '''public String getName()
    '''
def write():
    '''public void write(final OutputStream settingsStream)
    '''
def getScenarioRepositoryDatabase():
    '''public IloOdmScenarioRepositoryDatabaseImpl getScenarioRepositoryDatabase()
    '''
def getApplication():
    '''public IloOdmDeployerBaseImpl getApplication()
    '''
def setupServer():
    '''public void setupServer(final IloOdmServerDesc odmeServerDesc, final boolean optimizationServerEnabled, final boolean dataServerEnabled)
    public void setupServer(final IloOdmServerDesc odmeServerDesc, final boolean optimizationServerEnabled, final IloCredential odmeSystemCreds)
    '''
def getServer():
    '''public IloOdmServerDescImpl getServer()
    '''
def setServerURL():
    '''public void setServerURL(final String url)
    '''
def isOptimizationServerEnabled():
    '''public boolean isOptimizationServerEnabled()
    '''
def setOptimizationServerEnabled():
    '''public void setOptimizationServerEnabled(final boolean optimizationServerEnabled)
    '''
def getOptimizationServerParameters():
    '''public Map<String, String> getOptimizationServerParameters()
    '''
def setOptimizationServerParameters():
    '''public void setOptimizationServerParameters(final Map<String, String> parameters)
    '''
def isDataServerEnabled():
    '''public boolean isDataServerEnabled()
    '''
def setDataServerEnabled():
    '''public void setDataServerEnabled(final boolean dataServerEnabled)
    '''
def checkSettings():
    '''public String checkSettings()
    '''
def install():
    '''public void install()
    public void install(final IloCredential odmeAdminCreds, final X509TrustManager trustMgr)
    '''
def packageOdmApplication():
    '''public void packageOdmApplication(final OutputStream odmApplicationStream, final OutputStreamProvider osProvider)
    public void packageOdmApplication(final File odmApplicationFile)
    '''
def copy():
    '''public IloOdmDeploymentSettingsImpl copy(final String newSettingsName)
    '''
def flush():
    '''public void flush()
    '''
def getDefaultODMApplicationFile():
    '''public File getDefaultODMApplicationFile()
    '''
def getClasspathEntries():
    '''public String[] getClasspathEntries()
    '''
def setClasspathEntries():
    '''public void setClasspathEntries(final String[] classpathEntries)
    '''
def getDeploymentProperties():
    '''public Map<String, String> getDeploymentProperties()
    '''
def setDeploymentProperties():
    '''public void setDeploymentProperties(final Map<String, String> properties)
    '''
def getArchiveChecksum():
    '''public String getArchiveChecksum()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def clone():
    '''public IloOdmDeploymentSettingsImpl clone()
    '''
def getSystemCredentials():
    '''public IloCredential getSystemCredentials()
    '''
def PropertiesMap():
    '''public PropertiesMap(final Properties props)
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def getKey():
    '''public String getKey()
    '''
def getValue():
    '''public String getValue()
    '''
def setValue():
    '''public String setValue(final String value)
    '''
def remove():
    '''public void remove()
    '''
def size():
    '''public int size()
    '''
