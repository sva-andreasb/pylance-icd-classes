def PdfPKCS7():
'''public PdfPKCS7(final byte[] contentsKey, final byte[] certsKey, final String provider)
public PdfPKCS7(final byte[] contentsKey, final String provider)
public PdfPKCS7(final PrivateKey privKey, final Certificate[] certChain, final CRL[] crlList, final String hashAlgorithm, final String provider, final boolean hasRSAdata)
'''
pass
def update():
'''public void update(final byte[] buf, final int off, final int len)
'''
pass
def verify():
'''public boolean verify()
'''
pass
def getCertificates():
'''public Certificate[] getCertificates()
'''
pass
def getCRLs():
'''public Collection getCRLs()
'''
pass
def getSigningCertificate():
'''public X509Certificate getSigningCertificate()
'''
pass
def getVersion():
'''public int getVersion()
'''
pass
def getSigningInfoVersion():
'''public int getSigningInfoVersion()
'''
pass
def getDigestAlgorithm():
'''public String getDigestAlgorithm()
'''
pass
def getHashAlgorithm():
'''public String getHashAlgorithm()
'''
pass
def loadCacertsKeyStore():
'''public static KeyStore loadCacertsKeyStore()
public static KeyStore loadCacertsKeyStore(final String provider)
'''
pass
def verifyCertificate():
'''public static String verifyCertificate(final X509Certificate cert, final Collection crls, Calendar calendar)
'''
pass
def verifyCertificates():
'''public static Object[] verifyCertificates(final Certificate[] certs, final KeyStore keystore, final Collection crls, Calendar calendar)
'''
pass
def getIssuerFields():
'''public static X509Name getIssuerFields(final X509Certificate cert)
'''
pass
def getSubjectFields():
'''public static X509Name getSubjectFields(final X509Certificate cert)
'''
pass
def getEncodedPKCS1():
'''public byte[] getEncodedPKCS1()
'''
pass
def setExternalDigest():
'''public void setExternalDigest(final byte[] digest, final byte[] RSAdata, final String digestEncryptionAlgorithm)
'''
pass
def getEncodedPKCS7():
'''public byte[] getEncodedPKCS7()
public byte[] getEncodedPKCS7(final byte[] secondDigest, final Calendar signingTime)
'''
pass
def getAuthenticatedAttributeBytes():
'''public byte[] getAuthenticatedAttributeBytes(final byte[] secondDigest, final Calendar signingTime)
'''
pass
def getReason():
'''public String getReason()
'''
pass
def setReason():
'''public void setReason(final String reason)
'''
pass
def getLocation():
'''public String getLocation()
'''
pass
def setLocation():
'''public void setLocation(final String location)
'''
pass
def getSignDate():
'''public Calendar getSignDate()
'''
pass
def setSignDate():
'''public void setSignDate(final Calendar signDate)
'''
pass
def getSignName():
'''public String getSignName()
'''
pass
def setSignName():
'''public void setSignName(final String signName)
'''
pass
def X509Name():
'''public X509Name(final ASN1Sequence seq)
public X509Name(final String dirName)
'''
pass
def getField():
'''public String getField(final String name)
'''
pass
def getFieldArray():
'''public ArrayList getFieldArray(final String name)
'''
pass
def getFields():
'''public HashMap getFields()
'''
pass
def toString():
'''public String toString()
'''
pass
def X509NameTokenizer():
'''public X509NameTokenizer(final String oid)
'''
pass
def hasMoreTokens():
'''public boolean hasMoreTokens()
'''
pass
def nextToken():
'''public String nextToken()
'''
pass
