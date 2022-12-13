def ControlAdminServiceImpl():
    '''    public ControlAdminServiceImpl(final MBeanFactory localMBeanFactory)
    '''
def getInstance():
    '''    public static ControlAdminServiceImpl getInstance()
    '''
def currentAdjuncts():
    '''    public Set currentAdjuncts()
    '''
def currentServants():
    '''    public Set currentServants()
    '''
def currentWLMServants():
    '''    public Set currentWLMServants()
    '''
def activateProxyMBean():
    '''    public Serializable activateProxyMBean(final String type, final String configId, final String descriptor, final Properties keyProperties, final String stoken, final ObjectName objName, final byte[] descriptorBytes)
    public Serializable activateProxyMBean(final ModelMBeanInfo info, final ObjectName objName, final String stoken)
    public ObjectName activateProxyMBean(final String type, final String configId, final String descriptor, final Properties keyProperties, final String stoken, final ObjectName objName)
    '''
def removeListener():
    '''    public void removeListener(final ObjectName proxyObjectName)
    '''
def deactivateProxyMBean():
    '''    public void deactivateProxyMBean(final ObjectName objName, final String stoken)
    '''
def cleanupAdjunctJVM():
    '''    public void cleanupAdjunctJVM(final String stoken)
    '''
def cleanupServantJVM():
    '''    public void cleanupServantJVM(final String stoken)
    '''
def startupAdjunctJVM():
    '''    public void startupAdjunctJVM(final String stoken)
    '''
def startupServantJVM():
    '''    public void startupServantJVM(final String stoken)
    '''
def servantWLMQueueable():
    '''    public void servantWLMQueueable(final String stoken)
    '''
def remoteListenerAdded():
    '''    public void remoteListenerAdded(final ObjectName name)
    '''
def remoteListenerRemoved():
    '''    public void remoteListenerRemoved(final ObjectName name)
    '''
def handleServantNotifications():
    '''    public void handleServantNotifications(final Notification[] notifications)
    '''
def getControllerStringIOR():
    '''    public synchronized String getControllerStringIOR()
    '''
