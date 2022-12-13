MAX_OBJNAME_LENGTH = "int  20"
def OBPGenerator():
'''public OBPGenerator(final String interactionName)
public OBPGenerator(final String interactionName, final boolean ignoreAttributes)
public OBPGenerator(final String interactionName, final boolean ignoreAttributes, final boolean ignoreWildcards)
public OBPGenerator(final String interactionName, final boolean ignoreAttributes, final boolean ignoreWildcards, final boolean ignoreRecursion)
public OBPGenerator(final String interactionName, final boolean ignoreAttributes, final boolean ignoreWildcards, final boolean ignoreRecursion, final boolean treatListAsAtomic)
public OBPGenerator(final String interactionName, final boolean ignoreAttributes, final boolean ignoreWildcards, final boolean ignoreRecursion, final boolean treatListAsAtomic, final boolean processResponse)
'''
pass
def cloneOBP():
'''public static OBPInfo cloneOBP(final OBPInfo obpInfo)
'''
pass
def parse():
'''public static OBPInfo parse(final byte[] obpDoc)
public OBPInfo parse(final File file)
'''
pass
def toBytes():
'''public static byte[] toBytes(final OBPInfo obpInfo)
'''
pass
def create():
'''public OBPInfo create(final URL wsdlURL, final String serviceName, final String portName, final String operationName)
public OBPInfo create(final WSDLInfo wsdlInfo, final String serviceName, final String portName, final String operationName)
public OBPInfo create(final InputStream wsdlStream, final String operationName)
'''
pass
def optimizeRequest():
'''public OBPInfo optimizeRequest(OBPInfo obpInfo)
'''
pass
def optimizeResponse():
'''public OBPInfo optimizeResponse(OBPInfo obpInfo)
'''
pass
def getSampleRequestXML():
'''public byte[] getSampleRequestXML()
'''
pass
def getSampleResponseXML():
'''public byte[] getSampleResponseXML()
'''
pass
