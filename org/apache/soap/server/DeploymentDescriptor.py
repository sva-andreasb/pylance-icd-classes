SERVICE_TYPE_RPC = "int  0"
SERVICE_TYPE_MESSAGE = "int  1"
SCOPE_REQUEST = "int  0"
SCOPE_SESSION = "int  1"
SCOPE_APPLICATION = "int  2"
PROVIDER_JAVA = "byte  0"
PROVIDER_SCRIPT_FILE = "byte  1"
PROVIDER_SCRIPT_STRING = "byte  2"
PROVIDER_USER_DEFINED = "byte  3"
def DeploymentDescriptor():
'''public DeploymentDescriptor()
'''
pass
def buildFaultRouter():
'''public SOAPFaultRouter buildFaultRouter(final SOAPContext soapContext)
'''
pass
def buildSOAPMappingRegistry():
'''public static SOAPMappingRegistry buildSOAPMappingRegistry(final DeploymentDescriptor deploymentDescriptor, final SOAPContext soapContext)
'''
pass
def fromXML():
'''public static DeploymentDescriptor fromXML(final Reader characterStream)
public static DeploymentDescriptor fromXML(final Element element)
'''
pass
def getCheckMustUnderstands():
'''public boolean getCheckMustUnderstands()
'''
pass
def getDefaultSMRClass():
'''public String getDefaultSMRClass()
'''
pass
def getFaultListener():
'''public String[] getFaultListener()
'''
pass
def getID():
'''public String getID()
'''
pass
def getIsStatic():
'''public boolean getIsStatic()
'''
pass
def getMappings():
'''public TypeMapping[] getMappings()
'''
pass
def getMethods():
'''public String[] getMethods()
'''
pass
def getProps():
'''public Hashtable getProps()
'''
pass
def getProviderClass():
'''public String getProviderClass()
'''
pass
def getProviderType():
'''public byte getProviderType()
'''
pass
def getScope():
'''public int getScope()
'''
pass
def getScriptFilenameOrString():
'''public String getScriptFilenameOrString()
'''
pass
def getScriptLanguage():
'''public String getScriptLanguage()
'''
pass
def getServiceClass():
'''public String getServiceClass()
'''
pass
def getServiceType():
'''public int getServiceType()
'''
pass
def setCheckMustUnderstands():
'''public void setCheckMustUnderstands(final boolean checkMustUnderstands)
'''
pass
def setDefaultSMRClass():
'''public void setDefaultSMRClass(final String defaultSMRClass)
'''
pass
def setFaultListener():
'''public void setFaultListener(final String[] faultListener)
'''
pass
def setID():
'''public void setID(final String id)
'''
pass
def setIsStatic():
'''public void setIsStatic(final boolean isStatic)
'''
pass
def setMappings():
'''public void setMappings(final TypeMapping[] mappings)
'''
pass
def setMethods():
'''public void setMethods(final String[] methods)
'''
pass
def setProps():
'''public void setProps(final Hashtable props)
'''
pass
def setProviderClass():
'''public void setProviderClass(final String providerClass)
'''
pass
def setProviderType():
'''public void setProviderType(final byte providerType)
'''
pass
def setScope():
'''public void setScope(final int scope)
'''
pass
def setScriptFilenameOrString():
'''public void setScriptFilenameOrString(final String scriptFilenameOrString)
'''
pass
def setScriptLanguage():
'''public void setScriptLanguage(final String scriptLanguage)
'''
pass
def setServiceClass():
'''public void setServiceClass(final String serviceClass)
'''
pass
def setServiceType():
'''public void setServiceType(final int serviceType)
'''
pass
def toString():
'''public String toString()
'''
pass
def toXML():
'''public void toXML(final Writer out)
'''
pass
