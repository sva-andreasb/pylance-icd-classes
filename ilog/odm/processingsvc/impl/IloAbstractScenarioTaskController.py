COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloAbstractScenarioTaskController\n\n
    (final IloProcessingService ps, final IloExecutionScope scope, final IloTaskConfig config, final IloTaskInputOutput io, final List<IloTaskController> tasks)\n
    '''
def resetForSubmit():
    '''returns None\n\n
    resetForSubmit()\n
    '''
def addJobListener():
    '''returns None\n\n
    addJobListener(final IloJobListener listener)\n
    '''
def removeJobListener():
    '''returns None\n\n
    removeJobListener(final IloJobListener listener)\n
    '''
def removeAllJobListeners():
    '''returns None\n\n
    removeAllJobListeners()\n
    '''
def getCompletionLevel():
    '''returns int\n\n
    getCompletionLevel()\n
    '''
def getCompletionPhase():
    '''returns String\n\n
    getCompletionPhase()\n
    '''
def getState():
    '''returns State\n\n
    getState()\n
    '''
def waitForCompletion():
    '''returns None\n\n
    waitForCompletion(final long timeOut)\n
    '''
def getProcessingService():
    '''returns IloProcessingServiceImpl\n\n
    getProcessingService()\n
    '''
def getExecutionScope():
    '''returns IloScenarioExecutionScope\n\n
    getExecutionScope()\n
    '''
def getConfig():
    '''returns IloRelationalTaskConfig\n\n
    getConfig()\n
    '''
def getInputOutput():
    '''returns IloAbstractScenarioTaskInputOutput\n\n
    getInputOutput()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
