def RfcLDAPMessage():
    '''    public RfcLDAPMessage(final RfcRequest rfcRequest)
    public RfcLDAPMessage(final RfcRequest rfcRequest, final RfcControls controls)
    public RfcLDAPMessage(final ASN1Sequence asn1Sequence)
    public RfcLDAPMessage(final ASN1SequenceOf op)
    public RfcLDAPMessage(final ASN1Sequence op, final RfcControls controls)
    public RfcLDAPMessage(final ASN1Decoder asn1Decoder, final InputStream inputStream, final int n)
    '''
def getMessageID():
    '''    public final int getMessageID()
    '''
def getType():
    '''    public final int getType()
    '''
def getResponse():
    '''    public final ASN1Object getResponse()
    '''
def getRequest():
    '''    public final RfcRequest getRequest()
    '''
def isRequest():
    '''    public boolean isRequest()
    '''
def getControls():
    '''    public final RfcControls getControls()
    '''
def dupMessage():
    '''    public final Object dupMessage(final String s, final String s2, final boolean b)
    '''
def getRequestDN():
    '''    public final String getRequestDN()
    '''
def setRequestingMessage():
    '''    public final void setRequestingMessage(final LDAPMessage requestMessage)
    '''
def getRequestingMessage():
    '''    public final LDAPMessage getRequestingMessage()
    '''
