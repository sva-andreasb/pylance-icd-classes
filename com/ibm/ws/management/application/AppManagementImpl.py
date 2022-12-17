TEMP_EXTRACT_DIR = "String  \"Temp extraction dir for multiserver\""
CONFIG_ROOT = "String  \"Config Root for variable map\""
def ():
    '''returns AppManagementImpl\n\n
    (final Hashtable tbl)\n
    '''
def getGlobalSettings():
    '''returns Hashtable\n\n
    getGlobalSettings()\n
    '''
def setObjectName():
    '''returns None\n\n
    setObjectName(final ObjectName oName)\n
    '''
def sendJMXEvent():
    '''returns None\n\n
    sendJMXEvent(final Object e)\n
    sendJMXEvent(final String type, final Object e)\n
    '''
def checkIfAppExists():
    '''returns boolean\n\n
    checkIfAppExists(final String appName, final Hashtable prefs, final String workspaceID)\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def installApplication():
    '''returns None\n\n
    installApplication(final String localEarPath, final Hashtable properties, final String workspaceID)\n
    installApplication(final String localEarPath, final String appName, final Hashtable properties, final String workspaceID)\n
    '''
def installApplicationLocal():
    '''returns None\n\n
    installApplicationLocal(final String localEarPath, final String appName, final Hashtable properties, final AppNotification.Listener notf)\n
    installApplicationLocal(final String localEarPath, final String appName, final Hashtable properties, final AppNotification.Listener notf, final String workspaceID)\n
    '''
def uninstallApplicationLocal():
    '''returns None\n\n
    uninstallApplicationLocal(final String appName, final Hashtable props, final AppNotification.Listener notf)\n
    uninstallApplicationLocal(final String appName, final Hashtable props, final AppNotification.Listener notf, final String workspaceID)\n
    '''
def uninstallApplication():
    '''returns None\n\n
    uninstallApplication(final String appName, final Hashtable props, final String workspaceID)\n
    '''
def _uninstallApplication():
    '''returns None\n\n
    _uninstallApplication(final String appName, final Hashtable props, final AppNotification.Listener notf, final boolean isJMX, final String workspaceID)\n
    '''
def redeployApplicationLocal():
    '''returns None\n\n
    redeployApplicationLocal(final String localEarPath, final String appName, final Hashtable properties, final AppNotification.Listener notf, final String workspaceID)\n
    '''
def redeployApplication():
    '''returns None\n\n
    redeployApplication(final String localEarPath, final String appName, final Hashtable properties, final String workspaceID)\n
    '''
def getApplicationInfo():
    '''returns Vector\n\n
    getApplicationInfo(final String appName, final Hashtable prefs, final String workspaceID)\n
    '''
def getModuleInfo():
    '''returns Vector\n\n
    getModuleInfo(final String appName, final Hashtable prefs, final String uniqueModuleURI, final String workspaceID)\n
    '''
def setApplicationInfo():
    '''returns None\n\n
    setApplicationInfo(final String appName, final Hashtable prefs, final String workspaceID, final Vector tasks)\n
    '''
def setModuleInfo():
    '''returns None\n\n
    setModuleInfo(final String appName, final Hashtable prefs, final String uniqueModuleURI, final String workspaceID, final Vector tasks)\n
    '''
def moveModule():
    '''returns None\n\n
    moveModule(final String appName, final Hashtable prefs, final String uniqueModuleURI, final ObjectName on, final String wID)\n
    '''
def exportApplication():
    '''returns None\n\n
    exportApplication(final String appName, final String pathName, final Hashtable prefs, final String workspaceID)\n
    '''
def extractDDL():
    '''returns None\n\n
    extractDDL(final String appName, final String ddlPrefix, final String dirName, final Hashtable prefs, final String workspaceID)\n
    '''
def publishWSDL():
    '''returns None\n\n
    publishWSDL(final String appName, final String pathName, final Hashtable prefs, final String workspaceID)\n
    '''
def listSystemApplications():
    '''returns Vector\n\n
    listSystemApplications(final Hashtable prefs, final String wID)\n
    '''
def listApplicationsAsSystem():
    '''returns Vector\n\n
    listApplicationsAsSystem(final Hashtable prefs, final String wID)\n
    listApplicationsAsSystem(final String targetScope, final Hashtable prefs, final String wID)\n
    '''
def listApplications():
    '''returns Vector\n\n
    listApplications(final Hashtable prefs, final String wID)\n
    listApplications(final String targetScope, final Hashtable prefs, final String wID)\n
    '''
def listModules():
    '''returns Object\n\n
    listModules(final String appName, final Hashtable prefs, final String workspaceID)\n
    '''
def listURIs():
    '''returns List\n\n
    listURIs(final String appName, final String moduleURI, final Hashtable prefs, final String sessionID)\n
    '''
def removeAllAppsFromNode():
    '''returns None\n\n
    removeAllAppsFromNode(final String nodeName, final String cellName, final Hashtable prefs, final String wID)\n
    '''
def removeAllAppsFromServer():
    '''returns None\n\n
    removeAllAppsFromServer(final ObjectName objectName, final Hashtable prefs, final String wID)\n
    '''
def removeAllAppsFromCluster():
    '''returns None\n\n
    removeAllAppsFromCluster(final ObjectName objectName, final Hashtable prefs, final String wID)\n
    '''
def changeServerToCluster():
    '''returns None\n\n
    changeServerToCluster(final ObjectName serverName, final ObjectName clusterName, final Hashtable prefs, final String wID)\n
    '''
def clusterMemberAdded():
    '''returns None\n\n
    clusterMemberAdded(final ObjectName memberName, final ObjectName clusterName, final Hashtable prefs, final String wID)\n
    '''
def updateAccessIDs():
    '''returns None\n\n
    updateAccessIDs(final String appName, final Boolean bAll, final Hashtable prefs, final String wID)\n
    '''
def deleteUserAndGroupEntries():
    '''returns None\n\n
    deleteUserAndGroupEntries(final String appName, final Hashtable prefs, final String wID)\n
    '''
def startApplication():
    '''returns String\n\n
    startApplication(final String appName, final Hashtable prefs, final String wID)\n
    startApplication(final String appName, final String target, final Hashtable prefs, final String wID)\n
    '''
def stopApplication():
    '''returns String\n\n
    stopApplication(final String appName, final Hashtable prefs, final String wID)\n
    stopApplication(final String appName, final String target, final Hashtable prefs, final String wID)\n
    '''
def installStandaloneRAR():
    '''returns None\n\n
    installStandaloneRAR(final String rarPath, final Hashtable props, final String workspaceID)\n
    '''
def compareSecurityPolicy():
    '''returns Vector\n\n
    compareSecurityPolicy(final String policyData, final Hashtable preferences, final String workspaceID)\n
    '''
def compareSecurityPolicyAsSystem():
    '''returns Vector\n\n
    compareSecurityPolicyAsSystem(final String policyData, final Hashtable preferences, final String workspaceID)\n
    '''
def searchJNDIReferences():
    '''returns Hashtable\n\n
    searchJNDIReferences(final List sList, final String nodes, final Hashtable prefs, final String wID)\n
    '''
def updateApplication():
    '''returns None\n\n
    updateApplication(final String appName, final String contentURI, final String pathToContents, final String operation, final Hashtable properties, final String sessionID)\n
    '''
def updateApplicationLocal():
    '''returns None\n\n
    updateApplicationLocal(final String appName, final String contentURI, final String pathToContents, final String operation, final Hashtable properties, final AppNotification.Listener notfListener, final String sessionID)\n
    '''
def _updateApplication():
    '''returns None\n\n
    _updateApplication(final String appName, final String contentURI, final String pathToContents, final String operation, Hashtable props, final AppNotification.Listener notf, final String sessionID)\n
    '''
def updateClusterLocal():
    '''returns None\n\n
    updateClusterLocal(final String[] appNames, final Integer timeout, final Hashtable props, final String wsId, final AppNotification.Listener notif)\n
    '''
def updateCluster():
    '''returns None\n\n
    updateCluster(final String[] appNames, final Integer timeout, final Hashtable props, final String wsId)\n
    '''
def searchResources():
    '''returns List\n\n
    searchResources(final String appName, final Hashtable prefs, final String wID)\n
    '''
def convertRefToConfigID():
    '''returns List\n\n
    convertRefToConfigID(final String appName, final List resources, final Hashtable prefs, final String wID)\n
    '''
def getApplicationContents():
    '''returns byte[]\n\n
    getApplicationContents(final String appName, final String uri, final Hashtable prefs, final String wID)\n
    '''
def getDistributionStatus():
    '''returns None\n\n
    getDistributionStatus(final String appName, final Hashtable prefs, final String wID)\n
    '''
def getAppAssociation():
    '''returns String[]\n\n
    getAppAssociation(final String scope, final String retVal, final Hashtable prefs, final String wID)\n
    '''
def getEditionInfo():
    '''returns EditionInfo[]\n\n
    getEditionInfo(final String appName, final String edition, final Hashtable prefs, final String wID)\n
    '''
def setEditionInfo():
    '''returns None\n\n
    setEditionInfo(final EditionInfo[] info, final Hashtable prefs, final String wID)\n
    '''
