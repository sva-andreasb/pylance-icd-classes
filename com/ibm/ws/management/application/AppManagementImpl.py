TEMP_EXTRACT_DIR = "String  \"Temp extraction dir for multiserver\""
CONFIG_ROOT = "String  \"Config Root for variable map\""
def createLocalImpl():
    '''public static AppManagement createLocalImpl()
    public static AppManagement createLocalImpl(final String wasRoot)
    '''
def AppManagementImpl():
    '''public AppManagementImpl(final Hashtable tbl)
    '''
def getGlobalSettings():
    '''public Hashtable getGlobalSettings()
    '''
def setObjectName():
    '''public void setObjectName(final ObjectName oName)
    '''
def isLocalMode():
    '''public static boolean isLocalMode()
    '''
def sendJMXEvent():
    '''public void sendJMXEvent(final Object e)
    public void sendJMXEvent(final String type, final Object e)
    '''
def checkIfAppExists():
    '''public boolean checkIfAppExists(final String appName, final Hashtable prefs, final String workspaceID)
    '''
def run():
    '''public Object run()
    public Object run()
    public Object run()
    public Object run()
    public Object run()
    public Object run()
    public Object run()
    public Object run()
    public Object run()
    public Object run()
    '''
def installApplication():
    '''public void installApplication(final String localEarPath, final Hashtable properties, final String workspaceID)
    public void installApplication(final String localEarPath, final String appName, final Hashtable properties, final String workspaceID)
    '''
def installApplicationLocal():
    '''public void installApplicationLocal(final String localEarPath, final String appName, final Hashtable properties, final AppNotification.Listener notf)
    public void installApplicationLocal(final String localEarPath, final String appName, final Hashtable properties, final AppNotification.Listener notf, final String workspaceID)
    '''
def uninstallApplicationLocal():
    '''public void uninstallApplicationLocal(final String appName, final Hashtable props, final AppNotification.Listener notf)
    public void uninstallApplicationLocal(final String appName, final Hashtable props, final AppNotification.Listener notf, final String workspaceID)
    '''
def uninstallApplication():
    '''public void uninstallApplication(final String appName, final Hashtable props, final String workspaceID)
    '''
def _uninstallApplication():
    '''public void _uninstallApplication(final String appName, final Hashtable props, final AppNotification.Listener notf, final boolean isJMX, final String workspaceID)
    '''
def redeployApplicationLocal():
    '''public void redeployApplicationLocal(final String localEarPath, final String appName, final Hashtable properties, final AppNotification.Listener notf, final String workspaceID)
    '''
def redeployApplication():
    '''public void redeployApplication(final String localEarPath, final String appName, final Hashtable properties, final String workspaceID)
    '''
def getApplicationInfo():
    '''public Vector getApplicationInfo(final String appName, final Hashtable prefs, final String workspaceID)
    '''
def getModuleInfo():
    '''public Vector getModuleInfo(final String appName, final Hashtable prefs, final String uniqueModuleURI, final String workspaceID)
    '''
def setApplicationInfo():
    '''public void setApplicationInfo(final String appName, final Hashtable prefs, final String workspaceID, final Vector tasks)
    '''
def setModuleInfo():
    '''public void setModuleInfo(final String appName, final Hashtable prefs, final String uniqueModuleURI, final String workspaceID, final Vector tasks)
    '''
def moveModule():
    '''public void moveModule(final String appName, final Hashtable prefs, final String uniqueModuleURI, final ObjectName on, final String wID)
    '''
def exportApplication():
    '''public void exportApplication(final String appName, final String pathName, final Hashtable prefs, final String workspaceID)
    '''
def extractDDL():
    '''public void extractDDL(final String appName, final String ddlPrefix, final String dirName, final Hashtable prefs, final String workspaceID)
    '''
def publishWSDL():
    '''public void publishWSDL(final String appName, final String pathName, final Hashtable prefs, final String workspaceID)
    '''
def listSystemApplications():
    '''public Vector listSystemApplications(final Hashtable prefs, final String wID)
    '''
def listApplicationsAsSystem():
    '''public Vector listApplicationsAsSystem(final Hashtable prefs, final String wID)
    public Vector listApplicationsAsSystem(final String targetScope, final Hashtable prefs, final String wID)
    '''
def listApplications():
    '''public Vector listApplications(final Hashtable prefs, final String wID)
    public Vector listApplications(final String targetScope, final Hashtable prefs, final String wID)
    '''
def listModules():
    '''public Object listModules(final String appName, final Hashtable prefs, final String workspaceID)
    '''
def listURIs():
    '''public List listURIs(final String appName, final String moduleURI, final Hashtable prefs, final String sessionID)
    '''
def removeAllAppsFromNode():
    '''public void removeAllAppsFromNode(final String nodeName, final String cellName, final Hashtable prefs, final String wID)
    '''
def removeAllAppsFromServer():
    '''public void removeAllAppsFromServer(final ObjectName objectName, final Hashtable prefs, final String wID)
    '''
def removeAllAppsFromCluster():
    '''public void removeAllAppsFromCluster(final ObjectName objectName, final Hashtable prefs, final String wID)
    '''
def changeServerToCluster():
    '''public void changeServerToCluster(final ObjectName serverName, final ObjectName clusterName, final Hashtable prefs, final String wID)
    '''
def clusterMemberAdded():
    '''public void clusterMemberAdded(final ObjectName memberName, final ObjectName clusterName, final Hashtable prefs, final String wID)
    '''
def updateAccessIDs():
    '''public void updateAccessIDs(final String appName, final Boolean bAll, final Hashtable prefs, final String wID)
    '''
def deleteUserAndGroupEntries():
    '''public void deleteUserAndGroupEntries(final String appName, final Hashtable prefs, final String wID)
    '''
def startApplication():
    '''public String startApplication(final String appName, final Hashtable prefs, final String wID)
    public String startApplication(final String appName, final String target, final Hashtable prefs, final String wID)
    '''
def stopApplication():
    '''public String stopApplication(final String appName, final Hashtable prefs, final String wID)
    public String stopApplication(final String appName, final String target, final Hashtable prefs, final String wID)
    '''
def installStandaloneRAR():
    '''public void installStandaloneRAR(final String rarPath, final Hashtable props, final String workspaceID)
    '''
def compareSecurityPolicy():
    '''public Vector compareSecurityPolicy(final String policyData, final Hashtable preferences, final String workspaceID)
    '''
def compareSecurityPolicyAsSystem():
    '''public Vector compareSecurityPolicyAsSystem(final String policyData, final Hashtable preferences, final String workspaceID)
    '''
def searchJNDIReferences():
    '''public Hashtable searchJNDIReferences(final List sList, final String nodes, final Hashtable prefs, final String wID)
    '''
def updateApplication():
    '''public void updateApplication(final String appName, final String contentURI, final String pathToContents, final String operation, final Hashtable properties, final String sessionID)
    '''
def updateApplicationLocal():
    '''public void updateApplicationLocal(final String appName, final String contentURI, final String pathToContents, final String operation, final Hashtable properties, final AppNotification.Listener notfListener, final String sessionID)
    '''
def _updateApplication():
    '''public void _updateApplication(final String appName, final String contentURI, final String pathToContents, final String operation, Hashtable props, final AppNotification.Listener notf, final String sessionID)
    '''
def updateClusterLocal():
    '''public void updateClusterLocal(final String[] appNames, final Integer timeout, final Hashtable props, final String wsId, final AppNotification.Listener notif)
    '''
def updateCluster():
    '''public void updateCluster(final String[] appNames, final Integer timeout, final Hashtable props, final String wsId)
    '''
def searchResources():
    '''public List searchResources(final String appName, final Hashtable prefs, final String wID)
    '''
def convertRefToConfigID():
    '''public List convertRefToConfigID(final String appName, final List resources, final Hashtable prefs, final String wID)
    '''
def getApplicationContents():
    '''public byte[] getApplicationContents(final String appName, final String uri, final Hashtable prefs, final String wID)
    '''
def getDistributionStatus():
    '''public void getDistributionStatus(final String appName, final Hashtable prefs, final String wID)
    '''
def getAppAssociation():
    '''public String[] getAppAssociation(final String scope, final String retVal, final Hashtable prefs, final String wID)
    '''
def getEditionInfo():
    '''public EditionInfo[] getEditionInfo(final String appName, final String edition, final Hashtable prefs, final String wID)
    '''
def setEditionInfo():
    '''public void setEditionInfo(final EditionInfo[] info, final Hashtable prefs, final String wID)
    '''
def getCellName():
    '''public static String getCellName()
    '''
