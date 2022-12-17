def _ids():
    '''returns String[]\n\n
    _ids()\n
    '''
def addNotificationListener():
    '''returns None\n\n
    addNotificationListener(final ObjectName objectName, final ObjectName objectName2, final NotificationFilter notificationFilter, final Object o)\n
    '''
def addRMINotificationListener():
    '''returns ListenerIdentifier\n\n
    addRMINotificationListener(final ConsolidatedFilter consolidatedFilter, final RMINotificationListener rmiNotificationListener)\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final ObjectName objectName, final String s)\n
    '''
def getAttributes():
    '''returns AttributeList\n\n
    getAttributes(final ObjectName objectName, final String[] array)\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader(final ObjectName objectName)\n
    '''
def getClassLoaderFor():
    '''returns ClassLoader\n\n
    getClassLoaderFor(final ObjectName objectName)\n
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
    getMBeanInfo(final ObjectName objectName)\n
    '''
def getObjectInstance():
    '''returns ObjectInstance\n\n
    getObjectInstance(final ObjectName objectName)\n
    '''
def getServerMBean():
    '''returns ObjectName\n\n
    getServerMBean()\n
    '''
def invoke():
    '''returns Object\n\n
    invoke(final ObjectName objectName, final String s, final Object[] array, final String[] array2)\n
    '''
def isAlive():
    '''returns Session\n\n
    isAlive()\n
    '''
def isInstanceOf():
    '''returns boolean\n\n
    isInstanceOf(final ObjectName objectName, final String s)\n
    '''
def isRegistered():
    '''returns boolean\n\n
    isRegistered(final ObjectName objectName)\n
    '''
def pullNotifications():
    '''returns Notification[]\n\n
    pullNotifications(final ListenerIdentifier listenerIdentifier, final Integer n)\n
    '''
def queryMBeans():
    '''returns Set\n\n
    queryMBeans(final ObjectName objectName, final QueryExp queryExp)\n
    '''
def queryNames():
    '''returns Set\n\n
    queryNames(final ObjectName objectName, final QueryExp queryExp)\n
    '''
def removeNotificationListener():
    '''returns None\n\n
    removeNotificationListener(final ListenerIdentifier listenerIdentifier)\n
    '''
def removeNotificationListener_2():
    '''returns None\n\n
    removeNotificationListener_2(final ObjectName objectName, final ObjectName objectName2)\n
    '''
def removeNotificationListener_4():
    '''returns None\n\n
    removeNotificationListener_4(final ObjectName objectName, final ObjectName objectName2, final NotificationFilter notificationFilter, final Object o)\n
    '''
def resetFilter():
    '''returns None\n\n
    resetFilter(final ListenerIdentifier listenerIdentifier, final ConsolidatedFilter consolidatedFilter)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final ObjectName objectName, final Attribute attribute)\n
    '''
def setAttributes():
    '''returns AttributeList\n\n
    setAttributes(final ObjectName objectName, final AttributeList list)\n
    '''
