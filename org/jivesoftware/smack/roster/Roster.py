INITIAL_DEFAULT_NON_ROSTER_PRESENCE_MAP_SIZE = "int  1024"
def getInstanceFor():
'''public static synchronized Roster getInstanceFor(final XMPPConnection connection)
'''
pass
def getDefaultSubscriptionMode():
'''public static SubscriptionMode getDefaultSubscriptionMode()
'''
pass
def setDefaultSubscriptionMode():
'''public static void setDefaultSubscriptionMode(final SubscriptionMode subscriptionMode)
'''
pass
def processStanza():
'''public void processStanza(final Stanza stanza)
public void processStanza(final Stanza stanzav)
public void processStanza(final Stanza packet)
'''
pass
def authenticated():
'''public void authenticated(final XMPPConnection connection, final boolean resumed)
'''
pass
def connectionClosed():
'''public void connectionClosed()
'''
pass
def getSubscriptionMode():
'''public SubscriptionMode getSubscriptionMode()
'''
pass
def setSubscriptionMode():
'''public void setSubscriptionMode(final SubscriptionMode subscriptionMode)
'''
pass
def reload():
'''public void reload()
'''
pass
def processException():
'''public void processException(final Exception exception)
'''
pass
def reloadAndWait():
'''public void reloadAndWait()
'''
pass
def setRosterStore():
'''public boolean setRosterStore(final RosterStore rosterStore)
'''
pass
def isLoaded():
'''public boolean isLoaded()
'''
pass
def addRosterListener():
'''public boolean addRosterListener(final RosterListener rosterListener)
'''
pass
def removeRosterListener():
'''public boolean removeRosterListener(final RosterListener rosterListener)
'''
pass
def addRosterLoadedListener():
'''public boolean addRosterLoadedListener(final RosterLoadedListener rosterLoadedListener)
'''
pass
def removeRosterLoadedListener():
'''public boolean removeRosterLoadedListener(final RosterLoadedListener rosterLoadedListener)
'''
pass
def addPresenceEventListener():
'''public boolean addPresenceEventListener(final PresenceEventListener presenceEventListener)
'''
pass
def removePresenceEventListener():
'''public boolean removePresenceEventListener(final PresenceEventListener presenceEventListener)
'''
pass
def createGroup():
'''public RosterGroup createGroup(final String name)
'''
pass
def createEntry():
'''public void createEntry(final BareJid user, final String name, final String[] groups)
'''
pass
def preApproveAndCreateEntry():
'''public void preApproveAndCreateEntry(final BareJid user, final String name, final String[] groups)
'''
pass
def preApprove():
'''public void preApprove(final BareJid user)
'''
pass
def isSubscriptionPreApprovalSupported():
'''public boolean isSubscriptionPreApprovalSupported()
'''
pass
def sendSubscriptionRequest():
'''public void sendSubscriptionRequest(final BareJid jid)
'''
pass
def addSubscribeListener():
'''public boolean addSubscribeListener(final SubscribeListener subscribeListener)
'''
pass
def removeSubscribeListener():
'''public boolean removeSubscribeListener(final SubscribeListener subscribeListener)
'''
pass
def removeEntry():
'''public void removeEntry(final RosterEntry entry)
'''
pass
def getEntryCount():
'''public int getEntryCount()
'''
pass
def getEntriesAndAddListener():
'''public void getEntriesAndAddListener(final RosterListener rosterListener, final RosterEntries rosterEntries)
'''
pass
def getEntries():
'''public Set<RosterEntry> getEntries()
'''
pass
def getUnfiledEntryCount():
'''public int getUnfiledEntryCount()
'''
pass
def getUnfiledEntries():
'''public Set<RosterEntry> getUnfiledEntries()
'''
pass
def getEntry():
'''public RosterEntry getEntry(final BareJid jid)
'''
pass
def contains():
'''public boolean contains(final BareJid jid)
'''
pass
def getGroup():
'''public RosterGroup getGroup(final String name)
'''
pass
def getGroupCount():
'''public int getGroupCount()
'''
pass
def getGroups():
'''public Collection<RosterGroup> getGroups()
'''
pass
def getPresence():
'''public Presence getPresence(final BareJid jid)
'''
pass
def getPresenceResource():
'''public Presence getPresenceResource(final FullJid userWithResource)
'''
pass
def getAllPresences():
'''public List<Presence> getAllPresences(final BareJid bareJid)
'''
pass
def getAvailablePresences():
'''public List<Presence> getAvailablePresences(final BareJid bareJid)
'''
pass
def getPresences():
'''public List<Presence> getPresences(final BareJid jid)
'''
pass
def isSubscribedToMyPresence():
'''public boolean isSubscribedToMyPresence(final Jid jid)
'''
pass
def iAmSubscribedTo():
'''public boolean iAmSubscribedTo(final Jid jid)
'''
pass
def setRosterLoadedAtLoginDefault():
'''public static void setRosterLoadedAtLoginDefault(final boolean rosterLoadedAtLoginDefault)
'''
pass
def setRosterLoadedAtLogin():
'''public void setRosterLoadedAtLogin(final boolean rosterLoadedAtLogin)
'''
pass
def isRosterLoadedAtLogin():
'''public boolean isRosterLoadedAtLogin()
'''
pass
def isRosterVersioningSupported():
'''public boolean isRosterVersioningSupported()
'''
pass
def setDefaultNonRosterPresenceMapMaxSize():
'''public static void setDefaultNonRosterPresenceMapMaxSize(final int maximumSize)
'''
pass
def setNonRosterPresenceMapMaxSize():
'''public void setNonRosterPresenceMapMaxSize(final int maximumSize)
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
def run():
'''public void run()
'''
pass
def onSuccess():
'''public void onSuccess(final IQ packet)
'''
pass
def handleIQRequest():
'''public IQ handleIQRequest(final IQ iqRequest)
'''
pass
