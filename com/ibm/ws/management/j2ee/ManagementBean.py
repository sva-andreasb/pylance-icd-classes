def ejbCreate():
    '''returns None\n\n
    ejbCreate()\n
    '''
def setSessionContext():
    '''returns None\n\n
    setSessionContext(final SessionContext ctx)\n
    '''
def ejbRemove():
    '''returns None\n\n
    ejbRemove()\n
    '''
def ejbActivate():
    '''returns None\n\n
    ejbActivate()\n
    '''
def ejbPassivate():
    '''returns None\n\n
    ejbPassivate()\n
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
def getMBeanInfo():
    '''returns MBeanInfo\n\n
    getMBeanInfo(final ObjectName name)\n
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
def getListenerRegistry():
    '''returns ListenerRegistration\n\n
    getListenerRegistry()\n
    '''
def addNotificationListener():
    '''returns None\n\n
    addNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    '''
def removeNotificationListener():
    '''returns None\n\n
    removeNotificationListener(final ObjectName name, final NotificationListener listener)\n
    '''
