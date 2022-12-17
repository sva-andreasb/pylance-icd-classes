def ():
    '''returns DatagramDnsQuery\n\n
    (final InetSocketAddress sender, final InetSocketAddress recipient, final int id)\n
    (final InetSocketAddress sender, final InetSocketAddress recipient, final int id, final DnsOpCode opCode)\n
    '''
def content():
    '''returns DatagramDnsQuery\n\n
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
def setId():
    '''returns DatagramDnsQuery\n\n
    setId(final int id)\n
    '''
def setOpCode():
    '''returns DatagramDnsQuery\n\n
    setOpCode(final DnsOpCode opCode)\n
    '''
def setRecursionDesired():
    '''returns DatagramDnsQuery\n\n
    setRecursionDesired(final boolean recursionDesired)\n
    '''
def setZ():
    '''returns DatagramDnsQuery\n\n
    setZ(final int z)\n
    '''
def setRecord():
    '''returns DatagramDnsQuery\n\n
    setRecord(final DnsSection section, final DnsRecord record)\n
    '''
def addRecord():
    '''returns DatagramDnsQuery\n\n
    addRecord(final DnsSection section, final DnsRecord record)\n
    addRecord(final DnsSection section, final int index, final DnsRecord record)\n
    '''
def clear():
    '''returns DatagramDnsQuery\n\n
    clear(final DnsSection section)\n
    clear()\n
    '''
def touch():
    '''returns DatagramDnsQuery\n\n
    touch()\n
    touch(final Object hint)\n
    '''
def retain():
    '''returns DatagramDnsQuery\n\n
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
