TEMP_EXTRACT_DIR = "String  Temp extraction dir for multiserver""
CONFIG_ROOT = "String  Config Root for variable map""
def createLocalImpl():
'''public static AppManagement createLocalImpl()
public static AppManagement createLocalImpl(final String wasRoot)
'''
pass
def AppManagementImpl():
'''public AppManagementImpl(final Hashtable tbl)
'''
pass
def getGlobalSettings():
'''public Hashtable getGlobalSettings()
'''
pass
def setObjectName():
'''public void setObjectName(final ObjectName oName)
'''
pass
def isLocalMode():
'''public static boolean isLocalMode()
'''
pass
def sendJMXEvent():
'''public void sendJMXEvent(final Object e)
public void sendJMXEvent(final String type, final Object e)
'''
pass
def checkIfAppExists():
'''public boolean checkIfAppExists(final String appName, final Hashtable prefs, final String workspaceID)
'''
pass
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
pass
def installApplication():
'''public void installApplication(final String localEarPath, final Hashtable properties, final String workspaceID)
public void installApplication(final String localEarPath, final String appName, final Hashtable properties, final String workspaceID)
'''
pass
def installApplicationLocal():
'''public void installApplicationLocal(final String localEarPath, final String appName, final Hashtable properties, final AppNotification.Listener notf)
public void installApplicationLocal(final String localEarPath, final String appName, final Hashtable properties, final AppNotification.Listener notf, final String workspaceID)
'''
pass
def uninstallApplicationLocal():
'''public void uninstallApplicationLocal(final String appName, final Hashtable props, final AppNotification.Listener notf)
public void uninstallApplicationLocal(final String appName, final Hashtable props, final AppNotification.Listener notf, final String workspaceID)
'''
pass
def uninstallApplication():
'''public void uninstallApplication(final String appName, final Hashtable props, final String workspaceID)
'''
pass
def _uninstallApplication():
'''public void _uninstallApplication(final String appName, final Hashtable props, final AppNotification.Listener notf, final boolean isJMX, final String workspaceID)
'''
pass
def redeployApplicationLocal():
'''public void redeployApplicationLocal(final String localEarPath, final String appName, final Hashtable properties, final AppNotification.Listener notf, final String workspaceID)
'''
pass
def redeployApplication():
'''public void redeployApplication(final String localEarPath, final String appName, final Hashtable properties, final String workspaceID)
'''
pass
def getApplicationInfo():
'''public Vector getApplicationInfo(final String appName, final Hashtable prefs, final String workspaceID)
'''
pass
def getModuleInfo():
'''public Vector getModuleInfo(final String appName, final Hashtable prefs, final String uniqueModuleURI, final String workspaceID)
'''
pass
def setApplicationInfo():
'''public void setApplicationInfo(final String appName, final Hashtable prefs, final String workspaceID, final Vector tasks)
'''
pass
def setModuleInfo():
'''public void setModuleInfo(final String appName, final Hashtable prefs, final String uniqueModuleURI, final String workspaceID, final Vector tasks)
'''
pass
def moveModule():
'''public void moveModule(final String appName, final Hashtable prefs, final String uniqueModuleURI, final ObjectName on, final String wID)
'''
pass
def exportApplication():
'''public void exportApplication(final String appName, final String pathName, final Hashtable prefs, final String workspaceID)
'''
pass
def extractDDL():
'''public void extractDDL(final String appName, final String ddlPrefix, final String dirName, final Hashtable prefs, final String workspaceID)
'''
pass
def publishWSDL():
'''public void publishWSDL(final String appName, final String pathName, final Hashtable prefs, final String workspaceID)
'''
pass
def listSystemApplications():
'''public Vector listSystemApplications(final Hashtable prefs, final String wID)
'''
pass
def listApplicationsAsSystem():
'''public Vector listApplicationsAsSystem(final Hashtable prefs, final String wID)
public Vector listApplicationsAsSystem(final String targetScope, final Hashtable prefs, final String wID)
'''
pass
def listApplications():
'''public Vector listApplications(final Hashtable prefs, final String wID)
public Vector listApplications(final String targetScope, final Hashtable prefs, final String wID)
'''
pass
def listModules():
'''public Object listModules(final String appName, final Hashtable prefs, final String workspaceID)
'''
pass
def listURIs():
'''public List listURIs(final String appName, final String moduleURI, final Hashtable prefs, final String sessionID)
'''
pass
def removeAllAppsFromNode():
'''public void removeAllAppsFromNode(final String nodeName, final String cellName, final Hashtable prefs, final String wID)
'''
pass
def removeAllAppsFromServer():
'''public void removeAllAppsFromServer(final ObjectName objectName, final Hashtable prefs, final String wID)
'''
pass
def removeAllAppsFromCluster():
'''public void removeAllAppsFromCluster(final ObjectName objectName, final Hashtable prefs, final String wID)
'''
pass
def changeServerToCluster():
'''public void changeServerToCluster(final ObjectName serverName, final ObjectName clusterName, final Hashtable prefs, final String wID)
'''
pass
def clusterMemberAdded():
'''public void clusterMemberAdded(final ObjectName memberName, final ObjectName clusterName, final Hashtable prefs, final String wID)
'''
pass
def updateAccessIDs():
'''public void updateAccessIDs(final String appName, final Boolean bAll, final Hashtable prefs, final String wID)
'''
pass
def deleteUserAndGroupEntries():
'''public void deleteUserAndGroupEntries(final String appName, final Hashtable prefs, final String wID)
'''
pass
def startApplication():
'''public String startApplication(final String appName, final Hashtable prefs, final String wID)
public String startApplication(final String appName, final String target, final Hashtable prefs, final String wID)
'''
pass
def stopApplication():
'''public String stopApplication(final String appName, final Hashtable prefs, final String wID)
public String stopApplication(final String appName, final String target, final Hashtable prefs, final String wID)
'''
pass
def installStandaloneRAR():
'''public void installStandaloneRAR(final String rarPath, final Hashtable props, final String workspaceID)
'''
pass
def compareSecurityPolicy():
'''public Vector compareSecurityPolicy(final String policyData, final Hashtable preferences, final String workspaceID)
'''
pass
def compareSecurityPolicyAsSystem():
'''public Vector compareSecurityPolicyAsSystem(final String policyData, final Hashtable preferences, final String workspaceID)
'''
pass
def searchJNDIReferences():
'''public Hashtable searchJNDIReferences(final List sList, final String nodes, final Hashtable prefs, final String wID)
'''
pass
def updateApplication():
'''public void updateApplication(final String appName, final String contentURI, final String pathToContents, final String operation, final Hashtable properties, final String sessionID)
'''
pass
def updateApplicationLocal():
'''public void updateApplicationLocal(final String appName, final String contentURI, final String pathToContents, final String operation, final Hashtable properties, final AppNotification.Listener notfListener, final String sessionID)
'''
pass
def _updateApplication():
'''public void _updateApplication(final String appName, final String contentURI, final String pathToContents, final String operation, Hashtable props, final AppNotification.Listener notf, final String sessionID)
'''
pass
def updateClusterLocal():
'''public void updateClusterLocal(final String[] appNames, final Integer timeout, final Hashtable props, final String wsId, final AppNotification.Listener notif)
'''
pass
def updateCluster():
'''public void updateCluster(final String[] appNames, final Integer timeout, final Hashtable props, final String wsId)
'''
pass
def searchResources():
'''public List searchResources(final String appName, final Hashtable prefs, final String wID)
'''
pass
def convertRefToConfigID():
'''public List convertRefToConfigID(final String appName, final List resources, final Hashtable prefs, final String wID)
'''
pass
def getApplicationContents():
'''public byte[] getApplicationContents(final String appName, final String uri, final Hashtable prefs, final String wID)
'''
pass
def getDistributionStatus():
'''public void getDistributionStatus(final String appName, final Hashtable prefs, final String wID)
'''
pass
def getAppAssociation():
'''public String[] getAppAssociation(final String scope, final String retVal, final Hashtable prefs, final String wID)
'''
pass
def getEditionInfo():
'''public EditionInfo[] getEditionInfo(final String appName, final String edition, final Hashtable prefs, final String wID)
'''
pass
def setEditionInfo():
'''public void setEditionInfo(final EditionInfo[] info, final Hashtable prefs, final String wID)
'''
pass
def getCellName():
'''public static String getCellName()
'''
pass
