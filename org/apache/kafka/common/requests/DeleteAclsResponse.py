def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def DeleteAclsResponse():
    '''public DeleteAclsResponse(final int throttleTimeMs, final List<AclFilterResponse> responses)
    public DeleteAclsResponse(final Struct struct)
    '''
def throttleTimeMs():
    '''public int throttleTimeMs()
    '''
def responses():
    '''public List<AclFilterResponse> responses()
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def parse():
    '''public static DeleteAclsResponse parse(final ByteBuffer buffer, final short version)
    '''
def toString():
    '''public String toString()
    public String toString()
    public String toString()
    '''
def AclDeletionResult():
    '''public AclDeletionResult(final ApiError error, final AclBinding acl)
    public AclDeletionResult(final AclBinding acl)
    '''
def error():
    '''public ApiError error()
    public ApiError error()
    '''
def acl():
    '''public AclBinding acl()
    '''
def AclFilterResponse():
    '''public AclFilterResponse(final ApiError error, final Collection<AclDeletionResult> deletions)
    public AclFilterResponse(final Collection<AclDeletionResult> deletions)
    '''
def deletions():
    '''public Collection<AclDeletionResult> deletions()
    '''
