PRIVATE_PKCS1_MARKER = "String  \"-----BEGIN RSA PRIVATE KEY-----\""
PRIVATE_PKCS8_MARKER = "String  \"-----BEGIN PRIVATE KEY-----\""
CERTIFICATE_X509_MARKER = "String  \"-----BEGIN CERTIFICATE-----\""
PUBLIC_X509_MARKER = "String  \"-----BEGIN PUBLIC KEY-----\""
def ():
    '''returns PEMReader\n\n
    (final InputStream inStream)\n
    (final byte[] buffer)\n
    (final String fileName)\n
    '''
def getDerBytes():
    '''returns byte[]\n\n
    getDerBytes()\n
    '''
def getBeginMarker():
    '''returns String\n\n
    getBeginMarker()\n
    '''
