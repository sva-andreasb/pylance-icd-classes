def ():
    '''returns AbstractCommandStep\n\n
    (final AbstractTaskCommand parent, final CommandMetadata metadata)\n
    (final AbstractTaskCommand parent, final CommandData commandData)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled()\n
    '''
def listSetParams():
    '''returns Collection\n\n
    listSetParams(final int rowIndex)\n
    '''
def getParameter():
    '''returns Object\n\n
    getParameter(final String parameterName, final int rowIndex)\n
    '''
def setParameter():
    '''returns None\n\n
    setParameter(final String paramName, final Object value, final int rowIndex)\n
    '''
def getNumberOfRows():
    '''returns int\n\n
    getNumberOfRows()\n
    '''
def addRow():
    '''returns None\n\n
    addRow(final AttributeList rowData, final int rowIndex)\n
    '''
def deleteRow():
    '''returns None\n\n
    deleteRow(final int rowIndex)\n
    '''
def stepModified():
    '''returns None\n\n
    stepModified(final String stepName)\n
    '''
def commandParamModified():
    '''returns None\n\n
    commandParamModified()\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def isRequired():
    '''returns boolean\n\n
    isRequired()\n
    isRequired(final int rowIndex)\n
    '''
def getConfigSession():
    '''returns Session\n\n
    getConfigSession()\n
    '''
def getChoices():
    '''returns Object[]\n\n
    getChoices(final String paramName, final int rowIndex)\n
    '''
