def createCommand():
    '''returns AbstractAdminCommand\n\n
    createCommand(final CommandMetadata metadata)\n
    '''
def loadCommand():
    '''returns AbstractAdminCommand\n\n
    loadCommand(final CommandData cmdData)\n
    '''
def initCommandMetadata():
    '''returns List\n\n
    initCommandMetadata(final List metadata)\n
    '''
def createCommandStep():
    '''returns AbstractCommandStep\n\n
    createCommandStep(final AbstractTaskCommand taskCmd, final String stepName)\n
    '''
def loadCommandStep():
    '''returns AbstractCommandStep\n\n
    loadCommandStep(final AbstractTaskCommand taskCmd, final CommandStepData stepData)\n
    '''
def commandStepPosition():
    '''returns int\n\n
    commandStepPosition(final AbstractTaskCommand taskCmd, final String stepName)\n
    '''
