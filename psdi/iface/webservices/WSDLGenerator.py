WSDL_NS = "String  \"http://schemas.xmlsoap.org/wsdl/\""
MAXIMO_WSDL_NS_PREFIX = "String  \"mxws\""
TRANSPORT_HTTP = "String  \"http://schemas.xmlsoap.org/soap/http\""
STYLE_DOCUMENT = "String  \"document\""
USE_LITERAL = "String  \"literal\""
WSDLDIR = "String  \"wsdl\""
def WSDLGenerator():
    '''public WSDLGenerator(final String serviceName)
    public WSDLGenerator(final String serviceName, final String serviceDesc, final String serviceLongDesc)
    public WSDLGenerator(final String serviceName, final String serviceDesc, final String serviceLongDesc, final String soapVersion)
    public WSDLGenerator(final WSRegistryInfo wsRegInfo)
    '''
def getPortName():
    '''public QName getPortName(final boolean soap12)
    '''
def getBindingName():
    '''public String getBindingName(final boolean soap12)
    '''
def getServiceDescription():
    '''public String getServiceDescription()
    '''
def getWsdlFileName():
    '''public String getWsdlFileName()
    '''
def getWsdlNSUri():
    '''public String getWsdlNSUri()
    '''
def getServiceName():
    '''public String getServiceName()
    '''
def getWsdlUrl():
    '''public String getWsdlUrl()
    '''
def getSoapAddressUrl():
    '''public String getSoapAddressUrl()
    '''
def isWsdlGenerated():
    '''public boolean isWsdlGenerated()
    '''
