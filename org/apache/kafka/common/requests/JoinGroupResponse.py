UNKNOWN_PROTOCOL = "String  \"\""
UNKNOWN_GENERATION_ID = "int  -1"
UNKNOWN_MEMBER_ID = "String  \"\""
def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def JoinGroupResponse():
    '''public JoinGroupResponse(final Errors error, final int generationId, final String groupProtocol, final String memberId, final String leaderId, final Map<String, ByteBuffer> groupMembers)
    public JoinGroupResponse(final int throttleTimeMs, final Errors error, final int generationId, final String groupProtocol, final String memberId, final String leaderId, final Map<String, ByteBuffer> groupMembers)
    public JoinGroupResponse(final Struct struct)
    '''
def throttleTimeMs():
    '''public int throttleTimeMs()
    '''
def error():
    '''public Errors error()
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def generationId():
    '''public int generationId()
    '''
def groupProtocol():
    '''public String groupProtocol()
    '''
def memberId():
    '''public String memberId()
    '''
def leaderId():
    '''public String leaderId()
    '''
def isLeader():
    '''public boolean isLeader()
    '''
def members():
    '''public Map<String, ByteBuffer> members()
    '''
def parse():
    '''public static JoinGroupResponse parse(final ByteBuffer buffer, final short version)
    '''
def toString():
    '''public String toString()
    '''
