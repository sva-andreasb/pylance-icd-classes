def processStanza():
    '''returns None\n\n
    processStanza(final Stanza packet)\n
    '''
def authenticated():
    '''returns None\n\n
    authenticated(final XMPPConnection connection, final boolean resumed)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def isServiceEnabled():
    '''returns boolean\n\n
    isServiceEnabled(final Jid user)\n
    '''
def getJoinedRooms():
    '''returns List<EntityBareJid>\n\n
    getJoinedRooms()\n
    getJoinedRooms(final EntityJid user)\n
    '''
def getRoomInfo():
    '''returns RoomInfo\n\n
    getRoomInfo(final EntityBareJid room)\n
    '''
def getMucServiceDomains():
    '''returns List<DomainBareJid>\n\n
    getMucServiceDomains()\n
    '''
def getXMPPServiceDomains():
    '''returns List<DomainBareJid>\n\n
    getXMPPServiceDomains()\n
    '''
def providesMucService():
    '''returns boolean\n\n
    providesMucService(final DomainBareJid domainBareJid)\n
    '''
def getHostedRooms():
    '''returns List<HostedRoom>\n\n
    getHostedRooms(final DomainBareJid serviceName)\n
    '''
def decline():
    '''returns None\n\n
    decline(final EntityBareJid room, final EntityBareJid inviter, final String reason)\n
    '''
def addInvitationListener():
    '''returns None\n\n
    addInvitationListener(final InvitationListener listener)\n
    '''
def removeInvitationListener():
    '''returns None\n\n
    removeInvitationListener(final InvitationListener listener)\n
    '''
def setAutoJoinOnReconnect():
    '''returns None\n\n
    setAutoJoinOnReconnect(final boolean autoJoin)\n
    '''
def setAutoJoinFailedCallback():
    '''returns None\n\n
    setAutoJoinFailedCallback(final AutoJoinFailedCallback failedCallback)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
