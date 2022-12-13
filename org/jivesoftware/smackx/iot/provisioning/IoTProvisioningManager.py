def getInstanceFor():
'''public static synchronized IoTProvisioningManager getInstanceFor(final XMPPConnection connection)
'''
pass
def processStanza():
'''public void processStanza(final Stanza stanza)
public void processStanza(final Stanza stanza)
'''
pass
def handleIQRequest():
'''public IQ handleIQRequest(final IQ iqRequest)
'''
pass
def presenceSubscribed():
'''public void presenceSubscribed(final BareJid address, final Presence subscribedPresence)
'''
pass
def presenceUnsubscribed():
'''public void presenceUnsubscribed(final BareJid address, final Presence unsubscribedPresence)
'''
pass
def setConfiguredProvisioningServer():
'''public void setConfiguredProvisioningServer(final Jid provisioningServer)
'''
pass
def getConfiguredProvisioningServer():
'''public Jid getConfiguredProvisioningServer()
'''
pass
def findProvisioningServerComponent():
'''public DomainBareJid findProvisioningServerComponent()
'''
pass
def isFriend():
'''public boolean isFriend(final Jid provisioningServer, final BareJid friendInQuestion)
'''
pass
def iAmFriendOf():
'''public boolean iAmFriendOf(final BareJid otherJid)
'''
pass
def sendFriendshipRequest():
'''public void sendFriendshipRequest(final BareJid bareJid)
'''
pass
def sendFriendshipRequestIfRequired():
'''public void sendFriendshipRequestIfRequired(final BareJid jid)
'''
pass
def isMyFriend():
'''public boolean isMyFriend(final Jid friendInQuestion)
'''
pass
def unfriend():
'''public void unfriend(final Jid friend)
'''
pass
def addBecameFriendListener():
'''public boolean addBecameFriendListener(final BecameFriendListener becameFriendListener)
'''
pass
def removeBecameFriendListener():
'''public boolean removeBecameFriendListener(final BecameFriendListener becameFriendListener)
'''
pass
def addWasUnfriendedListener():
'''public boolean addWasUnfriendedListener(final WasUnfriendedListener wasUnfriendedListener)
'''
pass
def removeWasUnfriendedListener():
'''public boolean removeWasUnfriendedListener(final WasUnfriendedListener wasUnfriendedListener)
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
