XML_NAMESPACE_URI = "String  \"http://www.w3.org/XML/1998/namespace\""
XMLNS_NAMESPACE_URI = "String  \"http://www.w3.org/2000/xmlns/\""
def ():
    '''returns DOMNodePointer\n\n
    (final Node node, final Locale locale)\n
    (final Node node, final Locale locale, final String id)\n
    (final NodePointer parent, final Node node)\n
    '''
def testNode():
    '''returns boolean\n\n
    testNode(final NodeTest test)\n
    '''
def getName():
    '''returns QName\n\n
    getName()\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI()\n
    getNamespaceURI(final String prefix)\n
    '''
def getExpandedName():
    '''returns QName\n\n
    getExpandedName()\n
    '''
def childIterator():
    '''returns NodeIterator\n\n
    childIterator(final NodeTest test, final boolean reverse, final NodePointer startWith)\n
    '''
def attributeIterator():
    '''returns NodeIterator\n\n
    attributeIterator(final QName name)\n
    '''
def namespacePointer():
    '''returns NodePointer\n\n
    namespacePointer(final String prefix)\n
    '''
def namespaceIterator():
    '''returns NodeIterator\n\n
    namespaceIterator()\n
    '''
def getDefaultNamespaceURI():
    '''returns String\n\n
    getDefaultNamespaceURI()\n
    '''
def getBaseValue():
    '''returns Object\n\n
    getBaseValue()\n
    '''
def getImmediateNode():
    '''returns Object\n\n
    getImmediateNode()\n
    '''
def isActual():
    '''returns boolean\n\n
    isActual()\n
    '''
def isCollection():
    '''returns boolean\n\n
    isCollection()\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def isLeaf():
    '''returns boolean\n\n
    isLeaf()\n
    '''
def isLanguage():
    '''returns boolean\n\n
    isLanguage(final String lang)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final Object value)\n
    '''
def createChild():
    '''returns NodePointer\n\n
    createChild(final JXPathContext context, final QName name, int index)\n
    createChild(final JXPathContext context, final QName name, final int index, final Object value)\n
    '''
def createAttribute():
    '''returns NodePointer\n\n
    createAttribute(final JXPathContext context, final QName name)\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def asPath():
    '''returns String\n\n
    asPath()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object object)\n
    '''
def getValue():
    '''returns Object\n\n
    getValue()\n
    '''
def getPointerByID():
    '''returns Pointer\n\n
    getPointerByID(final JXPathContext context, final String id)\n
    '''
def compareChildNodePointers():
    '''returns int\n\n
    compareChildNodePointers(final NodePointer pointer1, final NodePointer pointer2)\n
    '''
