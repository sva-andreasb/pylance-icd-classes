def connectionClosed():
    '''returns None\n\n
    connectionClosed()\n
    '''
def connectionClosedOnError():
    '''returns None\n\n
    connectionClosedOnError(final Exception e)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final Connection connection)\n
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
def addRosterListener():
    '''returns None\n\n
    addRosterListener(final RosterListener rosterListener)\n
    '''
def removeRosterListener():
    '''returns None\n\n
    removeRosterListener(final RosterListener rosterListener)\n
    '''
def createGroup():
    '''returns RosterGroup\n\n
    createGroup(final String name)\n
    '''
def createEntry():
    '''returns None\n\n
    createEntry(final String user, final String name, final String[] groups)\n
    '''
def removeEntry():
    '''returns None\n\n
    removeEntry(final RosterEntry entry)\n
    '''
def getEntryCount():
    '''returns int\n\n
    getEntryCount()\n
    '''
def getEntries():
    '''returns Collection<RosterEntry>\n\n
    getEntries()\n
    '''
def getUnfiledEntryCount():
    '''returns int\n\n
    getUnfiledEntryCount()\n
    '''
def getUnfiledEntries():
    '''returns Collection<RosterEntry>\n\n
    getUnfiledEntries()\n
    '''
def getEntry():
    '''returns RosterEntry\n\n
    getEntry(final String user)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final String user)\n
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
    getPresence(final String user)\n
    '''
def getPresenceResource():
    '''returns Presence\n\n
    getPresenceResource(final String userWithResource)\n
    '''
def getPresences():
    '''returns Iterator<Presence>\n\n
    getPresences(final String user)\n
    '''
def processPacket():
    '''returns None\n\n
    processPacket(final Packet packet)\n
    processPacket(final Packet packet)\n
    '''
