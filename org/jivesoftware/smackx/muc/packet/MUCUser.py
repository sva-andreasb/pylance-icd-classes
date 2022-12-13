ELEMENT = "String  status""
NAMESPACE = "String  http://jabber.org/protocol/muc#user""
def MUCUser():
'''public MUCUser()
'''
pass
def getElementName():
'''public String getElementName()
public String getElementName()
public String getElementName()
public String getElementName()
'''
pass
def getNamespace():
'''public String getNamespace()
'''
pass
def toXML():
'''public XmlStringBuilder toXML(final String enclosingNamespace)
public XmlStringBuilder toXML(final String enclosingNamespace)
public XmlStringBuilder toXML(final String enclosingNamespace)
public XmlStringBuilder toXML(final String enclosingNamespace)
'''
pass
def getInvite():
'''public Invite getInvite()
'''
pass
def getDecline():
'''public Decline getDecline()
'''
pass
def getItem():
'''public MUCItem getItem()
'''
pass
def getPassword():
'''public String getPassword()
'''
pass
def getStatus():
'''public Set<Status> getStatus()
'''
pass
def hasStatus():
'''public boolean hasStatus()
'''
pass
def getDestroy():
'''public Destroy getDestroy()
'''
pass
def setInvite():
'''public void setInvite(final Invite invite)
'''
pass
def setDecline():
'''public void setDecline(final Decline decline)
'''
pass
def setItem():
'''public void setItem(final MUCItem item)
'''
pass
def setPassword():
'''public void setPassword(final String string)
'''
pass
def addStatusCodes():
'''public void addStatusCodes(final Set<Status> statusCodes)
'''
pass
def addStatusCode():
'''public void addStatusCode(final Status status)
'''
pass
def setDestroy():
'''public void setDestroy(final Destroy destroy)
'''
pass
def getFrom():
'''public static MUCUser getFrom(final Stanza packet)
public EntityJid getFrom()
public EntityBareJid getFrom()
'''
pass
def from():
'''public static MUCUser from(final Stanza packet)
'''
pass
def Invite():
'''public Invite(final String reason, final EntityFullJid from)
public Invite(final String reason, final EntityBareJid to)
public Invite(final String reason, final EntityJid from, final EntityBareJid to)
'''
pass
def getReason():
'''public String getReason()
public String getReason()
'''
pass
def getTo():
'''public EntityBareJid getTo()
public EntityBareJid getTo()
'''
pass
def Decline():
'''public Decline(final String reason, final EntityBareJid to)
public Decline(final String reason, final EntityBareJid from, final EntityBareJid to)
'''
pass
def create():
'''public static Status create(final String string)
public static Status create(final Integer i)
'''
pass
def getCode():
'''public int getCode()
'''
pass
def toString():
'''public String toString()
'''
pass
def equals():
'''public boolean equals(final Object other)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
