def AbstractCommandStep():
    '''public AbstractCommandStep(final AbstractTaskCommand parent, final CommandMetadata metadata)
    public AbstractCommandStep(final AbstractTaskCommand parent, final CommandData commandData)
    '''
def getCommandMetadata():
    '''public static CommandMetadata getCommandMetadata(final String cmdName)
    '''
def isEnabled():
    '''public boolean isEnabled()
    '''
def hashcode():
    '''public final int hashcode()
    '''
def equals():
    '''public final boolean equals(final Object obj)
    '''
def getCommandStepData():
    '''public final CommandStepData getCommandStepData()
    '''
def resetCommandData():
    '''public final void resetCommandData(final CommandData stepData)
    '''
def execute():
    '''public final void execute(final CommandHistory cmdHistory)
    public final void execute()
    '''
def listSetParams():
    '''public Collection listSetParams(final int rowIndex)
    '''
def getParameter():
    '''public Object getParameter(final String parameterName, final int rowIndex)
    '''
def setParameter():
    '''public void setParameter(final String paramName, final Object value, final int rowIndex)
    '''
def getNumberOfRows():
    '''public int getNumberOfRows()
    '''
def addRow():
    '''public void addRow(final AttributeList rowData, final int rowIndex)
    '''
def deleteRow():
    '''public void deleteRow(final int rowIndex)
    '''
def stepModified():
    '''public void stepModified(final String stepName)
    '''
def commandParamModified():
    '''public void commandParamModified()
    '''
def validate():
    '''public void validate()
    '''
def isRequired():
    '''public boolean isRequired()
    public boolean isRequired(final int rowIndex)
    '''
def getConfigSession():
    '''public Session getConfigSession()
    '''
def getChoices():
    '''public Object[] getChoices(final String paramName, final int rowIndex)
    '''
