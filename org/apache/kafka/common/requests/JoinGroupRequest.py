UNKNOWN_MEMBER_ID = "String  \"\""
def ():
    '''returns Builder\n\n
    (final Struct struct, final short versionId)\n
    (final String name, final ByteBuffer metadata)\n
    (final String groupId, final int sessionTimeout, final String memberId, final String protocolType, final List<ProtocolMetadata> groupProtocols)\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def groupId():
    '''returns String\n\n
    groupId()\n
    '''
def sessionTimeout():
    '''returns int\n\n
    sessionTimeout()\n
    '''
def rebalanceTimeout():
    '''returns int\n\n
    rebalanceTimeout()\n
    '''
def memberId():
    '''returns String\n\n
    memberId()\n
    '''
def groupProtocols():
    '''returns List<ProtocolMetadata>\n\n
    groupProtocols()\n
    '''
def protocolType():
    '''returns String\n\n
    protocolType()\n
    '''
def name():
    '''returns String\n\n
    name()\n
    '''
def metadata():
    '''returns ByteBuffer\n\n
    metadata()\n
    '''
def setRebalanceTimeout():
    '''returns Builder\n\n
    setRebalanceTimeout(final int rebalanceTimeout)\n
    '''
def build():
    '''returns JoinGroupRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
