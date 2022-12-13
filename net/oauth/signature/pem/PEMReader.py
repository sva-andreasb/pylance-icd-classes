PRIVATE_PKCS1_MARKER = "String  \"-----BEGIN RSA PRIVATE KEY-----\""
PRIVATE_PKCS8_MARKER = "String  \"-----BEGIN PRIVATE KEY-----\""
CERTIFICATE_X509_MARKER = "String  \"-----BEGIN CERTIFICATE-----\""
PUBLIC_X509_MARKER = "String  \"-----BEGIN PUBLIC KEY-----\""
def PEMReader():
    '''    public PEMReader(final InputStream inStream)
    public PEMReader(final byte[] buffer)
    public PEMReader(final String fileName)
    '''
def getDerBytes():
    '''    public byte[] getDerBytes()
    '''
def getBeginMarker():
    '''    public String getBeginMarker()
    '''
