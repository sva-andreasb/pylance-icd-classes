def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def DescribeConfigsRequest():
'''public DescribeConfigsRequest(final short version, final Map<Resource, Collection<String>> resourceToConfigNames, final boolean includeSynonyms)
public DescribeConfigsRequest(final Struct struct, final short version)
'''
pass
def resources():
'''public Collection<Resource> resources()
'''
pass
def configNames():
'''public Collection<String> configNames(final Resource resource)
'''
pass
def includeSynonyms():
'''public boolean includeSynonyms()
public Builder includeSynonyms(final boolean includeSynonyms)
'''
pass
def getErrorResponse():
'''public DescribeConfigsResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def parse():
'''public static DescribeConfigsRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def Builder():
'''public Builder(final Map<Resource, Collection<String>> resourceToConfigNames)
public Builder(final Collection<Resource> resources)
'''
pass
def build():
'''public DescribeConfigsRequest build(final short version)
'''
pass
