def VariablePointer():
    '''    public VariablePointer(final Variables variables, final QName name)
    public VariablePointer(final QName name)
    '''
def isContainer():
    '''    public boolean isContainer()
    '''
def getName():
    '''    public QName getName()
    '''
def getBaseValue():
    '''    public Object getBaseValue()
    '''
def isLeaf():
    '''    public boolean isLeaf()
    '''
def isCollection():
    '''    public boolean isCollection()
    '''
def getImmediateNode():
    '''    public Object getImmediateNode()
    public Object getImmediateNode()
    '''
def setValue():
    '''    public void setValue(final Object value)
    '''
def isActual():
    '''    public boolean isActual()
    '''
def setIndex():
    '''    public void setIndex(final int index)
    '''
def getImmediateValuePointer():
    '''    public NodePointer getImmediateValuePointer()
    '''
def getLength():
    '''    public int getLength()
    '''
def createPath():
    '''    public NodePointer createPath(final JXPathContext context, final Object value)
    public NodePointer createPath(final JXPathContext context)
    '''
def createChild():
    '''    public NodePointer createChild(final JXPathContext context, final QName name, final int index)
    public NodePointer createChild(final JXPathContext context, final QName name, final int index, final Object value)
    '''
def remove():
    '''    public void remove()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object object)
    '''
def asPath():
    '''    public String asPath()
    '''
def childIterator():
    '''    public NodeIterator childIterator(final NodeTest test, final boolean reverse, final NodePointer startWith)
    '''
def attributeIterator():
    '''    public NodeIterator attributeIterator(final QName name)
    '''
def namespaceIterator():
    '''    public NodeIterator namespaceIterator()
    '''
def namespacePointer():
    '''    public NodePointer namespacePointer(final String name)
    '''
def testNode():
    '''    public boolean testNode(final NodeTest nodeTest)
    '''
def compareChildNodePointers():
    '''    public int compareChildNodePointers(final NodePointer pointer1, final NodePointer pointer2)
    '''
