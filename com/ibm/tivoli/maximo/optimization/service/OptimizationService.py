def ():
    '''returns OptimizationService\n\n
    (final MXServer mxServer)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def deployOptimizationApp():
    '''returns None\n\n
    deployOptimizationApp(final String odmApplicationName, final ODMAppDeployInfo appDeployInfo, final UserInfo userInfo)\n
    '''
def runOptimization():
    '''returns boolean\n\n
    runOptimization(final UserInfo userInfo, final String odmApplicationName, final OptimizationInputProcessParameters inputProcessParameters, final OptimizationOutputProcessParameters outputProcessParameters)\n
    '''
def listenToODMERun():
    '''returns None\n\n
    listenToODMERun(final MboRemote listenerMbo, final boolean listen, final long skdProjectId)\n
    '''
def ODMEIsRunning():
    '''returns boolean\n\n
    ODMEIsRunning(final long skdProjectId)\n
    '''
def startSKDODMERUN():
    '''returns long\n\n
    startSKDODMERUN(final long skdProjectId, final String user, final String status)\n
    startSKDODMERUN(final long skdProjectId, final String user, final String status, final long skdOdmeRunIdIn)\n
    '''
def finishSKDODMERUN():
    '''returns None\n\n
    finishSKDODMERUN(final long skdProjectId, final String status)\n
    finishSKDODMERUN(final long skdProjectId, final String status, final long skdOdmeRunId)\n
    '''
def setJobIDSKDODMERUN():
    '''returns None\n\n
    setJobIDSKDODMERUN(final long skdOdmeRunId, final String mosJobId)\n
    '''
def getUseCPS():
    '''returns boolean\n\n
    getUseCPS(final UserInfo userInfo)\n
    '''
def getOptimizationMosAPIBaseURL():
    '''returns String\n\n
    getOptimizationMosAPIBaseURL(final UserInfo userInfo)\n
    '''
def getOptimizationMosAPIKey():
    '''returns String\n\n
    getOptimizationMosAPIKey(final UserInfo userInfo)\n
    '''
def cancelOptimizationJob():
    '''returns None\n\n
    cancelOptimizationJob(final String jobId, final UserInfo userInfo)\n
    '''
