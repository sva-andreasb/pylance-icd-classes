NAMESPACE = "String  \"jabber:x:roster\""
ELEMENT = "String  \"x\""
def ():
    '''returns RosterExchangeManager\n\n
    (final XMPPConnection connection)\n
    '''
def processStanza():
    '''returns None\n\n
    processStanza(final Stanza packet)\n
    '''
def addRosterListener():
    '''returns None\n\n
    addRosterListener(final RosterExchangeListener rosterExchangeListener)\n
    '''
def removeRosterListener():
    '''returns None\n\n
    removeRosterListener(final RosterExchangeListener rosterExchangeListener)\n
    '''
def send():
    '''returns None\n\n
    send(final Roster roster, final Jid targetUserID)\n
    send(final RosterEntry rosterEntry, final Jid targetUserID)\n
    send(final RosterGroup rosterGroup, final Jid targetUserID)\n
    '''
