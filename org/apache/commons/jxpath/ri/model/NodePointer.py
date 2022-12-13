WHOLE_COLLECTION = "int  Integer.MIN_VALUE"
UNKNOWN_NAMESPACE = "String  \"<<unknown namespace>>\""
def newNodePointer():
    '''public static NodePointer newNodePointer(final QName name, final Object bean, final Locale locale)
    '''
def newChildNodePointer():
    '''public static NodePointer newChildNodePointer(final NodePointer parent, final QName name, final Object bean)
    '''
def getParent():
    '''public NodePointer getParent()
    '''
def setAttribute():
    '''public void setAttribute(final boolean attribute)
    '''
def isAttribute():
    '''public boolean isAttribute()
    '''
def isRoot():
    '''public boolean isRoot()
    '''
def isNode():
    '''public boolean isNode()
    '''
def isContainer():
    '''public boolean isContainer()
    '''
def getIndex():
    '''public int getIndex()
    '''
def setIndex():
    '''public void setIndex(final int index)
    '''
def getValue():
    '''public Object getValue()
    '''
def getValuePointer():
    '''public NodePointer getValuePointer()
    '''
def getImmediateValuePointer():
    '''public NodePointer getImmediateValuePointer()
    '''
def isActual():
    '''public boolean isActual()
    '''
def getNodeValue():
    '''public Object getNodeValue()
    '''
def getNode():
    '''public Object getNode()
    '''
def getRootNode():
    '''public Object getRootNode()
    '''
def testNode():
    '''public boolean testNode(final NodeTest test)
    '''
def createPath():
    '''public NodePointer createPath(final JXPathContext context, final Object value)
    public NodePointer createPath(final JXPathContext context)
    '''
def remove():
    '''public void remove()
    '''
def createChild():
    '''public NodePointer createChild(final JXPathContext context, final QName name, final int index, final Object value)
    public NodePointer createChild(final JXPathContext context, final QName name, final int index)
    '''
def createAttribute():
    '''public NodePointer createAttribute(final JXPathContext context, final QName name)
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def isLanguage():
    '''public boolean isLanguage(final String lang)
    '''
def childIterator():
    '''public NodeIterator childIterator(final NodeTest test, final boolean reverse, final NodePointer startWith)
    '''
def attributeIterator():
    '''public NodeIterator attributeIterator(final QName qname)
    '''
def namespaceIterator():
    '''public NodeIterator namespaceIterator()
    '''
def namespacePointer():
    '''public NodePointer namespacePointer(final String namespace)
    '''
def getNamespaceURI():
    '''public String getNamespaceURI(final String prefix)
    public String getNamespaceURI()
    '''
def getExpandedName():
    '''public QName getExpandedName()
    '''
def getPointerByID():
    '''public Pointer getPointerByID(final JXPathContext context, final String id)
    '''
def getPointerByKey():
    '''public Pointer getPointerByKey(final JXPathContext context, final String key, final String value)
    '''
def asPath():
    '''public String asPath()
    '''
def clone():
    '''public Object clone()
    '''
def toString():
    '''public String toString()
    '''
def compareTo():
    '''public int compareTo(final Object object)
    '''
def printPointerChain():
    '''public void printPointerChain()
    '''
