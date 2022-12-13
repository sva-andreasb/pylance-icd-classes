def getDefaultKeyStore():
    '''public static KeyStore getDefaultKeyStore()
    '''
def getJavaKeyStore():
    '''public static KeyStore getJavaKeyStore()
    '''
def getPkcs12KeyStore():
    '''public static KeyStore getPkcs12KeyStore()
    '''
def loadKeyStore():
    '''public static void loadKeyStore(final KeyStore keyStore, final InputStream keyStream, final String storePass)
    '''
def getPrivateKey():
    '''public static PrivateKey getPrivateKey(final KeyStore keyStore, final String alias, final String keyPass)
    '''
def loadPrivateKeyFromKeyStore():
    '''public static PrivateKey loadPrivateKeyFromKeyStore(final KeyStore keyStore, final InputStream keyStream, final String storePass, final String alias, final String keyPass)
    '''
def getRsaKeyFactory():
    '''public static KeyFactory getRsaKeyFactory()
    '''
def getSha1WithRsaSignatureAlgorithm():
    '''public static Signature getSha1WithRsaSignatureAlgorithm()
    '''
def getSha256WithRsaSignatureAlgorithm():
    '''public static Signature getSha256WithRsaSignatureAlgorithm()
    '''
def sign():
    '''public static byte[] sign(final Signature signatureAlgorithm, final PrivateKey privateKey, final byte[] contentBytes)
    '''
def verify():
    '''public static boolean verify(final Signature signatureAlgorithm, final PublicKey publicKey, final byte[] signatureBytes, final byte[] contentBytes)
    public static X509Certificate verify(final Signature signatureAlgorithm, final X509TrustManager trustManager, final List<String> certChainBase64, final byte[] signatureBytes, final byte[] contentBytes)
    '''
def getX509CertificateFactory():
    '''public static CertificateFactory getX509CertificateFactory()
    '''
def loadKeyStoreFromCertificates():
    '''public static void loadKeyStoreFromCertificates(final KeyStore keyStore, final CertificateFactory certificateFactory, final InputStream certificateStream)
    '''
