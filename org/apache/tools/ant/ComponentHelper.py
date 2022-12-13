COMPONENT_HELPER_REFERENCE = "String  ant.ComponentHelper""
def getProject():
'''public Project getProject()
'''
pass
def getComponentHelper():
'''public static ComponentHelper getComponentHelper(final Project project)
'''
pass
def setNext():
'''public void setNext(final ComponentHelper next)
'''
pass
def getNext():
'''public ComponentHelper getNext()
'''
pass
def setProject():
'''public void setProject(final Project project)
'''
pass
def initSubProject():
'''public void initSubProject(final ComponentHelper helper)
'''
pass
def createComponent():
'''public Object createComponent(final UnknownElement ue, final String ns, final String componentType)
public Object createComponent(final String componentName)
'''
pass
def getComponentClass():
'''public Class getComponentClass(final String componentName)
'''
pass
def getDefinition():
'''public AntTypeDefinition getDefinition(final String componentName)
'''
pass
def initDefaultDefinitions():
'''public void initDefaultDefinitions()
'''
pass
def addTaskDefinition():
'''public void addTaskDefinition(final String taskName, final Class taskClass)
'''
pass
def checkTaskClass():
'''public void checkTaskClass(final Class taskClass)
'''
pass
def getTaskDefinitions():
'''public Hashtable getTaskDefinitions()
'''
pass
def getDataTypeDefinitions():
'''public Hashtable getDataTypeDefinitions()
'''
pass
def getRestrictedDefinitions():
'''public List getRestrictedDefinitions(final String componentName)
'''
pass
def addDataTypeDefinition():
'''public void addDataTypeDefinition(final String typeName, final Class typeClass)
public void addDataTypeDefinition(final AntTypeDefinition def)
'''
pass
def getAntTypeTable():
'''public Hashtable getAntTypeTable()
'''
pass
def createTask():
'''public Task createTask(final String taskType)
'''
pass
def createDataType():
'''public Object createDataType(final String typeName)
'''
pass
def getElementName():
'''public String getElementName(final Object element)
public String getElementName(final Object o, final boolean brief)
public static String getElementName(Project p, final Object o, final boolean brief)
'''
pass
def enterAntLib():
'''public void enterAntLib(final String uri)
'''
pass
def getCurrentAntlibUri():
'''public String getCurrentAntlibUri()
'''
pass
def exitAntLib():
'''public void exitAntLib()
'''
pass
def diagnoseCreationFailure():
'''public String diagnoseCreationFailure(final String componentName, final String type)
'''
pass
def get():
'''public Object get(final Object key)
'''
pass
def contains():
'''public synchronized boolean contains(final Object clazz)
'''
pass
def containsValue():
'''public boolean containsValue(final Object value)
'''
pass
def findMatches():
'''public synchronized List findMatches(final String prefix)
'''
pass
