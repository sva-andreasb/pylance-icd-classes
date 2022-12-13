ELEMENT = "String  \"affiliation\""
def Affiliation():
    '''    public Affiliation(final String node, final Type affiliation)
    public Affiliation(final String node, final Type affiliation, final AffiliationNamespace namespace)
    public Affiliation(final BareJid jid, final Type affiliation)
    public Affiliation(final BareJid jid, final Type affiliation, final AffiliationNamespace namespace)
    '''
def getNodeId():
    '''    public String getNodeId()
    '''
def getNode():
    '''    public String getNode()
    '''
def getType():
    '''    public Type getType()
    '''
def getAffiliation():
    '''    public Type getAffiliation()
    '''
def getJid():
    '''    public BareJid getJid()
    '''
def getElementName():
    '''    public String getElementName()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def getPubSubNamespace():
    '''    public PubSubNamespace getPubSubNamespace()
    '''
def isAffiliationModification():
    '''    public boolean isAffiliationModification()
    '''
def toXML():
    '''    public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def fromXmlns():
    '''    public static AffiliationNamespace fromXmlns(final String xmlns)
    '''
