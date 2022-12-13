def OptimizationService():
    '''public OptimizationService(final MXServer mxServer)
    '''
def init():
    '''public void init()
    '''
def deployOptimizationApp():
    '''public void deployOptimizationApp(final String odmApplicationName, final ODMAppDeployInfo appDeployInfo, final UserInfo userInfo)
    '''
def runOptimization():
    '''public boolean runOptimization(final UserInfo userInfo, final String odmApplicationName, final OptimizationInputProcessParameters inputProcessParameters, final OptimizationOutputProcessParameters outputProcessParameters)
    '''
def listenToODMERun():
    '''public void listenToODMERun(final MboRemote listenerMbo, final boolean listen, final long skdProjectId)
    '''
def ODMEIsRunning():
    '''public boolean ODMEIsRunning(final long skdProjectId)
    '''
def startSKDODMERUN():
    '''public long startSKDODMERUN(final long skdProjectId, final String user, final String status)
    public long startSKDODMERUN(final long skdProjectId, final String user, final String status, final long skdOdmeRunIdIn)
    '''
def finishSKDODMERUN():
    '''public void finishSKDODMERUN(final long skdProjectId, final String status)
    public void finishSKDODMERUN(final long skdProjectId, final String status, final long skdOdmeRunId)
    '''
def setJobIDSKDODMERUN():
    '''public void setJobIDSKDODMERUN(final long skdOdmeRunId, final String mosJobId)
    '''
def ODMEaddRunMsg():
    '''public synchronized void ODMEaddRunMsg(final long skdProjectId, final UserInfo userInfo, final String message, final boolean key)
    '''
def ODMEclearRunMsg():
    '''public synchronized void ODMEclearRunMsg(final long skdProjectId)
    '''
def ODMEclearCompleted():
    '''public synchronized void ODMEclearCompleted()
    '''
def getUseCPS():
    '''public boolean getUseCPS(final UserInfo userInfo)
    '''
def getOptimizationMosAPIBaseURL():
    '''public String getOptimizationMosAPIBaseURL(final UserInfo userInfo)
    '''
def getOptimizationMosAPIKey():
    '''public String getOptimizationMosAPIKey(final UserInfo userInfo)
    '''
def cancelOptimizationJob():
    '''public void cancelOptimizationJob(final String jobId, final UserInfo userInfo)
    '''
