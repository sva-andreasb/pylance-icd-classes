def ():
    '''returns AbstractTaskCommand\n\n
    (final TaskCommandMetadata inMetadata)\n
    (final CommandData commandData)\n
    '''
def getCurrentStep():
    '''returns CommandStep\n\n
    getCurrentStep(final int operation)\n
    getCurrentStep(final int operation, final String stepName)\n
    '''
def setCurrentStep():
    '''returns None\n\n
    setCurrentStep(final AbstractCommandStep newCurrentStep)\n
    '''
def getCurrentStepIndex():
    '''returns int\n\n
    getCurrentStepIndex()\n
    '''
def setCurrentStepIndex():
    '''returns None\n\n
    setCurrentStepIndex(final int index)\n
    '''
def listCommandSteps():
    '''returns String[]\n\n
    listCommandSteps()\n
    '''
def getCommandStep():
    '''returns CommandStep\n\n
    getCommandStep(final String stepName)\n
    '''
def addStep():
    '''returns None\n\n
    addStep(final AbstractCommandStep step, final int index)\n
    '''
def resetCommandData():
    '''returns None\n\n
    resetCommandData(final CommandData cmdData)\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def processTaskParameters():
    '''returns None\n\n
    processTaskParameters()\n
    '''
def commandParamsModified():
    '''returns None\n\n
    commandParamsModified()\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    '''
def getTaskCommandResult():
    '''returns TaskCommandResult\n\n
    getTaskCommandResult()\n
    '''
def listAllStepParamsData():
    '''returns None\n\n
    listAllStepParamsData()\n
    '''
