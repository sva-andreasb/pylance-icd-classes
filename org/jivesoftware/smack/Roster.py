def getDefaultSubscriptionMode():
    '''public static SubscriptionMode getDefaultSubscriptionMode()
    '''
def setDefaultSubscriptionMode():
    '''public static void setDefaultSubscriptionMode(final SubscriptionMode subscriptionMode)
    '''
def connectionClosed():
    '''public void connectionClosed()
    '''
def connectionClosedOnError():
    '''public void connectionClosedOnError(final Exception e)
    '''
def connectionCreated():
    '''public void connectionCreated(final Connection connection)
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
def addRosterListener():
    '''public void addRosterListener(final RosterListener rosterListener)
    '''
def removeRosterListener():
    '''public void removeRosterListener(final RosterListener rosterListener)
    '''
def createGroup():
    '''public RosterGroup createGroup(final String name)
    '''
def createEntry():
    '''public void createEntry(final String user, final String name, final String[] groups)
    '''
def removeEntry():
    '''public void removeEntry(final RosterEntry entry)
    '''
def getEntryCount():
    '''public int getEntryCount()
    '''
def getEntries():
    '''public Collection<RosterEntry> getEntries()
    '''
def getUnfiledEntryCount():
    '''public int getUnfiledEntryCount()
    '''
def getUnfiledEntries():
    '''public Collection<RosterEntry> getUnfiledEntries()
    '''
def getEntry():
    '''public RosterEntry getEntry(final String user)
    '''
def contains():
    '''public boolean contains(final String user)
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
    '''public Presence getPresence(final String user)
    '''
def getPresenceResource():
    '''public Presence getPresenceResource(final String userWithResource)
    '''
def getPresences():
    '''public Iterator<Presence> getPresences(final String user)
    '''
def processPacket():
    '''public void processPacket(final Packet packet)
    public void processPacket(final Packet packet)
    '''
