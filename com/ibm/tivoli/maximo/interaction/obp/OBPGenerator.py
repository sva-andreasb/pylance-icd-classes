MAX_OBJNAME_LENGTH = "int  20"
def ():
    '''returns OBPGenerator\n\n
    (final String interactionName)\n
    (final String interactionName, final boolean ignoreAttributes)\n
    (final String interactionName, final boolean ignoreAttributes, final boolean ignoreWildcards)\n
    (final String interactionName, final boolean ignoreAttributes, final boolean ignoreWildcards, final boolean ignoreRecursion)\n
    (final String interactionName, final boolean ignoreAttributes, final boolean ignoreWildcards, final boolean ignoreRecursion, final boolean treatListAsAtomic)\n
    (final String interactionName, final boolean ignoreAttributes, final boolean ignoreWildcards, final boolean ignoreRecursion, final boolean treatListAsAtomic, final boolean processResponse)\n
    '''
def parse():
    '''returns OBPInfo\n\n
    parse(final File file)\n
    '''
def create():
    '''returns OBPInfo\n\n
    create(final URL wsdlURL, final String serviceName, final String portName, final String operationName)\n
    create(final WSDLInfo wsdlInfo, final String serviceName, final String portName, final String operationName)\n
    create(final InputStream wsdlStream, final String operationName)\n
    '''
def optimizeRequest():
    '''returns OBPInfo\n\n
    optimizeRequest(OBPInfo obpInfo)\n
    '''
def optimizeResponse():
    '''returns OBPInfo\n\n
    optimizeResponse(OBPInfo obpInfo)\n
    '''
def getSampleRequestXML():
    '''returns byte[]\n\n
    getSampleRequestXML()\n
    '''
def getSampleResponseXML():
    '''returns byte[]\n\n
    getSampleResponseXML()\n
    '''
