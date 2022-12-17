def ():
    '''returns ControlNotificationHandler\n\n
    (final MBeanServer mbeanServer)\n
    (final Notification[] newNotifArray, final PushNotificationListener newListener)\n
    '''
def addNotificationListener():
    '''returns ListenerIdentifier\n\n
    addNotificationListener(final ConsolidatedFilter filter, final PushNotificationListener listener)\n
    '''
def addListener():
    '''returns boolean\n\n
    addListener(final WsNotifListener listener)\n
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
def handleRemoteNotification():
    '''returns None\n\n
    handleRemoteNotification(final Notification event)\n
    '''
def addControlNotificationListener():
    '''returns ListenerIdentifier\n\n
    addControlNotificationListener(final ConsolidatedFilter filter, final PushNotificationListener listener)\n
    '''
def removeNotificationListener():
    '''returns None\n\n
    removeNotificationListener(final ListenerIdentifier listenerId)\n
    '''
def resetFilter():
    '''returns None\n\n
    resetFilter(final ListenerIdentifier listenerId, final ConsolidatedFilter filter)\n
    '''
def pullNotifications():
    '''returns Notification[]\n\n
    pullNotifications(final ListenerIdentifier id, final Integer batchSize)\n
    '''
def stopUpstreamServerSending():
    '''returns None\n\n
    stopUpstreamServerSending()\n
    '''
def restartUpstreamServerSending():
    '''returns None\n\n
    restartUpstreamServerSending()\n
    '''
def getDownstreamProcessManager():
    '''returns DownstreamProcessManager\n\n
    getDownstreamProcessManager()\n
    '''
def getDownstreamServerManager():
    '''returns DownstreamServerManager\n\n
    getDownstreamServerManager()\n
    '''
def getServantProcessManager():
    '''returns DownstreamProcessManager\n\n
    getServantProcessManager()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    run()\n
    run()\n
    '''
