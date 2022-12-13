UNKNOWN_STATE = "String  "
UNKNOWN_PROTOCOL_TYPE = "String  "
UNKNOWN_PROTOCOL = "String  "
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def DescribeGroupsResponse():
'''public DescribeGroupsResponse(final Map<String, GroupMetadata> groups)
public DescribeGroupsResponse(final int throttleTimeMs, final Map<String, GroupMetadata> groups)
public DescribeGroupsResponse(final Struct struct)
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def groups():
'''public Map<String, GroupMetadata> groups()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def fromError():
'''public static DescribeGroupsResponse fromError(final Errors error, final List<String> groupIds)
public static DescribeGroupsResponse fromError(final int throttleTimeMs, final Errors error, final List<String> groupIds)
'''
pass
def parse():
'''public static DescribeGroupsResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def GroupMetadata():
'''public GroupMetadata(final Errors error, final String state, final String protocolType, final String protocol, final List<GroupMember> members)
'''
pass
def error():
'''public Errors error()
'''
pass
def state():
'''public String state()
'''
pass
def protocolType():
'''public String protocolType()
'''
pass
def protocol():
'''public String protocol()
'''
pass
def members():
'''public List<GroupMember> members()
'''
pass
def forError():
'''public static GroupMetadata forError(final Errors error)
'''
pass
def GroupMember():
'''public GroupMember(final String memberId, final String clientId, final String clientHost, final ByteBuffer memberMetadata, final ByteBuffer memberAssignment)
'''
pass
def memberId():
'''public String memberId()
'''
pass
def clientId():
'''public String clientId()
'''
pass
def clientHost():
'''public String clientHost()
'''
pass
def memberMetadata():
'''public ByteBuffer memberMetadata()
'''
pass
def memberAssignment():
'''public ByteBuffer memberAssignment()
'''
pass
