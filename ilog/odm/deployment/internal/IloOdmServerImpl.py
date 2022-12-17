COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def checkConnection():
    '''returns long\n\n
    checkConnection()\n
    checkConnection(final boolean checkDB)\n
    '''
def getDeployedApplicationsKeys():
    '''returns Set<IloOdmApplicationKey>\n\n
    getDeployedApplicationsKeys()\n
    '''
def uninstall():
    '''returns None\n\n
    uninstall(final IloOdmApplicationKey appDesc)\n
    '''
def setParameters():
    '''returns None\n\n
    setParameters(final IloOdmApplicationKey appDesc, final Map<String, String> parameters)\n
    '''
def exportApplication():
    '''returns IloOdmApplication\n\n
    exportApplication(final IloOdmApplicationKey appDesc)\n
    '''
def getCredentials():
    '''returns IloCredential\n\n
    getCredentials()\n
    '''
def getTrustManager():
    '''returns X509TrustManager\n\n
    getTrustManager()\n
    '''
def ():
    '''returns DeploymentManager\n\n
    ()\n
    '''
def deploy():
    '''returns String\n\n
    deploy(final IloDeploymentArchive deploymentArchive)\n
    '''
def isDeployed():
    '''returns boolean\n\n
    isDeployed(final String archiveChecksum)\n
    '''
def getODMApplicationsKeys():
    '''returns Set<IloOdmApplicationKey>\n\n
    getODMApplicationsKeys()\n
    '''
def undeploy():
    '''returns None\n\n
    undeploy(final IloOdmApplicationKey appDesc)\n
    '''
def getServerNanoTime():
    '''returns long\n\n
    getServerNanoTime()\n
    '''
