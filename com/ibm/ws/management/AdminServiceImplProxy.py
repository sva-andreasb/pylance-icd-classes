def getMBeanFactory():
    '''returns MBeanFactory\n\n
    getMBeanFactory()\n
    '''
def getCellName():
    '''returns String\n\n
    getCellName()\n
    '''
def getNodeName():
    '''returns String\n\n
    getNodeName()\n
    '''
def getProcessName():
    '''returns String\n\n
    getProcessName()\n
    '''
def getServerType():
    '''returns String\n\n
    getServerType()\n
    '''
def getCellType():
    '''returns String\n\n
    getCellType()\n
    '''
def isCellRegistered():
    '''returns boolean\n\n
    isCellRegistered()\n
    '''
def isAlive():
    '''returns Session\n\n
    isAlive()\n
    isAlive(final int timeout)\n
    '''
def getJvmType():
    '''returns String\n\n
    getJvmType()\n
    '''
def instantiate():
    '''returns Object\n\n
    instantiate(final String className)\n
    instantiate(final String className, final ObjectName loaderName)\n
    instantiate(final String className, final Object[] args, final String[] parameters)\n
    instantiate(final String className, final ObjectName loaderName, final Object[] args, final String[] parameters)\n
    '''
def createMBean():
    '''returns ObjectInstance\n\n
    createMBean(final String className, final ObjectName name)\n
    createMBean(final String className, final ObjectName name, final ObjectName loaderName)\n
    createMBean(final String className, final ObjectName name, final Object[] params, final String[] signature)\n
    createMBean(final String className, final ObjectName name, final ObjectName loaderName, final Object[] params, final String[] signature)\n
    '''
def registerMBean():
    '''returns ObjectInstance\n\n
    registerMBean(final Object object, final ObjectName name)\n
    '''
def getDomainName():
    '''returns String\n\n
    getDomainName()\n
    '''
def unregisterMBean():
    '''returns None\n\n
    unregisterMBean(final ObjectName name)\n
    '''
def queryMBeans():
    '''returns Set\n\n
    queryMBeans(final ObjectName name, final QueryExp query)\n
    '''
def queryNames():
    '''returns Set\n\n
    queryNames(final ObjectName name, final QueryExp query)\n
    '''
def isRegistered():
    '''returns boolean\n\n
    isRegistered(final ObjectName name)\n
    '''
def getMBeanCount():
    '''returns Integer\n\n
    getMBeanCount()\n
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
    invoke(final ObjectName origName, final String operationName, final Object[] params, final String[] signature)\n
    '''
def getDefaultDomain():
    '''returns String\n\n
    getDefaultDomain()\n
    '''
def getMBeanInfo():
    '''returns MBeanInfo\n\n
    getMBeanInfo(final ObjectName name)\n
    '''
def isInstanceOf():
    '''returns boolean\n\n
    isInstanceOf(final ObjectName name, final String className)\n
    '''
def addNotificationListener():
    '''returns None\n\n
    addNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    addNotificationListener(final ConsolidatedFilter filter, final PushNotificationListener listener)\n
    addNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)\n
    '''
def addNotificationListenerExtended():
    '''returns None\n\n
    addNotificationListenerExtended(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    '''
def removeNotificationListener():
    '''returns None\n\n
    removeNotificationListener(final ObjectName name, final NotificationListener listener)\n
    removeNotificationListener(final ListenerIdentifier listenerId)\n
    removeNotificationListener(final ObjectName name, final ObjectName listener)\n
    removeNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)\n
    removeNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    '''
def removeNotificationListenerExtended():
    '''returns None\n\n
    removeNotificationListenerExtended(final ObjectName name, final NotificationListener listener)\n
    removeNotificationListenerExtended(final NotificationListener listener)\n
    '''
def initializeNotificationService():
    '''returns None\n\n
    initializeNotificationService()\n
    '''
def getNotificationService():
    '''returns NotificationService\n\n
    getNotificationService()\n
    '''
def resetFilter():
    '''returns None\n\n
    resetFilter(final ListenerIdentifier listenerId, final ConsolidatedFilter filter)\n
    '''
def pullNotifications():
    '''returns Notification[]\n\n
    pullNotifications(final ListenerIdentifier id, final Integer batchSize)\n
    '''
def getProcessType():
    '''returns String\n\n
    getProcessType()\n
    '''
def setProcessType():
    '''returns None\n\n
    setProcessType(final String type)\n
    '''
def getServerMBean():
    '''returns ObjectName\n\n
    getServerMBean()\n
    '''
def getLocalServer():
    '''returns ObjectName\n\n
    getLocalServer()\n
    '''
def setLocalServer():
    '''returns None\n\n
    setLocalServer(final ObjectName svrBean)\n
    '''
def isLocalServer():
    '''returns boolean\n\n
    isLocalServer(final String cellname, final String nodename, final String servername)\n
    '''
def getDeploymentManagerAdminClient():
    '''returns AdminClient\n\n
    getDeploymentManagerAdminClient()\n
    '''
def zOSInitComplete():
    '''returns None\n\n
    zOSInitComplete()\n
    '''
def isZOSInitComplete():
    '''returns boolean\n\n
    isZOSInitComplete()\n
    '''
def transformConfigId():
    '''returns String\n\n
    transformConfigId(final String old)\n
    '''
def reverseTransformConfigId():
    '''returns String\n\n
    reverseTransformConfigId(final String old)\n
    '''
def getClassLoaderFor():
    '''returns ClassLoader\n\n
    getClassLoaderFor(final ObjectName name)\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader(final ObjectName name)\n
    '''
def getClassLoaderRepository():
    '''returns ClassLoaderRepository\n\n
    getClassLoaderRepository()\n
    '''
def getDomains():
    '''returns String[]\n\n
    getDomains()\n
    '''
def getObjectInstance():
    '''returns ObjectInstance\n\n
    getObjectInstance(final ObjectName name)\n
    '''
