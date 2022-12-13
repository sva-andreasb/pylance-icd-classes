ELEMENT = "String  \"item\""
NAMESPACE = "String  \"jabber:iq:roster\""
GROUP = "String  \"group\""
def RosterPacket():
    '''public RosterPacket()
    '''
def addRosterItem():
    '''public void addRosterItem(final Item item)
    '''
def getRosterItemCount():
    '''public int getRosterItemCount()
    '''
def getRosterItems():
    '''public List<Item> getRosterItems()
    '''
def getVersion():
    '''public String getVersion()
    '''
def setVersion():
    '''public void setVersion(final String version)
    '''
def Item():
    '''public Item(final BareJid jid, final String name)
    public Item(final BareJid jid, final String name, final boolean subscriptionPending)
    '''
def getElementName():
    '''public String getElementName()
    '''
def getUser():
    '''public String getUser()
    '''
def getJid():
    '''public BareJid getJid()
    '''
def getName():
    '''public String getName()
    '''
def setName():
    '''public void setName(final String name)
    '''
def getItemType():
    '''public ItemType getItemType()
    '''
def setItemType():
    '''public void setItemType(final ItemType itemType)
    '''
def setSubscriptionPending():
    '''public void setSubscriptionPending(final boolean subscriptionPending)
    '''
def isSubscriptionPending():
    '''public boolean isSubscriptionPending()
    '''
def isApproved():
    '''public boolean isApproved()
    '''
def setApproved():
    '''public void setApproved(final boolean approved)
    '''
def getGroupNames():
    '''public Set<String> getGroupNames()
    '''
def addGroupName():
    '''public void addGroupName(final String groupName)
    '''
def removeGroupName():
    '''public void removeGroupName(final String groupName)
    '''
def toXML():
    '''public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def fromString():
    '''public static ItemType fromString(final String string)
    '''
def asSymbol():
    '''public String asSymbol()
    '''
