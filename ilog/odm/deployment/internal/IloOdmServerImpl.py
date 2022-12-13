COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def equals():
    '''public boolean equals(final Object o)
    '''
def checkConnection():
    '''public ConnectionInfo checkConnection()
    public long checkConnection(final boolean checkDB)
    '''
def getDeployedApplicationsKeys():
    '''public Set<IloOdmApplicationKey> getDeployedApplicationsKeys()
    '''
def uninstall():
    '''public void uninstall(final IloOdmApplicationKey appDesc)
    '''
def getParameters():
    '''public Map<String, String> getParameters(final IloOdmApplicationKey appDesc)
    '''
def setParameters():
    '''public void setParameters(final IloOdmApplicationKey appDesc, final Map<String, String> parameters)
    '''
def exportApplication():
    '''public IloOdmApplication exportApplication(final IloOdmApplicationKey appDesc)
    '''
def getCredentials():
    '''public IloCredential getCredentials()
    '''
def getTrustManager():
    '''public X509TrustManager getTrustManager()
    '''
def DeploymentManager():
    '''public DeploymentManager()
    '''
def deploy():
    '''public String deploy(final IloDeploymentArchive deploymentArchive)
    '''
def isDeployed():
    '''public boolean isDeployed(final String archiveChecksum)
    '''
def getODMApplicationsKeys():
    '''public Set<IloOdmApplicationKey> getODMApplicationsKeys()
    '''
def undeploy():
    '''public void undeploy(final IloOdmApplicationKey appDesc)
    '''
def getServerNanoTime():
    '''public long getServerNanoTime()
    '''
