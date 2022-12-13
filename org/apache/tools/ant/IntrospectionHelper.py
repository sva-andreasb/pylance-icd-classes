def getHelper():
    '''    public static synchronized IntrospectionHelper getHelper(final Class c)
    public static IntrospectionHelper getHelper(final Project p, final Class c)
    '''
def setAttribute():
    '''    public void setAttribute(final Project p, final Object element, final String attributeName, final Object value)
    public void setAttribute(final Project p, final Object element, final String attributeName, final String value)
    '''
def addText():
    '''    public void addText(final Project project, final Object element, String text)
    '''
def throwNotSupported():
    '''    public void throwNotSupported(final Project project, final Object parent, final String elementName)
    '''
def createElement():
    '''    public Object createElement(final Project project, final Object parent, final String elementName)
    '''
def getElementCreator():
    '''    public Creator getElementCreator(final Project project, final String parentUri, final Object parent, final String elementName, final UnknownElement ue)
    '''
def isDynamic():
    '''    public boolean isDynamic()
    '''
def isContainer():
    '''    public boolean isContainer()
    '''
def supportsNestedElement():
    '''    public boolean supportsNestedElement(final String elementName)
    public boolean supportsNestedElement(final String parentUri, final String elementName)
    public boolean supportsNestedElement(final String parentUri, final String elementName, final Project project, final Object parent)
    '''
def supportsReflectElement():
    '''    public boolean supportsReflectElement(String parentUri, final String elementName)
    '''
def storeElement():
    '''    public void storeElement(final Project project, final Object parent, final Object child, final String elementName)
    '''
def getElementType():
    '''    public Class getElementType(final String elementName)
    '''
def getAttributeType():
    '''    public Class getAttributeType(final String attributeName)
    '''
def getAddTextMethod():
    '''    public Method getAddTextMethod()
    '''
def getElementMethod():
    '''    public Method getElementMethod(final String elementName)
    '''
def getAttributeMethod():
    '''    public Method getAttributeMethod(final String attributeName)
    '''
def supportsCharacters():
    '''    public boolean supportsCharacters()
    '''
def getAttributes():
    '''    public Enumeration getAttributes()
    '''
def getAttributeMap():
    '''    public Map getAttributeMap()
    '''
def getNestedElements():
    '''    public Enumeration getNestedElements()
    '''
def getNestedElementMap():
    '''    public Map getNestedElementMap()
    '''
def getExtensionPoints():
    '''    public List getExtensionPoints()
    '''
def set():
    '''    public void set(final Project p, final Object parent, final String value)
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
def clearCache():
    '''    public static void clearCache()
    '''
def setPolyType():
    '''    public void setPolyType(final String polyType)
    '''
def create():
    '''    public Object create()
    '''
def getRealObject():
    '''    public Object getRealObject()
    '''
def store():
    '''    public void store()
    '''
def MethodAndObject():
    '''    public MethodAndObject(final Method method, final Object object)
    '''
