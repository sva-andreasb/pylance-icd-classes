ELEMENT = "String  \"item\""
NAMESPACE = "String  \"jabber:iq:roster\""
GROUP = "String  \"group\""
def ():
    '''returns Item\n\n
    ()\n
    (final BareJid jid, final String name)\n
    (final BareJid jid, final String name, final boolean subscriptionPending)\n
    '''
def addRosterItem():
    '''returns None\n\n
    addRosterItem(final Item item)\n
    '''
def getRosterItemCount():
    '''returns int\n\n
    getRosterItemCount()\n
    '''
def getRosterItems():
    '''returns List<Item>\n\n
    getRosterItems()\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final String version)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getUser():
    '''returns String\n\n
    getUser()\n
    '''
def getJid():
    '''returns BareJid\n\n
    getJid()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getItemType():
    '''returns ItemType\n\n
    getItemType()\n
    '''
def setItemType():
    '''returns None\n\n
    setItemType(final ItemType itemType)\n
    '''
def setSubscriptionPending():
    '''returns None\n\n
    setSubscriptionPending(final boolean subscriptionPending)\n
    '''
def isSubscriptionPending():
    '''returns boolean\n\n
    isSubscriptionPending()\n
    '''
def isApproved():
    '''returns boolean\n\n
    isApproved()\n
    '''
def setApproved():
    '''returns None\n\n
    setApproved(final boolean approved)\n
    '''
def getGroupNames():
    '''returns Set<String>\n\n
    getGroupNames()\n
    '''
def addGroupName():
    '''returns None\n\n
    addGroupName(final String groupName)\n
    '''
def removeGroupName():
    '''returns None\n\n
    removeGroupName(final String groupName)\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def asSymbol():
    '''returns String\n\n
    asSymbol()\n
    '''
