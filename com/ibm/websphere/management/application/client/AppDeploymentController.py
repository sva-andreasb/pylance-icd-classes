taskHelperSuffix = "String  \"Helper\""
def ():
    '''returns AppDeploymentController\n\n
    (final AppDeploymentInfo info, final Hashtable prefs, final Vector taskI)\n
    (final Vector tAll, final Vector taskI, final Hashtable prefs)\n
    (final AppDeploymentInfo info, final Vector tAll, final Hashtable prefs, final Vector taskI)\n
    '''
def getDeploymentMode():
    '''returns long\n\n
    getDeploymentMode()\n
    '''
def getAppDeploymentTaskNames():
    '''returns String[]\n\n
    getAppDeploymentTaskNames()\n
    '''
def getFirstTask():
    '''returns AppDeploymentTask\n\n
    getFirstTask()\n
    '''
def getNextTask():
    '''returns AppDeploymentTask\n\n
    getNextTask()\n
    '''
def getTaskByName():
    '''returns AppDeploymentTask\n\n
    getTaskByName(final String taskName, final boolean b)\n
    getTaskByName(final String taskName)\n
    '''
def getAllTasks():
    '''returns Vector\n\n
    getAllTasks()\n
    '''
def getDependencyTask():
    '''returns None\n\n
    getDependencyTask(final String taskName)\n
    '''
def close():
    '''returns None\n\n
    close(final boolean bSave, final boolean bValidate, final boolean bClose)\n
    '''
def saveAndClose():
    '''returns None\n\n
    saveAndClose()\n
    '''
def validate():
    '''returns String[]\n\n
    validate()\n
    '''
def validateInTaskHelper():
    '''returns String[]\n\n
    validateInTaskHelper(final String taskName)\n
    '''
def getAppOptions():
    '''returns Hashtable\n\n
    getAppOptions()\n
    '''
def setAppOptions():
    '''returns None\n\n
    setAppOptions(final Hashtable tbl)\n
    '''
def getAppDeploymentSavedResults():
    '''returns Hashtable\n\n
    getAppDeploymentSavedResults()\n
    '''
def getTaskInfo():
    '''returns AppDeploymentTaskInfo\n\n
    getTaskInfo()\n
    getTaskInfo(final String taskName)\n
    '''
def isPartialDeploymentInfo():
    '''returns boolean\n\n
    isPartialDeploymentInfo()\n
    '''
def getSecurityPolicyData():
    '''returns String\n\n
    getSecurityPolicyData()\n
    '''
def getSecurityPolicyWarning():
    '''returns String\n\n
    getSecurityPolicyWarning()\n
    '''
def saveAsFile():
    '''returns None\n\n
    saveAsFile(final String moduleUri, final String fileUriInModule, final InputStream inputStream)\n
    '''
def createDeploymentPlan():
    '''returns None\n\n
    createDeploymentPlan(final OutputStream out)\n
    '''
def readDeploymentPlan():
    '''returns None\n\n
    readDeploymentPlan(final File file)\n
    readDeploymentPlan(final InputStream in)\n
    '''
def getSelectedOptions():
    '''returns List\n\n
    getSelectedOptions()\n
    '''
def getAppVersion():
    '''returns int\n\n
    getAppVersion()\n
    getAppVersion(final boolean checkForFeature)\n
    '''
def getRarVersion():
    '''returns int\n\n
    getRarVersion()\n
    '''
def getServerTable():
    '''returns Hashtable\n\n
    getServerTable()\n
    '''
def getAdminClient():
    '''returns AdminClient\n\n
    getAdminClient()\n
    '''
def getConfigSession():
    '''returns Session\n\n
    getConfigSession()\n
    '''
def getConfigService():
    '''returns ConfigService\n\n
    getConfigService()\n
    '''
def checkIfEnhancedEar():
    '''returns boolean\n\n
    checkIfEnhancedEar()\n
    '''
def getEnhancedEarDeploymentResource():
    '''returns Resource\n\n
    getEnhancedEarDeploymentResource(final String resName)\n
    '''
def postAllPrepareTask():
    '''returns None\n\n
    postAllPrepareTask(final AppDeploymentInfo appInstallInfo, final AppDeploymentTask task)\n
    '''
def setVariableMap():
    '''returns None\n\n
    setVariableMap(final Vector vtask)\n
    '''
def preAllCompleteTask():
    '''returns AppDeploymentTask\n\n
    preAllCompleteTask(final AppDeploymentTask t)\n
    '''
def getModifiedTaskData():
    '''returns String[][]\n\n
    getModifiedTaskData(final String taskName, final String[][] data)\n
    '''
def resetDataHolder():
    '''returns None\n\n
    resetDataHolder()\n
    '''
def getDataHolder():
    '''returns DataHolder\n\n
    getDataHolder()\n
    '''
