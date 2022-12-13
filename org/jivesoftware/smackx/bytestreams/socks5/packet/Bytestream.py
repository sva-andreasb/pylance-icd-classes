ELEMENT = "String  \"query\""
NAMESPACE = "String  \"http://jabber.org/protocol/bytestreams\""
def Bytestream():
    '''    public Bytestream()
    public Bytestream(final String SID)
    '''
def setSessionID():
    '''    public void setSessionID(final String sessionID)
    '''
def getSessionID():
    '''    public String getSessionID()
    '''
def setMode():
    '''    public void setMode(final Mode mode)
    '''
def getMode():
    '''    public Mode getMode()
    '''
def addStreamHost():
    '''    public StreamHost addStreamHost(final Jid JID, final String address)
    public StreamHost addStreamHost(final Jid JID, final String address, final int port)
    public void addStreamHost(final StreamHost host)
    '''
def getStreamHosts():
    '''    public List<StreamHost> getStreamHosts()
    '''
def getStreamHost():
    '''    public StreamHost getStreamHost(final Jid JID)
    '''
def countStreamHosts():
    '''    public int countStreamHosts()
    '''
def setUsedHost():
    '''    public void setUsedHost(final Jid JID)
    '''
def getUsedHost():
    '''    public StreamHostUsed getUsedHost()
    '''
def getToActivate():
    '''    public Activate getToActivate()
    '''
def setToActivate():
    '''    public void setToActivate(final Jid targetID)
    '''
def StreamHost():
    '''    public StreamHost(final Jid jid, final String address)
    public StreamHost(final Jid JID, final String address, final int port)
    '''
def getJID():
    '''    public Jid getJID()
    public Jid getJID()
    '''
def getAddress():
    '''    public String getAddress()
    '''
def getPort():
    '''    public int getPort()
    '''
def getElementName():
    '''    public String getElementName()
    public String getElementName()
    public String getElementName()
    '''
def toXML():
    '''    public XmlStringBuilder toXML(final String enclosingNamespace)
    public XmlStringBuilder toXML(final String enclosingNamespace)
    public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def StreamHostUsed():
    '''    public StreamHostUsed(final Jid JID)
    '''
def Activate():
    '''    public Activate(final Jid target)
    '''
def getTarget():
    '''    public Jid getTarget()
    '''
def fromName():
    '''    public static Mode fromName(final String name)
    '''
