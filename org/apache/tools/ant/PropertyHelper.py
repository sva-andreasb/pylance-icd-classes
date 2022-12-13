def getProperty():
    '''    public static Object getProperty(final Project project, final String name)
    public Object getProperty(final String ns, final String name)
    public Object getProperty(final String name)
    '''
def setProperty():
    '''    public static void setProperty(final Project project, final String name, final Object value)
    public boolean setProperty(final String ns, final String name, final Object value, final boolean verbose)
    public boolean setProperty(final String name, final Object value, final boolean verbose)
    '''
def setNewProperty():
    '''    public static void setNewProperty(final Project project, final String name, final Object value)
    public void setNewProperty(final String ns, final String name, final Object value)
    public void setNewProperty(final String name, final Object value)
    '''
def setProject():
    '''    public void setProject(final Project p)
    '''
def getProject():
    '''    public Project getProject()
    '''
def setNext():
    '''    public void setNext(final PropertyHelper next)
    '''
def getNext():
    '''    public PropertyHelper getNext()
    '''
def getPropertyHelper():
    '''    public static synchronized PropertyHelper getPropertyHelper(final Project project)
    '''
def getExpanders():
    '''    public Collection getExpanders()
    '''
def setPropertyHook():
    '''    public boolean setPropertyHook(final String ns, final String name, final Object value, final boolean inherited, final boolean user, final boolean isNew)
    '''
def getPropertyHook():
    '''    public Object getPropertyHook(final String ns, String name, final boolean user)
    '''
def parsePropertyString():
    '''    public void parsePropertyString(final String value, final Vector fragments, final Vector propertyRefs)
    '''
def replaceProperties():
    '''    public String replaceProperties(final String ns, final String value, final Hashtable keys)
    public String replaceProperties(final String value)
    '''
def parseProperties():
    '''    public Object parseProperties(final String value)
    '''
def containsProperties():
    '''    public boolean containsProperties(final String value)
    '''
def setUserProperty():
    '''    public void setUserProperty(final String ns, final String name, final Object value)
    public void setUserProperty(final String name, final Object value)
    '''
def setInheritedProperty():
    '''    public void setInheritedProperty(final String ns, final String name, final Object value)
    public void setInheritedProperty(final String name, final Object value)
    '''
def getUserProperty():
    '''    public Object getUserProperty(final String ns, final String name)
    public Object getUserProperty(final String name)
    '''
def getProperties():
    '''    public Hashtable getProperties()
    '''
def getUserProperties():
    '''    public Hashtable getUserProperties()
    '''
def getInheritedProperties():
    '''    public Hashtable getInheritedProperties()
    '''
def copyInheritedProperties():
    '''    public void copyInheritedProperties(final Project other)
    '''
def copyUserProperties():
    '''    public void copyUserProperties(final Project other)
    '''
def add():
    '''    public void add(final Delegate delegate)
    '''
def toBoolean():
    '''    public static Boolean toBoolean(final Object value)
    '''
def testIfCondition():
    '''    public boolean testIfCondition(final Object value)
    '''
def testUnlessCondition():
    '''    public boolean testUnlessCondition(final Object value)
    '''
def evaluate():
    '''    public Object evaluate(final String property, final PropertyHelper propertyHelper)
    public Object evaluate(final String prop, final PropertyHelper helper)
    '''
def parsePropertyName():
    '''    public String parsePropertyName(final String s, final ParsePosition pos, final ParseNextProperty notUsed)
    public String parsePropertyName(final String s, final ParsePosition pos, final ParseNextProperty notUsed)
    '''
