ATTR_CID = "String  \"cid\""
ATTR_HOST = "String  \"host\""
ATTR_JID = "String  \"jid\""
ATTR_PORT = "String  \"port\""
ATTR_PRIORITY = "String  \"priority\""
ATTR_TYPE = "String  \"type\""
def JingleS5BTransportCandidate():
    '''    public JingleS5BTransportCandidate(final String candidateId, final String host, final Jid jid, final int port, final int priority, final Type type)
    public JingleS5BTransportCandidate(final Bytestream.StreamHost streamHost, final int priority, final Type type)
    '''
def getCandidateId():
    '''    public String getCandidateId()
    '''
def getHost():
    '''    public String getHost()
    '''
def getJid():
    '''    public Jid getJid()
    '''
def getPort():
    '''    public int getPort()
    '''
def getPriority():
    '''    public int getPriority()
    '''
def getType():
    '''    public Type getType()
    '''
def toXML():
    '''    public CharSequence toXML(final String enclosingNamespace)
    '''
def getBuilder():
    '''    public static Builder getBuilder()
    '''
def getWeight():
    '''    public int getWeight()
    '''
def fromString():
    '''    public static Type fromString(final String name)
    '''
def setCandidateId():
    '''    public Builder setCandidateId(final String cid)
    '''
def setHost():
    '''    public Builder setHost(final String host)
    '''
def setJid():
    '''    public Builder setJid(final String jid)
    '''
def setPort():
    '''    public Builder setPort(final int port)
    '''
def setPriority():
    '''    public Builder setPriority(final int priority)
    '''
def setType():
    '''    public Builder setType(final Type type)
    '''
def build():
    '''    public JingleS5BTransportCandidate build()
    '''
