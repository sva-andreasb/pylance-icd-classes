def ControlAdminServiceImpl():
'''public ControlAdminServiceImpl(final MBeanFactory localMBeanFactory)
'''
pass
def getInstance():
'''public static ControlAdminServiceImpl getInstance()
'''
pass
def currentAdjuncts():
'''public Set currentAdjuncts()
'''
pass
def currentServants():
'''public Set currentServants()
'''
pass
def currentWLMServants():
'''public Set currentWLMServants()
'''
pass
def activateProxyMBean():
'''public Serializable activateProxyMBean(final String type, final String configId, final String descriptor, final Properties keyProperties, final String stoken, final ObjectName objName, final byte[] descriptorBytes)
public Serializable activateProxyMBean(final ModelMBeanInfo info, final ObjectName objName, final String stoken)
public ObjectName activateProxyMBean(final String type, final String configId, final String descriptor, final Properties keyProperties, final String stoken, final ObjectName objName)
'''
pass
def removeListener():
'''public void removeListener(final ObjectName proxyObjectName)
'''
pass
def deactivateProxyMBean():
'''public void deactivateProxyMBean(final ObjectName objName, final String stoken)
'''
pass
def cleanupAdjunctJVM():
'''public void cleanupAdjunctJVM(final String stoken)
'''
pass
def cleanupServantJVM():
'''public void cleanupServantJVM(final String stoken)
'''
pass
def startupAdjunctJVM():
'''public void startupAdjunctJVM(final String stoken)
'''
pass
def startupServantJVM():
'''public void startupServantJVM(final String stoken)
'''
pass
def servantWLMQueueable():
'''public void servantWLMQueueable(final String stoken)
'''
pass
def remoteListenerAdded():
'''public void remoteListenerAdded(final ObjectName name)
'''
pass
def remoteListenerRemoved():
'''public void remoteListenerRemoved(final ObjectName name)
'''
pass
def handleServantNotifications():
'''public void handleServantNotifications(final Notification[] notifications)
'''
pass
def getControllerStringIOR():
'''public synchronized String getControllerStringIOR()
'''
pass
