QNAME_TYPE = "int  1"
QNAME_DOCUMENT_TYPE = "int  2"
QNAME_ACCESSOR_ELEMENT = "int  3"
QNAME_ACCESSOR_ATTRIBUTE = "int  4"
def lookupPackageForNamespace():
    '''returns String\n\n
    lookupPackageForNamespace(final String uri)\n
    '''
def lookupPrefixForNamespace():
    '''returns String\n\n
    lookupPrefixForNamespace(final String uri)\n
    '''
def lookupSuffixForNamespace():
    '''returns String\n\n
    lookupSuffixForNamespace(final String uri)\n
    '''
def lookupJavanameForQName():
    '''returns String\n\n
    lookupJavanameForQName(final QName qname)\n
    lookupJavanameForQName(final QName qname, final int kind)\n
    '''
def getInterfaceExtensions():
    '''returns InterfaceExtension[]\n\n
    getInterfaceExtensions()\n
    getInterfaceExtensions(final String fullJavaName)\n
    '''
def getPrePostExtensions():
    '''returns PrePostExtension[]\n\n
    getPrePostExtensions()\n
    '''
def getPrePostExtension():
    '''returns PrePostExtension\n\n
    getPrePostExtension(final String fullJavaName)\n
    '''
def getUserTypes():
    '''returns UserType[]\n\n
    getUserTypes()\n
    '''
def lookupUserTypeForQName():
    '''returns UserType\n\n
    lookupUserTypeForQName(final QName qname)\n
    '''
