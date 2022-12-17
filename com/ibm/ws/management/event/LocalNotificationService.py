TIME_TO_WAIT_FOR_LISTENER = "long  60000L"
def ():
    '''returns LocalNotificationService\n\n
    ()\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    '''
def addNotificationListener():
    '''returns None\n\n
    addNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    '''
def addNotificationListenerExtended():
    '''returns None\n\n
    addNotificationListenerExtended(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    '''
def addListener():
    '''returns boolean\n\n
    addListener(final WsNotifListener listener)\n
    '''
def removeNotificationListener():
    '''returns None\n\n
    removeNotificationListener(final ObjectName name, final NotificationListener listener)\n
    removeNotificationListener(final ObjectName name, final NotificationListener listener, final NotificationFilter filter, final Object handback)\n
    '''
def removeNotificationListenerExtended():
    '''returns None\n\n
    removeNotificationListenerExtended(final ObjectName name, final NotificationListener listener)\n
    '''
def removeListener():
    '''returns boolean\n\n
    removeListener(final WsNotifListener listener)\n
    '''
def isNotificationEnabled():
    '''returns boolean\n\n
    isNotificationEnabled(final Notification n)\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final Notification event)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
