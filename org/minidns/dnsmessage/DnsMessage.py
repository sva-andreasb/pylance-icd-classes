def DnsMessage():
    '''    public DnsMessage(final byte[] data)
    '''
def toArray():
    '''    public byte[] toArray()
    '''
def asDatagram():
    '''    public DatagramPacket asDatagram(final InetAddress address, final int port)
    '''
def writeTo():
    '''    public void writeTo(final DataOutputStream dataOutputStream)
    '''
def getInByteBuffer():
    '''    public ByteBuffer getInByteBuffer()
    '''
def getQuestion():
    '''    public Question getQuestion()
    '''
def copyQuestions():
    '''    public List<Question> copyQuestions()
    '''
def getEdns():
    '''    public Edns getEdns()
    '''
def getOptPseudoRecord():
    '''    public Record<OPT> getOptPseudoRecord()
    '''
def isDnssecOk():
    '''    public boolean isDnssecOk()
    '''
def toString():
    '''    public String toString()
    '''
def asTerminalOutput():
    '''    public String asTerminalOutput()
    '''
def getAnswersFor():
    '''    public <D extends Data> Set<D> getAnswersFor(final Question q)
    '''
def asBuilder():
    '''    public Builder asBuilder()
    '''
def asNormalizedVersion():
    '''    public DnsMessage asNormalizedVersion()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object other)
    '''
def builder():
    '''    public static Builder builder()
    '''
def getValue():
    '''    public byte getValue()
    public byte getValue()
    '''
def getResponseCode():
    '''    public static RESPONSE_CODE getResponseCode(final int value)
    '''
def getOpcode():
    '''    public static OPCODE getOpcode(final int value)
    '''
def setId():
    '''    public Builder setId(final int id)
    '''
def setOpcode():
    '''    public Builder setOpcode(final OPCODE opcode)
    '''
def setResponseCode():
    '''    public Builder setResponseCode(final RESPONSE_CODE responseCode)
    '''
def setQrFlag():
    '''    public Builder setQrFlag(final boolean query)
    '''
def setAuthoritativeAnswer():
    '''    public Builder setAuthoritativeAnswer(final boolean authoritativeAnswer)
    '''
def setTruncated():
    '''    public Builder setTruncated(final boolean truncated)
    '''
def setRecursionDesired():
    '''    public Builder setRecursionDesired(final boolean recursionDesired)
    '''
def setRecursionAvailable():
    '''    public Builder setRecursionAvailable(final boolean recursionAvailable)
    '''
def setAuthenticData():
    '''    public Builder setAuthenticData(final boolean authenticData)
    '''
def setCheckDisabled():
    '''    public Builder setCheckDisabled(final boolean checkingDisabled)
    '''
def setCheckingDisabled():
    '''    public Builder setCheckingDisabled(final boolean checkingDisabled)
    '''
def copyFlagsFrom():
    '''    public void copyFlagsFrom(final DnsMessage dnsMessage)
    '''
def setReceiveTimestamp():
    '''    public Builder setReceiveTimestamp(final long receiveTimestamp)
    '''
def addQuestion():
    '''    public Builder addQuestion(final Question question)
    '''
def setQuestions():
    '''    public Builder setQuestions(final List<Question> questions)
    '''
def setQuestion():
    '''    public Builder setQuestion(final Question question)
    '''
def addAnswer():
    '''    public Builder addAnswer(final Record<? extends Data> answer)
    '''
def addAnswers():
    '''    public Builder addAnswers(final Collection<Record<? extends Data>> records)
    '''
def setAnswers():
    '''    public Builder setAnswers(final Collection<Record<? extends Data>> records)
    '''
def addNameserverRecords():
    '''    public Builder addNameserverRecords(final Record<? extends Data> record)
    '''
def setNameserverRecords():
    '''    public Builder setNameserverRecords(final Collection<Record<? extends Data>> records)
    '''
def setAdditionalResourceRecords():
    '''    public Builder setAdditionalResourceRecords(final Collection<Record<? extends Data>> records)
    '''
def addAdditionalResourceRecord():
    '''    public Builder addAdditionalResourceRecord(final Record<? extends Data> record)
    '''
def addAdditionalResourceRecords():
    '''    public Builder addAdditionalResourceRecords(final List<Record<? extends Data>> records)
    '''
def build():
    '''    public DnsMessage build()
    '''
