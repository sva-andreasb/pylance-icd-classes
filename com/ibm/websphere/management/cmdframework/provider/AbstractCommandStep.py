def AbstractCommandStep():
'''public AbstractCommandStep(final AbstractTaskCommand parent, final CommandMetadata metadata)
public AbstractCommandStep(final AbstractTaskCommand parent, final CommandData commandData)
'''
pass
def getCommandMetadata():
'''public static CommandMetadata getCommandMetadata(final String cmdName)
'''
pass
def isEnabled():
'''public boolean isEnabled()
'''
pass
def hashcode():
'''public final int hashcode()
'''
pass
def equals():
'''public final boolean equals(final Object obj)
'''
pass
def getCommandStepData():
'''public final CommandStepData getCommandStepData()
'''
pass
def resetCommandData():
'''public final void resetCommandData(final CommandData stepData)
'''
pass
def execute():
'''public final void execute(final CommandHistory cmdHistory)
public final void execute()
'''
pass
def listSetParams():
'''public Collection listSetParams(final int rowIndex)
'''
pass
def getParameter():
'''public Object getParameter(final String parameterName, final int rowIndex)
'''
pass
def setParameter():
'''public void setParameter(final String paramName, final Object value, final int rowIndex)
'''
pass
def getNumberOfRows():
'''public int getNumberOfRows()
'''
pass
def addRow():
'''public void addRow(final AttributeList rowData, final int rowIndex)
'''
pass
def deleteRow():
'''public void deleteRow(final int rowIndex)
'''
pass
def stepModified():
'''public void stepModified(final String stepName)
'''
pass
def commandParamModified():
'''public void commandParamModified()
'''
pass
def validate():
'''public void validate()
'''
pass
def isRequired():
'''public boolean isRequired()
public boolean isRequired(final int rowIndex)
'''
pass
def getConfigSession():
'''public Session getConfigSession()
'''
pass
def getChoices():
'''public Object[] getChoices(final String paramName, final int rowIndex)
'''
pass
