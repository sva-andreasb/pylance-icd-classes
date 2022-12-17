NAMESPACE = "String  \"urn:xmpp:blocking\""
def handleIQRequest():
    '''returns IQ\n\n
    handleIQRequest(final IQ iqRequest)\n
    handleIQRequest(final IQ iqRequest)\n
    '''
def authenticated():
    '''returns None\n\n
    authenticated(final XMPPConnection connection, final boolean resumed)\n
    '''
def isSupportedByServer():
    '''returns boolean\n\n
    isSupportedByServer()\n
    '''
def getBlockList():
    '''returns List<Jid>\n\n
    getBlockList()\n
    '''
def blockContacts():
    '''returns None\n\n
    blockContacts(final List<Jid> jids)\n
    '''
def unblockContacts():
    '''returns None\n\n
    unblockContacts(final List<Jid> jids)\n
    '''
def unblockAll():
    '''returns None\n\n
    unblockAll()\n
    '''
def addJidsBlockedListener():
    '''returns None\n\n
    addJidsBlockedListener(final JidsBlockedListener jidsBlockedListener)\n
    '''
def removeJidsBlockedListener():
    '''returns None\n\n
    removeJidsBlockedListener(final JidsBlockedListener jidsBlockedListener)\n
    '''
def addJidsUnblockedListener():
    '''returns None\n\n
    addJidsUnblockedListener(final JidsUnblockedListener jidsUnblockedListener)\n
    '''
def removeJidsUnblockedListener():
    '''returns None\n\n
    removeJidsUnblockedListener(final JidsUnblockedListener jidsUnblockedListener)\n
    '''
def addAllJidsUnblockedListener():
    '''returns None\n\n
    addAllJidsUnblockedListener(final AllJidsUnblockedListener allJidsUnblockedListener)\n
    '''
def removeAllJidsUnblockedListener():
    '''returns None\n\n
    removeAllJidsUnblockedListener(final AllJidsUnblockedListener allJidsUnblockedListener)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
