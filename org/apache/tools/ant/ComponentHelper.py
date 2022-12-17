COMPONENT_HELPER_REFERENCE = "String  \"ant.ComponentHelper\""
def getProject():
    '''returns Project\n\n
    getProject()\n
    '''
def setNext():
    '''returns None\n\n
    setNext(final ComponentHelper next)\n
    '''
def getNext():
    '''returns ComponentHelper\n\n
    getNext()\n
    '''
def setProject():
    '''returns None\n\n
    setProject(final Project project)\n
    '''
def initSubProject():
    '''returns None\n\n
    initSubProject(final ComponentHelper helper)\n
    '''
def createComponent():
    '''returns Object\n\n
    createComponent(final UnknownElement ue, final String ns, final String componentType)\n
    createComponent(final String componentName)\n
    '''
def getComponentClass():
    '''returns Class\n\n
    getComponentClass(final String componentName)\n
    '''
def getDefinition():
    '''returns AntTypeDefinition\n\n
    getDefinition(final String componentName)\n
    '''
def initDefaultDefinitions():
    '''returns None\n\n
    initDefaultDefinitions()\n
    '''
def addTaskDefinition():
    '''returns None\n\n
    addTaskDefinition(final String taskName, final Class taskClass)\n
    '''
def checkTaskClass():
    '''returns None\n\n
    checkTaskClass(final Class taskClass)\n
    '''
def getTaskDefinitions():
    '''returns Hashtable\n\n
    getTaskDefinitions()\n
    '''
def getDataTypeDefinitions():
    '''returns Hashtable\n\n
    getDataTypeDefinitions()\n
    '''
def getRestrictedDefinitions():
    '''returns List\n\n
    getRestrictedDefinitions(final String componentName)\n
    '''
def addDataTypeDefinition():
    '''returns None\n\n
    addDataTypeDefinition(final String typeName, final Class typeClass)\n
    addDataTypeDefinition(final AntTypeDefinition def)\n
    '''
def getAntTypeTable():
    '''returns Hashtable\n\n
    getAntTypeTable()\n
    '''
def createTask():
    '''returns Task\n\n
    createTask(final String taskType)\n
    '''
def createDataType():
    '''returns Object\n\n
    createDataType(final String typeName)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName(final Object element)\n
    getElementName(final Object o, final boolean brief)\n
    '''
def enterAntLib():
    '''returns None\n\n
    enterAntLib(final String uri)\n
    '''
def getCurrentAntlibUri():
    '''returns String\n\n
    getCurrentAntlibUri()\n
    '''
def exitAntLib():
    '''returns None\n\n
    exitAntLib()\n
    '''
def diagnoseCreationFailure():
    '''returns String\n\n
    diagnoseCreationFailure(final String componentName, final String type)\n
    '''
def get():
    '''returns Object\n\n
    get(final Object key)\n
    '''
def containsValue():
    '''returns boolean\n\n
    containsValue(final Object value)\n
    '''
