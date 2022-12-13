def PdfPKCS7():
    '''    public PdfPKCS7(final byte[] contentsKey, final byte[] certsKey, final String provider)
    public PdfPKCS7(final byte[] contentsKey, final String provider)
    public PdfPKCS7(final PrivateKey privKey, final Certificate[] certChain, final CRL[] crlList, final String hashAlgorithm, final String provider, final boolean hasRSAdata)
    '''
def update():
    '''    public void update(final byte[] buf, final int off, final int len)
    '''
def verify():
    '''    public boolean verify()
    '''
def getCertificates():
    '''    public Certificate[] getCertificates()
    '''
def getCRLs():
    '''    public Collection getCRLs()
    '''
def getSigningCertificate():
    '''    public X509Certificate getSigningCertificate()
    '''
def getVersion():
    '''    public int getVersion()
    '''
def getSigningInfoVersion():
    '''    public int getSigningInfoVersion()
    '''
def getDigestAlgorithm():
    '''    public String getDigestAlgorithm()
    '''
def getHashAlgorithm():
    '''    public String getHashAlgorithm()
    '''
def loadCacertsKeyStore():
    '''    public static KeyStore loadCacertsKeyStore()
    public static KeyStore loadCacertsKeyStore(final String provider)
    '''
def verifyCertificate():
    '''    public static String verifyCertificate(final X509Certificate cert, final Collection crls, Calendar calendar)
    '''
def verifyCertificates():
    '''    public static Object[] verifyCertificates(final Certificate[] certs, final KeyStore keystore, final Collection crls, Calendar calendar)
    '''
def getIssuerFields():
    '''    public static X509Name getIssuerFields(final X509Certificate cert)
    '''
def getSubjectFields():
    '''    public static X509Name getSubjectFields(final X509Certificate cert)
    '''
def getEncodedPKCS1():
    '''    public byte[] getEncodedPKCS1()
    '''
def setExternalDigest():
    '''    public void setExternalDigest(final byte[] digest, final byte[] RSAdata, final String digestEncryptionAlgorithm)
    '''
def getEncodedPKCS7():
    '''    public byte[] getEncodedPKCS7()
    public byte[] getEncodedPKCS7(final byte[] secondDigest, final Calendar signingTime)
    '''
def getAuthenticatedAttributeBytes():
    '''    public byte[] getAuthenticatedAttributeBytes(final byte[] secondDigest, final Calendar signingTime)
    '''
def getReason():
    '''    public String getReason()
    '''
def setReason():
    '''    public void setReason(final String reason)
    '''
def getLocation():
    '''    public String getLocation()
    '''
def setLocation():
    '''    public void setLocation(final String location)
    '''
def getSignDate():
    '''    public Calendar getSignDate()
    '''
def setSignDate():
    '''    public void setSignDate(final Calendar signDate)
    '''
def getSignName():
    '''    public String getSignName()
    '''
def setSignName():
    '''    public void setSignName(final String signName)
    '''
def X509Name():
    '''    public X509Name(final ASN1Sequence seq)
    public X509Name(final String dirName)
    '''
def getField():
    '''    public String getField(final String name)
    '''
def getFieldArray():
    '''    public ArrayList getFieldArray(final String name)
    '''
def getFields():
    '''    public HashMap getFields()
    '''
def toString():
    '''    public String toString()
    '''
def X509NameTokenizer():
    '''    public X509NameTokenizer(final String oid)
    '''
def hasMoreTokens():
    '''    public boolean hasMoreTokens()
    '''
def nextToken():
    '''    public String nextToken()
    '''
