def setAttribute():
    '''returns None\n\n
    setAttribute(final Project p, final Object element, final String attributeName, final Object value)\n
    setAttribute(final Project p, final Object element, final String attributeName, final String value)\n
    '''
def addText():
    '''returns None\n\n
    addText(final Project project, final Object element, String text)\n
    '''
def throwNotSupported():
    '''returns None\n\n
    throwNotSupported(final Project project, final Object parent, final String elementName)\n
    '''
def createElement():
    '''returns Object\n\n
    createElement(final Project project, final Object parent, final String elementName)\n
    '''
def getElementCreator():
    '''returns Creator\n\n
    getElementCreator(final Project project, final String parentUri, final Object parent, final String elementName, final UnknownElement ue)\n
    '''
def isDynamic():
    '''returns boolean\n\n
    isDynamic()\n
    '''
def isContainer():
    '''returns boolean\n\n
    isContainer()\n
    '''
def supportsNestedElement():
    '''returns boolean\n\n
    supportsNestedElement(final String elementName)\n
    supportsNestedElement(final String parentUri, final String elementName)\n
    supportsNestedElement(final String parentUri, final String elementName, final Project project, final Object parent)\n
    '''
def supportsReflectElement():
    '''returns boolean\n\n
    supportsReflectElement(String parentUri, final String elementName)\n
    '''
def storeElement():
    '''returns None\n\n
    storeElement(final Project project, final Object parent, final Object child, final String elementName)\n
    '''
def getElementType():
    '''returns Class\n\n
    getElementType(final String elementName)\n
    '''
def getAttributeType():
    '''returns Class\n\n
    getAttributeType(final String attributeName)\n
    '''
def getAddTextMethod():
    '''returns Method\n\n
    getAddTextMethod()\n
    '''
def getElementMethod():
    '''returns Method\n\n
    getElementMethod(final String elementName)\n
    '''
def getAttributeMethod():
    '''returns Method\n\n
    getAttributeMethod(final String attributeName)\n
    '''
def supportsCharacters():
    '''returns boolean\n\n
    supportsCharacters()\n
    '''
def getAttributes():
    '''returns Enumeration\n\n
    getAttributes()\n
    '''
def getAttributeMap():
    '''returns Map\n\n
    getAttributeMap()\n
    '''
def getNestedElements():
    '''returns Enumeration\n\n
    getNestedElements()\n
    '''
def getNestedElementMap():
    '''returns Map\n\n
    getNestedElementMap()\n
    '''
def getExtensionPoints():
    '''returns List\n\n
    getExtensionPoints()\n
    '''
def set():
    '''returns None\n\n
    set(final Project p, final Object parent, final String value)\n
    set(final Project p, final Object parent, final String value)\n
    set(final Project p, final Object parent, final String value)\n
    set(final Project p, final Object parent, final String value)\n
    set(final Project p, final Object parent, final String value)\n
    set(final Project p, final Object parent, final String value)\n
    set(final Project p, final Object parent, final String value)\n
    set(final Project p, final Object parent, final String value)\n
    set(final Project p, final Object parent, final String value)\n
    set(final Project p, final Object parent, final String value)\n
    '''
def setPolyType():
    '''returns None\n\n
    setPolyType(final String polyType)\n
    '''
def create():
    '''returns Object\n\n
    create()\n
    '''
def getRealObject():
    '''returns Object\n\n
    getRealObject()\n
    '''
def store():
    '''returns None\n\n
    store()\n
    '''
def ():
    '''returns MethodAndObject\n\n
    (final Method method, final Object object)\n
    '''
