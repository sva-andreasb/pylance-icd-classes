def modifyTaddmLaunchEntries():
    '''returns TaskResult\n\n
    modifyTaddmLaunchEntries()\n
    '''
def validateJMSSetup():
    '''returns List<TaskResult>\n\n
    validateJMSSetup(final List<DeploymentServer> serverList)\n
    '''
def nodeExists():
    '''returns boolean\n\n
    nodeExists(final String nodeName)\n
    '''
def isNodeAgentRunning():
    '''returns boolean\n\n
    isNodeAgentRunning(final String nodeName)\n
    '''
def virtualHostExists():
    '''returns boolean\n\n
    virtualHostExists(final String wasVirtualHostName, final String wasWebServerPort)\n
    '''
def createVirtualHost():
    '''returns TaskResult\n\n
    createVirtualHost(final String wasVirtualHostName, final String wasWebServerPort, final String wasAppServerName, final Boolean useHttpPort)\n
    '''
def deleteVirtualHost():
    '''returns TaskResult\n\n
    deleteVirtualHost(final String wasVirtualHostName)\n
    '''
def applicationServerExists():
    '''returns boolean\n\n
    applicationServerExists(final String applicationServerName)\n
    '''
def clusterExists():
    '''returns boolean\n\n
    clusterExists(final String clusterName)\n
    '''
def applicationServerExistsAndConfigured():
    '''returns boolean\n\n
    applicationServerExistsAndConfigured(final String wasAppServerName)\n
    '''
def deleteApplicationServer():
    '''returns TaskResult\n\n
    deleteApplicationServer(final String wasAppServerName)\n
    '''
def createApplicationServer():
    '''returns TaskResult\n\n
    createApplicationServer(final String wasNodeName, final String wasAppServerName)\n
    '''
def maximoApplicationInstalled():
    '''returns boolean\n\n
    maximoApplicationInstalled(final String application)\n
    '''
def webServerExists():
    '''returns boolean\n\n
    webServerExists(final List<DeploymentServer> serverList)\n
    '''
def webServerPortMatch():
    '''returns boolean\n\n
    webServerPortMatch(final String webServerName, final String wasWebServerPort)\n
    '''
def configureMaximoEnterpriseAdapter():
    '''returns TaskResult\n\n
    configureMaximoEnterpriseAdapter()\n
    '''
def startApplicationServer():
    '''returns boolean\n\n
    startApplicationServer(final String wasAppServerName)\n
    '''
def stopApplicationServer():
    '''returns boolean\n\n
    stopApplicationServer(final String wasAppServerName)\n
    '''
def getWASCellName():
    '''returns String\n\n
    getWASCellName()\n
    '''
def runJythonScript():
    '''returns TaskResult\n\n
    runJythonScript(final String fullyQualifiedPathToScript, final String[] args)\n
    runJythonScript(final String fullyQualifiedPathToScript, final String[] args, final HashSet<String> passwordSet)\n
    '''
def getTaskTotalTime():
    '''returns int\n\n
    getTaskTotalTime(final Task task)\n
    '''
def getTaskWeightCompleted():
    '''returns int\n\n
    getTaskWeightCompleted()\n
    '''
def aboutThisTask():
    '''returns String\n\n
    aboutThisTask(final Task task)\n
    '''
def createUsersInDirectory():
    '''returns TaskResult\n\n
    createUsersInDirectory(final List<String> userGroupList)\n
    createUsersInDirectory(final List<String> userGroupList, final HashSet<String> passwords)\n
    '''
def deleteUsersFromDirectory():
    '''returns TaskResult\n\n
    deleteUsersFromDirectory(final String userGroupList)\n
    '''
def disableAppSecurity():
    '''returns TaskResult\n\n
    disableAppSecurity()\n
    '''
def modifyWebXml():
    '''returns TaskResult\n\n
    modifyWebXml()\n
    modifyWebXml(final String authenticationScheme)\n
    '''
def preCheck():
    '''returns List<TaskResult>\n\n
    preCheck()\n
    '''
def validate():
    '''returns List<TaskResult>\n\n
    validate()\n
    '''
def runConfigurationStep():
    '''returns TaskResult\n\n
    runConfigurationStep()\n
    '''
def undoConfiguration():
    '''returns TaskResult\n\n
    undoConfiguration()\n
    '''
def verifyCompletion():
    '''returns TaskResult\n\n
    verifyCompletion()\n
    '''
def setupJ2eeConnection():
    '''returns ICfgJ2eeConnection\n\n
    setupJ2eeConnection()\n
    '''
