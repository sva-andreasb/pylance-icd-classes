def handleConnectionAdded():
    '''public void handleConnectionAdded()
    public void handleConnectionAdded(final ApnsClient apnsClient)
    '''
def handleConnectionRemoved():
    '''public void handleConnectionRemoved()
    public void handleConnectionRemoved(final ApnsClient apnsClient)
    '''
def handleConnectionCreationFailed():
    '''public void handleConnectionCreationFailed()
    public void handleConnectionCreationFailed(final ApnsClient apnsClient)
    '''
def sendNotification():
    '''public <T extends ApnsPushNotification> PushNotificationFuture<T, PushNotificationResponse<T>> sendNotification(final T notification)
    '''
def close():
    '''public CompletableFuture<Void> close()
    '''
def handleWriteFailure():
    '''public void handleWriteFailure(final ApnsClient apnsClient, final long notificationId)
    '''
def handleNotificationSent():
    '''public void handleNotificationSent(final ApnsClient apnsClient, final long notificationId)
    '''
def handleNotificationAccepted():
    '''public void handleNotificationAccepted(final ApnsClient apnsClient, final long notificationId)
    '''
def handleNotificationRejected():
    '''public void handleNotificationRejected(final ApnsClient apnsClient, final long notificationId)
    '''
