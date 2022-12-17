UNKNOWN_STATE = "String  \"\""
UNKNOWN_PROTOCOL_TYPE = "String  \"\""
UNKNOWN_PROTOCOL = "String  \"\""
def ():
    '''returns GroupMember\n\n
    (final Map<String, GroupMetadata> groups)\n
    (final int throttleTimeMs, final Map<String, GroupMetadata> groups)\n
    (final Struct struct)\n
    (final Errors error, final String state, final String protocolType, final String protocol, final List<GroupMember> members)\n
    (final String memberId, final String clientId, final String clientHost, final ByteBuffer memberMetadata, final ByteBuffer memberAssignment)\n
    '''
def throttleTimeMs():
    '''returns int\n\n
    throttleTimeMs()\n
    '''
def error():
    '''returns Errors\n\n
    error()\n
    '''
def state():
    '''returns String\n\n
    state()\n
    '''
def protocolType():
    '''returns String\n\n
    protocolType()\n
    '''
def protocol():
    '''returns String\n\n
    protocol()\n
    '''
def members():
    '''returns List<GroupMember>\n\n
    members()\n
    '''
def memberId():
    '''returns String\n\n
    memberId()\n
    '''
def clientId():
    '''returns String\n\n
    clientId()\n
    '''
def clientHost():
    '''returns String\n\n
    clientHost()\n
    '''
def memberMetadata():
    '''returns ByteBuffer\n\n
    memberMetadata()\n
    '''
def memberAssignment():
    '''returns ByteBuffer\n\n
    memberAssignment()\n
    '''
