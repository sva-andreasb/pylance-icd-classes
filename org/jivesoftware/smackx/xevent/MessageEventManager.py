def getInstanceFor():
    '''    public static synchronized MessageEventManager getInstanceFor(final XMPPConnection connection)
    '''
def processStanza():
    '''    public void processStanza(final Stanza packet)
    '''
def addNotificationsRequests():
    '''    public static void addNotificationsRequests(final Message message, final boolean offline, final boolean delivered, final boolean displayed, final boolean composing)
    '''
def addMessageEventRequestListener():
    '''    public void addMessageEventRequestListener(final MessageEventRequestListener messageEventRequestListener)
    '''
def removeMessageEventRequestListener():
    '''    public void removeMessageEventRequestListener(final MessageEventRequestListener messageEventRequestListener)
    '''
def addMessageEventNotificationListener():
    '''    public void addMessageEventNotificationListener(final MessageEventNotificationListener messageEventNotificationListener)
    '''
def removeMessageEventNotificationListener():
    '''    public void removeMessageEventNotificationListener(final MessageEventNotificationListener messageEventNotificationListener)
    '''
def sendDeliveredNotification():
    '''    public void sendDeliveredNotification(final Jid to, final String packetID)
    '''
def sendDisplayedNotification():
    '''    public void sendDisplayedNotification(final Jid to, final String packetID)
    '''
def sendComposingNotification():
    '''    public void sendComposingNotification(final Jid to, final String packetID)
    '''
def sendCancelledNotification():
    '''    public void sendCancelledNotification(final Jid to, final String packetID)
    '''
