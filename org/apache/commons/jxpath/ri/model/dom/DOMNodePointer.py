XML_NAMESPACE_URI = "String  \"http://www.w3.org/XML/1998/namespace\""
XMLNS_NAMESPACE_URI = "String  \"http://www.w3.org/2000/xmlns/\""
def DOMNodePointer():
    '''public DOMNodePointer(final Node node, final Locale locale)
    public DOMNodePointer(final Node node, final Locale locale, final String id)
    public DOMNodePointer(final NodePointer parent, final Node node)
    '''
def testNode():
    '''public boolean testNode(final NodeTest test)
    public static boolean testNode(final NodePointer pointer, final Node node, final NodeTest test)
    '''
def getName():
    '''public QName getName()
    '''
def getNamespaceURI():
    '''public String getNamespaceURI()
    public String getNamespaceURI(final String prefix)
    '''
def getExpandedName():
    '''public QName getExpandedName()
    '''
def childIterator():
    '''public NodeIterator childIterator(final NodeTest test, final boolean reverse, final NodePointer startWith)
    '''
def attributeIterator():
    '''public NodeIterator attributeIterator(final QName name)
    '''
def namespacePointer():
    '''public NodePointer namespacePointer(final String prefix)
    '''
def namespaceIterator():
    '''public NodeIterator namespaceIterator()
    '''
def getDefaultNamespaceURI():
    '''public String getDefaultNamespaceURI()
    '''
def getBaseValue():
    '''public Object getBaseValue()
    '''
def getImmediateNode():
    '''public Object getImmediateNode()
    '''
def isActual():
    '''public boolean isActual()
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
def isLanguage():
    '''public boolean isLanguage(final String lang)
    '''
def setValue():
    '''public void setValue(final Object value)
    '''
def createChild():
    '''public NodePointer createChild(final JXPathContext context, final QName name, int index)
    public NodePointer createChild(final JXPathContext context, final QName name, final int index, final Object value)
    '''
def createAttribute():
    '''public NodePointer createAttribute(final JXPathContext context, final QName name)
    '''
def remove():
    '''public void remove()
    '''
def asPath():
    '''public String asPath()
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object object)
    '''
def getPrefix():
    '''public static String getPrefix(final Node node)
    '''
def getLocalName():
    '''public static String getLocalName(final Node node)
    '''
def getValue():
    '''public Object getValue()
    '''
def getPointerByID():
    '''public Pointer getPointerByID(final JXPathContext context, final String id)
    '''
def compareChildNodePointers():
    '''public int compareChildNodePointers(final NodePointer pointer1, final NodePointer pointer2)
    '''
