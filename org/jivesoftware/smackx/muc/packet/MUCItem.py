ELEMENT = "String  \"item\""
def ():
    '''returns MUCItem\n\n
    (final MUCAffiliation affiliation)\n
    (final MUCRole role)\n
    (final MUCRole role, final Resourcepart nick)\n
    (final MUCAffiliation affiliation, final Jid jid, final String reason)\n
    (final MUCAffiliation affiliation, final Jid jid)\n
    (final MUCRole role, final Resourcepart nick, final String reason)\n
    (final MUCAffiliation affiliation, final MUCRole role, final Jid actor, final String reason, final Jid jid, final Resourcepart nick, final Resourcepart actorNick)\n
    '''
def getActor():
    '''returns Jid\n\n
    getActor()\n
    '''
def getActorNick():
    '''returns Resourcepart\n\n
    getActorNick()\n
    '''
def getReason():
    '''returns String\n\n
    getReason()\n
    '''
def getAffiliation():
    '''returns MUCAffiliation\n\n
    getAffiliation()\n
    '''
def getJid():
    '''returns Jid\n\n
    getJid()\n
    '''
def getNick():
    '''returns Resourcepart\n\n
    getNick()\n
    '''
def getRole():
    '''returns MUCRole\n\n
    getRole()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
