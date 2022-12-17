def ():
    '''returns SimpleApnsPushNotification\n\n
    (final String token, final String topic, final String payload)\n
    (final String token, final String topic, final String payload, final Instant invalidationTime)\n
    (final String token, final String topic, final String payload, final Instant invalidationTime, final DeliveryPriority priority)\n
    (final String token, final String topic, final String payload, final Instant invalidationTime, final DeliveryPriority priority, final PushType pushType)\n
    (final String token, final String topic, final String payload, final Instant invalidationTime, final DeliveryPriority priority, final String collapseId)\n
    (final String token, final String topic, final String payload, final Instant invalidationTime, final DeliveryPriority priority, final PushType pushType, final String collapseId)\n
    (final String token, final String topic, final String payload, final Instant invalidationTime, final DeliveryPriority priority, final String collapseId, final UUID apnsId)\n
    (final String token, final String topic, final String payload, final Instant invalidationTime, final DeliveryPriority priority, final PushType pushType, final String collapseId, final UUID apnsId)\n
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
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
