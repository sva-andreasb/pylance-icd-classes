def getProperty():
'''public static Object getProperty(final Project project, final String name)
public Object getProperty(final String ns, final String name)
public Object getProperty(final String name)
'''
pass
def setProperty():
'''public static void setProperty(final Project project, final String name, final Object value)
public boolean setProperty(final String ns, final String name, final Object value, final boolean verbose)
public boolean setProperty(final String name, final Object value, final boolean verbose)
'''
pass
def setNewProperty():
'''public static void setNewProperty(final Project project, final String name, final Object value)
public void setNewProperty(final String ns, final String name, final Object value)
public void setNewProperty(final String name, final Object value)
'''
pass
def setProject():
'''public void setProject(final Project p)
'''
pass
def getProject():
'''public Project getProject()
'''
pass
def setNext():
'''public void setNext(final PropertyHelper next)
'''
pass
def getNext():
'''public PropertyHelper getNext()
'''
pass
def getPropertyHelper():
'''public static synchronized PropertyHelper getPropertyHelper(final Project project)
'''
pass
def getExpanders():
'''public Collection getExpanders()
'''
pass
def setPropertyHook():
'''public boolean setPropertyHook(final String ns, final String name, final Object value, final boolean inherited, final boolean user, final boolean isNew)
'''
pass
def getPropertyHook():
'''public Object getPropertyHook(final String ns, String name, final boolean user)
'''
pass
def parsePropertyString():
'''public void parsePropertyString(final String value, final Vector fragments, final Vector propertyRefs)
'''
pass
def replaceProperties():
'''public String replaceProperties(final String ns, final String value, final Hashtable keys)
public String replaceProperties(final String value)
'''
pass
def parseProperties():
'''public Object parseProperties(final String value)
'''
pass
def containsProperties():
'''public boolean containsProperties(final String value)
'''
pass
def setUserProperty():
'''public void setUserProperty(final String ns, final String name, final Object value)
public void setUserProperty(final String name, final Object value)
'''
pass
def setInheritedProperty():
'''public void setInheritedProperty(final String ns, final String name, final Object value)
public void setInheritedProperty(final String name, final Object value)
'''
pass
def getUserProperty():
'''public Object getUserProperty(final String ns, final String name)
public Object getUserProperty(final String name)
'''
pass
def getProperties():
'''public Hashtable getProperties()
'''
pass
def getUserProperties():
'''public Hashtable getUserProperties()
'''
pass
def getInheritedProperties():
'''public Hashtable getInheritedProperties()
'''
pass
def copyInheritedProperties():
'''public void copyInheritedProperties(final Project other)
'''
pass
def copyUserProperties():
'''public void copyUserProperties(final Project other)
'''
pass
def add():
'''public void add(final Delegate delegate)
'''
pass
def toBoolean():
'''public static Boolean toBoolean(final Object value)
'''
pass
def testIfCondition():
'''public boolean testIfCondition(final Object value)
'''
pass
def testUnlessCondition():
'''public boolean testUnlessCondition(final Object value)
'''
pass
def evaluate():
'''public Object evaluate(final String property, final PropertyHelper propertyHelper)
public Object evaluate(final String prop, final PropertyHelper helper)
'''
pass
def parsePropertyName():
'''public String parsePropertyName(final String s, final ParsePosition pos, final ParseNextProperty notUsed)
public String parsePropertyName(final String s, final ParsePosition pos, final ParseNextProperty notUsed)
'''
pass