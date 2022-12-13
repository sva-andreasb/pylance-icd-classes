def CertificateValidator():
    '''public CertificateValidator(final KeyStore trustStore, final Collection<? extends CRL> crls)
    '''
def validate():
    '''public void validate(final KeyStore keyStore)
    public String validate(final KeyStore keyStore, final String keyAlias)
    public void validate(final KeyStore keyStore, final Certificate cert)
    public void validate(final Certificate[] certChain)
    '''
def getTrustStore():
    '''public KeyStore getTrustStore()
    '''
def getMaxCertPathLength():
    '''public int getMaxCertPathLength()
    '''
def setMaxCertPathLength():
    '''public void setMaxCertPathLength(final int maxCertPathLength)
    '''
def isEnableCRLDP():
    '''public boolean isEnableCRLDP()
    '''
def setEnableCRLDP():
    '''public void setEnableCRLDP(final boolean enableCRLDP)
    '''
def isEnableOCSP():
    '''public boolean isEnableOCSP()
    '''
def setEnableOCSP():
    '''public void setEnableOCSP(final boolean enableOCSP)
    '''
def getOcspResponderURL():
    '''public String getOcspResponderURL()
    '''
def setOcspResponderURL():
    '''public void setOcspResponderURL(final String ocspResponderURL)
    '''
