def ():
    '''returns IlvDefaultDataContainer\n\n
    ()\n
    '''
def getParent():
    '''returns Object\n\n
    getParent(final Object key)\n
    '''
def getChildAt():
    '''returns Object\n\n
    getChildAt(final Object key, final int n)\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount(final Object key)\n
    '''
def getIndexOfChild():
    '''returns int\n\n
    getIndexOfChild(final Object key, final Object o)\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle(final Object o)\n
    getTitle()\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final Object o, final String title)\n
    setTitle(final String a)\n
    '''
def getNodeProperty():
    '''returns Object\n\n
    getNodeProperty(final Object key, final String key2)\n
    '''
def setNodeProperty():
    '''returns None\n\n
    setNodeProperty(final Object key, final String key2, final Object value)\n
    '''
def getCategory():
    '''returns String\n\n
    getCategory(final Object o)\n
    '''
def insertNode():
    '''returns None\n\n
    insertNode(final Object key, final Object element, int index)\n
    '''
def removeNode():
    '''returns boolean\n\n
    removeNode(final Object key, final Object key2)\n
    '''
def acceptChild():
    '''returns boolean\n\n
    acceptChild(final Object o, final String s)\n
    acceptChild(final String s)\n
    '''
def canRemove():
    '''returns boolean\n\n
    canRemove(final Object o, final Object o2)\n
    '''
def addDataContainerListener():
    '''returns None\n\n
    addDataContainerListener(final DataContainerListener dataContainerListener)\n
    '''
def removeDataContainerListener():
    '''returns None\n\n
    removeDataContainerListener(final DataContainerListener dataContainerListener)\n
    '''
def fireNodeAdditionEvent():
    '''returns None\n\n
    fireNodeAdditionEvent(final Object o, final Object o2, final int n)\n
    '''
def fireNodeRemovalEvent():
    '''returns None\n\n
    fireNodeRemovalEvent(final Object o, final Object o2, final int n)\n
    '''
def firePropertyChangeEvent():
    '''returns None\n\n
    firePropertyChangeEvent(final Object o, final Object o2, final int n, final String s, final Object o3, final Object o4)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String key)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String key, final Object value)\n
    '''
def canRemoveChild():
    '''returns boolean\n\n
    canRemoveChild(final Object o)\n
    '''
