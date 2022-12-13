PUSHNOTF_LOGGER = "String  maximo.pushnotification""
def PushNotificationService():
'''public PushNotificationService()
public PushNotificationService(final MXServer mxServer)
'''
pass
def sendMessage():
'''public void sendMessage(final UserInfo userInfo, final String msg)
public void sendMessage(final UserInfo userInfo, final NotificationMessage notificationMessage)
public void sendMessage(final UserInfo userInfo, final NotificationMessage notificationMessage, final String eventName)
public void sendMessage(final UserInfo userInfo, final NotificationMessage notificationMessage, final String eventName, final String projectName)
'''
pass
def sendMessageforUserId():
'''public void sendMessageforUserId(final UserInfo userInfo, final String notifMessageJsonStr, final String msgRecevingUserId, final String notifMessage, final String eventName, final String projectName)
public void sendMessageforUserId(final UserInfo userInfo, String msgRecevingUserId, final NotificationMessage notificationMessage, final String eventName, final String projectName)
'''
pass
def getProviderDevTypeSet():
'''public MboSetRemote getProviderDevTypeSet(final UserInfo userInfo, final String deviceType, final String projectName)
'''
pass
def getProviderMbo():
'''public MboRemote getProviderMbo()
'''
pass
def getProviderName():
'''public String getProviderName()
'''
pass
def getNotificationMessage():
'''public NotificationMessage getNotificationMessage(final String msg, final String deviceId)
public NotificationMessage getNotificationMessage(final NotificationMessage notificationMessage, final String deviceId)
'''
pass
def getRouterHandler():
'''public BaseRouterHandler getRouterHandler()
'''
pass
def setProviderName():
'''public void setProviderName(final String providername)
'''
pass
