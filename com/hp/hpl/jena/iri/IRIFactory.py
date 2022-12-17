def ():
    '''returns IRIFactory\n\n
    ()\n
    (final IRIFactory template)\n
    '''
def setSameSchemeRelativeReferences():
    '''returns None\n\n
    setSameSchemeRelativeReferences(final String scheme)\n
    '''
def allowUnwiseCharacters():
    '''returns None\n\n
    allowUnwiseCharacters()\n
    '''
def setQueryCharacterRestrictions():
    '''returns None\n\n
    setQueryCharacterRestrictions(final boolean restrict)\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final String enc)\n
    '''
def create():
    '''returns IRI\n\n
    create(final String scheme, final String userInfo, final String host, final int port, final String path, final String query, final String fragment)\n
    create(final String scheme, final String authority, final String path, final String query, final String fragment)\n
    '''
def construct():
    '''returns IRI\n\n
    construct(final String scheme, final String userInfo, final String host, final int port, final String path, final String query, final String fragment)\n
    construct(final String scheme, final String authority, final String path, final String query, final String fragment)\n
    '''
def isError():
    '''returns boolean\n\n
    isError(final int code)\n
    '''
def isWarning():
    '''returns boolean\n\n
    isWarning(final int code)\n
    '''
def setIsError():
    '''returns None\n\n
    setIsError(final int code, final boolean set)\n
    '''
def setIsWarning():
    '''returns None\n\n
    setIsWarning(final int code, final boolean set)\n
    '''
def ignoring():
    '''returns boolean\n\n
    ignoring(final int code)\n
    '''
def useSpecificationURI():
    '''returns None\n\n
    useSpecificationURI(final boolean asErrors)\n
    '''
def useSpecificationIRI():
    '''returns None\n\n
    useSpecificationIRI(final boolean asErrors)\n
    '''
def useSpecificationRDF():
    '''returns None\n\n
    useSpecificationRDF(final boolean asErrors)\n
    '''
def useSpecificationXMLSchema():
    '''returns None\n\n
    useSpecificationXMLSchema(final boolean asErrors)\n
    '''
def useSpecificationXMLSystemID():
    '''returns None\n\n
    useSpecificationXMLSystemID(final boolean asErrors)\n
    '''
def useSpecificationXLink():
    '''returns None\n\n
    useSpecificationXLink(final boolean asErrors)\n
    '''
def shouldViolation():
    '''returns None\n\n
    shouldViolation(final boolean isError, final boolean isWarning)\n
    '''
def securityViolation():
    '''returns None\n\n
    securityViolation(final boolean isError, final boolean isWarning)\n
    '''
def dnsViolation():
    '''returns None\n\n
    dnsViolation(final boolean isError, final boolean isWarning)\n
    '''
def mintingViolation():
    '''returns None\n\n
    mintingViolation(final boolean isError, final boolean isWarning)\n
    '''
def useSchemeSpecificRules():
    '''returns None\n\n
    useSchemeSpecificRules(final String scheme, final boolean asErrors)\n
    '''
