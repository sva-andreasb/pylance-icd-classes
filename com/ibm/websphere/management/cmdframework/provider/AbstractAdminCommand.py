ASYNC_CUSTOM_TAG = "String  async""
DYNAMIC_CUSTOM_TAG = "String  dynamicStep""
PRIVATE_CUSTOM_TAG = "String  private""
def AbstractAdminCommand():
'''public AbstractAdminCommand(final CommandMetadata metadata)
public AbstractAdminCommand(final CommandData inCommandData)
'''
pass
def getCommandMetadata():
'''public static CommandMetadata getCommandMetadata(final String cmdName)
public CommandMetadata getCommandMetadata()
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def setLocale():
'''public void setLocale(final Locale locale)
'''
pass
def getName():
'''public String getName()
'''
pass
def getTargetObject():
'''public Object getTargetObject()
'''
pass
def setTargetObject():
'''public void setTargetObject(final Object obj)
'''
pass
def listSetParams():
'''public Collection listSetParams()
'''
pass
def getParameter():
'''public Object getParameter(final String parameterName)
'''
pass
def isAsyncCommand():
'''public boolean isAsyncCommand()
'''
pass
def isDynamicStepCommand():
'''public boolean isDynamicStepCommand()
'''
pass
def isPrivateParameter():
'''public boolean isPrivateParameter(final String paramName)
'''
pass
def listAllParameterName():
'''public List listAllParameterName()
'''
pass
def listParameterName():
'''public List listParameterName()
'''
pass
def setParameter():
'''public void setParameter(final String paramName, final Object value)
'''
pass
def setOrigParameterValue():
'''public void setOrigParameterValue(final String paramName, final Object value)
'''
pass
def getOrigParameterValue():
'''public Object getOrigParameterValue(final String paramName)
'''
pass
def getChoices():
'''public Object[] getChoices(final String paramName)
'''
pass
def getTargetObjectChoices():
'''public Object[] getTargetObjectChoices()
'''
pass
def validate():
'''public void validate()
'''
pass
def setConfigSession():
'''public void setConfigSession(final Session session)
'''
pass
def getConfigSession():
'''public Session getConfigSession()
'''
pass
def getCommandResult():
'''public CommandResult getCommandResult()
'''
pass
def save():
'''public void save(final OutputStream outputStream)
'''
pass
def execute():
'''public void execute(final CommandHistory cmdHistory)
'''
pass
def setCommandSession():
'''public void setCommandSession(final TaskCommandSession session)
'''
pass
def getCommandSession():
'''public TaskCommandSession getCommandSession()
'''
pass
def setCmdHandler():
'''public void setCmdHandler(final CmdNotificationHandler handler)
'''
pass
def getResult():
'''public Collection getResult()
'''
pass
def sendNotification():
'''public void sendNotification(final CommandNotification cmdNotification)
'''
pass
def redo():
'''public void redo()
'''
pass
def cleanupUploadedFiles():
'''public void cleanupUploadedFiles()
'''
pass
def resetCommandData():
'''public void resetCommandData(final CommandData cmdData)
'''
pass
def generateScript():
'''public String generateScript(final String lang)
'''
pass
def setCmdMgrType():
'''public void setCmdMgrType(final Integer cmdMgrType)
'''
pass
def getCmdMgrType():
'''public Integer getCmdMgrType()
'''
pass
def createParameterMetadata():
'''public ParameterMetadata createParameterMetadata(final String pmName, final Hashtable featureList)
'''
pass
def CmdNotificationListener():
'''public CmdNotificationListener()
public CmdNotificationListener(final long cmdSession)
'''
pass
def handleNotification():
'''public void handleNotification(final Notification notf, final Object handback)
'''
pass
def removeListener():
'''public void removeListener()
'''
pass
def isSuccess():
'''public boolean isSuccess()
'''
pass
def isComplete():
'''public boolean isComplete()
'''
pass
