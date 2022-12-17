XML_NAMESPACE_URI = "String  \"http://www.w3.org/XML/1998/namespace\""
XMLNS_NAMESPACE_URI = "String  \"http://www.w3.org/2000/xmlns/\""
def ():
    '''returns JDOMNodePointer\n\n
    (final Object node, final Locale locale)\n
    (final Object node, final Locale locale, final String id)\n
    (final NodePointer parent, final Object node)\n
    '''
def childIterator():
    '''returns NodeIterator\n\n
    childIterator(final NodeTest test, final boolean reverse, final NodePointer startWith)\n
    '''
def attributeIterator():
    '''returns NodeIterator\n\n
    attributeIterator(final QName name)\n
    '''
def namespaceIterator():
    '''returns NodeIterator\n\n
    namespaceIterator()\n
    '''
def namespacePointer():
    '''returns NodePointer\n\n
    namespacePointer(final String prefix)\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI()\n
    getNamespaceURI(final String prefix)\n
    '''
def compareChildNodePointers():
    '''returns int\n\n
    compareChildNodePointers(final NodePointer pointer1, final NodePointer pointer2)\n
    '''
def getBaseValue():
    '''returns Object\n\n
    getBaseValue()\n
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
def getName():
    '''returns QName\n\n
    getName()\n
    '''
def getExpandedName():
    '''returns QName\n\n
    getExpandedName()\n
    '''
def getImmediateNode():
    '''returns Object\n\n
    getImmediateNode()\n
    '''
def getValue():
    '''returns Object\n\n
    getValue()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final Object value)\n
    '''
def testNode():
    '''returns boolean\n\n
    testNode(final NodeTest test)\n
    '''
def isLanguage():
    '''returns boolean\n\n
    isLanguage(final String lang)\n
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
