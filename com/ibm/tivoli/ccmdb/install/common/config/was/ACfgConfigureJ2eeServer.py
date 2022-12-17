def ():
    '''returns ACfgConfigureJ2eeServer\n\n
    ()\n
    '''
def applicationServerExists():
    '''returns boolean\n\n
    applicationServerExists(final String serverName)\n
    '''
def applicationServerExistsAndConfigured():
    '''returns boolean\n\n
    applicationServerExistsAndConfigured(final String appServerName)\n
    '''
def configMEAXmls():
    '''returns TaskResult\n\n
    configMEAXmls()\n
    '''
def createApplicationServer():
    '''returns TaskResult\n\n
    createApplicationServer(final String nodeName, final String serverName)\n
    '''
def createUsersInDirectory():
    '''returns TaskResult\n\n
    createUsersInDirectory(final List<String> userListAndGroupMemberString)\n
    createUsersInDirectory(final List<String> userListAndGroupMemberString, final HashSet<String> passwords)\n
    '''
def createVirtualHost():
    '''returns TaskResult\n\n
    createVirtualHost(final String virtualHostName, final String webServerPort, final String applicationServerName, final Boolean addHttpPort)\n
    '''
def maximoApplicationInstalled():
    '''returns boolean\n\n
    maximoApplicationInstalled(final String applicationName)\n
    '''
def modifyTaddmLaunchEntries():
    '''returns TaskResult\n\n
    modifyTaddmLaunchEntries()\n
    '''
def modifyWebXml():
    '''returns TaskResult\n\n
    modifyWebXml()\n
    '''
def disableAppSecurity():
    '''returns TaskResult\n\n
    disableAppSecurity()\n
    '''
def runJythonScript():
    '''returns TaskResult\n\n
    runJythonScript(final String script, final String[] args)\n
    '''
def startApplicationServer():
    '''returns boolean\n\n
    startApplicationServer(final String serverName)\n
    '''
def stopApplicationServer():
    '''returns boolean\n\n
    stopApplicationServer(final String serverName)\n
    '''
def virtualHostExists():
    '''returns boolean\n\n
    virtualHostExists(final String virtualHostName, final String webServerPort)\n
    '''
def wasDataSourceExists():
    '''returns boolean\n\n
    wasDataSourceExists()\n
    '''
def webServerExists():
    '''returns boolean\n\n
    webServerExists()\n
    '''
def aboutThisTask():
    '''returns String\n\n
    aboutThisTask(final Task taskAction)\n
    '''
def getTaskTotalTime():
    '''returns int\n\n
    getTaskTotalTime(final Task taskAction)\n
    '''
def getTaskWeightCompleted():
    '''returns int\n\n
    getTaskWeightCompleted()\n
    '''
def preCheck():
    '''returns List<TaskResult>\n\n
    preCheck()\n
    '''
def runConfigurationStep():
    '''returns TaskResult\n\n
    runConfigurationStep()\n
    '''
def undoConfiguration():
    '''returns TaskResult\n\n
    undoConfiguration()\n
    '''
def validate():
    '''returns List<TaskResult>\n\n
    validate()\n
    '''
def verifyCompletion():
    '''returns TaskResult\n\n
    verifyCompletion()\n
    '''
def isNodeAgentRunning():
    '''returns boolean\n\n
    isNodeAgentRunning()\n
    '''
def deleteApplicationServer():
    '''returns TaskResult\n\n
    deleteApplicationServer()\n
    '''
def deleteUsersFromDirectory():
    '''returns TaskResult\n\n
    deleteUsersFromDirectory(final String userListAndGroupMembershipString)\n
    '''
def deleteVirtualHost():
    '''returns TaskResult\n\n
    deleteVirtualHost(final String virtualHost)\n
    '''
def undeployApplication():
    '''returns TaskResult\n\n
    undeployApplication(final String applicationName)\n
    '''
def addUsersAndGroupsToVMM():
    '''returns List<String>\n\n
    addUsersAndGroupsToVMM(final List<ProductTrackingInformation> productInformationList, final Document doc)\n
    '''
def setupJ2eeConnection():
    '''returns ICfgJ2eeConnection\n\n
    setupJ2eeConnection()\n
    '''
