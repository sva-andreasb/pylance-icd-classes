def handlePushNotificationAccepted():
    '''returns None\n\n
    handlePushNotificationAccepted(final Http2Headers headers, final ByteBuf payload)\n
    '''
def handlePushNotificationRejected():
    '''returns None\n\n
    handlePushNotificationRejected(final Http2Headers headers, final ByteBuf payload, final RejectionReason rejectionReason, final Instant deviceTokenExpirationTimestamp)\n
    '''
def getToken():
    '''returns String\n\n
    getToken()\n
    '''
def getPayload():
    '''returns String\n\n
    getPayload()\n
    '''
def getExpiration():
    '''returns Instant\n\n
    getExpiration()\n
    '''
def getPriority():
    '''returns DeliveryPriority\n\n
    getPriority()\n
    '''
def getPushType():
    '''returns PushType\n\n
    getPushType()\n
    '''
def getTopic():
    '''returns String\n\n
    getTopic()\n
    '''
def getCollapseId():
    '''returns String\n\n
    getCollapseId()\n
    '''
def getApnsId():
    '''returns UUID\n\n
    getApnsId()\n
    '''
