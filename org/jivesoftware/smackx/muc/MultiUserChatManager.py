def getInstanceFor():
    '''    public static synchronized MultiUserChatManager getInstanceFor(final XMPPConnection connection)
    '''
def processStanza():
    '''    public void processStanza(final Stanza packet)
    '''
def authenticated():
    '''    public void authenticated(final XMPPConnection connection, final boolean resumed)
    '''
def run():
    '''    public void run()
    '''
def getMultiUserChat():
    '''    public synchronized MultiUserChat getMultiUserChat(final EntityBareJid jid)
    '''
def isServiceEnabled():
    '''    public boolean isServiceEnabled(final Jid user)
    '''
def getJoinedRooms():
    '''    public Set<EntityBareJid> getJoinedRooms()
    public List<EntityBareJid> getJoinedRooms(final EntityJid user)
    '''
def getRoomInfo():
    '''    public RoomInfo getRoomInfo(final EntityBareJid room)
    '''
def getMucServiceDomains():
    '''    public List<DomainBareJid> getMucServiceDomains()
    '''
def getXMPPServiceDomains():
    '''    public List<DomainBareJid> getXMPPServiceDomains()
    '''
def providesMucService():
    '''    public boolean providesMucService(final DomainBareJid domainBareJid)
    '''
def getHostedRooms():
    '''    public List<HostedRoom> getHostedRooms(final DomainBareJid serviceName)
    '''
def getRoomsHostedBy():
    '''    public Map<EntityBareJid, HostedRoom> getRoomsHostedBy(final DomainBareJid serviceName)
    '''
def decline():
    '''    public void decline(final EntityBareJid room, final EntityBareJid inviter, final String reason)
    '''
def addInvitationListener():
    '''    public void addInvitationListener(final InvitationListener listener)
    '''
def removeInvitationListener():
    '''    public void removeInvitationListener(final InvitationListener listener)
    '''
def setAutoJoinOnReconnect():
    '''    public void setAutoJoinOnReconnect(final boolean autoJoin)
    '''
def setAutoJoinFailedCallback():
    '''    public void setAutoJoinFailedCallback(final AutoJoinFailedCallback failedCallback)
    '''
def connectionCreated():
    '''    public void connectionCreated(final XMPPConnection connection)
    '''
