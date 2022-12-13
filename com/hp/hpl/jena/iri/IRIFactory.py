def iriImplementation():
    '''public static IRIFactory iriImplementation()
    '''
def uriImplementation():
    '''public static IRIFactory uriImplementation()
    '''
def semanticWebImplementation():
    '''public static IRIFactory semanticWebImplementation()
    '''
def jenaImplementation():
    '''public static IRIFactory jenaImplementation()
    '''
def IRIFactory():
    '''public IRIFactory()
    public IRIFactory(final IRIFactory template)
    '''
def setSameSchemeRelativeReferences():
    '''public void setSameSchemeRelativeReferences(final String scheme)
    '''
def allowUnwiseCharacters():
    '''public void allowUnwiseCharacters()
    '''
def setQueryCharacterRestrictions():
    '''public void setQueryCharacterRestrictions(final boolean restrict)
    '''
def setEncoding():
    '''public void setEncoding(final String enc)
    '''
def create():
    '''public IRI create(final String scheme, final String userInfo, final String host, final int port, final String path, final String query, final String fragment)
    public IRI create(final String scheme, final String authority, final String path, final String query, final String fragment)
    '''
def construct():
    '''public IRI construct(final String scheme, final String userInfo, final String host, final int port, final String path, final String query, final String fragment)
    public IRI construct(final String scheme, final String authority, final String path, final String query, final String fragment)
    '''
def isError():
    '''public boolean isError(final int code)
    '''
def isWarning():
    '''public boolean isWarning(final int code)
    '''
def setIsError():
    '''public void setIsError(final int code, final boolean set)
    '''
def setIsWarning():
    '''public void setIsWarning(final int code, final boolean set)
    '''
def ignoring():
    '''public boolean ignoring(final int code)
    '''
def useSpecificationURI():
    '''public void useSpecificationURI(final boolean asErrors)
    '''
def useSpecificationIRI():
    '''public void useSpecificationIRI(final boolean asErrors)
    '''
def useSpecificationRDF():
    '''public void useSpecificationRDF(final boolean asErrors)
    '''
def useSpecificationXMLSchema():
    '''public void useSpecificationXMLSchema(final boolean asErrors)
    '''
def useSpecificationXMLSystemID():
    '''public void useSpecificationXMLSystemID(final boolean asErrors)
    '''
def useSpecificationXLink():
    '''public void useSpecificationXLink(final boolean asErrors)
    '''
def shouldViolation():
    '''public void shouldViolation(final boolean isError, final boolean isWarning)
    '''
def securityViolation():
    '''public void securityViolation(final boolean isError, final boolean isWarning)
    '''
def dnsViolation():
    '''public void dnsViolation(final boolean isError, final boolean isWarning)
    '''
def mintingViolation():
    '''public void mintingViolation(final boolean isError, final boolean isWarning)
    '''
def useSchemeSpecificRules():
    '''public void useSchemeSpecificRules(final String scheme, final boolean asErrors)
    '''
def setJenaImplementation():
    '''public static void setJenaImplementation(final IRIFactory jf)
    '''
def setIriImplementation():
    '''public static void setIriImplementation(final IRIFactory iriF)
    '''
def setUriImplementation():
    '''public static void setUriImplementation(final IRIFactory uriF)
    '''
def setSemanticWebImplementation():
    '''public static void setSemanticWebImplementation(final IRIFactory sw)
    '''
