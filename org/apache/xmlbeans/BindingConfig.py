QNAME_TYPE = "int  1"
QNAME_DOCUMENT_TYPE = "int  2"
QNAME_ACCESSOR_ELEMENT = "int  3"
QNAME_ACCESSOR_ATTRIBUTE = "int  4"
def lookupPackageForNamespace():
'''public String lookupPackageForNamespace(final String uri)
'''
pass
def lookupPrefixForNamespace():
'''public String lookupPrefixForNamespace(final String uri)
'''
pass
def lookupSuffixForNamespace():
'''public String lookupSuffixForNamespace(final String uri)
'''
pass
def lookupJavanameForQName():
'''public String lookupJavanameForQName(final QName qname)
public String lookupJavanameForQName(final QName qname, final int kind)
'''
pass
def getInterfaceExtensions():
'''public InterfaceExtension[] getInterfaceExtensions()
public InterfaceExtension[] getInterfaceExtensions(final String fullJavaName)
'''
pass
def getPrePostExtensions():
'''public PrePostExtension[] getPrePostExtensions()
'''
pass
def getPrePostExtension():
'''public PrePostExtension getPrePostExtension(final String fullJavaName)
'''
pass
def getUserTypes():
'''public UserType[] getUserTypes()
'''
pass
def lookupUserTypeForQName():
'''public UserType lookupUserTypeForQName(final QName qname)
'''
pass