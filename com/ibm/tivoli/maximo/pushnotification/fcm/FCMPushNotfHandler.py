PUSHNOTF_LOGGER = "String  \"maximo.pushnotification\""
FCMPUSHNOTF_REGISTRATIONTOKEN = "String  \"REGISTRATIONTOKEN\""
MESSAGE_KEY = "String  \"message\""
def ():
    '''returns FCMPushNotfHandler\n\n
    ()\n
    (final NotificationMessage notificationMessage)\n
    '''
def getProperties():
    '''returns List<RouterPropsInfo>\n\n
    getProperties()\n
    '''
def setProviderCredentials():
    '''returns None\n\n
    setProviderCredentials(final String deviceType, final String serviceAcctJson, final String projectId, final String endPointUrl, final String projectUri, final String messageUri, final String messagingScope)\n
    '''
def invoke():
    '''returns byte[]\n\n
    invoke(final Map metaData, byte[] data)\n
    '''
def getHandlerURL():
    '''returns String\n\n
    getHandlerURL()\n
    '''
def getHeaders():
    '''returns Map\n\n
    getHeaders(final String serviceacctjson)\n
    '''
def getFCMNotificationMessage():
    '''returns JSONObject\n\n
    getFCMNotificationMessage()\n
    '''
def getFCMDataMessage():
    '''returns JSONObject\n\n
    getFCMDataMessage()\n
    '''
