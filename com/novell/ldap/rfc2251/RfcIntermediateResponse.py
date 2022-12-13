TAG_RESPONSE_NAME = "int  0"
TAG_RESPONSE = "int  1"
def RfcIntermediateResponse():
    '''public RfcIntermediateResponse(final ASN1Decoder asn1Decoder, final InputStream inputStream, final int n)
    '''
def getResponseName():
    '''public final RfcLDAPOID getResponseName()
    '''
def getResponse():
    '''public final ASN1OctetString getResponse()
    '''
def getIdentifier():
    '''public final ASN1Identifier getIdentifier()
    '''
def getResultCode():
    '''public final ASN1Enumerated getResultCode()
    '''
def getMatchedDN():
    '''public final RfcLDAPDN getMatchedDN()
    '''
def getReferral():
    '''public final RfcReferral getReferral()
    '''
def getErrorMessage():
    '''public final RfcLDAPString getErrorMessage()
    '''
