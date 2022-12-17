PUSHNOTF_LOGGER = "String  \"maximo.pushnotification\""
def ():
    '''returns PushNotificationService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final UserInfo userInfo, final String msg)\n
    sendMessage(final UserInfo userInfo, final NotificationMessage notificationMessage)\n
    sendMessage(final UserInfo userInfo, final NotificationMessage notificationMessage, final String eventName)\n
    sendMessage(final UserInfo userInfo, final NotificationMessage notificationMessage, final String eventName, final String projectName)\n
    '''
def sendMessageforUserId():
    '''returns None\n\n
    sendMessageforUserId(final UserInfo userInfo, final String notifMessageJsonStr, final String msgRecevingUserId, final String notifMessage, final String eventName, final String projectName)\n
    sendMessageforUserId(final UserInfo userInfo, String msgRecevingUserId, final NotificationMessage notificationMessage, final String eventName, final String projectName)\n
    '''
def getProviderDevTypeSet():
    '''returns MboSetRemote\n\n
    getProviderDevTypeSet(final UserInfo userInfo, final String deviceType, final String projectName)\n
    '''
def getProviderMbo():
    '''returns MboRemote\n\n
    getProviderMbo()\n
    '''
def getProviderName():
    '''returns String\n\n
    getProviderName()\n
    '''
def getNotificationMessage():
    '''returns NotificationMessage\n\n
    getNotificationMessage(final String msg, final String deviceId)\n
    getNotificationMessage(final NotificationMessage notificationMessage, final String deviceId)\n
    '''
def getRouterHandler():
    '''returns BaseRouterHandler\n\n
    getRouterHandler()\n
    '''
def setProviderName():
    '''returns None\n\n
    setProviderName(final String providername)\n
    '''
