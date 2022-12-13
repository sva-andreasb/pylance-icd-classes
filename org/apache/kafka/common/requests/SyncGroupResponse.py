def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def SyncGroupResponse():
    '''    public SyncGroupResponse(final Errors error, final ByteBuffer memberState)
    public SyncGroupResponse(final int throttleTimeMs, final Errors error, final ByteBuffer memberState)
    public SyncGroupResponse(final Struct struct)
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
def memberAssignment():
    '''    public ByteBuffer memberAssignment()
    '''
def parse():
    '''    public static SyncGroupResponse parse(final ByteBuffer buffer, final short version)
    '''
