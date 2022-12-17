def ():
    '''returns RequiredModelMBean\n\n
    ()\n
    (final ModelMBeanInfo modelMBeanInfo)\n
    '''
def load():
    '''returns None\n\n
    load()\n
    '''
def postDeregister():
    '''returns None\n\n
    postDeregister()\n
    '''
def preDeregister():
    '''returns None\n\n
    preDeregister()\n
    '''
def store():
    '''returns None\n\n
    store()\n
    '''
def postRegister():
    '''returns None\n\n
    postRegister(final Boolean b)\n
    '''
def sendNotification():
    '''returns None\n\n
    sendNotification(final String s)\n
    sendNotification(final Notification notification)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final Attribute attribute)\n
    '''
def sendAttributeChangeNotification():
    '''returns None\n\n
    sendAttributeChangeNotification(final AttributeChangeNotification attributeChangeNotification)\n
    sendAttributeChangeNotification(final Attribute attribute, final Attribute attribute2)\n
    '''
def getMBeanInfo():
    '''returns MBeanInfo\n\n
    getMBeanInfo()\n
    '''
def getNotificationInfo():
    '''returns MBeanNotificationInfo[]\n\n
    getNotificationInfo()\n
    '''
def removeNotificationListener():
    '''returns None\n\n
    removeNotificationListener(final NotificationListener notificationListener)\n
    removeNotificationListener(final NotificationListener notificationListener, final NotificationFilter notificationFilter, final Object o)\n
    '''
def setModelMBeanInfo():
    '''returns None\n\n
    setModelMBeanInfo(final ModelMBeanInfo modelMBeanInfo)\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final String str)\n
    '''
def setManagedResource():
    '''returns None\n\n
    setManagedResource(final Object managedResource, final String str)\n
    '''
def removeAttributeChangeNotificationListener():
    '''returns None\n\n
    removeAttributeChangeNotificationListener(final NotificationListener notificationListener, final String anObject)\n
    '''
def getAttributes():
    '''returns AttributeList\n\n
    getAttributes(final String[] array)\n
    '''
def setAttributes():
    '''returns AttributeList\n\n
    setAttributes(final AttributeList list)\n
    '''
def addAttributeChangeNotificationListener():
    '''returns None\n\n
    addAttributeChangeNotificationListener(final NotificationListener notificationListener, final String str, final Object o)\n
    '''
def addNotificationListener():
    '''returns None\n\n
    addNotificationListener(final NotificationListener notificationListener, final NotificationFilter notificationFilter, final Object o)\n
    '''
def preRegister():
    '''returns ObjectName\n\n
    preRegister(final MBeanServer server, final ObjectName objectName)\n
    '''
def invoke():
    '''returns Object\n\n
    invoke(final String s, final Object[] array, final String[] array2)\n
    '''
