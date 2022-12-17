UNKNOWN_PROTOCOL = "String  \"\""
UNKNOWN_GENERATION_ID = "int  -1"
UNKNOWN_MEMBER_ID = "String  \"\""
def ():
    '''returns JoinGroupResponse\n\n
    (final Errors error, final int generationId, final String groupProtocol, final String memberId, final String leaderId, final Map<String, ByteBuffer> groupMembers)\n
    (final int throttleTimeMs, final Errors error, final int generationId, final String groupProtocol, final String memberId, final String leaderId, final Map<String, ByteBuffer> groupMembers)\n
    (final Struct struct)\n
    '''
def throttleTimeMs():
    '''returns int\n\n
    throttleTimeMs()\n
    '''
def error():
    '''returns Errors\n\n
    error()\n
    '''
def generationId():
    '''returns int\n\n
    generationId()\n
    '''
def groupProtocol():
    '''returns String\n\n
    groupProtocol()\n
    '''
def memberId():
    '''returns String\n\n
    memberId()\n
    '''
def leaderId():
    '''returns String\n\n
    leaderId()\n
    '''
def isLeader():
    '''returns boolean\n\n
    isLeader()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
