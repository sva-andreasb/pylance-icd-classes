def OptimizationService():
'''public OptimizationService(final MXServer mxServer)
'''
pass
def init():
'''public void init()
'''
pass
def deployOptimizationApp():
'''public void deployOptimizationApp(final String odmApplicationName, final ODMAppDeployInfo appDeployInfo, final UserInfo userInfo)
'''
pass
def runOptimization():
'''public boolean runOptimization(final UserInfo userInfo, final String odmApplicationName, final OptimizationInputProcessParameters inputProcessParameters, final OptimizationOutputProcessParameters outputProcessParameters)
'''
pass
def listenToODMERun():
'''public void listenToODMERun(final MboRemote listenerMbo, final boolean listen, final long skdProjectId)
'''
pass
def ODMEIsRunning():
'''public boolean ODMEIsRunning(final long skdProjectId)
'''
pass
def startSKDODMERUN():
'''public long startSKDODMERUN(final long skdProjectId, final String user, final String status)
public long startSKDODMERUN(final long skdProjectId, final String user, final String status, final long skdOdmeRunIdIn)
'''
pass
def finishSKDODMERUN():
'''public void finishSKDODMERUN(final long skdProjectId, final String status)
public void finishSKDODMERUN(final long skdProjectId, final String status, final long skdOdmeRunId)
'''
pass
def setJobIDSKDODMERUN():
'''public void setJobIDSKDODMERUN(final long skdOdmeRunId, final String mosJobId)
'''
pass
def ODMEaddRunMsg():
'''public synchronized void ODMEaddRunMsg(final long skdProjectId, final UserInfo userInfo, final String message, final boolean key)
'''
pass
def ODMEclearRunMsg():
'''public synchronized void ODMEclearRunMsg(final long skdProjectId)
'''
pass
def ODMEclearCompleted():
'''public synchronized void ODMEclearCompleted()
'''
pass
def getUseCPS():
'''public boolean getUseCPS(final UserInfo userInfo)
'''
pass
def getOptimizationMosAPIBaseURL():
'''public String getOptimizationMosAPIBaseURL(final UserInfo userInfo)
'''
pass
def getOptimizationMosAPIKey():
'''public String getOptimizationMosAPIKey(final UserInfo userInfo)
'''
pass
def cancelOptimizationJob():
'''public void cancelOptimizationJob(final String jobId, final UserInfo userInfo)
'''
pass
