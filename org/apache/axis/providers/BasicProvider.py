OPTION_WSDL_PORTTYPE = "String  \"wsdlPortType\""
OPTION_WSDL_SERVICEELEMENT = "String  \"wsdlServiceElement\""
OPTION_WSDL_SERVICEPORT = "String  \"wsdlServicePort\""
OPTION_WSDL_TARGETNAMESPACE = "String  \"wsdlTargetNamespace\""
OPTION_WSDL_INPUTSCHEMA = "String  \"wsdlInputSchema\""
OPTION_WSDL_SOAPACTION_MODE = "String  \"wsdlSoapActionMode\""
OPTION_EXTRACLASSES = "String  \"extraClasses\""
def addOperation():
    '''returns None\n\n
    addOperation(final String name, final QName qname)\n
    '''
def getOperationName():
    '''returns String\n\n
    getOperationName(final QName qname)\n
    '''
def getOperationQNames():
    '''returns QName[]\n\n
    getOperationQNames()\n
    '''
def getOperationNames():
    '''returns String[]\n\n
    getOperationNames()\n
    '''
def generateWSDL():
    '''returns None\n\n
    generateWSDL(final MessageContext msgContext)\n
    '''
