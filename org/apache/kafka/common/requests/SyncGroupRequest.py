def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def SyncGroupRequest():
    '''public SyncGroupRequest(final Struct struct, final short version)
    '''
def getErrorResponse():
    '''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def groupId():
    '''public String groupId()
    '''
def generationId():
    '''public int generationId()
    '''
def groupAssignment():
    '''public Map<String, ByteBuffer> groupAssignment()
    '''
def memberId():
    '''public String memberId()
    '''
def parse():
    '''public static SyncGroupRequest parse(final ByteBuffer buffer, final short version)
    '''
def Builder():
    '''public Builder(final String groupId, final int generationId, final String memberId, final Map<String, ByteBuffer> groupAssignment)
    '''
def build():
    '''public SyncGroupRequest build(final short version)
    '''
def toString():
    '''public String toString()
    '''
