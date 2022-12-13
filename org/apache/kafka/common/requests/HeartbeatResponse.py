def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def HeartbeatResponse():
    '''    public HeartbeatResponse(final Errors error)
    public HeartbeatResponse(final int throttleTimeMs, final Errors error)
    public HeartbeatResponse(final Struct struct)
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
def parse():
    '''    public static HeartbeatResponse parse(final ByteBuffer buffer, final short version)
    '''
