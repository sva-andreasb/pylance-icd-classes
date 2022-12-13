FLAG_DNSSEC_OK = "int  32768"
def Edns():
    '''    public Edns(final Record<OPT> optRecord)
    public Edns(final Builder builder)
    '''
def getEdnsOption():
    '''    public <O extends EdnsOption> O getEdnsOption(final OptionCode optionCode)
    '''
def asRecord():
    '''    public Record<OPT> asRecord()
    '''
def asTerminalOutput():
    '''    public String asTerminalOutput()
    '''
def toString():
    '''    public String toString()
    '''
def fromRecord():
    '''    public static Edns fromRecord(final Record<? extends Data> record)
    '''
def builder():
    '''    public static Builder builder()
    '''
def from():
    '''    public static OptionCode from(final int optionCode)
    '''
def setUdpPayloadSize():
    '''    public Builder setUdpPayloadSize(final int udpPayloadSize)
    '''
def setDnssecOk():
    '''    public Builder setDnssecOk(final boolean dnssecOk)
    public Builder setDnssecOk()
    '''
def addEdnsOption():
    '''    public Builder addEdnsOption(final EdnsOption ednsOption)
    '''
def build():
    '''    public Edns build()
    '''
