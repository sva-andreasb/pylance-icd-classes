WHOLE_COLLECTION = "int  Integer.MIN_VALUE"
UNKNOWN_NAMESPACE = "String  \"<<unknown namespace>>\""
def getParent():
    '''returns NodePointer\n\n
    getParent()\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final boolean attribute)\n
    '''
def isAttribute():
    '''returns boolean\n\n
    isAttribute()\n
    '''
def isRoot():
    '''returns boolean\n\n
    isRoot()\n
    '''
def isNode():
    '''returns boolean\n\n
    isNode()\n
    '''
def isContainer():
    '''returns boolean\n\n
    isContainer()\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex()\n
    '''
def setIndex():
    '''returns None\n\n
    setIndex(final int index)\n
    '''
def getValue():
    '''returns Object\n\n
    getValue()\n
    '''
def getValuePointer():
    '''returns NodePointer\n\n
    getValuePointer()\n
    '''
def getImmediateValuePointer():
    '''returns NodePointer\n\n
    getImmediateValuePointer()\n
    '''
def isActual():
    '''returns boolean\n\n
    isActual()\n
    '''
def getNodeValue():
    '''returns Object\n\n
    getNodeValue()\n
    '''
def getNode():
    '''returns Object\n\n
    getNode()\n
    '''
def getRootNode():
    '''returns Object\n\n
    getRootNode()\n
    '''
def testNode():
    '''returns boolean\n\n
    testNode(final NodeTest test)\n
    '''
def createPath():
    '''returns NodePointer\n\n
    createPath(final JXPathContext context, final Object value)\n
    createPath(final JXPathContext context)\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def createChild():
    '''returns NodePointer\n\n
    createChild(final JXPathContext context, final QName name, final int index, final Object value)\n
    createChild(final JXPathContext context, final QName name, final int index)\n
    '''
def createAttribute():
    '''returns NodePointer\n\n
    createAttribute(final JXPathContext context, final QName name)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def isLanguage():
    '''returns boolean\n\n
    isLanguage(final String lang)\n
    '''
def childIterator():
    '''returns NodeIterator\n\n
    childIterator(final NodeTest test, final boolean reverse, final NodePointer startWith)\n
    '''
def attributeIterator():
    '''returns NodeIterator\n\n
    attributeIterator(final QName qname)\n
    '''
def namespaceIterator():
    '''returns NodeIterator\n\n
    namespaceIterator()\n
    '''
def namespacePointer():
    '''returns NodePointer\n\n
    namespacePointer(final String namespace)\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI(final String prefix)\n
    getNamespaceURI()\n
    '''
def getExpandedName():
    '''returns QName\n\n
    getExpandedName()\n
    '''
def getPointerByID():
    '''returns Pointer\n\n
    getPointerByID(final JXPathContext context, final String id)\n
    '''
def getPointerByKey():
    '''returns Pointer\n\n
    getPointerByKey(final JXPathContext context, final String key, final String value)\n
    '''
def asPath():
    '''returns String\n\n
    asPath()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object object)\n
    '''
def printPointerChain():
    '''returns None\n\n
    printPointerChain()\n
    '''
