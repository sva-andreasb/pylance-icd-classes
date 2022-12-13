def getLocalProxy():
    '''    public static AppManagement getLocalProxy()
    '''
def getJMXProxyForClient():
    '''    public static AppManagement getJMXProxyForClient(final AdminClient adminClient)
    '''
def getJMXProxyForServer():
    '''    public static AppManagement getJMXProxyForServer()
    '''
def sendJMXEvent():
    '''    public void sendJMXEvent(final Object arg0)
    public void sendJMXEvent(final String s, final Object arg0)
    '''
def getGlobalSettings():
    '''    public Hashtable getGlobalSettings()
    '''
def clusterMemberAdded():
    '''    public void clusterMemberAdded(final ObjectName arg0, final ObjectName arg1, final Hashtable arg2, final String arg3)
    '''
def changeServerToCluster():
    '''    public void changeServerToCluster(final ObjectName arg0, final ObjectName arg1, final Hashtable arg2, final String arg3)
    '''
def removeAllAppsFromCluster():
    '''    public void removeAllAppsFromCluster(final ObjectName arg0, final Hashtable arg1, final String arg2)
    '''
def removeAllAppsFromServer():
    '''    public void removeAllAppsFromServer(final ObjectName arg0, final Hashtable arg1, final String arg2)
    '''
def removeAllAppsFromNode():
    '''    public void removeAllAppsFromNode(final String arg0, final String arg1, final Hashtable arg2, final String arg3)
    '''
def checkIfAppExists():
    '''    public boolean checkIfAppExists(final String arg0, final Hashtable arg1, final String arg2)
    '''
def installStandaloneRAR():
    '''    public void installStandaloneRAR(final String arg0, final Hashtable arg1, final String arg2)
    '''
def compareSecurityPolicy():
    '''    public Vector compareSecurityPolicy(final String arg0, final Hashtable arg1, final String arg2)
    '''
def listModules():
    '''    public Object listModules(final String arg0, final Hashtable arg1, final String arg2)
    '''
def listApplications():
    '''    public Vector listApplications(final Hashtable arg0, final String arg1)
    public Vector listApplications(final String targetScope, final Hashtable props, final String sessionID)
    '''
def extractDDL():
    '''    public void extractDDL(final String arg0, final String arg1, final String arg2, final Hashtable arg3, final String arg4)
    '''
def exportApplication():
    '''    public void exportApplication(final String arg0, final String arg1, final Hashtable arg2, final String arg3)
    '''
def moveModule():
    '''    public void moveModule(final String arg0, final Hashtable arg1, final String arg2, final ObjectName arg3, final String arg4)
    '''
def setModuleInfo():
    '''    public void setModuleInfo(final String arg0, final Hashtable arg1, final String arg2, final String arg3, final Vector arg4)
    '''
def setApplicationInfo():
    '''    public void setApplicationInfo(final String arg0, final Hashtable arg1, final String arg2, final Vector arg3)
    '''
def getModuleInfo():
    '''    public Vector getModuleInfo(final String arg0, final Hashtable arg1, final String arg2, final String arg3)
    '''
def getApplicationInfo():
    '''    public Vector getApplicationInfo(final String arg0, final Hashtable arg1, final String arg2)
    '''
def redeployApplication():
    '''    public void redeployApplication(final String localEarPath, final String arg1, final Hashtable properties, final String arg3)
    '''
def redeployApplicationLocal():
    '''    public void redeployApplicationLocal(final String arg0, final String arg1, final Hashtable arg2, final AppNotification.Listener arg3, final String arg4)
    '''
def uninstallApplication():
    '''    public void uninstallApplication(final String arg0, final Hashtable arg1, final String arg2)
    '''
def uninstallApplicationLocal():
    '''    public void uninstallApplicationLocal(final String arg0, final Hashtable arg1, final AppNotification.Listener arg2, final String arg3)
    public void uninstallApplicationLocal(final String arg0, final Hashtable arg1, final AppNotification.Listener arg2)
    '''
def installApplicationLocal():
    '''    public void installApplicationLocal(final String arg0, final String arg1, final Hashtable arg2, final AppNotification.Listener arg3, final String arg4)
    public void installApplicationLocal(final String arg0, final String arg1, final Hashtable arg2, final AppNotification.Listener arg3)
    '''
def installApplication():
    '''    public void installApplication(final String localEarPath, final String appName, final Hashtable properties, final String workspaceID)
    public void installApplication(final String localEarPath, final Hashtable properties, final String workspaceID)
    '''
def updateAccessIDs():
    '''    public void updateAccessIDs(final String appName, final Boolean bAll, final Hashtable prefs, final String wID)
    '''
def deleteUserAndGroupEntries():
    '''    public void deleteUserAndGroupEntries(final String appName, final Hashtable prefs, final String wID)
    '''
def startApplication():
    '''    public String startApplication(final String appName, final Hashtable prefs, final String wID)
    public String startApplication(final String appName, final String target, final Hashtable prefs, final String wID)
    '''
def stopApplication():
    '''    public String stopApplication(final String appName, final Hashtable prefs, final String wID)
    public String stopApplication(final String appName, final String target, final Hashtable prefs, final String wID)
    '''
def publishWSDL():
    '''    public void publishWSDL(final String arg0, final String arg1, final Hashtable arg2, final String arg3)
    '''
def searchJNDIReferences():
    '''    public Hashtable searchJNDIReferences(final List sList, final String nodes, final Hashtable prefs, final String wID)
    '''
def updateApplication():
    '''    public void updateApplication(final String appName, final String contentURI, final String pathToContents, final String operation, final Hashtable properties, final String sessionID)
    '''
def updateApplicationLocal():
    '''    public void updateApplicationLocal(final String appName, final String contentURI, final String pathToContents, final String operation, final Hashtable properties, final AppNotification.Listener notf, final String sessionID)
    '''
def listURIs():
    '''    public List listURIs(final String appName, final String moduleURI, final Hashtable prefs, final String sessionID)
    '''
def updateCluster():
    '''    public void updateCluster(final String[] arg0, final Integer arg1, final Hashtable arg2, final String arg3)
    '''
def updateClusterLocal():
    '''    public void updateClusterLocal(final String[] arg0, final Integer arg1, final Hashtable arg2, final String arg3, final AppNotification.Listener arg4)
    '''
def searchResources():
    '''    public List searchResources(final String appName, final Hashtable prefs, final String wID)
    '''
def convertRefToConfigID():
    '''    public List convertRefToConfigID(final String appName, final List resources, final Hashtable prefs, final String wID)
    '''
def getApplicationContents():
    '''    public byte[] getApplicationContents(final String appName, final String uri, final Hashtable prefs, final String wID)
    '''
def getDistributionStatus():
    '''    public void getDistributionStatus(final String appName, final Hashtable prefs, final String wID)
    '''
def getAppAssociation():
    '''    public String[] getAppAssociation(final String scope, final String retVal, final Hashtable prefs, final String wID)
    '''
def getEditionInfo():
    '''    public EditionInfo[] getEditionInfo(final String appName, final String edition, final Hashtable prefs, final String wID)
    '''
def setEditionInfo():
    '''    public void setEditionInfo(final EditionInfo[] info, final Hashtable prefs, final String wID)
    '''
def listSystemApplications():
    '''    public Vector listSystemApplications(final Hashtable prefs, final String sessionID)
    '''
