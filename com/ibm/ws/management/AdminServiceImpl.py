def AdminServiceImpl():
    '''public AdminServiceImpl()
    '''
def getMBeanFactory():
    '''public MBeanFactory getMBeanFactory()
    '''
def getCellName():
    '''public String getCellName()
    '''
def getNodeName():
    '''public String getNodeName()
    '''
def getProcessName():
    '''public String getProcessName()
    '''
def getServerType():
    '''public String getServerType()
    '''
def getCellType():
    '''public String getCellType()
    '''
def isCellRegistered():
    '''public boolean isCellRegistered()
    '''
def isAlive():
    '''public Session isAlive()
    public Session isAlive(final int timeout)
    '''
def getJvmType():
    '''public String getJvmType()
    '''
def instantiate():
    '''public Object instantiate(final String className)
    public Object instantiate(final String className, final ObjectName loaderName)
    public Object instantiate(final String className, final Object[] args, final String[] parameters)
    public Object instantiate(final String className, final ObjectName loaderName, final Object[] args, final String[] parameters)
    '''
def createMBean():
    '''public ObjectInstance createMBean(final String className, final ObjectName name)
    public ObjectInstance createMBean(final String className, final ObjectName name, final ObjectName loaderName)
    public ObjectInstance createMBean(final String className, final ObjectName name, final Object[] params, final String[] signature)
    public ObjectInstance createMBean(final String className, final ObjectName name, final ObjectName loaderName, final Object[] params, final String[] signature)
    '''
def registerMBean():
    '''public ObjectInstance registerMBean(final Object object, final ObjectName name)
    '''
def getDomainName():
    '''public String getDomainName()
    '''
def unregisterMBean():
    '''public void unregisterMBean(final ObjectName name)
    '''
def queryMBeans():
    '''public Set queryMBeans(final ObjectName name, final QueryExp query)
    '''
def queryNames():
    '''public Set queryNames(final ObjectName name, final QueryExp query)
    '''
def isRegistered():
    '''public boolean isRegistered(final ObjectName name)
    '''
def getMBeanCount():
    '''public Integer getMBeanCount()
    '''
def getAttribute():
    '''public Object getAttribute(ObjectName name, final String attribute)
    '''
def getAttributes():
    '''public AttributeList getAttributes(ObjectName name, final String[] attributes)
    '''
def setAttribute():
    '''public void setAttribute(ObjectName name, final Attribute attribute)
    '''
def setAttributes():
    '''public AttributeList setAttributes(ObjectName name, final AttributeList attributes)
    '''
def invoke():
    '''public Object invoke(final ObjectName origName, final String operationName, final Object[] params, final String[] signature)
    '''
def run():
    '''public Object run()
    public Object run()
    public Object run()
    '''
def getDefaultDomain():
    '''public String getDefaultDomain()
    '''
def getMBeanInfo():
    '''public MBeanInfo getMBeanInfo(ObjectName name)
    '''
def isInstanceOf():
    '''public boolean isInstanceOf(ObjectName name, final String className)
    '''
def addNotificationListener():
    '''public void addNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)
    public ListenerIdentifier addNotificationListener(final ConsolidatedFilter filter, final PushNotificationListener listener)
    public void addNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)
    '''
def addNotificationListenerExtended():
    '''public void addNotificationListenerExtended(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)
    '''
def removeNotificationListener():
    '''public void removeNotificationListener(final ObjectName name, final NotificationListener listener)
    public void removeNotificationListener(final ListenerIdentifier listenerId)
    public void removeNotificationListener(final ObjectName name, final ObjectName listener)
    public void removeNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)
    public void removeNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)
    '''
def removeNotificationListenerExtended():
    '''public void removeNotificationListenerExtended(final ObjectName name, final NotificationListener listener)
    public void removeNotificationListenerExtended(final NotificationListener listener)
    '''
def initializeNotificationService():
    '''public void initializeNotificationService()
    '''
def getNotificationService():
    '''public NotificationService getNotificationService()
    '''
def resetFilter():
    '''public void resetFilter(final ListenerIdentifier listenerId, final ConsolidatedFilter filter)
    '''
def pullNotifications():
    '''public Notification[] pullNotifications(final ListenerIdentifier id, final Integer batchSize)
    '''
def getProcessType():
    '''public String getProcessType()
    '''
def setProcessType():
    '''public void setProcessType(final String type)
    '''
def getServerMBean():
    '''public ObjectName getServerMBean()
    '''
def getLocalServer():
    '''public ObjectName getLocalServer()
    '''
def setLocalServer():
    '''public void setLocalServer(final ObjectName svrBean)
    '''
def isLocalServer():
    '''public boolean isLocalServer(final String cellname, final String nodename, final String servername)
    '''
def getDeploymentManagerAdminClient():
    '''public AdminClient getDeploymentManagerAdminClient()
    '''
def getPlatformUtils():
    '''public static PlatformUtils getPlatformUtils()
    '''
def zOSInitComplete():
    '''public void zOSInitComplete()
    '''
def isZOSInitComplete():
    '''public boolean isZOSInitComplete()
    '''
def transformConfigId():
    '''public String transformConfigId(final String old)
    '''
def reverseTransformConfigId():
    '''public String reverseTransformConfigId(final String old)
    '''
def getClassLoaderFor():
    '''public ClassLoader getClassLoaderFor(final ObjectName name)
    '''
def getClassLoader():
    '''public ClassLoader getClassLoader(final ObjectName name)
    '''
def getClassLoaderRepository():
    '''public ClassLoaderRepository getClassLoaderRepository()
    '''
def getDomains():
    '''public String[] getDomains()
    '''
def getObjectInstance():
    '''public ObjectInstance getObjectInstance(final ObjectName name)
    '''
def checkAdminContext():
    '''public void checkAdminContext()
    '''
def mbeanFilter():
    '''public static boolean mbeanFilter(final ObjectName name, final ArrayList mbeanProps)
    '''
