def AdminClientImpl():
'''public AdminClientImpl(final InvocationHandler handler)
public AdminClientImpl(final AdminServiceProxy proxy)
'''
pass
def getType():
'''public String getType()
'''
pass
def getConnectorProperties():
'''public Properties getConnectorProperties()
'''
pass
def isAlive():
'''public Session isAlive()
public Session isAlive(final int timeout)
'''
pass
def queryNames():
'''public Set queryNames(final ObjectName name, final QueryExp query)
'''
pass
def getMBeanCount():
'''public Integer getMBeanCount()
'''
pass
def getDomainName():
'''public String getDomainName()
'''
pass
def getDefaultDomain():
'''public String getDefaultDomain()
'''
pass
def getServerMBean():
'''public ObjectName getServerMBean()
'''
pass
def getMBeanInfo():
'''public MBeanInfo getMBeanInfo(final ObjectName name)
'''
pass
def isInstanceOf():
'''public boolean isInstanceOf(final ObjectName name, final String className)
'''
pass
def isRegistered():
'''public boolean isRegistered(final ObjectName name)
'''
pass
def getAttribute():
'''public Object getAttribute(final ObjectName name, final String attribute)
'''
pass
def getAttributes():
'''public AttributeList getAttributes(final ObjectName name, final String[] attributes)
'''
pass
def setAttribute():
'''public void setAttribute(final ObjectName name, final Attribute attribute)
'''
pass
def setAttributes():
'''public AttributeList setAttributes(final ObjectName name, final AttributeList attributes)
'''
pass
def invoke():
'''public Object invoke(final ObjectName name, final String operationName, final Object[] params, final String[] signature)
'''
pass
def addNotificationListener():
'''public void addNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)
public void addNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)
'''
pass
def addNotificationListenerExtended():
'''public void addNotificationListenerExtended(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)
'''
pass
def removeNotificationListener():
'''public void removeNotificationListener(final ObjectName name, final NotificationListener listener)
public void removeNotificationListener(final ObjectName name, final ObjectName listener)
public void removeNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)
'''
pass
def removeNotificationListenerExtended():
'''public void removeNotificationListenerExtended(final ObjectName name, final NotificationListener listener)
public void removeNotificationListenerExtended(final NotificationListener listener)
'''
pass
def getProxy():
'''public AdminServiceProxy getProxy()
'''
pass
def queryMBeans():
'''public Set queryMBeans(final ObjectName name, final QueryExp query)
'''
pass
def getObjectInstance():
'''public ObjectInstance getObjectInstance(final ObjectName objectName)
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
