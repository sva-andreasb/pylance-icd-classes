def SignatureInfo():
    '''public SignatureInfo()
    '''
def getSignatureConfig():
    '''public SignatureConfig getSignatureConfig()
    '''
def setSignatureConfig():
    '''public void setSignatureConfig(final SignatureConfig signatureConfig)
    '''
def verifySignature():
    '''public boolean verifySignature()
    '''
def confirmSignature():
    '''public void confirmSignature()
    '''
def signDigest():
    '''public byte[] signDigest(final byte[] digest)
    '''
def getSignatureParts():
    '''public Iterable<SignaturePart> getSignatureParts()
    '''
def iterator():
    '''public Iterator<SignaturePart> iterator()
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def next():
    '''public SignaturePart next()
    '''
def remove():
    '''public void remove()
    '''
def preSign():
    '''public DigestInfo preSign(final Document document, final List<DigestInfo> digestInfos)
    '''
def postSign():
    '''public void postSign(final Document document, final byte[] signatureValue)
    '''
def getPackagePart():
    '''public PackagePart getPackagePart()
    '''
def getSigner():
    '''public X509Certificate getSigner()
    '''
def getCertChain():
    '''public List<X509Certificate> getCertChain()
    '''
def getSignatureDocument():
    '''public SignatureDocument getSignatureDocument()
    '''
def validate():
    '''public boolean validate()
    '''
