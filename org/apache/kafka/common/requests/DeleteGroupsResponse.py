def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def DeleteGroupsResponse():
    '''public DeleteGroupsResponse(final Map<String, Errors> errors)
    public DeleteGroupsResponse(final int throttleTimeMs, final Map<String, Errors> errors)
    public DeleteGroupsResponse(final Struct struct)
    '''
def throttleTimeMs():
    '''public int throttleTimeMs()
    '''
def errors():
    '''public Map<String, Errors> errors()
    '''
def hasError():
    '''public boolean hasError(final String group)
    '''
def get():
    '''public Errors get(final String group)
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def parse():
    '''public static DeleteGroupsResponse parse(final ByteBuffer buffer, final short version)
    '''
