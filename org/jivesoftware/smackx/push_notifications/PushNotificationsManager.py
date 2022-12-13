def getInstanceFor():
    '''public static synchronized PushNotificationsManager getInstanceFor(final XMPPConnection connection)
    '''
def isSupported():
    '''public boolean isSupported()
    '''
def enable():
    '''public boolean enable(final Jid pushJid, final String node)
    public boolean enable(final Jid pushJid, final String node, final HashMap<String, String> publishOptions)
    '''
def disableAll():
    '''public boolean disableAll(final Jid pushJid)
    '''
def disable():
    '''public boolean disable(final Jid pushJid, final String node)
    '''
def connectionCreated():
    '''public void connectionCreated(final XMPPConnection connection)
    '''
