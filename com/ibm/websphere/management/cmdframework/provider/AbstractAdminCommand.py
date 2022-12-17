ASYNC_CUSTOM_TAG = "String  \"async\""
DYNAMIC_CUSTOM_TAG = "String  \"dynamicStep\""
PRIVATE_CUSTOM_TAG = "String  \"private\""
def ():
    '''returns CmdNotificationListener\n\n
    (final CommandMetadata metadata)\n
    (final CommandData inCommandData)\n
    ()\n
    (final long cmdSession)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getCommandMetadata():
    '''returns CommandMetadata\n\n
    getCommandMetadata()\n
    '''
def getTargetObject():
    '''returns Object\n\n
    getTargetObject()\n
    '''
def setTargetObject():
    '''returns None\n\n
    setTargetObject(final Object obj)\n
    '''
def listSetParams():
    '''returns Collection\n\n
    listSetParams()\n
    '''
def getParameter():
    '''returns Object\n\n
    getParameter(final String parameterName)\n
    '''
def isAsyncCommand():
    '''returns boolean\n\n
    isAsyncCommand()\n
    '''
def isDynamicStepCommand():
    '''returns boolean\n\n
    isDynamicStepCommand()\n
    '''
def isPrivateParameter():
    '''returns boolean\n\n
    isPrivateParameter(final String paramName)\n
    '''
def listAllParameterName():
    '''returns List\n\n
    listAllParameterName()\n
    '''
def listParameterName():
    '''returns List\n\n
    listParameterName()\n
    '''
def setParameter():
    '''returns None\n\n
    setParameter(final String paramName, final Object value)\n
    '''
def setOrigParameterValue():
    '''returns None\n\n
    setOrigParameterValue(final String paramName, final Object value)\n
    '''
def getOrigParameterValue():
    '''returns Object\n\n
    getOrigParameterValue(final String paramName)\n
    '''
def getChoices():
    '''returns Object[]\n\n
    getChoices(final String paramName)\n
    '''
def getTargetObjectChoices():
    '''returns Object[]\n\n
    getTargetObjectChoices()\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def setConfigSession():
    '''returns None\n\n
    setConfigSession(final Session session)\n
    '''
def getConfigSession():
    '''returns Session\n\n
    getConfigSession()\n
    '''
def getCommandResult():
    '''returns CommandResult\n\n
    getCommandResult()\n
    '''
def save():
    '''returns None\n\n
    save(final OutputStream outputStream)\n
    '''
def execute():
    '''returns None\n\n
    execute(final CommandHistory cmdHistory)\n
    '''
def setCommandSession():
    '''returns None\n\n
    setCommandSession(final TaskCommandSession session)\n
    '''
def getCommandSession():
    '''returns TaskCommandSession\n\n
    getCommandSession()\n
    '''
def setCmdHandler():
    '''returns None\n\n
    setCmdHandler(final CmdNotificationHandler handler)\n
    '''
def getResult():
    '''returns Collection\n\n
    getResult()\n
    '''
def sendNotification():
    '''returns None\n\n
    sendNotification(final CommandNotification cmdNotification)\n
    '''
def redo():
    '''returns None\n\n
    redo()\n
    '''
def cleanupUploadedFiles():
    '''returns None\n\n
    cleanupUploadedFiles()\n
    '''
def resetCommandData():
    '''returns None\n\n
    resetCommandData(final CommandData cmdData)\n
    '''
def generateScript():
    '''returns String\n\n
    generateScript(final String lang)\n
    '''
def setCmdMgrType():
    '''returns None\n\n
    setCmdMgrType(final Integer cmdMgrType)\n
    '''
def getCmdMgrType():
    '''returns Integer\n\n
    getCmdMgrType()\n
    '''
def createParameterMetadata():
    '''returns ParameterMetadata\n\n
    createParameterMetadata(final String pmName, final Hashtable featureList)\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final Notification notf, final Object handback)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener()\n
    '''
def isSuccess():
    '''returns boolean\n\n
    isSuccess()\n
    '''
def isComplete():
    '''returns boolean\n\n
    isComplete()\n
    '''
