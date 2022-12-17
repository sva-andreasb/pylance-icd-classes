def processStanza():
    '''returns None\n\n
    processStanza(final Stanza stanza)\n
    processStanza(final Stanza stanza)\n
    '''
def handleIQRequest():
    '''returns IQ\n\n
    handleIQRequest(final IQ iqRequest)\n
    '''
def presenceSubscribed():
    '''returns None\n\n
    presenceSubscribed(final BareJid address, final Presence subscribedPresence)\n
    '''
def presenceUnsubscribed():
    '''returns None\n\n
    presenceUnsubscribed(final BareJid address, final Presence unsubscribedPresence)\n
    '''
def setConfiguredProvisioningServer():
    '''returns None\n\n
    setConfiguredProvisioningServer(final Jid provisioningServer)\n
    '''
def getConfiguredProvisioningServer():
    '''returns Jid\n\n
    getConfiguredProvisioningServer()\n
    '''
def findProvisioningServerComponent():
    '''returns DomainBareJid\n\n
    findProvisioningServerComponent()\n
    '''
def isFriend():
    '''returns boolean\n\n
    isFriend(final Jid provisioningServer, final BareJid friendInQuestion)\n
    '''
def iAmFriendOf():
    '''returns boolean\n\n
    iAmFriendOf(final BareJid otherJid)\n
    '''
def sendFriendshipRequest():
    '''returns None\n\n
    sendFriendshipRequest(final BareJid bareJid)\n
    '''
def sendFriendshipRequestIfRequired():
    '''returns None\n\n
    sendFriendshipRequestIfRequired(final BareJid jid)\n
    '''
def isMyFriend():
    '''returns boolean\n\n
    isMyFriend(final Jid friendInQuestion)\n
    '''
def unfriend():
    '''returns None\n\n
    unfriend(final Jid friend)\n
    '''
def addBecameFriendListener():
    '''returns boolean\n\n
    addBecameFriendListener(final BecameFriendListener becameFriendListener)\n
    '''
def removeBecameFriendListener():
    '''returns boolean\n\n
    removeBecameFriendListener(final BecameFriendListener becameFriendListener)\n
    '''
def addWasUnfriendedListener():
    '''returns boolean\n\n
    addWasUnfriendedListener(final WasUnfriendedListener wasUnfriendedListener)\n
    '''
def removeWasUnfriendedListener():
    '''returns boolean\n\n
    removeWasUnfriendedListener(final WasUnfriendedListener wasUnfriendedListener)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
