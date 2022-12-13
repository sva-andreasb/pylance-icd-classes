taskHelperSuffix = "String  \"Helper\""
def readArchive():
    '''public static AppDeploymentController readArchive(final String ear, final Hashtable preferences)
    public static AppDeploymentController readArchive(final String ear, final Hashtable preferences, final Vector taskI)
    '''
def AppDeploymentController():
    '''public AppDeploymentController(final AppDeploymentInfo info, final Hashtable prefs, final Vector taskI)
    public AppDeploymentController(final Vector tAll, final Vector taskI, final Hashtable prefs)
    public AppDeploymentController(final AppDeploymentInfo info, final Vector tAll, final Hashtable prefs, final Vector taskI)
    '''
def getDeploymentMode():
    '''public long getDeploymentMode()
    '''
def getAppDeploymentTaskNames():
    '''public String[] getAppDeploymentTaskNames()
    '''
def getFirstTask():
    '''public AppDeploymentTask getFirstTask()
    '''
def getNextTask():
    '''public AppDeploymentTask getNextTask()
    '''
def getTaskByName():
    '''public AppDeploymentTask getTaskByName(final String taskName, final boolean b)
    public AppDeploymentTask getTaskByName(final String taskName)
    '''
def getAllTasks():
    '''public Vector getAllTasks()
    '''
def getDependencyTask():
    '''public void getDependencyTask(final String taskName)
    '''
def close():
    '''public void close(final boolean bSave, final boolean bValidate, final boolean bClose)
    '''
def saveAndClose():
    '''public void saveAndClose()
    '''
def validate():
    '''public String[] validate()
    '''
def validateInTaskHelper():
    '''public String[] validateInTaskHelper(final String taskName)
    '''
def getAppOptions():
    '''public Hashtable getAppOptions()
    '''
def setAppOptions():
    '''public void setAppOptions(final Hashtable tbl)
    '''
def getAppDeploymentSavedResults():
    '''public Hashtable getAppDeploymentSavedResults()
    '''
def getTaskInfo():
    '''public AppDeploymentTaskInfo getTaskInfo()
    public AppDeploymentTaskInfo getTaskInfo(final String taskName)
    '''
def isPartialDeploymentInfo():
    '''public boolean isPartialDeploymentInfo()
    '''
def getSecurityPolicyData():
    '''public String getSecurityPolicyData()
    '''
def getSecurityPolicyWarning():
    '''public String getSecurityPolicyWarning()
    '''
def saveAsFile():
    '''public void saveAsFile(final String moduleUri, final String fileUriInModule, final InputStream inputStream)
    '''
def createDeploymentPlan():
    '''public void createDeploymentPlan(final OutputStream out)
    '''
def readDeploymentPlan():
    '''public void readDeploymentPlan(final File file)
    public void readDeploymentPlan(final InputStream in)
    '''
def getSelectedOptions():
    '''public List getSelectedOptions()
    '''
def getAppVersion():
    '''public int getAppVersion()
    public int getAppVersion(final boolean checkForFeature)
    '''
def getRarVersion():
    '''public int getRarVersion()
    '''
def getServerTable():
    '''public Hashtable getServerTable()
    '''
def getAdminClient():
    '''public AdminClient getAdminClient()
    '''
def getConfigSession():
    '''public Session getConfigSession()
    '''
def getConfigService():
    '''public ConfigService getConfigService()
    '''
def checkIfEnhancedEar():
    '''public boolean checkIfEnhancedEar()
    '''
def getEnhancedEarDeploymentResource():
    '''public Resource getEnhancedEarDeploymentResource(final String resName)
    '''
def postAllPrepareTask():
    '''public void postAllPrepareTask(final AppDeploymentInfo appInstallInfo, final AppDeploymentTask task)
    '''
def setVariableMap():
    '''public void setVariableMap(final Vector vtask)
    '''
def preAllCompleteTask():
    '''public AppDeploymentTask preAllCompleteTask(final AppDeploymentTask t)
    '''
def getModifiedTaskData():
    '''public String[][] getModifiedTaskData(final String taskName, final String[][] data)
    '''
def resetDataHolder():
    '''public void resetDataHolder()
    '''
def getDataHolder():
    '''public DataHolder getDataHolder()
    '''
