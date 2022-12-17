def ():
    '''returns DatagramDnsResponse\n\n
    (final InetSocketAddress sender, final InetSocketAddress recipient, final int id)\n
    (final InetSocketAddress sender, final InetSocketAddress recipient, final int id, final DnsOpCode opCode)\n
    (final InetSocketAddress sender, final InetSocketAddress recipient, final int id, final DnsOpCode opCode, final DnsResponseCode responseCode)\n
    '''
def content():
    '''returns DatagramDnsResponse\n\n
    content()\n
    '''
def sender():
    '''returns InetSocketAddress\n\n
    sender()\n
    '''
def recipient():
    '''returns InetSocketAddress\n\n
    recipient()\n
    '''
def setAuthoritativeAnswer():
    '''returns DatagramDnsResponse\n\n
    setAuthoritativeAnswer(final boolean authoritativeAnswer)\n
    '''
def setTruncated():
    '''returns DatagramDnsResponse\n\n
    setTruncated(final boolean truncated)\n
    '''
def setRecursionAvailable():
    '''returns DatagramDnsResponse\n\n
    setRecursionAvailable(final boolean recursionAvailable)\n
    '''
def setCode():
    '''returns DatagramDnsResponse\n\n
    setCode(final DnsResponseCode code)\n
    '''
def setId():
    '''returns DatagramDnsResponse\n\n
    setId(final int id)\n
    '''
def setOpCode():
    '''returns DatagramDnsResponse\n\n
    setOpCode(final DnsOpCode opCode)\n
    '''
def setRecursionDesired():
    '''returns DatagramDnsResponse\n\n
    setRecursionDesired(final boolean recursionDesired)\n
    '''
def setZ():
    '''returns DatagramDnsResponse\n\n
    setZ(final int z)\n
    '''
def setRecord():
    '''returns DatagramDnsResponse\n\n
    setRecord(final DnsSection section, final DnsRecord record)\n
    '''
def addRecord():
    '''returns DatagramDnsResponse\n\n
    addRecord(final DnsSection section, final DnsRecord record)\n
    addRecord(final DnsSection section, final int index, final DnsRecord record)\n
    '''
def clear():
    '''returns DatagramDnsResponse\n\n
    clear(final DnsSection section)\n
    clear()\n
    '''
def touch():
    '''returns DatagramDnsResponse\n\n
    touch()\n
    touch(final Object hint)\n
    '''
def retain():
    '''returns DatagramDnsResponse\n\n
    retain()\n
    retain(final int increment)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
