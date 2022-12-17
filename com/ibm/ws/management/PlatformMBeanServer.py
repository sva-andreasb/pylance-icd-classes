def ():
    '''returns PlatformMBeanServer\n\n
    (final MBeanServer mbserver)\n
    '''
def getDefaultMBeanServer():
    '''returns MBeanServer\n\n
    getDefaultMBeanServer()\n
    '''
def getAdminService():
    '''returns AdminService\n\n
    getAdminService()\n
    '''
def addNotificationListener():
    '''returns None\n\n
    addNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    addNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)\n
    '''
def createMBean():
    '''returns ObjectInstance\n\n
    createMBean(final String className, final ObjectName name)\n
    createMBean(final String className, final ObjectName name, final Object[] params, final String[] signature)\n
    createMBean(final String className, final ObjectName name, final ObjectName loaderName)\n
    createMBean(final String className, final ObjectName name, final ObjectName loaderName, final Object[] params, final String[] signature)\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader(final ObjectName loaderName)\n
    '''
def getClassLoaderRepository():
    '''returns ClassLoaderRepository\n\n
    getClassLoaderRepository()\n
    '''
def getDefaultDomain():
    '''returns String\n\n
    getDefaultDomain()\n
    '''
def getDomains():
    '''returns String[]\n\n
    getDomains()\n
    '''
def getObjectInstance():
    '''returns ObjectInstance\n\n
    getObjectInstance(final ObjectName name)\n
    '''
def instantiate():
    '''returns Object\n\n
    instantiate(final String className)\n
    instantiate(final String className, final ObjectName loaderName)\n
    instantiate(final String className, final Object[] params, final String[] signature)\n
    instantiate(final String className, final ObjectName loaderName, final Object[] params, final String[] signature)\n
    '''
def queryMBeans():
    '''returns Set\n\n
    queryMBeans(final ObjectName name, final QueryExp query)\n
    '''
def removeNotificationListener():
    '''returns None\n\n
    removeNotificationListener(final ObjectName name, final NotificationListener listener)\n
    removeNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    removeNotificationListener(final ObjectName name, final ObjectName listener)\n
    removeNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)\n
    '''
def registerMBean():
    '''returns ObjectInstance\n\n
    registerMBean(final Object modelMBean, ObjectName modelMBeanName)\n
    '''
def unregisterMBean():
    '''returns None\n\n
    unregisterMBean(final ObjectName name)\n
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
def getMBeanInfo():
    '''returns MBeanInfo\n\n
    getMBeanInfo(final ObjectName name)\n
    '''
def isInstanceOf():
    '''returns boolean\n\n
    isInstanceOf(final ObjectName name, final String className)\n
    '''
def getClassLoaderFor():
    '''returns ClassLoader\n\n
    getClassLoaderFor(final ObjectName mbeanName)\n
    '''
def deserialize():
    '''returns ObjectInputStream\n\n
    deserialize(final ObjectName name, final byte[] data)\n
    deserialize(final String className, final byte[] data)\n
    deserialize(final String className, final ObjectName loaderName, final byte[] data)\n
    '''
def initControlAdmin():
    '''returns None\n\n
    initControlAdmin()\n
    '''
def setAdminProps():
    '''returns None\n\n
    setAdminProps(final Properties adminProps)\n
    '''
