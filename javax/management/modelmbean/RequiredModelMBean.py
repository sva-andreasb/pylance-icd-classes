def RequiredModelMBean():
    '''    public RequiredModelMBean()
    public RequiredModelMBean(final ModelMBeanInfo modelMBeanInfo)
    '''
def load():
    '''    public void load()
    '''
def postDeregister():
    '''    public void postDeregister()
    '''
def preDeregister():
    '''    public void preDeregister()
    '''
def store():
    '''    public void store()
    '''
def postRegister():
    '''    public void postRegister(final Boolean b)
    '''
def sendNotification():
    '''    public void sendNotification(final String s)
    public void sendNotification(final Notification notification)
    '''
def setAttribute():
    '''    public void setAttribute(final Attribute attribute)
    '''
def sendAttributeChangeNotification():
    '''    public void sendAttributeChangeNotification(final AttributeChangeNotification attributeChangeNotification)
    public void sendAttributeChangeNotification(final Attribute attribute, final Attribute attribute2)
    '''
def getMBeanInfo():
    '''    public MBeanInfo getMBeanInfo()
    '''
def getNotificationInfo():
    '''    public MBeanNotificationInfo[] getNotificationInfo()
    '''
def removeNotificationListener():
    '''    public void removeNotificationListener(final NotificationListener notificationListener)
    public void removeNotificationListener(final NotificationListener notificationListener, final NotificationFilter notificationFilter, final Object o)
    '''
def setModelMBeanInfo():
    '''    public void setModelMBeanInfo(final ModelMBeanInfo modelMBeanInfo)
    '''
def getAttribute():
    '''    public Object getAttribute(final String str)
    '''
def setManagedResource():
    '''    public void setManagedResource(final Object managedResource, final String str)
    '''
def removeAttributeChangeNotificationListener():
    '''    public void removeAttributeChangeNotificationListener(final NotificationListener notificationListener, final String anObject)
    '''
def getAttributes():
    '''    public AttributeList getAttributes(final String[] array)
    '''
def setAttributes():
    '''    public AttributeList setAttributes(final AttributeList list)
    '''
def addAttributeChangeNotificationListener():
    '''    public void addAttributeChangeNotificationListener(final NotificationListener notificationListener, final String str, final Object o)
    '''
def addNotificationListener():
    '''    public void addNotificationListener(final NotificationListener notificationListener, final NotificationFilter notificationFilter, final Object o)
    '''
def preRegister():
    '''    public ObjectName preRegister(final MBeanServer server, final ObjectName objectName)
    '''
def invoke():
    '''    public Object invoke(final String s, final Object[] array, final String[] array2)
    '''
