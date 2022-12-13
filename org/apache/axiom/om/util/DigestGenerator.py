md5DigestAlgorithm = "String  \"MD5\""
shaDigestAlgorithm = "String  \"SHA\""
sha1DigestAlgorithm = "String  \"SHA1\""
def getDigest():
    '''public byte[] getDigest(final OMDocument document, final String digestAlgorithm)
    public byte[] getDigest(final OMNode node, final String digestAlgorithm)
    public byte[] getDigest(final OMElement element, final String digestAlgorithm)
    public byte[] getDigest(final OMProcessingInstruction pi, final String digestAlgorithm)
    public byte[] getDigest(final OMAttribute attribute, final String digestAlgorithm)
    public byte[] getDigest(final OMText text, final String digestAlgorithm)
    '''
def getExpandedName():
    '''public String getExpandedName(final OMElement element)
    public String getExpandedName(final OMAttribute attribute)
    '''
def getAttributesWithoutNS():
    '''public Collection getAttributesWithoutNS(final OMElement element)
    '''
def getValidElements():
    '''public Collection getValidElements(final OMDocument document)
    '''
def getStringRepresentation():
    '''public String getStringRepresentation(final byte[] array)
    '''
def compareOMNode():
    '''public boolean compareOMNode(final OMNode node, final OMNode comparingNode, final String digestAlgorithm)
    '''
def compareOMDocument():
    '''public boolean compareOMDocument(final OMDocument document, final OMDocument comparingDocument, final String digestAlgorithm)
    '''
def compareOMAttribute():
    '''public boolean compareOMAttribute(final OMAttribute attribute, final OMAttribute comparingAttribute, final String digestAlgorithm)
    '''
