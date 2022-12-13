XML_NS = "String  http://www.w3.org/2000/xmlns/""
XML_DIGSIG_NS = "String  http://www.w3.org/2000/09/xmldsig#""
OO_DIGSIG_NS = "String  http://schemas.openxmlformats.org/package/2006/digital-signature""
MS_DIGSIG_NS = "String  http://schemas.microsoft.com/office/2006/digsig""
XADES_132_NS = "String  http://uri.etsi.org/01903/v1.3.2#""
XADES_141_NS = "String  http://uri.etsi.org/01903/v1.4.1#""
def setSignatureConfig():
'''public void setSignatureConfig(final SignatureConfig signatureConfig)
'''
pass
def preSign():
'''public void preSign(final Document document, final List<Reference> references, final List<XMLObject> objects)
'''
pass
def postSign():
'''public void postSign(final Document document)
'''
pass
def newReference():
'''public static Reference newReference(final String uri, final List<Transform> transforms, final String type, final String id, final byte[] digestValue, final SignatureConfig signatureConfig)
'''
pass
def brokenJvmWorkaround():
'''public static void brokenJvmWorkaround(final Reference reference)
'''
pass
def run():
'''public Void run()
'''
pass
