INITIAL_DEFAULT_NON_ROSTER_PRESENCE_MAP_SIZE = "int  1024"
def getInstanceFor():
    '''public static synchronized Roster getInstanceFor(final XMPPConnection connection)
    '''
def getDefaultSubscriptionMode():
    '''public static SubscriptionMode getDefaultSubscriptionMode()
    '''
def setDefaultSubscriptionMode():
    '''public static void setDefaultSubscriptionMode(final SubscriptionMode subscriptionMode)
    '''
def processStanza():
    '''public void processStanza(final Stanza stanza)
    public void processStanza(final Stanza stanzav)
    public void processStanza(final Stanza packet)
    '''
def authenticated():
    '''public void authenticated(final XMPPConnection connection, final boolean resumed)
    '''
def connectionClosed():
    '''public void connectionClosed()
    '''
def getSubscriptionMode():
    '''public SubscriptionMode getSubscriptionMode()
    '''
def setSubscriptionMode():
    '''public void setSubscriptionMode(final SubscriptionMode subscriptionMode)
    '''
def reload():
    '''public void reload()
    '''
def processException():
    '''public void processException(final Exception exception)
    '''
def reloadAndWait():
    '''public void reloadAndWait()
    '''
def setRosterStore():
    '''public boolean setRosterStore(final RosterStore rosterStore)
    '''
def isLoaded():
    '''public boolean isLoaded()
    '''
def addRosterListener():
    '''public boolean addRosterListener(final RosterListener rosterListener)
    '''
def removeRosterListener():
    '''public boolean removeRosterListener(final RosterListener rosterListener)
    '''
def addRosterLoadedListener():
    '''public boolean addRosterLoadedListener(final RosterLoadedListener rosterLoadedListener)
    '''
def removeRosterLoadedListener():
    '''public boolean removeRosterLoadedListener(final RosterLoadedListener rosterLoadedListener)
    '''
def addPresenceEventListener():
    '''public boolean addPresenceEventListener(final PresenceEventListener presenceEventListener)
    '''
def removePresenceEventListener():
    '''public boolean removePresenceEventListener(final PresenceEventListener presenceEventListener)
    '''
def createGroup():
    '''public RosterGroup createGroup(final String name)
    '''
def createEntry():
    '''public void createEntry(final BareJid user, final String name, final String[] groups)
    '''
def preApproveAndCreateEntry():
    '''public void preApproveAndCreateEntry(final BareJid user, final String name, final String[] groups)
    '''
def preApprove():
    '''public void preApprove(final BareJid user)
    '''
def isSubscriptionPreApprovalSupported():
    '''public boolean isSubscriptionPreApprovalSupported()
    '''
def sendSubscriptionRequest():
    '''public void sendSubscriptionRequest(final BareJid jid)
    '''
def addSubscribeListener():
    '''public boolean addSubscribeListener(final SubscribeListener subscribeListener)
    '''
def removeSubscribeListener():
    '''public boolean removeSubscribeListener(final SubscribeListener subscribeListener)
    '''
def removeEntry():
    '''public void removeEntry(final RosterEntry entry)
    '''
def getEntryCount():
    '''public int getEntryCount()
    '''
def getEntriesAndAddListener():
    '''public void getEntriesAndAddListener(final RosterListener rosterListener, final RosterEntries rosterEntries)
    '''
def getEntries():
    '''public Set<RosterEntry> getEntries()
    '''
def getUnfiledEntryCount():
    '''public int getUnfiledEntryCount()
    '''
def getUnfiledEntries():
    '''public Set<RosterEntry> getUnfiledEntries()
    '''
def getEntry():
    '''public RosterEntry getEntry(final BareJid jid)
    '''
def contains():
    '''public boolean contains(final BareJid jid)
    '''
def getGroup():
    '''public RosterGroup getGroup(final String name)
    '''
def getGroupCount():
    '''public int getGroupCount()
    '''
def getGroups():
    '''public Collection<RosterGroup> getGroups()
    '''
def getPresence():
    '''public Presence getPresence(final BareJid jid)
    '''
def getPresenceResource():
    '''public Presence getPresenceResource(final FullJid userWithResource)
    '''
def getAllPresences():
    '''public List<Presence> getAllPresences(final BareJid bareJid)
    '''
def getAvailablePresences():
    '''public List<Presence> getAvailablePresences(final BareJid bareJid)
    '''
def getPresences():
    '''public List<Presence> getPresences(final BareJid jid)
    '''
def isSubscribedToMyPresence():
    '''public boolean isSubscribedToMyPresence(final Jid jid)
    '''
def iAmSubscribedTo():
    '''public boolean iAmSubscribedTo(final Jid jid)
    '''
def setRosterLoadedAtLoginDefault():
    '''public static void setRosterLoadedAtLoginDefault(final boolean rosterLoadedAtLoginDefault)
    '''
def setRosterLoadedAtLogin():
    '''public void setRosterLoadedAtLogin(final boolean rosterLoadedAtLogin)
    '''
def isRosterLoadedAtLogin():
    '''public boolean isRosterLoadedAtLogin()
    '''
def isRosterVersioningSupported():
    '''public boolean isRosterVersioningSupported()
    '''
def setDefaultNonRosterPresenceMapMaxSize():
    '''public static void setDefaultNonRosterPresenceMapMaxSize(final int maximumSize)
    '''
def setNonRosterPresenceMapMaxSize():
    '''public void setNonRosterPresenceMapMaxSize(final int maximumSize)
    '''
def connectionCreated():
    '''public void connectionCreated(final XMPPConnection connection)
    '''
def run():
    '''public void run()
    '''
def onSuccess():
    '''public void onSuccess(final IQ packet)
    '''
def handleIQRequest():
    '''public IQ handleIQRequest(final IQ iqRequest)
    '''
