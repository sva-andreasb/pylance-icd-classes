FLAG_DNSSEC_OK = "int  32768"
def Edns():
'''public Edns(final Record<OPT> optRecord)
public Edns(final Builder builder)
'''
pass
def getEdnsOption():
'''public <O extends EdnsOption> O getEdnsOption(final OptionCode optionCode)
'''
pass
def asRecord():
'''public Record<OPT> asRecord()
'''
pass
def asTerminalOutput():
'''public String asTerminalOutput()
'''
pass
def toString():
'''public String toString()
'''
pass
def fromRecord():
'''public static Edns fromRecord(final Record<? extends Data> record)
'''
pass
def builder():
'''public static Builder builder()
'''
pass
def from():
'''public static OptionCode from(final int optionCode)
'''
pass
def setUdpPayloadSize():
'''public Builder setUdpPayloadSize(final int udpPayloadSize)
'''
pass
def setDnssecOk():
'''public Builder setDnssecOk(final boolean dnssecOk)
public Builder setDnssecOk()
'''
pass
def addEdnsOption():
'''public Builder addEdnsOption(final EdnsOption ednsOption)
'''
pass
def build():
'''public Edns build()
'''
pass
