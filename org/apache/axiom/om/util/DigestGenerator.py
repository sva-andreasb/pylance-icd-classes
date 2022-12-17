md5DigestAlgorithm = "String  \"MD5\""
shaDigestAlgorithm = "String  \"SHA\""
sha1DigestAlgorithm = "String  \"SHA1\""
def getDigest():
    '''returns byte[]\n\n
    getDigest(final OMDocument document, final String digestAlgorithm)\n
    getDigest(final OMNode node, final String digestAlgorithm)\n
    getDigest(final OMElement element, final String digestAlgorithm)\n
    getDigest(final OMProcessingInstruction pi, final String digestAlgorithm)\n
    getDigest(final OMAttribute attribute, final String digestAlgorithm)\n
    getDigest(final OMText text, final String digestAlgorithm)\n
    '''
def getExpandedName():
    '''returns String\n\n
    getExpandedName(final OMElement element)\n
    getExpandedName(final OMAttribute attribute)\n
    '''
def getAttributesWithoutNS():
    '''returns Collection\n\n
    getAttributesWithoutNS(final OMElement element)\n
    '''
def getValidElements():
    '''returns Collection\n\n
    getValidElements(final OMDocument document)\n
    '''
def getStringRepresentation():
    '''returns String\n\n
    getStringRepresentation(final byte[] array)\n
    '''
def compareOMNode():
    '''returns boolean\n\n
    compareOMNode(final OMNode node, final OMNode comparingNode, final String digestAlgorithm)\n
    '''
def compareOMDocument():
    '''returns boolean\n\n
    compareOMDocument(final OMDocument document, final OMDocument comparingDocument, final String digestAlgorithm)\n
    '''
def compareOMAttribute():
    '''returns boolean\n\n
    compareOMAttribute(final OMAttribute attribute, final OMAttribute comparingAttribute, final String digestAlgorithm)\n
    '''
