def ():
    '''returns X509NameTokenizer\n\n
    (final byte[] contentsKey, final byte[] certsKey, final String provider)\n
    (final byte[] contentsKey, final String provider)\n
    (final PrivateKey privKey, final Certificate[] certChain, final CRL[] crlList, final String hashAlgorithm, final String provider, final boolean hasRSAdata)\n
    (final ASN1Sequence seq)\n
    (final String dirName)\n
    (final String oid)\n
    '''
def update():
    '''returns None\n\n
    update(final byte[] buf, final int off, final int len)\n
    '''
def verify():
    '''returns boolean\n\n
    verify()\n
    '''
def getCertificates():
    '''returns Certificate[]\n\n
    getCertificates()\n
    '''
def getCRLs():
    '''returns Collection\n\n
    getCRLs()\n
    '''
def getSigningCertificate():
    '''returns X509Certificate\n\n
    getSigningCertificate()\n
    '''
def getVersion():
    '''returns int\n\n
    getVersion()\n
    '''
def getSigningInfoVersion():
    '''returns int\n\n
    getSigningInfoVersion()\n
    '''
def getDigestAlgorithm():
    '''returns String\n\n
    getDigestAlgorithm()\n
    '''
def getHashAlgorithm():
    '''returns String\n\n
    getHashAlgorithm()\n
    '''
def getEncodedPKCS1():
    '''returns byte[]\n\n
    getEncodedPKCS1()\n
    '''
def setExternalDigest():
    '''returns None\n\n
    setExternalDigest(final byte[] digest, final byte[] RSAdata, final String digestEncryptionAlgorithm)\n
    '''
def getEncodedPKCS7():
    '''returns byte[]\n\n
    getEncodedPKCS7()\n
    getEncodedPKCS7(final byte[] secondDigest, final Calendar signingTime)\n
    '''
def getAuthenticatedAttributeBytes():
    '''returns byte[]\n\n
    getAuthenticatedAttributeBytes(final byte[] secondDigest, final Calendar signingTime)\n
    '''
def getReason():
    '''returns String\n\n
    getReason()\n
    '''
def setReason():
    '''returns None\n\n
    setReason(final String reason)\n
    '''
def getLocation():
    '''returns String\n\n
    getLocation()\n
    '''
def setLocation():
    '''returns None\n\n
    setLocation(final String location)\n
    '''
def getSignDate():
    '''returns Calendar\n\n
    getSignDate()\n
    '''
def setSignDate():
    '''returns None\n\n
    setSignDate(final Calendar signDate)\n
    '''
def getSignName():
    '''returns String\n\n
    getSignName()\n
    '''
def setSignName():
    '''returns None\n\n
    setSignName(final String signName)\n
    '''
def getField():
    '''returns String\n\n
    getField(final String name)\n
    '''
def getFieldArray():
    '''returns ArrayList\n\n
    getFieldArray(final String name)\n
    '''
def getFields():
    '''returns HashMap\n\n
    getFields()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def hasMoreTokens():
    '''returns boolean\n\n
    hasMoreTokens()\n
    '''
def nextToken():
    '''returns String\n\n
    nextToken()\n
    '''
