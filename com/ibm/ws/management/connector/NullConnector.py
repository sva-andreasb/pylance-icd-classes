def ():
    '''returns NullConnector\n\n
    ()\n
    (final Properties props)\n
    '''
def addNotificationListener():
    '''returns None\n\n
    addNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    addNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)\n
    '''
def addNotificationListenerExtended():
    '''returns None\n\n
    addNotificationListenerExtended(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final ObjectName name, final String attribute)\n
    '''
def getAttributes():
    '''returns AttributeList\n\n
    getAttributes(final ObjectName name, final String[] attributes)\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader(final ObjectName name)\n
    '''
def getClassLoaderFor():
    '''returns ClassLoader\n\n
    getClassLoaderFor(final ObjectName name)\n
    '''
def getConnectorProperties():
    '''returns Properties\n\n
    getConnectorProperties()\n
    '''
def getDefaultDomain():
    '''returns String\n\n
    getDefaultDomain()\n
    '''
def getDomainName():
    '''returns String\n\n
    getDomainName()\n
    '''
def getMBeanCount():
    '''returns Integer\n\n
    getMBeanCount()\n
    '''
def getMBeanInfo():
    '''returns MBeanInfo\n\n
    getMBeanInfo(final ObjectName name)\n
    '''
def getObjectInstance():
    '''returns ObjectInstance\n\n
    getObjectInstance(final ObjectName name)\n
    '''
def getServerMBean():
    '''returns ObjectName\n\n
    getServerMBean()\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
def invoke():
    '''returns Object\n\n
    invoke(final ObjectName name, final String operationName, final Object[] params, final String[] signature)\n
    '''
def isAlive():
    '''returns Session\n\n
    isAlive()\n
    isAlive(final int timeout)\n
    '''
def isInstanceOf():
    '''returns boolean\n\n
    isInstanceOf(final ObjectName name, final String className)\n
    '''
def isRegistered():
    '''returns boolean\n\n
    isRegistered(final ObjectName name)\n
    '''
def queryMBeans():
    '''returns Set\n\n
    queryMBeans(final ObjectName name, final QueryExp query)\n
    '''
def queryNames():
    '''returns Set\n\n
    queryNames(final ObjectName name, final QueryExp query)\n
    '''
def removeNotificationListener():
    '''returns None\n\n
    removeNotificationListener(final ObjectName name, final NotificationListener listener)\n
    removeNotificationListener(final ObjectName name, final ObjectName listener)\n
    removeNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)\n
    '''
def removeNotificationListenerExtended():
    '''returns None\n\n
    removeNotificationListenerExtended(final NotificationListener listener)\n
    removeNotificationListenerExtended(final ObjectName name, final NotificationListener listener)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final ObjectName name, final Attribute attribute)\n
    '''
def setAttributes():
    '''returns AttributeList\n\n
    setAttributes(final ObjectName name, final AttributeList attributes)\n
    '''
