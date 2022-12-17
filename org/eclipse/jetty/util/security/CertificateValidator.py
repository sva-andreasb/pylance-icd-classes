def ():
    '''returns CertificateValidator\n\n
    (final KeyStore trustStore, final Collection<? extends CRL> crls)\n
    '''
def validate():
    '''returns None\n\n
    validate(final KeyStore keyStore)\n
    validate(final KeyStore keyStore, final String keyAlias)\n
    validate(final KeyStore keyStore, final Certificate cert)\n
    validate(final Certificate[] certChain)\n
    '''
def getTrustStore():
    '''returns KeyStore\n\n
    getTrustStore()\n
    '''
def getMaxCertPathLength():
    '''returns int\n\n
    getMaxCertPathLength()\n
    '''
def setMaxCertPathLength():
    '''returns None\n\n
    setMaxCertPathLength(final int maxCertPathLength)\n
    '''
def isEnableCRLDP():
    '''returns boolean\n\n
    isEnableCRLDP()\n
    '''
def setEnableCRLDP():
    '''returns None\n\n
    setEnableCRLDP(final boolean enableCRLDP)\n
    '''
def isEnableOCSP():
    '''returns boolean\n\n
    isEnableOCSP()\n
    '''
def setEnableOCSP():
    '''returns None\n\n
    setEnableOCSP(final boolean enableOCSP)\n
    '''
def getOcspResponderURL():
    '''returns String\n\n
    getOcspResponderURL()\n
    '''
def setOcspResponderURL():
    '''returns None\n\n
    setOcspResponderURL(final String ocspResponderURL)\n
    '''
