QNAME_TYPE = "int  1"
QNAME_DOCUMENT_TYPE = "int  2"
QNAME_ACCESSOR_ELEMENT = "int  3"
QNAME_ACCESSOR_ATTRIBUTE = "int  4"
def lookupPackageForNamespace():
    '''public String lookupPackageForNamespace(final String uri)
    '''
def lookupPrefixForNamespace():
    '''public String lookupPrefixForNamespace(final String uri)
    '''
def lookupSuffixForNamespace():
    '''public String lookupSuffixForNamespace(final String uri)
    '''
def lookupJavanameForQName():
    '''public String lookupJavanameForQName(final QName qname)
    public String lookupJavanameForQName(final QName qname, final int kind)
    '''
def getInterfaceExtensions():
    '''public InterfaceExtension[] getInterfaceExtensions()
    public InterfaceExtension[] getInterfaceExtensions(final String fullJavaName)
    '''
def getPrePostExtensions():
    '''public PrePostExtension[] getPrePostExtensions()
    '''
def getPrePostExtension():
    '''public PrePostExtension getPrePostExtension(final String fullJavaName)
    '''
def getUserTypes():
    '''public UserType[] getUserTypes()
    '''
def lookupUserTypeForQName():
    '''public UserType lookupUserTypeForQName(final QName qname)
    '''
