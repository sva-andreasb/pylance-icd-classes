def getInstanceFor():
'''public static synchronized MessageEventManager getInstanceFor(final XMPPConnection connection)
'''
pass
def processStanza():
'''public void processStanza(final Stanza packet)
'''
pass
def addNotificationsRequests():
'''public static void addNotificationsRequests(final Message message, final boolean offline, final boolean delivered, final boolean displayed, final boolean composing)
'''
pass
def addMessageEventRequestListener():
'''public void addMessageEventRequestListener(final MessageEventRequestListener messageEventRequestListener)
'''
pass
def removeMessageEventRequestListener():
'''public void removeMessageEventRequestListener(final MessageEventRequestListener messageEventRequestListener)
'''
pass
def addMessageEventNotificationListener():
'''public void addMessageEventNotificationListener(final MessageEventNotificationListener messageEventNotificationListener)
'''
pass
def removeMessageEventNotificationListener():
'''public void removeMessageEventNotificationListener(final MessageEventNotificationListener messageEventNotificationListener)
'''
pass
def sendDeliveredNotification():
'''public void sendDeliveredNotification(final Jid to, final String packetID)
'''
pass
def sendDisplayedNotification():
'''public void sendDisplayedNotification(final Jid to, final String packetID)
'''
pass
def sendComposingNotification():
'''public void sendComposingNotification(final Jid to, final String packetID)
'''
pass
def sendCancelledNotification():
'''public void sendCancelledNotification(final Jid to, final String packetID)
'''
pass
