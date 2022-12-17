INITIAL_DEFAULT_NON_ROSTER_PRESENCE_MAP_SIZE = "int  1024"
def processStanza():
    '''returns None\n\n
    processStanza(final Stanza stanza)\n
    processStanza(final Stanza stanzav)\n
    processStanza(final Stanza packet)\n
    '''
def authenticated():
    '''returns None\n\n
    authenticated(final XMPPConnection connection, final boolean resumed)\n
    '''
def connectionClosed():
    '''returns None\n\n
    connectionClosed()\n
    '''
def getSubscriptionMode():
    '''returns SubscriptionMode\n\n
    getSubscriptionMode()\n
    '''
def setSubscriptionMode():
    '''returns None\n\n
    setSubscriptionMode(final SubscriptionMode subscriptionMode)\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    '''
def processException():
    '''returns None\n\n
    processException(final Exception exception)\n
    '''
def reloadAndWait():
    '''returns None\n\n
    reloadAndWait()\n
    '''
def setRosterStore():
    '''returns boolean\n\n
    setRosterStore(final RosterStore rosterStore)\n
    '''
def isLoaded():
    '''returns boolean\n\n
    isLoaded()\n
    '''
def addRosterListener():
    '''returns boolean\n\n
    addRosterListener(final RosterListener rosterListener)\n
    '''
def removeRosterListener():
    '''returns boolean\n\n
    removeRosterListener(final RosterListener rosterListener)\n
    '''
def addRosterLoadedListener():
    '''returns boolean\n\n
    addRosterLoadedListener(final RosterLoadedListener rosterLoadedListener)\n
    '''
def removeRosterLoadedListener():
    '''returns boolean\n\n
    removeRosterLoadedListener(final RosterLoadedListener rosterLoadedListener)\n
    '''
def addPresenceEventListener():
    '''returns boolean\n\n
    addPresenceEventListener(final PresenceEventListener presenceEventListener)\n
    '''
def removePresenceEventListener():
    '''returns boolean\n\n
    removePresenceEventListener(final PresenceEventListener presenceEventListener)\n
    '''
def createGroup():
    '''returns RosterGroup\n\n
    createGroup(final String name)\n
    '''
def createEntry():
    '''returns None\n\n
    createEntry(final BareJid user, final String name, final String[] groups)\n
    '''
def preApproveAndCreateEntry():
    '''returns None\n\n
    preApproveAndCreateEntry(final BareJid user, final String name, final String[] groups)\n
    '''
def preApprove():
    '''returns None\n\n
    preApprove(final BareJid user)\n
    '''
def isSubscriptionPreApprovalSupported():
    '''returns boolean\n\n
    isSubscriptionPreApprovalSupported()\n
    '''
def sendSubscriptionRequest():
    '''returns None\n\n
    sendSubscriptionRequest(final BareJid jid)\n
    '''
def addSubscribeListener():
    '''returns boolean\n\n
    addSubscribeListener(final SubscribeListener subscribeListener)\n
    '''
def removeSubscribeListener():
    '''returns boolean\n\n
    removeSubscribeListener(final SubscribeListener subscribeListener)\n
    '''
def removeEntry():
    '''returns None\n\n
    removeEntry(final RosterEntry entry)\n
    '''
def getEntryCount():
    '''returns int\n\n
    getEntryCount()\n
    '''
def getEntriesAndAddListener():
    '''returns None\n\n
    getEntriesAndAddListener(final RosterListener rosterListener, final RosterEntries rosterEntries)\n
    '''
def getEntries():
    '''returns Set<RosterEntry>\n\n
    getEntries()\n
    '''
def getUnfiledEntryCount():
    '''returns int\n\n
    getUnfiledEntryCount()\n
    '''
def getUnfiledEntries():
    '''returns Set<RosterEntry>\n\n
    getUnfiledEntries()\n
    '''
def getEntry():
    '''returns RosterEntry\n\n
    getEntry(final BareJid jid)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final BareJid jid)\n
    '''
def getGroup():
    '''returns RosterGroup\n\n
    getGroup(final String name)\n
    '''
def getGroupCount():
    '''returns int\n\n
    getGroupCount()\n
    '''
def getGroups():
    '''returns Collection<RosterGroup>\n\n
    getGroups()\n
    '''
def getPresence():
    '''returns Presence\n\n
    getPresence(final BareJid jid)\n
    '''
def getPresenceResource():
    '''returns Presence\n\n
    getPresenceResource(final FullJid userWithResource)\n
    '''
def getAllPresences():
    '''returns List<Presence>\n\n
    getAllPresences(final BareJid bareJid)\n
    '''
def getAvailablePresences():
    '''returns List<Presence>\n\n
    getAvailablePresences(final BareJid bareJid)\n
    '''
def getPresences():
    '''returns List<Presence>\n\n
    getPresences(final BareJid jid)\n
    '''
def isSubscribedToMyPresence():
    '''returns boolean\n\n
    isSubscribedToMyPresence(final Jid jid)\n
    '''
def iAmSubscribedTo():
    '''returns boolean\n\n
    iAmSubscribedTo(final Jid jid)\n
    '''
def setRosterLoadedAtLogin():
    '''returns None\n\n
    setRosterLoadedAtLogin(final boolean rosterLoadedAtLogin)\n
    '''
def isRosterLoadedAtLogin():
    '''returns boolean\n\n
    isRosterLoadedAtLogin()\n
    '''
def isRosterVersioningSupported():
    '''returns boolean\n\n
    isRosterVersioningSupported()\n
    '''
def setNonRosterPresenceMapMaxSize():
    '''returns None\n\n
    setNonRosterPresenceMapMaxSize(final int maximumSize)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def onSuccess():
    '''returns None\n\n
    onSuccess(final IQ packet)\n
    '''
def handleIQRequest():
    '''returns IQ\n\n
    handleIQRequest(final IQ iqRequest)\n
    '''
