def ():
    '''returns DefaultDnsQuery\n\n
    (final int id)\n
    (final int id, final DnsOpCode opCode)\n
    '''
def setId():
    '''returns DnsQuery\n\n
    setId(final int id)\n
    '''
def setOpCode():
    '''returns DnsQuery\n\n
    setOpCode(final DnsOpCode opCode)\n
    '''
def setRecursionDesired():
    '''returns DnsQuery\n\n
    setRecursionDesired(final boolean recursionDesired)\n
    '''
def setZ():
    '''returns DnsQuery\n\n
    setZ(final int z)\n
    '''
def setRecord():
    '''returns DnsQuery\n\n
    setRecord(final DnsSection section, final DnsRecord record)\n
    '''
def addRecord():
    '''returns DnsQuery\n\n
    addRecord(final DnsSection section, final DnsRecord record)\n
    addRecord(final DnsSection section, final int index, final DnsRecord record)\n
    '''
def clear():
    '''returns DnsQuery\n\n
    clear(final DnsSection section)\n
    clear()\n
    '''
def touch():
    '''returns DnsQuery\n\n
    touch()\n
    touch(final Object hint)\n
    '''
def retain():
    '''returns DnsQuery\n\n
    retain()\n
    retain(final int increment)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
