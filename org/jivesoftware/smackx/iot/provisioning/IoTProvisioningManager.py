def getInstanceFor():
    '''    public static synchronized IoTProvisioningManager getInstanceFor(final XMPPConnection connection)
    '''
def processStanza():
    '''    public void processStanza(final Stanza stanza)
    public void processStanza(final Stanza stanza)
    '''
def handleIQRequest():
    '''    public IQ handleIQRequest(final IQ iqRequest)
    '''
def presenceSubscribed():
    '''    public void presenceSubscribed(final BareJid address, final Presence subscribedPresence)
    '''
def presenceUnsubscribed():
    '''    public void presenceUnsubscribed(final BareJid address, final Presence unsubscribedPresence)
    '''
def setConfiguredProvisioningServer():
    '''    public void setConfiguredProvisioningServer(final Jid provisioningServer)
    '''
def getConfiguredProvisioningServer():
    '''    public Jid getConfiguredProvisioningServer()
    '''
def findProvisioningServerComponent():
    '''    public DomainBareJid findProvisioningServerComponent()
    '''
def isFriend():
    '''    public boolean isFriend(final Jid provisioningServer, final BareJid friendInQuestion)
    '''
def iAmFriendOf():
    '''    public boolean iAmFriendOf(final BareJid otherJid)
    '''
def sendFriendshipRequest():
    '''    public void sendFriendshipRequest(final BareJid bareJid)
    '''
def sendFriendshipRequestIfRequired():
    '''    public void sendFriendshipRequestIfRequired(final BareJid jid)
    '''
def isMyFriend():
    '''    public boolean isMyFriend(final Jid friendInQuestion)
    '''
def unfriend():
    '''    public void unfriend(final Jid friend)
    '''
def addBecameFriendListener():
    '''    public boolean addBecameFriendListener(final BecameFriendListener becameFriendListener)
    '''
def removeBecameFriendListener():
    '''    public boolean removeBecameFriendListener(final BecameFriendListener becameFriendListener)
    '''
def addWasUnfriendedListener():
    '''    public boolean addWasUnfriendedListener(final WasUnfriendedListener wasUnfriendedListener)
    '''
def removeWasUnfriendedListener():
    '''    public boolean removeWasUnfriendedListener(final WasUnfriendedListener wasUnfriendedListener)
    '''
def connectionCreated():
    '''    public void connectionCreated(final XMPPConnection connection)
    '''
