def AdminServiceImpl():
'''public AdminServiceImpl()
'''
pass
def getMBeanFactory():
'''public MBeanFactory getMBeanFactory()
'''
pass
def getCellName():
'''public String getCellName()
'''
pass
def getNodeName():
'''public String getNodeName()
'''
pass
def getProcessName():
'''public String getProcessName()
'''
pass
def getServerType():
'''public String getServerType()
'''
pass
def getCellType():
'''public String getCellType()
'''
pass
def isCellRegistered():
'''public boolean isCellRegistered()
'''
pass
def isAlive():
'''public Session isAlive()
public Session isAlive(final int timeout)
'''
pass
def getJvmType():
'''public String getJvmType()
'''
pass
def instantiate():
'''public Object instantiate(final String className)
public Object instantiate(final String className, final ObjectName loaderName)
public Object instantiate(final String className, final Object[] args, final String[] parameters)
public Object instantiate(final String className, final ObjectName loaderName, final Object[] args, final String[] parameters)
'''
pass
def createMBean():
'''public ObjectInstance createMBean(final String className, final ObjectName name)
public ObjectInstance createMBean(final String className, final ObjectName name, final ObjectName loaderName)
public ObjectInstance createMBean(final String className, final ObjectName name, final Object[] params, final String[] signature)
public ObjectInstance createMBean(final String className, final ObjectName name, final ObjectName loaderName, final Object[] params, final String[] signature)
'''
pass
def registerMBean():
'''public ObjectInstance registerMBean(final Object object, final ObjectName name)
'''
pass
def getDomainName():
'''public String getDomainName()
'''
pass
def unregisterMBean():
'''public void unregisterMBean(final ObjectName name)
'''
pass
def queryMBeans():
'''public Set queryMBeans(final ObjectName name, final QueryExp query)
'''
pass
def queryNames():
'''public Set queryNames(final ObjectName name, final QueryExp query)
'''
pass
def isRegistered():
'''public boolean isRegistered(final ObjectName name)
'''
pass
def getMBeanCount():
'''public Integer getMBeanCount()
'''
pass
def getAttribute():
'''public Object getAttribute(ObjectName name, final String attribute)
'''
pass
def getAttributes():
'''public AttributeList getAttributes(ObjectName name, final String[] attributes)
'''
pass
def setAttribute():
'''public void setAttribute(ObjectName name, final Attribute attribute)
'''
pass
def setAttributes():
'''public AttributeList setAttributes(ObjectName name, final AttributeList attributes)
'''
pass
def invoke():
'''public Object invoke(final ObjectName origName, final String operationName, final Object[] params, final String[] signature)
'''
pass
def run():
'''public Object run()
public Object run()
public Object run()
'''
pass
def getDefaultDomain():
'''public String getDefaultDomain()
'''
pass
def getMBeanInfo():
'''public MBeanInfo getMBeanInfo(ObjectName name)
'''
pass
def isInstanceOf():
'''public boolean isInstanceOf(ObjectName name, final String className)
'''
pass
def addNotificationListener():
'''public void addNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)
public ListenerIdentifier addNotificationListener(final ConsolidatedFilter filter, final PushNotificationListener listener)
public void addNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)
'''
pass
def addNotificationListenerExtended():
'''public void addNotificationListenerExtended(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)
'''
pass
def removeNotificationListener():
'''public void removeNotificationListener(final ObjectName name, final NotificationListener listener)
public void removeNotificationListener(final ListenerIdentifier listenerId)
public void removeNotificationListener(final ObjectName name, final ObjectName listener)
public void removeNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)
public void removeNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)
'''
pass
def removeNotificationListenerExtended():
'''public void removeNotificationListenerExtended(final ObjectName name, final NotificationListener listener)
public void removeNotificationListenerExtended(final NotificationListener listener)
'''
pass
def initializeNotificationService():
'''public void initializeNotificationService()
'''
pass
def getNotificationService():
'''public NotificationService getNotificationService()
'''
pass
def resetFilter():
'''public void resetFilter(final ListenerIdentifier listenerId, final ConsolidatedFilter filter)
'''
pass
def pullNotifications():
'''public Notification[] pullNotifications(final ListenerIdentifier id, final Integer batchSize)
'''
pass
def getProcessType():
'''public String getProcessType()
'''
pass
def setProcessType():
'''public void setProcessType(final String type)
'''
pass
def getServerMBean():
'''public ObjectName getServerMBean()
'''
pass
def getLocalServer():
'''public ObjectName getLocalServer()
'''
pass
def setLocalServer():
'''public void setLocalServer(final ObjectName svrBean)
'''
pass
def isLocalServer():
'''public boolean isLocalServer(final String cellname, final String nodename, final String servername)
'''
pass
def getDeploymentManagerAdminClient():
'''public AdminClient getDeploymentManagerAdminClient()
'''
pass
def getPlatformUtils():
'''public static PlatformUtils getPlatformUtils()
'''
pass
def zOSInitComplete():
'''public void zOSInitComplete()
'''
pass
def isZOSInitComplete():
'''public boolean isZOSInitComplete()
'''
pass
def transformConfigId():
'''public String transformConfigId(final String old)
'''
pass
def reverseTransformConfigId():
'''public String reverseTransformConfigId(final String old)
'''
pass
def getClassLoaderFor():
'''public ClassLoader getClassLoaderFor(final ObjectName name)
'''
pass
def getClassLoader():
'''public ClassLoader getClassLoader(final ObjectName name)
'''
pass
def getClassLoaderRepository():
'''public ClassLoaderRepository getClassLoaderRepository()
'''
pass
def getDomains():
'''public String[] getDomains()
'''
pass
def getObjectInstance():
'''public ObjectInstance getObjectInstance(final ObjectName name)
'''
pass
def checkAdminContext():
'''public void checkAdminContext()
'''
pass
def mbeanFilter():
'''public static boolean mbeanFilter(final ObjectName name, final ArrayList mbeanProps)
'''
pass
