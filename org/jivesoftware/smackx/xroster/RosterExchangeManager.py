NAMESPACE = "String  \"jabber:x:roster\""
ELEMENT = "String  \"x\""
def getInstanceFor():
    '''    public static synchronized RosterExchangeManager getInstanceFor(final XMPPConnection connection)
    '''
def RosterExchangeManager():
    '''    public RosterExchangeManager(final XMPPConnection connection)
    '''
def processStanza():
    '''    public void processStanza(final Stanza packet)
    '''
def addRosterListener():
    '''    public void addRosterListener(final RosterExchangeListener rosterExchangeListener)
    '''
def removeRosterListener():
    '''    public void removeRosterListener(final RosterExchangeListener rosterExchangeListener)
    '''
def send():
    '''    public void send(final Roster roster, final Jid targetUserID)
    public void send(final RosterEntry rosterEntry, final Jid targetUserID)
    public void send(final RosterGroup rosterGroup, final Jid targetUserID)
    '''
