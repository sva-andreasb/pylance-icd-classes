ELEMENT = "String  \"status\""
NAMESPACE = "String  \"http://jabber.org/protocol/muc#user\""
def MUCUser():
    '''    public MUCUser()
    '''
def getElementName():
    '''    public String getElementName()
    public String getElementName()
    public String getElementName()
    public String getElementName()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def toXML():
    '''    public XmlStringBuilder toXML(final String enclosingNamespace)
    public XmlStringBuilder toXML(final String enclosingNamespace)
    public XmlStringBuilder toXML(final String enclosingNamespace)
    public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def getInvite():
    '''    public Invite getInvite()
    '''
def getDecline():
    '''    public Decline getDecline()
    '''
def getItem():
    '''    public MUCItem getItem()
    '''
def getPassword():
    '''    public String getPassword()
    '''
def getStatus():
    '''    public Set<Status> getStatus()
    '''
def hasStatus():
    '''    public boolean hasStatus()
    '''
def getDestroy():
    '''    public Destroy getDestroy()
    '''
def setInvite():
    '''    public void setInvite(final Invite invite)
    '''
def setDecline():
    '''    public void setDecline(final Decline decline)
    '''
def setItem():
    '''    public void setItem(final MUCItem item)
    '''
def setPassword():
    '''    public void setPassword(final String string)
    '''
def addStatusCodes():
    '''    public void addStatusCodes(final Set<Status> statusCodes)
    '''
def addStatusCode():
    '''    public void addStatusCode(final Status status)
    '''
def setDestroy():
    '''    public void setDestroy(final Destroy destroy)
    '''
def getFrom():
    '''    public static MUCUser getFrom(final Stanza packet)
    public EntityJid getFrom()
    public EntityBareJid getFrom()
    '''
def from():
    '''    public static MUCUser from(final Stanza packet)
    '''
def Invite():
    '''    public Invite(final String reason, final EntityFullJid from)
    public Invite(final String reason, final EntityBareJid to)
    public Invite(final String reason, final EntityJid from, final EntityBareJid to)
    '''
def getReason():
    '''    public String getReason()
    public String getReason()
    '''
def getTo():
    '''    public EntityBareJid getTo()
    public EntityBareJid getTo()
    '''
def Decline():
    '''    public Decline(final String reason, final EntityBareJid to)
    public Decline(final String reason, final EntityBareJid from, final EntityBareJid to)
    '''
def create():
    '''    public static Status create(final String string)
    public static Status create(final Integer i)
    '''
def getCode():
    '''    public int getCode()
    '''
def toString():
    '''    public String toString()
    '''
def equals():
    '''    public boolean equals(final Object other)
    '''
def hashCode():
    '''    public int hashCode()
    '''
