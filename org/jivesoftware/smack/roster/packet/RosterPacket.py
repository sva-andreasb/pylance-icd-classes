ELEMENT = "String  item""
NAMESPACE = "String  jabber:iq:roster""
GROUP = "String  group""
def RosterPacket():
'''public RosterPacket()
'''
pass
def addRosterItem():
'''public void addRosterItem(final Item item)
'''
pass
def getRosterItemCount():
'''public int getRosterItemCount()
'''
pass
def getRosterItems():
'''public List<Item> getRosterItems()
'''
pass
def getVersion():
'''public String getVersion()
'''
pass
def setVersion():
'''public void setVersion(final String version)
'''
pass
def Item():
'''public Item(final BareJid jid, final String name)
public Item(final BareJid jid, final String name, final boolean subscriptionPending)
'''
pass
def getElementName():
'''public String getElementName()
'''
pass
def getUser():
'''public String getUser()
'''
pass
def getJid():
'''public BareJid getJid()
'''
pass
def getName():
'''public String getName()
'''
pass
def setName():
'''public void setName(final String name)
'''
pass
def getItemType():
'''public ItemType getItemType()
'''
pass
def setItemType():
'''public void setItemType(final ItemType itemType)
'''
pass
def setSubscriptionPending():
'''public void setSubscriptionPending(final boolean subscriptionPending)
'''
pass
def isSubscriptionPending():
'''public boolean isSubscriptionPending()
'''
pass
def isApproved():
'''public boolean isApproved()
'''
pass
def setApproved():
'''public void setApproved(final boolean approved)
'''
pass
def getGroupNames():
'''public Set<String> getGroupNames()
'''
pass
def addGroupName():
'''public void addGroupName(final String groupName)
'''
pass
def removeGroupName():
'''public void removeGroupName(final String groupName)
'''
pass
def toXML():
'''public XmlStringBuilder toXML(final String enclosingNamespace)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def fromString():
'''public static ItemType fromString(final String string)
'''
pass
def asSymbol():
'''public String asSymbol()
'''
pass
