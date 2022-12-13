UNKNOWN_STATE = "String  \"\""
UNKNOWN_PROTOCOL_TYPE = "String  \"\""
UNKNOWN_PROTOCOL = "String  \"\""
def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def DescribeGroupsResponse():
    '''    public DescribeGroupsResponse(final Map<String, GroupMetadata> groups)
    public DescribeGroupsResponse(final int throttleTimeMs, final Map<String, GroupMetadata> groups)
    public DescribeGroupsResponse(final Struct struct)
    '''
def throttleTimeMs():
    '''    public int throttleTimeMs()
    '''
def groups():
    '''    public Map<String, GroupMetadata> groups()
    '''
def errorCounts():
    '''    public Map<Errors, Integer> errorCounts()
    '''
def fromError():
    '''    public static DescribeGroupsResponse fromError(final Errors error, final List<String> groupIds)
    public static DescribeGroupsResponse fromError(final int throttleTimeMs, final Errors error, final List<String> groupIds)
    '''
def parse():
    '''    public static DescribeGroupsResponse parse(final ByteBuffer buffer, final short version)
    '''
def GroupMetadata():
    '''    public GroupMetadata(final Errors error, final String state, final String protocolType, final String protocol, final List<GroupMember> members)
    '''
def error():
    '''    public Errors error()
    '''
def state():
    '''    public String state()
    '''
def protocolType():
    '''    public String protocolType()
    '''
def protocol():
    '''    public String protocol()
    '''
def members():
    '''    public List<GroupMember> members()
    '''
def forError():
    '''    public static GroupMetadata forError(final Errors error)
    '''
def GroupMember():
    '''    public GroupMember(final String memberId, final String clientId, final String clientHost, final ByteBuffer memberMetadata, final ByteBuffer memberAssignment)
    '''
def memberId():
    '''    public String memberId()
    '''
def clientId():
    '''    public String clientId()
    '''
def clientHost():
    '''    public String clientHost()
    '''
def memberMetadata():
    '''    public ByteBuffer memberMetadata()
    '''
def memberAssignment():
    '''    public ByteBuffer memberAssignment()
    '''
