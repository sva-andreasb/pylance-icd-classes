WSDL_NS = "String  \"http://schemas.xmlsoap.org/wsdl/\""
MAXIMO_WSDL_NS_PREFIX = "String  \"mxws\""
TRANSPORT_HTTP = "String  \"http://schemas.xmlsoap.org/soap/http\""
STYLE_DOCUMENT = "String  \"document\""
USE_LITERAL = "String  \"literal\""
WSDLDIR = "String  \"wsdl\""
def ():
    '''returns WSDLGenerator\n\n
    (final String serviceName)\n
    (final String serviceName, final String serviceDesc, final String serviceLongDesc)\n
    (final String serviceName, final String serviceDesc, final String serviceLongDesc, final String soapVersion)\n
    (final WSRegistryInfo wsRegInfo)\n
    '''
def getPortName():
    '''returns QName\n\n
    getPortName(final boolean soap12)\n
    '''
def getBindingName():
    '''returns String\n\n
    getBindingName(final boolean soap12)\n
    '''
def getServiceDescription():
    '''returns String\n\n
    getServiceDescription()\n
    '''
def getWsdlFileName():
    '''returns String\n\n
    getWsdlFileName()\n
    '''
def getWsdlNSUri():
    '''returns String\n\n
    getWsdlNSUri()\n
    '''
def getServiceName():
    '''returns String\n\n
    getServiceName()\n
    '''
def getWsdlUrl():
    '''returns String\n\n
    getWsdlUrl()\n
    '''
def getSoapAddressUrl():
    '''returns String\n\n
    getSoapAddressUrl()\n
    '''
def isWsdlGenerated():
    '''returns boolean\n\n
    isWsdlGenerated()\n
    '''
