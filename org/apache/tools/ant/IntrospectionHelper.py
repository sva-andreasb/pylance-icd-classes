def getHelper():
'''public static synchronized IntrospectionHelper getHelper(final Class c)
public static IntrospectionHelper getHelper(final Project p, final Class c)
'''
pass
def setAttribute():
'''public void setAttribute(final Project p, final Object element, final String attributeName, final Object value)
public void setAttribute(final Project p, final Object element, final String attributeName, final String value)
'''
pass
def addText():
'''public void addText(final Project project, final Object element, String text)
'''
pass
def throwNotSupported():
'''public void throwNotSupported(final Project project, final Object parent, final String elementName)
'''
pass
def createElement():
'''public Object createElement(final Project project, final Object parent, final String elementName)
'''
pass
def getElementCreator():
'''public Creator getElementCreator(final Project project, final String parentUri, final Object parent, final String elementName, final UnknownElement ue)
'''
pass
def isDynamic():
'''public boolean isDynamic()
'''
pass
def isContainer():
'''public boolean isContainer()
'''
pass
def supportsNestedElement():
'''public boolean supportsNestedElement(final String elementName)
public boolean supportsNestedElement(final String parentUri, final String elementName)
public boolean supportsNestedElement(final String parentUri, final String elementName, final Project project, final Object parent)
'''
pass
def supportsReflectElement():
'''public boolean supportsReflectElement(String parentUri, final String elementName)
'''
pass
def storeElement():
'''public void storeElement(final Project project, final Object parent, final Object child, final String elementName)
'''
pass
def getElementType():
'''public Class getElementType(final String elementName)
'''
pass
def getAttributeType():
'''public Class getAttributeType(final String attributeName)
'''
pass
def getAddTextMethod():
'''public Method getAddTextMethod()
'''
pass
def getElementMethod():
'''public Method getElementMethod(final String elementName)
'''
pass
def getAttributeMethod():
'''public Method getAttributeMethod(final String attributeName)
'''
pass
def supportsCharacters():
'''public boolean supportsCharacters()
'''
pass
def getAttributes():
'''public Enumeration getAttributes()
'''
pass
def getAttributeMap():
'''public Map getAttributeMap()
'''
pass
def getNestedElements():
'''public Enumeration getNestedElements()
'''
pass
def getNestedElementMap():
'''public Map getNestedElementMap()
'''
pass
def getExtensionPoints():
'''public List getExtensionPoints()
'''
pass
def set():
'''public void set(final Project p, final Object parent, final String value)
public void set(final Project p, final Object parent, final String value)
public void set(final Project p, final Object parent, final String value)
public void set(final Project p, final Object parent, final String value)
public void set(final Project p, final Object parent, final String value)
public void set(final Project p, final Object parent, final String value)
public void set(final Project p, final Object parent, final String value)
public void set(final Project p, final Object parent, final String value)
public void set(final Project p, final Object parent, final String value)
public void set(final Project p, final Object parent, final String value)
'''
pass
def clearCache():
'''public static void clearCache()
'''
pass
def setPolyType():
'''public void setPolyType(final String polyType)
'''
pass
def create():
'''public Object create()
'''
pass
def getRealObject():
'''public Object getRealObject()
'''
pass
def store():
'''public void store()
'''
pass
def MethodAndObject():
'''public MethodAndObject(final Method method, final Object object)
'''
pass
