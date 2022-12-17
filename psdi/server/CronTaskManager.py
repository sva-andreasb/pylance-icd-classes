def ():
    '''returns CronIncrementThread\n\n
    ()\n
    (final MXServer mxServer)\n
    (final CronTaskManager cm)\n
    ()\n
    '''
def configFromProperties():
    '''returns None\n\n
    configFromProperties()\n
    '''
def suspendCrontasks():
    '''returns None\n\n
    suspendCrontasks()\n
    '''
def isReadyForAdminMode():
    '''returns boolean\n\n
    isReadyForAdminMode()\n
    '''
def activeCronThreads():
    '''returns Enumeration\n\n
    activeCronThreads()\n
    '''
def loadCrontask():
    '''returns None\n\n
    loadCrontask(final String taskName, final String instanceName, final String className)\n
    '''
def restart():
    '''returns None\n\n
    restart()\n
    '''
def handleAutoRemoval():
    '''returns None\n\n
    handleAutoRemoval(final CronTask cronTask)\n
    '''
def getInstanceMbo():
    '''returns CrontaskInstanceRemote\n\n
    getInstanceMbo(final String taskName, final String instanceName)\n
    '''
def deactivate():
    '''returns None\n\n
    deactivate(final String taskName, final String instName)\n
    deactivate(final String key)\n
    '''
def activate():
    '''returns None\n\n
    activate(final CrontaskInstanceRemote inst)\n
    '''
def runTenantsChanged():
    '''returns None\n\n
    runTenantsChanged()\n
    '''
def logSql():
    '''returns None\n\n
    logSql(final String sql, final Connection con)\n
    '''
def setLastKPICronTaskRun():
    '''returns None\n\n
    setLastKPICronTaskRun()\n
    '''
def getLastKPICronTaskRun():
    '''returns Date\n\n
    getLastKPICronTaskRun()\n
    '''
def eventValidate():
    '''returns boolean\n\n
    eventValidate(final EventMessage em)\n
    '''
def preSaveEventAction():
    '''returns None\n\n
    preSaveEventAction(final EventMessage em)\n
    '''
def eventAction():
    '''returns None\n\n
    eventAction(final EventMessage em)\n
    '''
def postCommitEventAction():
    '''returns None\n\n
    postCommitEventAction(final EventMessage em)\n
    '''
def markShutdown():
    '''returns None\n\n
    markShutdown()\n
    '''
def isMarkedForShutDown():
    '''returns boolean\n\n
    isMarkedForShutDown()\n
    '''
def startTask():
    '''returns None\n\n
    startTask()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def removeDeadSessions():
    '''returns None\n\n
    removeDeadSessions()\n
    '''
def removeDeadTenantSessions():
    '''returns None\n\n
    removeDeadTenantSessions()\n
    '''
def printTaskSchedulerInfo():
    '''returns None\n\n
    printTaskSchedulerInfo()\n
    '''
