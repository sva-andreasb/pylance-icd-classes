def ():
    '''returns IPCConnectorClient\n\n
    (final Properties props)\n
    '''
def setUserAndPwd():
    '''returns None\n\n
    setUserAndPwd(final String uid, final String pwd)\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    run()\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
def getProxyProperties():
    '''returns Properties\n\n
    getProxyProperties()\n
    '''
def openRemoteNotificationChannel():
    '''returns RemoteReceiver\n\n
    openRemoteNotificationChannel(final AdminServiceProxy proxy)\n
    '''
def isAlive():
    '''returns Session\n\n
    isAlive()\n
    isAlive(final int timeout)\n
    '''
def queryNames():
    '''returns Set\n\n
    queryNames(final ObjectName name, final QueryExp query)\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final ObjectName name, final String attribute)\n
    '''
def getAttributes():
    '''returns AttributeList\n\n
    getAttributes(final ObjectName name, final String[] attributes)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final ObjectName name, final Attribute attribute)\n
    '''
def setAttributes():
    '''returns AttributeList\n\n
    setAttributes(final ObjectName name, final AttributeList attributes)\n
    '''
def invoke():
    '''returns Object\n\n
    invoke(final ObjectName name, final String operationName, final Object[] params, final String[] signature)\n
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
def getServerMBean():
    '''returns ObjectName\n\n
    getServerMBean()\n
    '''
def getMBeanInfo():
    '''returns MBeanInfo\n\n
    getMBeanInfo(final ObjectName name)\n
    '''
def isRegistered():
    '''returns boolean\n\n
    isRegistered(final ObjectName name)\n
    '''
def getClassLoaderFor():
    '''returns ClassLoader\n\n
    getClassLoaderFor(final ObjectName name)\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader(final ObjectName name)\n
    '''
def isInstanceOf():
    '''returns boolean\n\n
    isInstanceOf(final ObjectName name, final String className)\n
    '''
def queryMBeans():
    '''returns Set\n\n
    queryMBeans(final ObjectName name, final QueryExp query)\n
    '''
def getObjectInstance():
    '''returns ObjectInstance\n\n
    getObjectInstance(final ObjectName name)\n
    '''
def addNotificationListener():
    '''returns None\n\n
    addNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)\n
    addNotificationListener(final ConsolidatedFilter filter, final PushNotificationListener listener)\n
    addNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    '''
def removeNotificationListener():
    '''returns None\n\n
    removeNotificationListener(final ObjectName name, final ObjectName listener)\n
    removeNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)\n
    removeNotificationListener(final ListenerIdentifier listenerId)\n
    removeNotificationListener(final ObjectName name, final NotificationListener listener)\n
    '''
def resetFilter():
    '''returns None\n\n
    resetFilter(final ListenerIdentifier listenerId, final ConsolidatedFilter filters)\n
    '''
def pullNotifications():
    '''returns Notification[]\n\n
    pullNotifications(final ListenerIdentifier id, final Integer batchSize)\n
    '''
def removeNotificationListenerExtended():
    '''returns None\n\n
    removeNotificationListenerExtended(final NotificationListener listener)\n
    removeNotificationListenerExtended(final ObjectName name, final NotificationListener listener)\n
    '''
def addNotificationListenerExtended():
    '''returns None\n\n
    addNotificationListenerExtended(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    '''
