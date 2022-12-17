def ():
    '''returns Subscription\n\n
    (final Jid subscriptionJid)\n
    (final Jid subscriptionJid, final String nodeId)\n
    (final Jid subscriptionJid, final State state)\n
    (final Jid jid, final String nodeId, final String subscriptionId, final State state)\n
    (final Jid jid, final String nodeId, final String subscriptionId, final State state, final boolean configRequired)\n
    '''
def getJid():
    '''returns Jid\n\n
    getJid()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getState():
    '''returns State\n\n
    getState()\n
    '''
def isConfigRequired():
    '''returns boolean\n\n
    isConfigRequired()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
