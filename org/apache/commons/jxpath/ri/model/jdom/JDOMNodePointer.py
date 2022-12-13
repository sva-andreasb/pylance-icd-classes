XML_NAMESPACE_URI = "String  http://www.w3.org/XML/1998/namespace""
XMLNS_NAMESPACE_URI = "String  http://www.w3.org/2000/xmlns/""
def JDOMNodePointer():
'''public JDOMNodePointer(final Object node, final Locale locale)
public JDOMNodePointer(final Object node, final Locale locale, final String id)
public JDOMNodePointer(final NodePointer parent, final Object node)
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
def namespaceIterator():
'''public NodeIterator namespaceIterator()
'''
pass
def namespacePointer():
'''public NodePointer namespacePointer(final String prefix)
'''
pass
def getNamespaceURI():
'''public String getNamespaceURI()
public String getNamespaceURI(final String prefix)
'''
pass
def compareChildNodePointers():
'''public int compareChildNodePointers(final NodePointer pointer1, final NodePointer pointer2)
'''
pass
def getBaseValue():
'''public Object getBaseValue()
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
def getName():
'''public QName getName()
'''
pass
def getExpandedName():
'''public QName getExpandedName()
'''
pass
def getImmediateNode():
'''public Object getImmediateNode()
'''
pass
def getValue():
'''public Object getValue()
'''
pass
def setValue():
'''public void setValue(final Object value)
'''
pass
def testNode():
'''public boolean testNode(final NodeTest test)
public static boolean testNode(final NodePointer pointer, final Object node, final NodeTest test)
'''
pass
def getPrefix():
'''public static String getPrefix(final Object node)
'''
pass
def getLocalName():
'''public static String getLocalName(final Object node)
'''
pass
def isLanguage():
'''public boolean isLanguage(final String lang)
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
