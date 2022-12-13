def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def DescribeConfigsRequest():
    '''    public DescribeConfigsRequest(final short version, final Map<Resource, Collection<String>> resourceToConfigNames, final boolean includeSynonyms)
    public DescribeConfigsRequest(final Struct struct, final short version)
    '''
def resources():
    '''    public Collection<Resource> resources()
    '''
def configNames():
    '''    public Collection<String> configNames(final Resource resource)
    '''
def includeSynonyms():
    '''    public boolean includeSynonyms()
    public Builder includeSynonyms(final boolean includeSynonyms)
    '''
def getErrorResponse():
    '''    public DescribeConfigsResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def parse():
    '''    public static DescribeConfigsRequest parse(final ByteBuffer buffer, final short version)
    '''
def Builder():
    '''    public Builder(final Map<Resource, Collection<String>> resourceToConfigNames)
    public Builder(final Collection<Resource> resources)
    '''
def build():
    '''    public DescribeConfigsRequest build(final short version)
    '''
