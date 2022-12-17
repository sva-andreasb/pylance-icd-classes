def createMBean():
    '''returns ObjectInstance\n\n
    createMBean(final String p1, final ObjectName p2)\n
    createMBean(final String p1, final ObjectName p2, final ObjectName p3)\n
    createMBean(final String p1, final ObjectName p2, final Object[] p3, final String[] p4)\n
    createMBean(final String p1, final ObjectName p2, final ObjectName p3, final Object[] p4, final String[] p5)\n
    '''
def registerMBean():
    '''returns ObjectInstance\n\n
    registerMBean(final Object p1, final ObjectName p2)\n
    '''
def unregisterMBean():
    '''returns None\n\n
    unregisterMBean(final ObjectName p1)\n
    '''
def getObjectInstance():
    '''returns ObjectInstance\n\n
    getObjectInstance(final ObjectName p1)\n
    '''
def queryMBeans():
    '''returns Set\n\n
    queryMBeans(final ObjectName p1, final QueryExp p2)\n
    '''
def queryNames():
    '''returns Set\n\n
    queryNames(final ObjectName p1, final QueryExp p2)\n
    '''
def isRegistered():
    '''returns boolean\n\n
    isRegistered(final ObjectName p1)\n
    '''
def getMBeanCount():
    '''returns Integer\n\n
    getMBeanCount()\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final ObjectName p1, final String p2)\n
    '''
def getAttributes():
    '''returns AttributeList\n\n
    getAttributes(final ObjectName p1, final String[] p2)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final ObjectName p1, final Attribute p2)\n
    '''
def setAttributes():
    '''returns AttributeList\n\n
    setAttributes(final ObjectName p1, final AttributeList p2)\n
    '''
def invoke():
    '''returns Object\n\n
    invoke(final ObjectName name, final String operationName, final Object[] params, final String[] signature)\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    '''
def getDefaultDomain():
    '''returns String\n\n
    getDefaultDomain()\n
    '''
def getDomains():
    '''returns String[]\n\n
    getDomains()\n
    '''
def addNotificationListener():
    '''returns None\n\n
    addNotificationListener(final ObjectName p1, final NotificationListener p2, final NotificationFilter p3, final Object p4)\n
    addNotificationListener(final ObjectName p1, final ObjectName p2, final NotificationFilter p3, final Object p4)\n
    '''
def removeNotificationListener():
    '''returns None\n\n
    removeNotificationListener(final ObjectName p1, final ObjectName p2)\n
    removeNotificationListener(final ObjectName p1, final ObjectName p2, final NotificationFilter p3, final Object p4)\n
    removeNotificationListener(final ObjectName p1, final NotificationListener p2)\n
    removeNotificationListener(final ObjectName p1, final NotificationListener p2, final NotificationFilter p3, final Object p4)\n
    '''
def getMBeanInfo():
    '''returns MBeanInfo\n\n
    getMBeanInfo(final ObjectName p1)\n
    '''
def isInstanceOf():
    '''returns boolean\n\n
    isInstanceOf(final ObjectName p1, final String p2)\n
    '''
def instantiate():
    '''returns Object\n\n
    instantiate(final String p1)\n
    instantiate(final String p1, final ObjectName p2)\n
    instantiate(final String p1, final Object[] p2, final String[] p3)\n
    instantiate(final String p1, final ObjectName p2, final Object[] p3, final String[] p4)\n
    '''
def deserialize():
    '''returns ObjectInputStream\n\n
    deserialize(final ObjectName p1, final byte[] p2)\n
    deserialize(final String p1, final byte[] p2)\n
    deserialize(final String p1, final ObjectName p2, final byte[] p3)\n
    '''
def getClassLoaderFor():
    '''returns ClassLoader\n\n
    getClassLoaderFor(final ObjectName p1)\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader(final ObjectName p1)\n
    '''
def getClassLoaderRepository():
    '''returns ClassLoaderRepository\n\n
    getClassLoaderRepository()\n
    '''
