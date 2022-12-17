def ():
    '''returns ClientTaskCmdNotificationListener\n\n
    (final TaskCommandMetadata metadata)\n
    (final long cmdSession)\n
    '''
def getCommandStep():
    '''returns CommandStep\n\n
    getCommandStep(final String stepName)\n
    '''
def processTaskParameters():
    '''returns None\n\n
    processTaskParameters()\n
    '''
def listCommandSteps():
    '''returns String[]\n\n
    listCommandSteps()\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    execute(final CommandHistory cmdHistory)\n
    '''
def getCurrentStep():
    '''returns CommandStep\n\n
    getCurrentStep(final int operation, final String stepName)\n
    '''
def getCommandSession():
    '''returns TaskCommandSession\n\n
    getCommandSession()\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener()\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final Notification notf, final Object handback)\n
    '''
