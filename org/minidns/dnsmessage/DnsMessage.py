def ():
    '''returns DnsMessage\n\n
    (final byte[] data)\n
    '''
def toArray():
    '''returns byte[]\n\n
    toArray()\n
    '''
def asDatagram():
    '''returns DatagramPacket\n\n
    asDatagram(final InetAddress address, final int port)\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final DataOutputStream dataOutputStream)\n
    '''
def getInByteBuffer():
    '''returns ByteBuffer\n\n
    getInByteBuffer()\n
    '''
def getQuestion():
    '''returns Question\n\n
    getQuestion()\n
    '''
def copyQuestions():
    '''returns List<Question>\n\n
    copyQuestions()\n
    '''
def getEdns():
    '''returns Edns\n\n
    getEdns()\n
    '''
def getOptPseudoRecord():
    '''returns Record<OPT>\n\n
    getOptPseudoRecord()\n
    '''
def isDnssecOk():
    '''returns boolean\n\n
    isDnssecOk()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def asTerminalOutput():
    '''returns String\n\n
    asTerminalOutput()\n
    '''
def asBuilder():
    '''returns Builder\n\n
    asBuilder()\n
    '''
def asNormalizedVersion():
    '''returns DnsMessage\n\n
    asNormalizedVersion()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def getValue():
    '''returns byte\n\n
    getValue()\n
    getValue()\n
    '''
def setId():
    '''returns Builder\n\n
    setId(final int id)\n
    '''
def setOpcode():
    '''returns Builder\n\n
    setOpcode(final OPCODE opcode)\n
    '''
def setResponseCode():
    '''returns Builder\n\n
    setResponseCode(final RESPONSE_CODE responseCode)\n
    '''
def setQrFlag():
    '''returns Builder\n\n
    setQrFlag(final boolean query)\n
    '''
def setAuthoritativeAnswer():
    '''returns Builder\n\n
    setAuthoritativeAnswer(final boolean authoritativeAnswer)\n
    '''
def setTruncated():
    '''returns Builder\n\n
    setTruncated(final boolean truncated)\n
    '''
def setRecursionDesired():
    '''returns Builder\n\n
    setRecursionDesired(final boolean recursionDesired)\n
    '''
def setRecursionAvailable():
    '''returns Builder\n\n
    setRecursionAvailable(final boolean recursionAvailable)\n
    '''
def setAuthenticData():
    '''returns Builder\n\n
    setAuthenticData(final boolean authenticData)\n
    '''
def setCheckDisabled():
    '''returns Builder\n\n
    setCheckDisabled(final boolean checkingDisabled)\n
    '''
def setCheckingDisabled():
    '''returns Builder\n\n
    setCheckingDisabled(final boolean checkingDisabled)\n
    '''
def copyFlagsFrom():
    '''returns None\n\n
    copyFlagsFrom(final DnsMessage dnsMessage)\n
    '''
def setReceiveTimestamp():
    '''returns Builder\n\n
    setReceiveTimestamp(final long receiveTimestamp)\n
    '''
def addQuestion():
    '''returns Builder\n\n
    addQuestion(final Question question)\n
    '''
def setQuestions():
    '''returns Builder\n\n
    setQuestions(final List<Question> questions)\n
    '''
def setQuestion():
    '''returns Builder\n\n
    setQuestion(final Question question)\n
    '''
def addAnswer():
    '''returns Builder\n\n
    addAnswer(final Record<? extends Data> answer)\n
    '''
def addAnswers():
    '''returns Builder\n\n
    addAnswers(final Collection<Record<? extends Data>> records)\n
    '''
def setAnswers():
    '''returns Builder\n\n
    setAnswers(final Collection<Record<? extends Data>> records)\n
    '''
def addNameserverRecords():
    '''returns Builder\n\n
    addNameserverRecords(final Record<? extends Data> record)\n
    '''
def setNameserverRecords():
    '''returns Builder\n\n
    setNameserverRecords(final Collection<Record<? extends Data>> records)\n
    '''
def setAdditionalResourceRecords():
    '''returns Builder\n\n
    setAdditionalResourceRecords(final Collection<Record<? extends Data>> records)\n
    '''
def addAdditionalResourceRecord():
    '''returns Builder\n\n
    addAdditionalResourceRecord(final Record<? extends Data> record)\n
    '''
def addAdditionalResourceRecords():
    '''returns Builder\n\n
    addAdditionalResourceRecords(final List<Record<? extends Data>> records)\n
    '''
def build():
    '''returns DnsMessage\n\n
    build()\n
    '''
