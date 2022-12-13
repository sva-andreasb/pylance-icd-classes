NAMESPACE_V1 = "String  \"urn:xmpp:jingle:transports:s5b:1\""
ATTR_DSTADDR = "String  \"dstaddr\""
ATTR_MODE = "String  \"mode\""
ATTR_SID = "String  \"sid\""
def getStreamId():
    '''    public String getStreamId()
    '''
def getDestinationAddress():
    '''    public String getDestinationAddress()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def hasCandidate():
    '''    public boolean hasCandidate(final String candidateId)
    '''
def getCandidate():
    '''    public JingleS5BTransportCandidate getCandidate(final String candidateId)
    '''
def getBuilder():
    '''    public static Builder getBuilder()
    '''
def Builder():
    '''    public Builder()
    '''
def setStreamId():
    '''    public Builder setStreamId(final String sid)
    '''
def setDestinationAddress():
    '''    public Builder setDestinationAddress(final String dstAddr)
    '''
def setMode():
    '''    public Builder setMode(final Bytestream.Mode mode)
    '''
def addTransportCandidate():
    '''    public Builder addTransportCandidate(final JingleS5BTransportCandidate candidate)
    '''
def setTransportInfo():
    '''    public Builder setTransportInfo(final JingleContentTransportInfo info)
    '''
def setCandidateUsed():
    '''    public Builder setCandidateUsed(final String candidateId)
    '''
def setCandidateActivated():
    '''    public Builder setCandidateActivated(final String candidateId)
    '''
def setCandidateError():
    '''    public Builder setCandidateError()
    '''
def setProxyError():
    '''    public Builder setProxyError()
    '''
def build():
    '''    public JingleS5BTransport build()
    '''
