def ():
    '''returns RemoteCommandMgrImpl\n\n
    ()\n
    '''
def listCommandGroups():
    '''returns ArrayList\n\n
    listCommandGroups()\n
    '''
def listAllCommands():
    '''returns ArrayList\n\n
    listAllCommands()\n
    '''
def listCommands():
    '''returns ArrayList\n\n
    listCommands(final String commandGroup)\n
    listCommands()\n
    '''
def listCommandStepsWithData():
    '''returns ArrayList\n\n
    listCommandStepsWithData(final TaskCommandSession session, final EObjectSerializer cmdDataEObj)\n
    '''
def getCmdSession():
    '''returns TaskCommandSession\n\n
    getCmdSession(final String commandName)\n
    '''
def executeAsync():
    '''returns CommandResult\n\n
    executeAsync(final TaskCommandSession session, final EObjectSerializer command)\n
    '''
def execute():
    '''returns CommandResult\n\n
    execute(final EObjectSerializer command)\n
    execute(final TaskCommandSession session, final EObjectSerializer command)\n
    '''
def processTaskParameters():
    '''returns ArrayList\n\n
    processTaskParameters(final TaskCommandSession session, final EObjectSerializer command)\n
    '''
def listAllStepParamsData():
    '''returns None\n\n
    listAllStepParamsData(final TaskCommandData cmdData)\n
    '''
def getCommandGroupMetaInfo():
    '''returns EObjectSerializer\n\n
    getCommandGroupMetaInfo(final String commandGrpName, final Locale locale)\n
    '''
def getAllCommandGrpMetaInfo():
    '''returns Collection\n\n
    getAllCommandGrpMetaInfo(final Locale locale)\n
    '''
def getCommandMetaInfo():
    '''returns EObjectSerializer\n\n
    getCommandMetaInfo(final String commandName, final Locale locale)\n
    '''
def getAllCommandMetaInfo():
    '''returns Collection\n\n
    getAllCommandMetaInfo(final Locale locale)\n
    '''
def getCurrentStep():
    '''returns EObjectSerializer\n\n
    getCurrentStep(final TaskCommandSession session, final EObjectSerializer cliCmdStepDataEObj, final Integer operation, final String stepName)\n
    '''
def getCurrentStepInList():
    '''returns ArrayList\n\n
    getCurrentStepInList(final TaskCommandSession session, final EObjectSerializer cliCmdStepDataEObj, final Integer operation, final String stepName)\n
    '''
def contructSteps():
    '''returns ArrayList\n\n
    contructSteps(final String taskCmdName)\n
    '''
def sendCmdNotification():
    '''returns None\n\n
    sendCmdNotification(final String type, final Object e)\n
    '''
