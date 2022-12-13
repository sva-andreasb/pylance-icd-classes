COMPONENT_HELPER_REFERENCE = "String  \"ant.ComponentHelper\""
def getProject():
    '''public Project getProject()
    '''
def getComponentHelper():
    '''public static ComponentHelper getComponentHelper(final Project project)
    '''
def setNext():
    '''public void setNext(final ComponentHelper next)
    '''
def getNext():
    '''public ComponentHelper getNext()
    '''
def setProject():
    '''public void setProject(final Project project)
    '''
def initSubProject():
    '''public void initSubProject(final ComponentHelper helper)
    '''
def createComponent():
    '''public Object createComponent(final UnknownElement ue, final String ns, final String componentType)
    public Object createComponent(final String componentName)
    '''
def getComponentClass():
    '''public Class getComponentClass(final String componentName)
    '''
def getDefinition():
    '''public AntTypeDefinition getDefinition(final String componentName)
    '''
def initDefaultDefinitions():
    '''public void initDefaultDefinitions()
    '''
def addTaskDefinition():
    '''public void addTaskDefinition(final String taskName, final Class taskClass)
    '''
def checkTaskClass():
    '''public void checkTaskClass(final Class taskClass)
    '''
def getTaskDefinitions():
    '''public Hashtable getTaskDefinitions()
    '''
def getDataTypeDefinitions():
    '''public Hashtable getDataTypeDefinitions()
    '''
def getRestrictedDefinitions():
    '''public List getRestrictedDefinitions(final String componentName)
    '''
def addDataTypeDefinition():
    '''public void addDataTypeDefinition(final String typeName, final Class typeClass)
    public void addDataTypeDefinition(final AntTypeDefinition def)
    '''
def getAntTypeTable():
    '''public Hashtable getAntTypeTable()
    '''
def createTask():
    '''public Task createTask(final String taskType)
    '''
def createDataType():
    '''public Object createDataType(final String typeName)
    '''
def getElementName():
    '''public String getElementName(final Object element)
    public String getElementName(final Object o, final boolean brief)
    public static String getElementName(Project p, final Object o, final boolean brief)
    '''
def enterAntLib():
    '''public void enterAntLib(final String uri)
    '''
def getCurrentAntlibUri():
    '''public String getCurrentAntlibUri()
    '''
def exitAntLib():
    '''public void exitAntLib()
    '''
def diagnoseCreationFailure():
    '''public String diagnoseCreationFailure(final String componentName, final String type)
    '''
def get():
    '''public Object get(final Object key)
    '''
def contains():
    '''public synchronized boolean contains(final Object clazz)
    '''
def containsValue():
    '''public boolean containsValue(final Object value)
    '''
def findMatches():
    '''public synchronized List findMatches(final String prefix)
    '''
