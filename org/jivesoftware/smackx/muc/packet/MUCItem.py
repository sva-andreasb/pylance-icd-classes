ELEMENT = "String  \"item\""
def MUCItem():
    '''    public MUCItem(final MUCAffiliation affiliation)
    public MUCItem(final MUCRole role)
    public MUCItem(final MUCRole role, final Resourcepart nick)
    public MUCItem(final MUCAffiliation affiliation, final Jid jid, final String reason)
    public MUCItem(final MUCAffiliation affiliation, final Jid jid)
    public MUCItem(final MUCRole role, final Resourcepart nick, final String reason)
    public MUCItem(final MUCAffiliation affiliation, final MUCRole role, final Jid actor, final String reason, final Jid jid, final Resourcepart nick, final Resourcepart actorNick)
    '''
def getActor():
    '''    public Jid getActor()
    '''
def getActorNick():
    '''    public Resourcepart getActorNick()
    '''
def getReason():
    '''    public String getReason()
    '''
def getAffiliation():
    '''    public MUCAffiliation getAffiliation()
    '''
def getJid():
    '''    public Jid getJid()
    '''
def getNick():
    '''    public Resourcepart getNick()
    '''
def getRole():
    '''    public MUCRole getRole()
    '''
def toXML():
    '''    public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def getElementName():
    '''    public String getElementName()
    '''
