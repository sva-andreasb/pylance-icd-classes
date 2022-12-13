UNKNOWN_MEMBER_ID = "String  \"\""
def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def JoinGroupRequest():
    '''    public JoinGroupRequest(final Struct struct, final short versionId)
    '''
def getErrorResponse():
    '''    public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def groupId():
    '''    public String groupId()
    '''
def sessionTimeout():
    '''    public int sessionTimeout()
    '''
def rebalanceTimeout():
    '''    public int rebalanceTimeout()
    '''
def memberId():
    '''    public String memberId()
    '''
def groupProtocols():
    '''    public List<ProtocolMetadata> groupProtocols()
    '''
def protocolType():
    '''    public String protocolType()
    '''
def parse():
    '''    public static JoinGroupRequest parse(final ByteBuffer buffer, final short version)
    '''
def ProtocolMetadata():
    '''    public ProtocolMetadata(final String name, final ByteBuffer metadata)
    '''
def name():
    '''    public String name()
    '''
def metadata():
    '''    public ByteBuffer metadata()
    '''
def Builder():
    '''    public Builder(final String groupId, final int sessionTimeout, final String memberId, final String protocolType, final List<ProtocolMetadata> groupProtocols)
    '''
def setRebalanceTimeout():
    '''    public Builder setRebalanceTimeout(final int rebalanceTimeout)
    '''
def build():
    '''    public JoinGroupRequest build(final short version)
    '''
def toString():
    '''    public String toString()
    '''
