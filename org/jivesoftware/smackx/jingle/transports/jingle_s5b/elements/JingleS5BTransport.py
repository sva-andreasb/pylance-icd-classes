NAMESPACE_V1 = "String  urn:xmpp:jingle:transports:s5b:1""
ATTR_DSTADDR = "String  dstaddr""
ATTR_MODE = "String  mode""
ATTR_SID = "String  sid""
def getStreamId():
'''public String getStreamId()
'''
pass
def getDestinationAddress():
'''public String getDestinationAddress()
'''
pass
def getNamespace():
'''public String getNamespace()
'''
pass
def hasCandidate():
'''public boolean hasCandidate(final String candidateId)
'''
pass
def getCandidate():
'''public JingleS5BTransportCandidate getCandidate(final String candidateId)
'''
pass
def getBuilder():
'''public static Builder getBuilder()
'''
pass
def Builder():
'''public Builder()
'''
pass
def setStreamId():
'''public Builder setStreamId(final String sid)
'''
pass
def setDestinationAddress():
'''public Builder setDestinationAddress(final String dstAddr)
'''
pass
def setMode():
'''public Builder setMode(final Bytestream.Mode mode)
'''
pass
def addTransportCandidate():
'''public Builder addTransportCandidate(final JingleS5BTransportCandidate candidate)
'''
pass
def setTransportInfo():
'''public Builder setTransportInfo(final JingleContentTransportInfo info)
'''
pass
def setCandidateUsed():
'''public Builder setCandidateUsed(final String candidateId)
'''
pass
def setCandidateActivated():
'''public Builder setCandidateActivated(final String candidateId)
'''
pass
def setCandidateError():
'''public Builder setCandidateError()
'''
pass
def setProxyError():
'''public Builder setProxyError()
'''
pass
def build():
'''public JingleS5BTransport build()
'''
pass
