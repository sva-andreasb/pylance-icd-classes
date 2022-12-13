XML_NAMESPACE_URI = "String  \"http://www.w3.org/XML/1998/namespace\""
XMLNS_NAMESPACE_URI = "String  \"http://www.w3.org/2000/xmlns/\""
def JDOMNodePointer():
    '''    public JDOMNodePointer(final Object node, final Locale locale)
    public JDOMNodePointer(final Object node, final Locale locale, final String id)
    public JDOMNodePointer(final NodePointer parent, final Object node)
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
    '''    public NodePointer namespacePointer(final String prefix)
    '''
def getNamespaceURI():
    '''    public String getNamespaceURI()
    public String getNamespaceURI(final String prefix)
    '''
def compareChildNodePointers():
    '''    public int compareChildNodePointers(final NodePointer pointer1, final NodePointer pointer2)
    '''
def getBaseValue():
    '''    public Object getBaseValue()
    '''
def isCollection():
    '''    public boolean isCollection()
    '''
def getLength():
    '''    public int getLength()
    '''
def isLeaf():
    '''    public boolean isLeaf()
    '''
def getName():
    '''    public QName getName()
    '''
def getExpandedName():
    '''    public QName getExpandedName()
    '''
def getImmediateNode():
    '''    public Object getImmediateNode()
    '''
def getValue():
    '''    public Object getValue()
    '''
def setValue():
    '''    public void setValue(final Object value)
    '''
def testNode():
    '''    public boolean testNode(final NodeTest test)
    public static boolean testNode(final NodePointer pointer, final Object node, final NodeTest test)
    '''
def getPrefix():
    '''    public static String getPrefix(final Object node)
    '''
def getLocalName():
    '''    public static String getLocalName(final Object node)
    '''
def isLanguage():
    '''    public boolean isLanguage(final String lang)
    '''
def createChild():
    '''    public NodePointer createChild(final JXPathContext context, final QName name, int index)
    public NodePointer createChild(final JXPathContext context, final QName name, final int index, final Object value)
    '''
def createAttribute():
    '''    public NodePointer createAttribute(final JXPathContext context, final QName name)
    '''
def remove():
    '''    public void remove()
    '''
def asPath():
    '''    public String asPath()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object object)
    '''
