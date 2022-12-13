UNKNOWN_PROTOCOL = "String  "
UNKNOWN_GENERATION_ID = "int  -1"
UNKNOWN_MEMBER_ID = "String  "
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def JoinGroupResponse():
'''public JoinGroupResponse(final Errors error, final int generationId, final String groupProtocol, final String memberId, final String leaderId, final Map<String, ByteBuffer> groupMembers)
public JoinGroupResponse(final int throttleTimeMs, final Errors error, final int generationId, final String groupProtocol, final String memberId, final String leaderId, final Map<String, ByteBuffer> groupMembers)
public JoinGroupResponse(final Struct struct)
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def error():
'''public Errors error()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def generationId():
'''public int generationId()
'''
pass
def groupProtocol():
'''public String groupProtocol()
'''
pass
def memberId():
'''public String memberId()
'''
pass
def leaderId():
'''public String leaderId()
'''
pass
def isLeader():
'''public boolean isLeader()
'''
pass
def members():
'''public Map<String, ByteBuffer> members()
'''
pass
def parse():
'''public static JoinGroupResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def toString():
'''public String toString()
'''
pass
