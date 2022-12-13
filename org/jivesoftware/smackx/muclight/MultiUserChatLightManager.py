def getInstanceFor():
    '''    public static synchronized MultiUserChatLightManager getInstanceFor(final XMPPConnection connection)
    '''
def getMultiUserChatLight():
    '''    public synchronized MultiUserChatLight getMultiUserChatLight(final EntityBareJid jid)
    '''
def isFeatureSupported():
    '''    public boolean isFeatureSupported(final DomainBareJid mucLightService)
    '''
def getOccupiedRooms():
    '''    public List<Jid> getOccupiedRooms(final DomainBareJid mucLightService)
    '''
def getLocalServices():
    '''    public List<DomainBareJid> getLocalServices()
    '''
def getUsersAndRoomsBlocked():
    '''    public List<Jid> getUsersAndRoomsBlocked(final DomainBareJid mucLightService)
    '''
def getRoomsBlocked():
    '''    public List<Jid> getRoomsBlocked(final DomainBareJid mucLightService)
    '''
def getUsersBlocked():
    '''    public List<Jid> getUsersBlocked(final DomainBareJid mucLightService)
    '''
def blockRoom():
    '''    public void blockRoom(final DomainBareJid mucLightService, final Jid roomJid)
    '''
def blockRooms():
    '''    public void blockRooms(final DomainBareJid mucLightService, final List<Jid> roomsJids)
    '''
def blockUser():
    '''    public void blockUser(final DomainBareJid mucLightService, final Jid userJid)
    '''
def blockUsers():
    '''    public void blockUsers(final DomainBareJid mucLightService, final List<Jid> usersJids)
    '''
def unblockRoom():
    '''    public void unblockRoom(final DomainBareJid mucLightService, final Jid roomJid)
    '''
def unblockRooms():
    '''    public void unblockRooms(final DomainBareJid mucLightService, final List<Jid> roomsJids)
    '''
def unblockUser():
    '''    public void unblockUser(final DomainBareJid mucLightService, final Jid userJid)
    '''
def unblockUsers():
    '''    public void unblockUsers(final DomainBareJid mucLightService, final List<Jid> usersJids)
    '''
