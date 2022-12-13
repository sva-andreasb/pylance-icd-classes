REFERRAL = "int  3"
def RfcLDAPResult():
    '''    public RfcLDAPResult(final ASN1Enumerated asn1Enumerated, final RfcLDAPDN rfcLDAPDN, final RfcLDAPString rfcLDAPString)
    public RfcLDAPResult(final ASN1Enumerated asn1Enumerated, final RfcLDAPDN rfcLDAPDN, final RfcLDAPString rfcLDAPString, final RfcReferral rfcReferral)
    public RfcLDAPResult(final ASN1Decoder asn1Decoder, final InputStream inputStream, final int n)
    '''
def getResultCode():
    '''    public final ASN1Enumerated getResultCode()
    '''
def getMatchedDN():
    '''    public final RfcLDAPDN getMatchedDN()
    '''
def getErrorMessage():
    '''    public final RfcLDAPString getErrorMessage()
    '''
def getReferral():
    '''    public final RfcReferral getReferral()
    '''
