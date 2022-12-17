def ():
    '''returns ControlAdminServiceImpl\n\n
    (final MBeanFactory localMBeanFactory)\n
    '''
def currentAdjuncts():
    '''returns Set\n\n
    currentAdjuncts()\n
    '''
def currentServants():
    '''returns Set\n\n
    currentServants()\n
    '''
def currentWLMServants():
    '''returns Set\n\n
    currentWLMServants()\n
    '''
def activateProxyMBean():
    '''returns ObjectName\n\n
    activateProxyMBean(final String type, final String configId, final String descriptor, final Properties keyProperties, final String stoken, final ObjectName objName, final byte[] descriptorBytes)\n
    activateProxyMBean(final ModelMBeanInfo info, final ObjectName objName, final String stoken)\n
    activateProxyMBean(final String type, final String configId, final String descriptor, final Properties keyProperties, final String stoken, final ObjectName objName)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final ObjectName proxyObjectName)\n
    '''
def deactivateProxyMBean():
    '''returns None\n\n
    deactivateProxyMBean(final ObjectName objName, final String stoken)\n
    '''
def cleanupAdjunctJVM():
    '''returns None\n\n
    cleanupAdjunctJVM(final String stoken)\n
    '''
def cleanupServantJVM():
    '''returns None\n\n
    cleanupServantJVM(final String stoken)\n
    '''
def startupAdjunctJVM():
    '''returns None\n\n
    startupAdjunctJVM(final String stoken)\n
    '''
def startupServantJVM():
    '''returns None\n\n
    startupServantJVM(final String stoken)\n
    '''
def servantWLMQueueable():
    '''returns None\n\n
    servantWLMQueueable(final String stoken)\n
    '''
def remoteListenerAdded():
    '''returns None\n\n
    remoteListenerAdded(final ObjectName name)\n
    '''
def remoteListenerRemoved():
    '''returns None\n\n
    remoteListenerRemoved(final ObjectName name)\n
    '''
def handleServantNotifications():
    '''returns None\n\n
    handleServantNotifications(final Notification[] notifications)\n
    '''
