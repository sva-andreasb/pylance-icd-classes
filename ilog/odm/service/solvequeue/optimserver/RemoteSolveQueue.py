COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns RemoteSolveQueue\n\n
    (final IloDataService dataService, final String optimServerLocation, final String archiveChecksum)\n
    '''
def getRunningTaskInteractor():
    '''returns RunningOptimTaskInteractor\n\n
    getRunningTaskInteractor(final IloScenario scenario)\n
    '''
def notifyCredentialInvalidated():
    '''returns None\n\n
    notifyCredentialInvalidated()\n
    '''
def getCountOfTasksToCompleteBeforeShutdown():
    '''returns int\n\n
    getCountOfTasksToCompleteBeforeShutdown()\n
    '''
def submitTask():
    '''returns None\n\n
    submitTask(final IloAbstractScenarioTaskInputOutput jobIO)\n
    '''
def getTaskDetails():
    '''returns TaskDetails\n\n
    getTaskDetails(final IloScenario scenario)\n
    '''
def ensureTaskCompletion():
    '''returns None\n\n
    ensureTaskCompletion(final IloScenario scenario)\n
    '''
def getRunningOptimTaskInteractor():
    '''returns RunningOptimTaskInteractor\n\n
    getRunningOptimTaskInteractor(final IloScenario scenario)\n
    '''
def cancelWaitingTask():
    '''returns boolean\n\n
    cancelWaitingTask(final IloScenario scenario)\n
    '''
