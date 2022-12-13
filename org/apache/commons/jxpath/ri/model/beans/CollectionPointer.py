def CollectionPointer():
'''public CollectionPointer(final Object collection, final Locale locale)
public CollectionPointer(final NodePointer parent, final Object collection)
'''
pass
def getName():
'''public QName getName()
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
def isContainer():
'''public boolean isContainer()
'''
pass
def getImmediateNode():
'''public Object getImmediateNode()
'''
pass
def setValue():
'''public void setValue(final Object value)
'''
pass
def setIndex():
'''public void setIndex(final int index)
'''
pass
def getValuePointer():
'''public NodePointer getValuePointer()
'''
pass
def createPath():
'''public NodePointer createPath(final JXPathContext context)
public NodePointer createPath(final JXPathContext context, final Object value)
'''
pass
def createChild():
'''public NodePointer createChild(final JXPathContext context, final QName name, final int index, final Object value)
public NodePointer createChild(final JXPathContext context, final QName name, final int index)
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
'''public NodePointer namespacePointer(final String namespace)
'''
pass
def testNode():
'''public boolean testNode(final NodeTest nodeTest)
'''
pass
def compareChildNodePointers():
'''public int compareChildNodePointers(final NodePointer pointer1, final NodePointer pointer2)
'''
pass
def asPath():
'''public String asPath()
'''
pass
