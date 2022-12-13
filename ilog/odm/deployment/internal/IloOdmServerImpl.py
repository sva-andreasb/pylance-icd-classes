COPYRIGHT_NOTICE = "String  Copyright IBM Corporation 2005,2012""
def equals():
'''public boolean equals(final Object o)
'''
pass
def checkConnection():
'''public ConnectionInfo checkConnection()
public long checkConnection(final boolean checkDB)
'''
pass
def getDeployedApplicationsKeys():
'''public Set<IloOdmApplicationKey> getDeployedApplicationsKeys()
'''
pass
def uninstall():
'''public void uninstall(final IloOdmApplicationKey appDesc)
'''
pass
def getParameters():
'''public Map<String, String> getParameters(final IloOdmApplicationKey appDesc)
'''
pass
def setParameters():
'''public void setParameters(final IloOdmApplicationKey appDesc, final Map<String, String> parameters)
'''
pass
def exportApplication():
'''public IloOdmApplication exportApplication(final IloOdmApplicationKey appDesc)
'''
pass
def getCredentials():
'''public IloCredential getCredentials()
'''
pass
def getTrustManager():
'''public X509TrustManager getTrustManager()
'''
pass
def DeploymentManager():
'''public DeploymentManager()
'''
pass
def deploy():
'''public String deploy(final IloDeploymentArchive deploymentArchive)
'''
pass
def isDeployed():
'''public boolean isDeployed(final String archiveChecksum)
'''
pass
def getODMApplicationsKeys():
'''public Set<IloOdmApplicationKey> getODMApplicationsKeys()
'''
pass
def undeploy():
'''public void undeploy(final IloOdmApplicationKey appDesc)
'''
pass
def getServerNanoTime():
'''public long getServerNanoTime()
'''
pass
