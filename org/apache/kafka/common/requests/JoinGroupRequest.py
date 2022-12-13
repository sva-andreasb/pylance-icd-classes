UNKNOWN_MEMBER_ID = "String  "
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def JoinGroupRequest():
'''public JoinGroupRequest(final Struct struct, final short versionId)
'''
pass
def getErrorResponse():
'''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def groupId():
'''public String groupId()
'''
pass
def sessionTimeout():
'''public int sessionTimeout()
'''
pass
def rebalanceTimeout():
'''public int rebalanceTimeout()
'''
pass
def memberId():
'''public String memberId()
'''
pass
def groupProtocols():
'''public List<ProtocolMetadata> groupProtocols()
'''
pass
def protocolType():
'''public String protocolType()
'''
pass
def parse():
'''public static JoinGroupRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def ProtocolMetadata():
'''public ProtocolMetadata(final String name, final ByteBuffer metadata)
'''
pass
def name():
'''public String name()
'''
pass
def metadata():
'''public ByteBuffer metadata()
'''
pass
def Builder():
'''public Builder(final String groupId, final int sessionTimeout, final String memberId, final String protocolType, final List<ProtocolMetadata> groupProtocols)
'''
pass
def setRebalanceTimeout():
'''public Builder setRebalanceTimeout(final int rebalanceTimeout)
'''
pass
def build():
'''public JoinGroupRequest build(final short version)
'''
pass
def toString():
'''public String toString()
'''
pass
