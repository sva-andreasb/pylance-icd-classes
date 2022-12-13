def SimpleApnsPushNotification():
    '''public SimpleApnsPushNotification(final String token, final String topic, final String payload)
    public SimpleApnsPushNotification(final String token, final String topic, final String payload, final Instant invalidationTime)
    public SimpleApnsPushNotification(final String token, final String topic, final String payload, final Instant invalidationTime, final DeliveryPriority priority)
    public SimpleApnsPushNotification(final String token, final String topic, final String payload, final Instant invalidationTime, final DeliveryPriority priority, final PushType pushType)
    public SimpleApnsPushNotification(final String token, final String topic, final String payload, final Instant invalidationTime, final DeliveryPriority priority, final String collapseId)
    public SimpleApnsPushNotification(final String token, final String topic, final String payload, final Instant invalidationTime, final DeliveryPriority priority, final PushType pushType, final String collapseId)
    public SimpleApnsPushNotification(final String token, final String topic, final String payload, final Instant invalidationTime, final DeliveryPriority priority, final String collapseId, final UUID apnsId)
    public SimpleApnsPushNotification(final String token, final String topic, final String payload, final Instant invalidationTime, final DeliveryPriority priority, final PushType pushType, final String collapseId, final UUID apnsId)
    '''
def getToken():
    '''public String getToken()
    '''
def getPayload():
    '''public String getPayload()
    '''
def getExpiration():
    '''public Instant getExpiration()
    '''
def getPriority():
    '''public DeliveryPriority getPriority()
    '''
def getPushType():
    '''public PushType getPushType()
    '''
def getTopic():
    '''public String getTopic()
    '''
def getCollapseId():
    '''public String getCollapseId()
    '''
def getApnsId():
    '''public UUID getApnsId()
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def toString():
    '''public String toString()
    '''
