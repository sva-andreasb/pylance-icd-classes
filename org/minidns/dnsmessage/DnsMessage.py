def DnsMessage():
'''public DnsMessage(final byte[] data)
'''
pass
def toArray():
'''public byte[] toArray()
'''
pass
def asDatagram():
'''public DatagramPacket asDatagram(final InetAddress address, final int port)
'''
pass
def writeTo():
'''public void writeTo(final DataOutputStream dataOutputStream)
'''
pass
def getInByteBuffer():
'''public ByteBuffer getInByteBuffer()
'''
pass
def getQuestion():
'''public Question getQuestion()
'''
pass
def copyQuestions():
'''public List<Question> copyQuestions()
'''
pass
def getEdns():
'''public Edns getEdns()
'''
pass
def getOptPseudoRecord():
'''public Record<OPT> getOptPseudoRecord()
'''
pass
def isDnssecOk():
'''public boolean isDnssecOk()
'''
pass
def toString():
'''public String toString()
'''
pass
def asTerminalOutput():
'''public String asTerminalOutput()
'''
pass
def getAnswersFor():
'''public <D extends Data> Set<D> getAnswersFor(final Question q)
'''
pass
def asBuilder():
'''public Builder asBuilder()
'''
pass
def asNormalizedVersion():
'''public DnsMessage asNormalizedVersion()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object other)
'''
pass
def builder():
'''public static Builder builder()
'''
pass
def getValue():
'''public byte getValue()
public byte getValue()
'''
pass
def getResponseCode():
'''public static RESPONSE_CODE getResponseCode(final int value)
'''
pass
def getOpcode():
'''public static OPCODE getOpcode(final int value)
'''
pass
def setId():
'''public Builder setId(final int id)
'''
pass
def setOpcode():
'''public Builder setOpcode(final OPCODE opcode)
'''
pass
def setResponseCode():
'''public Builder setResponseCode(final RESPONSE_CODE responseCode)
'''
pass
def setQrFlag():
'''public Builder setQrFlag(final boolean query)
'''
pass
def setAuthoritativeAnswer():
'''public Builder setAuthoritativeAnswer(final boolean authoritativeAnswer)
'''
pass
def setTruncated():
'''public Builder setTruncated(final boolean truncated)
'''
pass
def setRecursionDesired():
'''public Builder setRecursionDesired(final boolean recursionDesired)
'''
pass
def setRecursionAvailable():
'''public Builder setRecursionAvailable(final boolean recursionAvailable)
'''
pass
def setAuthenticData():
'''public Builder setAuthenticData(final boolean authenticData)
'''
pass
def setCheckDisabled():
'''public Builder setCheckDisabled(final boolean checkingDisabled)
'''
pass
def setCheckingDisabled():
'''public Builder setCheckingDisabled(final boolean checkingDisabled)
'''
pass
def copyFlagsFrom():
'''public void copyFlagsFrom(final DnsMessage dnsMessage)
'''
pass
def setReceiveTimestamp():
'''public Builder setReceiveTimestamp(final long receiveTimestamp)
'''
pass
def addQuestion():
'''public Builder addQuestion(final Question question)
'''
pass
def setQuestions():
'''public Builder setQuestions(final List<Question> questions)
'''
pass
def setQuestion():
'''public Builder setQuestion(final Question question)
'''
pass
def addAnswer():
'''public Builder addAnswer(final Record<? extends Data> answer)
'''
pass
def addAnswers():
'''public Builder addAnswers(final Collection<Record<? extends Data>> records)
'''
pass
def setAnswers():
'''public Builder setAnswers(final Collection<Record<? extends Data>> records)
'''
pass
def addNameserverRecords():
'''public Builder addNameserverRecords(final Record<? extends Data> record)
'''
pass
def setNameserverRecords():
'''public Builder setNameserverRecords(final Collection<Record<? extends Data>> records)
'''
pass
def setAdditionalResourceRecords():
'''public Builder setAdditionalResourceRecords(final Collection<Record<? extends Data>> records)
'''
pass
def addAdditionalResourceRecord():
'''public Builder addAdditionalResourceRecord(final Record<? extends Data> record)
'''
pass
def addAdditionalResourceRecords():
'''public Builder addAdditionalResourceRecords(final List<Record<? extends Data>> records)
'''
pass
def build():
'''public DnsMessage build()
'''
pass
