def ContainerPointer():
    '''public ContainerPointer(final Container container, final Locale locale)
    public ContainerPointer(final NodePointer parent, final Container container)
    '''
def isContainer():
    '''public boolean isContainer()
    '''
def getName():
    '''public QName getName()
    '''
def getBaseValue():
    '''public Object getBaseValue()
    '''
def isCollection():
    '''public boolean isCollection()
    '''
def getLength():
    '''public int getLength()
    '''
def isLeaf():
    '''public boolean isLeaf()
    '''
def getImmediateNode():
    '''public Object getImmediateNode()
    '''
def setValue():
    '''public void setValue(final Object value)
    '''
def getImmediateValuePointer():
    '''public NodePointer getImmediateValuePointer()
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object object)
    '''
def childIterator():
    '''public NodeIterator childIterator(final NodeTest test, final boolean reverse, final NodePointer startWith)
    '''
def attributeIterator():
    '''public NodeIterator attributeIterator(final QName name)
    '''
def namespaceIterator():
    '''public NodeIterator namespaceIterator()
    '''
def namespacePointer():
    '''public NodePointer namespacePointer(final String namespace)
    '''
def testNode():
    '''public boolean testNode(final NodeTest nodeTest)
    '''
def compareChildNodePointers():
    '''public int compareChildNodePointers(final NodePointer pointer1, final NodePointer pointer2)
    '''
def asPath():
    '''public String asPath()
    '''
