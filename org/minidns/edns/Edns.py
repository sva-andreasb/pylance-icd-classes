FLAG_DNSSEC_OK = "int  32768"
def ():
    '''returns Edns\n\n
    (final Record<OPT> optRecord)\n
    (final Builder builder)\n
    '''
def asRecord():
    '''returns Record<OPT>\n\n
    asRecord()\n
    '''
def asTerminalOutput():
    '''returns String\n\n
    asTerminalOutput()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setUdpPayloadSize():
    '''returns Builder\n\n
    setUdpPayloadSize(final int udpPayloadSize)\n
    '''
def setDnssecOk():
    '''returns Builder\n\n
    setDnssecOk(final boolean dnssecOk)\n
    setDnssecOk()\n
    '''
def addEdnsOption():
    '''returns Builder\n\n
    addEdnsOption(final EdnsOption ednsOption)\n
    '''
def build():
    '''returns Edns\n\n
    build()\n
    '''
