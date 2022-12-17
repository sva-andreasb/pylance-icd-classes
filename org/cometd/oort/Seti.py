def ():
    '''returns Event\n\n
    (final Oort oort)\n
    (final Seti source, final String userId, final String url)\n
    '''
def isDebugEnabled():
    '''returns boolean\n\n
    isDebugEnabled()\n
    '''
def setDebugEnabled():
    '''returns None\n\n
    setDebugEnabled(final boolean debug)\n
    '''
def getOort():
    '''returns Oort\n\n
    getOort()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def configureChannel():
    '''returns None\n\n
    configureChannel(final ConfigurableServerChannel channel)\n
    configureChannel(final ConfigurableServerChannel channel)\n
    configureChannel(final ConfigurableServerChannel channel)\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(final ClientSessionChannel channel, final Message message)\n
    onMessage(final ClientSessionChannel channel, final Message message)\n
    '''
def associate():
    '''returns boolean\n\n
    associate(final String userId, final ServerSession session)\n
    '''
def isAssociated():
    '''returns boolean\n\n
    isAssociated(final String userId)\n
    '''
def isPresent():
    '''returns boolean\n\n
    isPresent(final String userId)\n
    '''
def disassociate():
    '''returns boolean\n\n
    disassociate(final String userId, final ServerSession session)\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final String toUserId, final String toChannel, final Object data)\n
    sendMessage(final Collection<String> toUserIds, final String toChannel, final Object data)\n
    '''
def addPresenceListener():
    '''returns None\n\n
    addPresenceListener(final PresenceListener listener)\n
    '''
def removePresenceListener():
    '''returns None\n\n
    removePresenceListener(final PresenceListener listener)\n
    '''
def send():
    '''returns None\n\n
    send(final String toUser, final String toChannel, final Object data)\n
    send(final String toUser, final String toChannel, final Object data)\n
    '''
def receive():
    '''returns None\n\n
    receive(final String toUser, final String toChannel, final Object data)\n
    receive(final String toUser, final String toChannel, final Object data)\n
    '''
def removed():
    '''returns None\n\n
    removed(final ServerSession session, final boolean timeout)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getUserId():
    '''returns String\n\n
    getUserId()\n
    '''
def getURL():
    '''returns String\n\n
    getURL()\n
    '''
