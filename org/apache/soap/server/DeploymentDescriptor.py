SERVICE_TYPE_RPC = "int  0"
SERVICE_TYPE_MESSAGE = "int  1"
SCOPE_REQUEST = "int  0"
SCOPE_SESSION = "int  1"
SCOPE_APPLICATION = "int  2"
PROVIDER_JAVA = "byte  0"
PROVIDER_SCRIPT_FILE = "byte  1"
PROVIDER_SCRIPT_STRING = "byte  2"
PROVIDER_USER_DEFINED = "byte  3"
def ():
    '''returns DeploymentDescriptor\n\n
    ()\n
    '''
def buildFaultRouter():
    '''returns SOAPFaultRouter\n\n
    buildFaultRouter(final SOAPContext soapContext)\n
    '''
def getCheckMustUnderstands():
    '''returns boolean\n\n
    getCheckMustUnderstands()\n
    '''
def getDefaultSMRClass():
    '''returns String\n\n
    getDefaultSMRClass()\n
    '''
def getFaultListener():
    '''returns String[]\n\n
    getFaultListener()\n
    '''
def getID():
    '''returns String\n\n
    getID()\n
    '''
def getIsStatic():
    '''returns boolean\n\n
    getIsStatic()\n
    '''
def getMappings():
    '''returns TypeMapping[]\n\n
    getMappings()\n
    '''
def getMethods():
    '''returns String[]\n\n
    getMethods()\n
    '''
def getProps():
    '''returns Hashtable\n\n
    getProps()\n
    '''
def getProviderClass():
    '''returns String\n\n
    getProviderClass()\n
    '''
def getProviderType():
    '''returns byte\n\n
    getProviderType()\n
    '''
def getScope():
    '''returns int\n\n
    getScope()\n
    '''
def getScriptFilenameOrString():
    '''returns String\n\n
    getScriptFilenameOrString()\n
    '''
def getScriptLanguage():
    '''returns String\n\n
    getScriptLanguage()\n
    '''
def getServiceClass():
    '''returns String\n\n
    getServiceClass()\n
    '''
def getServiceType():
    '''returns int\n\n
    getServiceType()\n
    '''
def setCheckMustUnderstands():
    '''returns None\n\n
    setCheckMustUnderstands(final boolean checkMustUnderstands)\n
    '''
def setDefaultSMRClass():
    '''returns None\n\n
    setDefaultSMRClass(final String defaultSMRClass)\n
    '''
def setFaultListener():
    '''returns None\n\n
    setFaultListener(final String[] faultListener)\n
    '''
def setID():
    '''returns None\n\n
    setID(final String id)\n
    '''
def setIsStatic():
    '''returns None\n\n
    setIsStatic(final boolean isStatic)\n
    '''
def setMappings():
    '''returns None\n\n
    setMappings(final TypeMapping[] mappings)\n
    '''
def setMethods():
    '''returns None\n\n
    setMethods(final String[] methods)\n
    '''
def setProps():
    '''returns None\n\n
    setProps(final Hashtable props)\n
    '''
def setProviderClass():
    '''returns None\n\n
    setProviderClass(final String providerClass)\n
    '''
def setProviderType():
    '''returns None\n\n
    setProviderType(final byte providerType)\n
    '''
def setScope():
    '''returns None\n\n
    setScope(final int scope)\n
    '''
def setScriptFilenameOrString():
    '''returns None\n\n
    setScriptFilenameOrString(final String scriptFilenameOrString)\n
    '''
def setScriptLanguage():
    '''returns None\n\n
    setScriptLanguage(final String scriptLanguage)\n
    '''
def setServiceClass():
    '''returns None\n\n
    setServiceClass(final String serviceClass)\n
    '''
def setServiceType():
    '''returns None\n\n
    setServiceType(final int serviceType)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toXML():
    '''returns None\n\n
    toXML(final Writer out)\n
    '''
