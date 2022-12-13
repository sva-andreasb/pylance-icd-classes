def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def LeaveGroupResponse():
    '''    public LeaveGroupResponse(final Errors error)
    public LeaveGroupResponse(final int throttleTimeMs, final Errors error)
    public LeaveGroupResponse(final Struct struct)
    '''
def throttleTimeMs():
    '''    public int throttleTimeMs()
    '''
def error():
    '''    public Errors error()
    '''
def errorCounts():
    '''    public Map<Errors, Integer> errorCounts()
    '''
def toStruct():
    '''    public Struct toStruct(final short version)
    '''
def parse():
    '''    public static LeaveGroupResponse parse(final ByteBuffer buffer, final short versionId)
    '''
