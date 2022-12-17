ELEMENT = "String  \"status\""
NAMESPACE = "String  \"http://jabber.org/protocol/muc#user\""
def ():
    '''returns Decline\n\n
    ()\n
    (final String reason, final EntityFullJid from)\n
    (final String reason, final EntityBareJid to)\n
    (final String reason, final EntityJid from, final EntityBareJid to)\n
    (final String reason, final EntityBareJid to)\n
    (final String reason, final EntityBareJid from, final EntityBareJid to)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    getElementName()\n
    getElementName()\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    toXML(final String enclosingNamespace)\n
    toXML(final String enclosingNamespace)\n
    toXML(final String enclosingNamespace)\n
    '''
def getInvite():
    '''returns Invite\n\n
    getInvite()\n
    '''
def getDecline():
    '''returns Decline\n\n
    getDecline()\n
    '''
def getItem():
    '''returns MUCItem\n\n
    getItem()\n
    '''
def getPassword():
    '''returns String\n\n
    getPassword()\n
    '''
def getStatus():
    '''returns Set<Status>\n\n
    getStatus()\n
    '''
def hasStatus():
    '''returns boolean\n\n
    hasStatus()\n
    '''
def getDestroy():
    '''returns Destroy\n\n
    getDestroy()\n
    '''
def setInvite():
    '''returns None\n\n
    setInvite(final Invite invite)\n
    '''
def setDecline():
    '''returns None\n\n
    setDecline(final Decline decline)\n
    '''
def setItem():
    '''returns None\n\n
    setItem(final MUCItem item)\n
    '''
def setPassword():
    '''returns None\n\n
    setPassword(final String string)\n
    '''
def addStatusCodes():
    '''returns None\n\n
    addStatusCodes(final Set<Status> statusCodes)\n
    '''
def addStatusCode():
    '''returns None\n\n
    addStatusCode(final Status status)\n
    '''
def setDestroy():
    '''returns None\n\n
    setDestroy(final Destroy destroy)\n
    '''
def getFrom():
    '''returns EntityBareJid\n\n
    getFrom()\n
    getFrom()\n
    '''
def getReason():
    '''returns String\n\n
    getReason()\n
    getReason()\n
    '''
def getTo():
    '''returns EntityBareJid\n\n
    getTo()\n
    getTo()\n
    '''
def getCode():
    '''returns int\n\n
    getCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
