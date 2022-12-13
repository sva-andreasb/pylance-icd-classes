def getDefaultKeyStore():
'''public static KeyStore getDefaultKeyStore()
'''
pass
def getJavaKeyStore():
'''public static KeyStore getJavaKeyStore()
'''
pass
def getPkcs12KeyStore():
'''public static KeyStore getPkcs12KeyStore()
'''
pass
def loadKeyStore():
'''public static void loadKeyStore(final KeyStore keyStore, final InputStream keyStream, final String storePass)
'''
pass
def getPrivateKey():
'''public static PrivateKey getPrivateKey(final KeyStore keyStore, final String alias, final String keyPass)
'''
pass
def loadPrivateKeyFromKeyStore():
'''public static PrivateKey loadPrivateKeyFromKeyStore(final KeyStore keyStore, final InputStream keyStream, final String storePass, final String alias, final String keyPass)
'''
pass
def getRsaKeyFactory():
'''public static KeyFactory getRsaKeyFactory()
'''
pass
def getSha1WithRsaSignatureAlgorithm():
'''public static Signature getSha1WithRsaSignatureAlgorithm()
'''
pass
def getSha256WithRsaSignatureAlgorithm():
'''public static Signature getSha256WithRsaSignatureAlgorithm()
'''
pass
def sign():
'''public static byte[] sign(final Signature signatureAlgorithm, final PrivateKey privateKey, final byte[] contentBytes)
'''
pass
def verify():
'''public static boolean verify(final Signature signatureAlgorithm, final PublicKey publicKey, final byte[] signatureBytes, final byte[] contentBytes)
public static X509Certificate verify(final Signature signatureAlgorithm, final X509TrustManager trustManager, final List<String> certChainBase64, final byte[] signatureBytes, final byte[] contentBytes)
'''
pass
def getX509CertificateFactory():
'''public static CertificateFactory getX509CertificateFactory()
'''
pass
def loadKeyStoreFromCertificates():
'''public static void loadKeyStoreFromCertificates(final KeyStore keyStore, final CertificateFactory certificateFactory, final InputStream certificateStream)
'''
pass
