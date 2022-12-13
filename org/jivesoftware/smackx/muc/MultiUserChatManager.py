def getInstanceFor():
'''public static synchronized MultiUserChatManager getInstanceFor(final XMPPConnection connection)
'''
pass
def processStanza():
'''public void processStanza(final Stanza packet)
'''
pass
def authenticated():
'''public void authenticated(final XMPPConnection connection, final boolean resumed)
'''
pass
def run():
'''public void run()
'''
pass
def getMultiUserChat():
'''public synchronized MultiUserChat getMultiUserChat(final EntityBareJid jid)
'''
pass
def isServiceEnabled():
'''public boolean isServiceEnabled(final Jid user)
'''
pass
def getJoinedRooms():
'''public Set<EntityBareJid> getJoinedRooms()
public List<EntityBareJid> getJoinedRooms(final EntityJid user)
'''
pass
def getRoomInfo():
'''public RoomInfo getRoomInfo(final EntityBareJid room)
'''
pass
def getMucServiceDomains():
'''public List<DomainBareJid> getMucServiceDomains()
'''
pass
def getXMPPServiceDomains():
'''public List<DomainBareJid> getXMPPServiceDomains()
'''
pass
def providesMucService():
'''public boolean providesMucService(final DomainBareJid domainBareJid)
'''
pass
def getHostedRooms():
'''public List<HostedRoom> getHostedRooms(final DomainBareJid serviceName)
'''
pass
def getRoomsHostedBy():
'''public Map<EntityBareJid, HostedRoom> getRoomsHostedBy(final DomainBareJid serviceName)
'''
pass
def decline():
'''public void decline(final EntityBareJid room, final EntityBareJid inviter, final String reason)
'''
pass
def addInvitationListener():
'''public void addInvitationListener(final InvitationListener listener)
'''
pass
def removeInvitationListener():
'''public void removeInvitationListener(final InvitationListener listener)
'''
pass
def setAutoJoinOnReconnect():
'''public void setAutoJoinOnReconnect(final boolean autoJoin)
'''
pass
def setAutoJoinFailedCallback():
'''public void setAutoJoinFailedCallback(final AutoJoinFailedCallback failedCallback)
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
