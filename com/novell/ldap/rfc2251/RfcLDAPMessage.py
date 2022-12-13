def RfcLDAPMessage():
'''public RfcLDAPMessage(final RfcRequest rfcRequest)
public RfcLDAPMessage(final RfcRequest rfcRequest, final RfcControls controls)
public RfcLDAPMessage(final ASN1Sequence asn1Sequence)
public RfcLDAPMessage(final ASN1SequenceOf op)
public RfcLDAPMessage(final ASN1Sequence op, final RfcControls controls)
public RfcLDAPMessage(final ASN1Decoder asn1Decoder, final InputStream inputStream, final int n)
'''
pass
def getMessageID():
'''public final int getMessageID()
'''
pass
def getType():
'''public final int getType()
'''
pass
def getResponse():
'''public final ASN1Object getResponse()
'''
pass
def getRequest():
'''public final RfcRequest getRequest()
'''
pass
def isRequest():
'''public boolean isRequest()
'''
pass
def getControls():
'''public final RfcControls getControls()
'''
pass
def dupMessage():
'''public final Object dupMessage(final String s, final String s2, final boolean b)
'''
pass
def getRequestDN():
'''public final String getRequestDN()
'''
pass
def setRequestingMessage():
'''public final void setRequestingMessage(final LDAPMessage requestMessage)
'''
pass
def getRequestingMessage():
'''public final LDAPMessage getRequestingMessage()
'''
pass
