TEXT = "String  \"text\""
ITEM = "String  \"item\""
def getStanzaId():
    '''    public String getStanzaId()
    '''
def getPacketID():
    '''    public String getPacketID()
    '''
def setStanzaId():
    '''    public void setStanzaId(final String id)
    public String setStanzaId()
    '''
def setPacketID():
    '''    public void setPacketID(final String packetID)
    '''
def hasStanzaIdSet():
    '''    public boolean hasStanzaIdSet()
    '''
def getTo():
    '''    public Jid getTo()
    '''
def setTo():
    '''    public void setTo(final String to)
    public void setTo(final Jid to)
    '''
def getFrom():
    '''    public Jid getFrom()
    '''
def setFrom():
    '''    public void setFrom(final String from)
    public void setFrom(final Jid from)
    '''
def getError():
    '''    public StanzaError getError()
    '''
def setError():
    '''    public void setError(final StanzaError error)
    public void setError(final StanzaError.Builder xmppErrorBuilder)
    '''
def getLanguage():
    '''    public String getLanguage()
    '''
def setLanguage():
    '''    public void setLanguage(final String language)
    '''
def getExtensions():
    '''    public List<ExtensionElement> getExtensions()
    public List<ExtensionElement> getExtensions(final String elementName, final String namespace)
    '''
def getExtension():
    '''    public ExtensionElement getExtension(final String namespace)
    public <PE extends ExtensionElement> PE getExtension(final String elementName, final String namespace)
    '''
def addExtension():
    '''    public void addExtension(final ExtensionElement extension)
    '''
def overrideExtension():
    '''    public ExtensionElement overrideExtension(final ExtensionElement extension)
    '''
def addExtensions():
    '''    public void addExtensions(final Collection<ExtensionElement> extensions)
    '''
def hasExtension():
    '''    public boolean hasExtension(final String elementName, final String namespace)
    public boolean hasExtension(final String namespace)
    '''
def removeExtension():
    '''    public ExtensionElement removeExtension(final String elementName, final String namespace)
    public ExtensionElement removeExtension(final ExtensionElement extension)
    '''
def getDefaultLanguage():
    '''    public static String getDefaultLanguage()
    '''
