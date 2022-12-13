ASYNC_CUSTOM_TAG = "String  \"async\""
DYNAMIC_CUSTOM_TAG = "String  \"dynamicStep\""
PRIVATE_CUSTOM_TAG = "String  \"private\""
def AbstractAdminCommand():
    '''public AbstractAdminCommand(final CommandMetadata metadata)
    public AbstractAdminCommand(final CommandData inCommandData)
    '''
def getCommandMetadata():
    '''public static CommandMetadata getCommandMetadata(final String cmdName)
    public CommandMetadata getCommandMetadata()
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def setLocale():
    '''public void setLocale(final Locale locale)
    '''
def getName():
    '''public String getName()
    '''
def getTargetObject():
    '''public Object getTargetObject()
    '''
def setTargetObject():
    '''public void setTargetObject(final Object obj)
    '''
def listSetParams():
    '''public Collection listSetParams()
    '''
def getParameter():
    '''public Object getParameter(final String parameterName)
    '''
def isAsyncCommand():
    '''public boolean isAsyncCommand()
    '''
def isDynamicStepCommand():
    '''public boolean isDynamicStepCommand()
    '''
def isPrivateParameter():
    '''public boolean isPrivateParameter(final String paramName)
    '''
def listAllParameterName():
    '''public List listAllParameterName()
    '''
def listParameterName():
    '''public List listParameterName()
    '''
def setParameter():
    '''public void setParameter(final String paramName, final Object value)
    '''
def setOrigParameterValue():
    '''public void setOrigParameterValue(final String paramName, final Object value)
    '''
def getOrigParameterValue():
    '''public Object getOrigParameterValue(final String paramName)
    '''
def getChoices():
    '''public Object[] getChoices(final String paramName)
    '''
def getTargetObjectChoices():
    '''public Object[] getTargetObjectChoices()
    '''
def validate():
    '''public void validate()
    '''
def setConfigSession():
    '''public void setConfigSession(final Session session)
    '''
def getConfigSession():
    '''public Session getConfigSession()
    '''
def getCommandResult():
    '''public CommandResult getCommandResult()
    '''
def save():
    '''public void save(final OutputStream outputStream)
    '''
def execute():
    '''public void execute(final CommandHistory cmdHistory)
    '''
def setCommandSession():
    '''public void setCommandSession(final TaskCommandSession session)
    '''
def getCommandSession():
    '''public TaskCommandSession getCommandSession()
    '''
def setCmdHandler():
    '''public void setCmdHandler(final CmdNotificationHandler handler)
    '''
def getResult():
    '''public Collection getResult()
    '''
def sendNotification():
    '''public void sendNotification(final CommandNotification cmdNotification)
    '''
def redo():
    '''public void redo()
    '''
def cleanupUploadedFiles():
    '''public void cleanupUploadedFiles()
    '''
def resetCommandData():
    '''public void resetCommandData(final CommandData cmdData)
    '''
def generateScript():
    '''public String generateScript(final String lang)
    '''
def setCmdMgrType():
    '''public void setCmdMgrType(final Integer cmdMgrType)
    '''
def getCmdMgrType():
    '''public Integer getCmdMgrType()
    '''
def createParameterMetadata():
    '''public ParameterMetadata createParameterMetadata(final String pmName, final Hashtable featureList)
    '''
def CmdNotificationListener():
    '''public CmdNotificationListener()
    public CmdNotificationListener(final long cmdSession)
    '''
def handleNotification():
    '''public void handleNotification(final Notification notf, final Object handback)
    '''
def removeListener():
    '''public void removeListener()
    '''
def isSuccess():
    '''public boolean isSuccess()
    '''
def isComplete():
    '''public boolean isComplete()
    '''
