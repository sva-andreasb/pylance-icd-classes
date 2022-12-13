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
    '''    public DeploymentDescriptor()
    '''
def buildFaultRouter():
    '''    public SOAPFaultRouter buildFaultRouter(final SOAPContext soapContext)
    '''
def buildSOAPMappingRegistry():
    '''    public static SOAPMappingRegistry buildSOAPMappingRegistry(final DeploymentDescriptor deploymentDescriptor, final SOAPContext soapContext)
    '''
def fromXML():
    '''    public static DeploymentDescriptor fromXML(final Reader characterStream)
    public static DeploymentDescriptor fromXML(final Element element)
    '''
def getCheckMustUnderstands():
    '''    public boolean getCheckMustUnderstands()
    '''
def getDefaultSMRClass():
    '''    public String getDefaultSMRClass()
    '''
def getFaultListener():
    '''    public String[] getFaultListener()
    '''
def getID():
    '''    public String getID()
    '''
def getIsStatic():
    '''    public boolean getIsStatic()
    '''
def getMappings():
    '''    public TypeMapping[] getMappings()
    '''
def getMethods():
    '''    public String[] getMethods()
    '''
def getProps():
    '''    public Hashtable getProps()
    '''
def getProviderClass():
    '''    public String getProviderClass()
    '''
def getProviderType():
    '''    public byte getProviderType()
    '''
def getScope():
    '''    public int getScope()
    '''
def getScriptFilenameOrString():
    '''    public String getScriptFilenameOrString()
    '''
def getScriptLanguage():
    '''    public String getScriptLanguage()
    '''
def getServiceClass():
    '''    public String getServiceClass()
    '''
def getServiceType():
    '''    public int getServiceType()
    '''
def setCheckMustUnderstands():
    '''    public void setCheckMustUnderstands(final boolean checkMustUnderstands)
    '''
def setDefaultSMRClass():
    '''    public void setDefaultSMRClass(final String defaultSMRClass)
    '''
def setFaultListener():
    '''    public void setFaultListener(final String[] faultListener)
    '''
def setID():
    '''    public void setID(final String id)
    '''
def setIsStatic():
    '''    public void setIsStatic(final boolean isStatic)
    '''
def setMappings():
    '''    public void setMappings(final TypeMapping[] mappings)
    '''
def setMethods():
    '''    public void setMethods(final String[] methods)
    '''
def setProps():
    '''    public void setProps(final Hashtable props)
    '''
def setProviderClass():
    '''    public void setProviderClass(final String providerClass)
    '''
def setProviderType():
    '''    public void setProviderType(final byte providerType)
    '''
def setScope():
    '''    public void setScope(final int scope)
    '''
def setScriptFilenameOrString():
    '''    public void setScriptFilenameOrString(final String scriptFilenameOrString)
    '''
def setScriptLanguage():
    '''    public void setScriptLanguage(final String scriptLanguage)
    '''
def setServiceClass():
    '''    public void setServiceClass(final String serviceClass)
    '''
def setServiceType():
    '''    public void setServiceType(final int serviceType)
    '''
def toString():
    '''    public String toString()
    '''
def toXML():
    '''    public void toXML(final Writer out)
    '''
