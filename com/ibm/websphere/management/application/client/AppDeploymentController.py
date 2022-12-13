taskHelperSuffix = "String  Helper""
def readArchive():
'''public static AppDeploymentController readArchive(final String ear, final Hashtable preferences)
public static AppDeploymentController readArchive(final String ear, final Hashtable preferences, final Vector taskI)
'''
pass
def AppDeploymentController():
'''public AppDeploymentController(final AppDeploymentInfo info, final Hashtable prefs, final Vector taskI)
public AppDeploymentController(final Vector tAll, final Vector taskI, final Hashtable prefs)
public AppDeploymentController(final AppDeploymentInfo info, final Vector tAll, final Hashtable prefs, final Vector taskI)
'''
pass
def getDeploymentMode():
'''public long getDeploymentMode()
'''
pass
def getAppDeploymentTaskNames():
'''public String[] getAppDeploymentTaskNames()
'''
pass
def getFirstTask():
'''public AppDeploymentTask getFirstTask()
'''
pass
def getNextTask():
'''public AppDeploymentTask getNextTask()
'''
pass
def getTaskByName():
'''public AppDeploymentTask getTaskByName(final String taskName, final boolean b)
public AppDeploymentTask getTaskByName(final String taskName)
'''
pass
def getAllTasks():
'''public Vector getAllTasks()
'''
pass
def getDependencyTask():
'''public void getDependencyTask(final String taskName)
'''
pass
def close():
'''public void close(final boolean bSave, final boolean bValidate, final boolean bClose)
'''
pass
def saveAndClose():
'''public void saveAndClose()
'''
pass
def validate():
'''public String[] validate()
'''
pass
def validateInTaskHelper():
'''public String[] validateInTaskHelper(final String taskName)
'''
pass
def getAppOptions():
'''public Hashtable getAppOptions()
'''
pass
def setAppOptions():
'''public void setAppOptions(final Hashtable tbl)
'''
pass
def getAppDeploymentSavedResults():
'''public Hashtable getAppDeploymentSavedResults()
'''
pass
def getTaskInfo():
'''public AppDeploymentTaskInfo getTaskInfo()
public AppDeploymentTaskInfo getTaskInfo(final String taskName)
'''
pass
def isPartialDeploymentInfo():
'''public boolean isPartialDeploymentInfo()
'''
pass
def getSecurityPolicyData():
'''public String getSecurityPolicyData()
'''
pass
def getSecurityPolicyWarning():
'''public String getSecurityPolicyWarning()
'''
pass
def saveAsFile():
'''public void saveAsFile(final String moduleUri, final String fileUriInModule, final InputStream inputStream)
'''
pass
def createDeploymentPlan():
'''public void createDeploymentPlan(final OutputStream out)
'''
pass
def readDeploymentPlan():
'''public void readDeploymentPlan(final File file)
public void readDeploymentPlan(final InputStream in)
'''
pass
def getSelectedOptions():
'''public List getSelectedOptions()
'''
pass
def getAppVersion():
'''public int getAppVersion()
public int getAppVersion(final boolean checkForFeature)
'''
pass
def getRarVersion():
'''public int getRarVersion()
'''
pass
def getServerTable():
'''public Hashtable getServerTable()
'''
pass
def getAdminClient():
'''public AdminClient getAdminClient()
'''
pass
def getConfigSession():
'''public Session getConfigSession()
'''
pass
def getConfigService():
'''public ConfigService getConfigService()
'''
pass
def checkIfEnhancedEar():
'''public boolean checkIfEnhancedEar()
'''
pass
def getEnhancedEarDeploymentResource():
'''public Resource getEnhancedEarDeploymentResource(final String resName)
'''
pass
def postAllPrepareTask():
'''public void postAllPrepareTask(final AppDeploymentInfo appInstallInfo, final AppDeploymentTask task)
'''
pass
def setVariableMap():
'''public void setVariableMap(final Vector vtask)
'''
pass
def preAllCompleteTask():
'''public AppDeploymentTask preAllCompleteTask(final AppDeploymentTask t)
'''
pass
def getModifiedTaskData():
'''public String[][] getModifiedTaskData(final String taskName, final String[][] data)
'''
pass
def resetDataHolder():
'''public void resetDataHolder()
'''
pass
def getDataHolder():
'''public DataHolder getDataHolder()
'''
pass
