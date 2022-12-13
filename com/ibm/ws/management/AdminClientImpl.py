def AdminClientImpl():
    '''public AdminClientImpl(final InvocationHandler handler)
    public AdminClientImpl(final AdminServiceProxy proxy)
    '''
def getType():
    '''public String getType()
    '''
def getConnectorProperties():
    '''public Properties getConnectorProperties()
    '''
def isAlive():
    '''public Session isAlive()
    public Session isAlive(final int timeout)
    '''
def queryNames():
    '''public Set queryNames(final ObjectName name, final QueryExp query)
    '''
def getMBeanCount():
    '''public Integer getMBeanCount()
    '''
def getDomainName():
    '''public String getDomainName()
    '''
def getDefaultDomain():
    '''public String getDefaultDomain()
    '''
def getServerMBean():
    '''public ObjectName getServerMBean()
    '''
def getMBeanInfo():
    '''public MBeanInfo getMBeanInfo(final ObjectName name)
    '''
def isInstanceOf():
    '''public boolean isInstanceOf(final ObjectName name, final String className)
    '''
def isRegistered():
    '''public boolean isRegistered(final ObjectName name)
    '''
def getAttribute():
    '''public Object getAttribute(final ObjectName name, final String attribute)
    '''
def getAttributes():
    '''public AttributeList getAttributes(final ObjectName name, final String[] attributes)
    '''
def setAttribute():
    '''public void setAttribute(final ObjectName name, final Attribute attribute)
    '''
def setAttributes():
    '''public AttributeList setAttributes(final ObjectName name, final AttributeList attributes)
    '''
def invoke():
    '''public Object invoke(final ObjectName name, final String operationName, final Object[] params, final String[] signature)
    '''
def addNotificationListener():
    '''public void addNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)
    public void addNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)
    '''
def addNotificationListenerExtended():
    '''public void addNotificationListenerExtended(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)
    '''
def removeNotificationListener():
    '''public void removeNotificationListener(final ObjectName name, final NotificationListener listener)
    public void removeNotificationListener(final ObjectName name, final ObjectName listener)
    public void removeNotificationListener(final ObjectName name, final ObjectName listener, final NotificationFilter filter, final Object handback)
    '''
def removeNotificationListenerExtended():
    '''public void removeNotificationListenerExtended(final ObjectName name, final NotificationListener listener)
    public void removeNotificationListenerExtended(final NotificationListener listener)
    '''
def getProxy():
    '''public AdminServiceProxy getProxy()
    '''
def queryMBeans():
    '''public Set queryMBeans(final ObjectName name, final QueryExp query)
    '''
def getObjectInstance():
    '''public ObjectInstance getObjectInstance(final ObjectName objectName)
    '''
def getClassLoaderFor():
    '''public ClassLoader getClassLoaderFor(final ObjectName name)
    '''
def getClassLoader():
    '''public ClassLoader getClassLoader(final ObjectName name)
    '''
