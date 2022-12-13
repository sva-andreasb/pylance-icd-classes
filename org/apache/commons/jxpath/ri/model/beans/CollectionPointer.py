def CollectionPointer():
    '''public CollectionPointer(final Object collection, final Locale locale)
    public CollectionPointer(final NodePointer parent, final Object collection)
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
def isContainer():
    '''public boolean isContainer()
    '''
def getImmediateNode():
    '''public Object getImmediateNode()
    '''
def setValue():
    '''public void setValue(final Object value)
    '''
def setIndex():
    '''public void setIndex(final int index)
    '''
def getValuePointer():
    '''public NodePointer getValuePointer()
    '''
def createPath():
    '''public NodePointer createPath(final JXPathContext context)
    public NodePointer createPath(final JXPathContext context, final Object value)
    '''
def createChild():
    '''public NodePointer createChild(final JXPathContext context, final QName name, final int index, final Object value)
    public NodePointer createChild(final JXPathContext context, final QName name, final int index)
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
