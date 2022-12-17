def ():
    '''returns Builder\n\n
    (final short version, final Map<Resource, Collection<String>> resourceToConfigNames, final boolean includeSynonyms)\n
    (final Struct struct, final short version)\n
    (final Map<Resource, Collection<String>> resourceToConfigNames)\n
    (final Collection<Resource> resources)\n
    '''
def resources():
    '''returns Collection<Resource>\n\n
    resources()\n
    '''
def configNames():
    '''returns Collection<String>\n\n
    configNames(final Resource resource)\n
    '''
def includeSynonyms():
    '''returns Builder\n\n
    includeSynonyms()\n
    includeSynonyms(final boolean includeSynonyms)\n
    '''
def getErrorResponse():
    '''returns DescribeConfigsResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def build():
    '''returns DescribeConfigsRequest\n\n
    build(final short version)\n
    '''
