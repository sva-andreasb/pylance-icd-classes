def ():
    '''returns SignatureInfo\n\n
    ()\n
    '''
def getSignatureConfig():
    '''returns SignatureConfig\n\n
    getSignatureConfig()\n
    '''
def setSignatureConfig():
    '''returns None\n\n
    setSignatureConfig(final SignatureConfig signatureConfig)\n
    '''
def verifySignature():
    '''returns boolean\n\n
    verifySignature()\n
    '''
def confirmSignature():
    '''returns None\n\n
    confirmSignature()\n
    '''
def signDigest():
    '''returns byte[]\n\n
    signDigest(final byte[] digest)\n
    '''
def getSignatureParts():
    '''returns Iterable<SignaturePart>\n\n
    getSignatureParts()\n
    '''
def iterator():
    '''returns Iterator<SignaturePart>\n\n
    iterator()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns SignaturePart\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def preSign():
    '''returns DigestInfo\n\n
    preSign(final Document document, final List<DigestInfo> digestInfos)\n
    '''
def postSign():
    '''returns None\n\n
    postSign(final Document document, final byte[] signatureValue)\n
    '''
def getPackagePart():
    '''returns PackagePart\n\n
    getPackagePart()\n
    '''
def getSigner():
    '''returns X509Certificate\n\n
    getSigner()\n
    '''
def getCertChain():
    '''returns List<X509Certificate>\n\n
    getCertChain()\n
    '''
def getSignatureDocument():
    '''returns SignatureDocument\n\n
    getSignatureDocument()\n
    '''
def validate():
    '''returns boolean\n\n
    validate()\n
    '''
