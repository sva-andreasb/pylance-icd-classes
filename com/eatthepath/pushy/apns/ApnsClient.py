def handleConnectionAdded():
'''public void handleConnectionAdded()
public void handleConnectionAdded(final ApnsClient apnsClient)
'''
pass
def handleConnectionRemoved():
'''public void handleConnectionRemoved()
public void handleConnectionRemoved(final ApnsClient apnsClient)
'''
pass
def handleConnectionCreationFailed():
'''public void handleConnectionCreationFailed()
public void handleConnectionCreationFailed(final ApnsClient apnsClient)
'''
pass
def sendNotification():
'''public <T extends ApnsPushNotification> PushNotificationFuture<T, PushNotificationResponse<T>> sendNotification(final T notification)
'''
pass
def close():
'''public CompletableFuture<Void> close()
'''
pass
def handleWriteFailure():
'''public void handleWriteFailure(final ApnsClient apnsClient, final long notificationId)
'''
pass
def handleNotificationSent():
'''public void handleNotificationSent(final ApnsClient apnsClient, final long notificationId)
'''
pass
def handleNotificationAccepted():
'''public void handleNotificationAccepted(final ApnsClient apnsClient, final long notificationId)
'''
pass
def handleNotificationRejected():
'''public void handleNotificationRejected(final ApnsClient apnsClient, final long notificationId)
'''
pass
