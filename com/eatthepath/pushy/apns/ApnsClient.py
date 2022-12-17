def handleConnectionAdded():
    '''returns None\n\n
    handleConnectionAdded()\n
    handleConnectionAdded(final ApnsClient apnsClient)\n
    '''
def handleConnectionRemoved():
    '''returns None\n\n
    handleConnectionRemoved()\n
    handleConnectionRemoved(final ApnsClient apnsClient)\n
    '''
def handleConnectionCreationFailed():
    '''returns None\n\n
    handleConnectionCreationFailed()\n
    handleConnectionCreationFailed(final ApnsClient apnsClient)\n
    '''
def close():
    '''returns CompletableFuture<Void>\n\n
    close()\n
    '''
def handleWriteFailure():
    '''returns None\n\n
    handleWriteFailure(final ApnsClient apnsClient, final long notificationId)\n
    '''
def handleNotificationSent():
    '''returns None\n\n
    handleNotificationSent(final ApnsClient apnsClient, final long notificationId)\n
    '''
def handleNotificationAccepted():
    '''returns None\n\n
    handleNotificationAccepted(final ApnsClient apnsClient, final long notificationId)\n
    '''
def handleNotificationRejected():
    '''returns None\n\n
    handleNotificationRejected(final ApnsClient apnsClient, final long notificationId)\n
    '''
