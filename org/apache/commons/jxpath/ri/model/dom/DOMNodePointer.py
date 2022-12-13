XML_NAMESPACE_URI = "String  http://www.w3.org/XML/1998/namespace""
XMLNS_NAMESPACE_URI = "String  http://www.w3.org/2000/xmlns/""
def DOMNodePointer():
'''public DOMNodePointer(final Node node, final Locale locale)
public DOMNodePointer(final Node node, final Locale locale, final String id)
public DOMNodePointer(final NodePointer parent, final Node node)
'''
pass
def testNode():
'''public boolean testNode(final NodeTest test)
public static boolean testNode(final NodePointer pointer, final Node node, final NodeTest test)
'''
pass
def getName():
'''public QName getName()
'''
pass
def getNamespaceURI():
'''public String getNamespaceURI()
public String getNamespaceURI(final String prefix)
'''
pass
def getExpandedName():
'''public QName getExpandedName()
'''
pass
def childIterator():
'''public NodeIterator childIterator(final NodeTest test, final boolean reverse, final NodePointer startWith)
'''
pass
def attributeIterator():
'''public NodeIterator attributeIterator(final QName name)
'''
pass
def namespacePointer():
'''public NodePointer namespacePointer(final String prefix)
'''
pass
def namespaceIterator():
'''public NodeIterator namespaceIterator()
'''
pass
def getDefaultNamespaceURI():
'''public String getDefaultNamespaceURI()
'''
pass
def getBaseValue():
'''public Object getBaseValue()
'''
pass
def getImmediateNode():
'''public Object getImmediateNode()
'''
pass
def isActual():
'''public boolean isActual()
'''
pass
def isCollection():
'''public boolean isCollection()
'''
pass
def getLength():
'''public int getLength()
'''
pass
def isLeaf():
'''public boolean isLeaf()
'''
pass
def isLanguage():
'''public boolean isLanguage(final String lang)
'''
pass
def setValue():
'''public void setValue(final Object value)
'''
pass
def createChild():
'''public NodePointer createChild(final JXPathContext context, final QName name, int index)
public NodePointer createChild(final JXPathContext context, final QName name, final int index, final Object value)
'''
pass
def createAttribute():
'''public NodePointer createAttribute(final JXPathContext context, final QName name)
'''
pass
def remove():
'''public void remove()
'''
pass
def asPath():
'''public String asPath()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object object)
'''
pass
def getPrefix():
'''public static String getPrefix(final Node node)
'''
pass
def getLocalName():
'''public static String getLocalName(final Node node)
'''
pass
def getValue():
'''public Object getValue()
'''
pass
def getPointerByID():
'''public Pointer getPointerByID(final JXPathContext context, final String id)
'''
pass
def compareChildNodePointers():
'''public int compareChildNodePointers(final NodePointer pointer1, final NodePointer pointer2)
'''
pass
