COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
OPTIMIZATION_SERVICE_USER = "String  \"__optimservice\""
OPTIMIZATION_SERVICE_PWD = "String  \"manager\""
def setProcessingService():
    '''returns None\n\n
    setProcessingService(final IloScenarioProcessingService ps)\n
    '''
def getOptimizationTaskType():
    '''returns OptimizationTaskType\n\n
    getOptimizationTaskType(final IloScenario scenario)\n
    '''
def getTaskName():
    '''returns String\n\n
    getTaskName(final IloScenario scenario)\n
    '''
def call():
    '''returns Object\n\n
    call()\n
    '''
def submit():
    '''returns boolean\n\n
    submit(final IloJobInputOutput jobIO)\n
    '''
def canSubmitTask():
    '''returns boolean\n\n
    canSubmitTask(final IloAbstractScenarioTaskInputOutput jobIO)\n
    '''
def onCompletion():
    '''returns None\n\n
    onCompletion(final IloScenario scenario)\n
    '''
def onSubmit():
    '''returns None\n\n
    onSubmit(final IloScenario scenario, final TaskDetails taskDetails)\n
    '''
