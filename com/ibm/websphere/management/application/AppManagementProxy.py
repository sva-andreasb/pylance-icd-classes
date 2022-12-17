def sendJMXEvent():
    '''returns None\n\n
    sendJMXEvent(final Object arg0)\n
    sendJMXEvent(final String s, final Object arg0)\n
    '''
def getGlobalSettings():
    '''returns Hashtable\n\n
    getGlobalSettings()\n
    '''
def clusterMemberAdded():
    '''returns None\n\n
    clusterMemberAdded(final ObjectName arg0, final ObjectName arg1, final Hashtable arg2, final String arg3)\n
    '''
def changeServerToCluster():
    '''returns None\n\n
    changeServerToCluster(final ObjectName arg0, final ObjectName arg1, final Hashtable arg2, final String arg3)\n
    '''
def removeAllAppsFromCluster():
    '''returns None\n\n
    removeAllAppsFromCluster(final ObjectName arg0, final Hashtable arg1, final String arg2)\n
    '''
def removeAllAppsFromServer():
    '''returns None\n\n
    removeAllAppsFromServer(final ObjectName arg0, final Hashtable arg1, final String arg2)\n
    '''
def removeAllAppsFromNode():
    '''returns None\n\n
    removeAllAppsFromNode(final String arg0, final String arg1, final Hashtable arg2, final String arg3)\n
    '''
def checkIfAppExists():
    '''returns boolean\n\n
    checkIfAppExists(final String arg0, final Hashtable arg1, final String arg2)\n
    '''
def installStandaloneRAR():
    '''returns None\n\n
    installStandaloneRAR(final String arg0, final Hashtable arg1, final String arg2)\n
    '''
def compareSecurityPolicy():
    '''returns Vector\n\n
    compareSecurityPolicy(final String arg0, final Hashtable arg1, final String arg2)\n
    '''
def listModules():
    '''returns Object\n\n
    listModules(final String arg0, final Hashtable arg1, final String arg2)\n
    '''
def listApplications():
    '''returns Vector\n\n
    listApplications(final Hashtable arg0, final String arg1)\n
    listApplications(final String targetScope, final Hashtable props, final String sessionID)\n
    '''
def extractDDL():
    '''returns None\n\n
    extractDDL(final String arg0, final String arg1, final String arg2, final Hashtable arg3, final String arg4)\n
    '''
def exportApplication():
    '''returns None\n\n
    exportApplication(final String arg0, final String arg1, final Hashtable arg2, final String arg3)\n
    '''
def moveModule():
    '''returns None\n\n
    moveModule(final String arg0, final Hashtable arg1, final String arg2, final ObjectName arg3, final String arg4)\n
    '''
def setModuleInfo():
    '''returns None\n\n
    setModuleInfo(final String arg0, final Hashtable arg1, final String arg2, final String arg3, final Vector arg4)\n
    '''
def setApplicationInfo():
    '''returns None\n\n
    setApplicationInfo(final String arg0, final Hashtable arg1, final String arg2, final Vector arg3)\n
    '''
def getModuleInfo():
    '''returns Vector\n\n
    getModuleInfo(final String arg0, final Hashtable arg1, final String arg2, final String arg3)\n
    '''
def getApplicationInfo():
    '''returns Vector\n\n
    getApplicationInfo(final String arg0, final Hashtable arg1, final String arg2)\n
    '''
def redeployApplication():
    '''returns None\n\n
    redeployApplication(final String localEarPath, final String arg1, final Hashtable properties, final String arg3)\n
    '''
def redeployApplicationLocal():
    '''returns None\n\n
    redeployApplicationLocal(final String arg0, final String arg1, final Hashtable arg2, final AppNotification.Listener arg3, final String arg4)\n
    '''
def uninstallApplication():
    '''returns None\n\n
    uninstallApplication(final String arg0, final Hashtable arg1, final String arg2)\n
    '''
def uninstallApplicationLocal():
    '''returns None\n\n
    uninstallApplicationLocal(final String arg0, final Hashtable arg1, final AppNotification.Listener arg2, final String arg3)\n
    uninstallApplicationLocal(final String arg0, final Hashtable arg1, final AppNotification.Listener arg2)\n
    '''
def installApplicationLocal():
    '''returns None\n\n
    installApplicationLocal(final String arg0, final String arg1, final Hashtable arg2, final AppNotification.Listener arg3, final String arg4)\n
    installApplicationLocal(final String arg0, final String arg1, final Hashtable arg2, final AppNotification.Listener arg3)\n
    '''
def installApplication():
    '''returns None\n\n
    installApplication(final String localEarPath, final String appName, final Hashtable properties, final String workspaceID)\n
    installApplication(final String localEarPath, final Hashtable properties, final String workspaceID)\n
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
def publishWSDL():
    '''returns None\n\n
    publishWSDL(final String arg0, final String arg1, final Hashtable arg2, final String arg3)\n
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
    updateApplicationLocal(final String appName, final String contentURI, final String pathToContents, final String operation, final Hashtable properties, final AppNotification.Listener notf, final String sessionID)\n
    '''
def listURIs():
    '''returns List\n\n
    listURIs(final String appName, final String moduleURI, final Hashtable prefs, final String sessionID)\n
    '''
def updateCluster():
    '''returns None\n\n
    updateCluster(final String[] arg0, final Integer arg1, final Hashtable arg2, final String arg3)\n
    '''
def updateClusterLocal():
    '''returns None\n\n
    updateClusterLocal(final String[] arg0, final Integer arg1, final Hashtable arg2, final String arg3, final AppNotification.Listener arg4)\n
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
def listSystemApplications():
    '''returns Vector\n\n
    listSystemApplications(final Hashtable prefs, final String sessionID)\n
    '''
