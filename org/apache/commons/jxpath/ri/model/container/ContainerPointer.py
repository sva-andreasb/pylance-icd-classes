def ():
    '''returns ContainerPointer\n\n
    (final Container container, final Locale locale)\n
    (final NodePointer parent, final Container container)\n
    '''
def isContainer():
    '''returns boolean\n\n
    isContainer()\n
    '''
def getName():
    '''returns QName\n\n
    getName()\n
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
def getImmediateNode():
    '''returns Object\n\n
    getImmediateNode()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final Object value)\n
    '''
def getImmediateValuePointer():
    '''returns NodePointer\n\n
    getImmediateValuePointer()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object object)\n
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
    namespacePointer(final String namespace)\n
    '''
def testNode():
    '''returns boolean\n\n
    testNode(final NodeTest nodeTest)\n
    '''
def compareChildNodePointers():
    '''returns int\n\n
    compareChildNodePointers(final NodePointer pointer1, final NodePointer pointer2)\n
    '''
def asPath():
    '''returns String\n\n
    asPath()\n
    '''
