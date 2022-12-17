PUSHNOTF_LOGGER = "String  \"maximo.pushnotification\""
MESSAGE_KEY = "String  \"message\""
def ():
    '''returns IBMPushNotfHandler\n\n
    (final NotificationMessage notificationMessage)\n
    ()\n
    '''
def setProviderCredentials():
    '''returns None\n\n
    setProviderCredentials(final String deviceType, final String clientSecret, final String appGUID, final String authURL, final String endpointUrl, final String apiKey)\n
    '''
def invoke():
    '''returns byte[]\n\n
    invoke(final Map metaData, byte[] data)\n
    '''
def getHandlerURL():
    '''returns String\n\n
    getHandlerURL()\n
    '''
def getAuthURL():
    '''returns String\n\n
    getAuthURL()\n
    '''
def getHeaders():
    '''returns Map\n\n
    getHeaders()\n
    '''
def getIBMNotificationMessage():
    '''returns IBMNotificationMessage\n\n
    getIBMNotificationMessage()\n
    '''
def setMessagePayload():
    '''returns None\n\n
    setMessagePayload()\n
    '''
def getMessagePayload():
    '''returns byte[]\n\n
    getMessagePayload()\n
    '''
def getProperties():
    '''returns List<RouterPropsInfo>\n\n
    getProperties()\n
    '''
