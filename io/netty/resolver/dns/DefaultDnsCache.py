def ():
    '''returns DefaultDnsCache\n\n
    ()\n
    (final int minTtl, final int maxTtl, final int negativeTtl)\n
    '''
def minTtl():
    '''returns int\n\n
    minTtl()\n
    '''
def maxTtl():
    '''returns int\n\n
    maxTtl()\n
    '''
def negativeTtl():
    '''returns int\n\n
    negativeTtl()\n
    '''
def clear():
    '''returns boolean\n\n
    clear()\n
    clear(final String hostname)\n
    '''
def cache():
    '''returns DnsCacheEntry\n\n
    cache(final String hostname, final DnsRecord[] additionals, final InetAddress address, final long originalTtl, final EventLoop loop)\n
    cache(final String hostname, final DnsRecord[] additionals, final Throwable cause, final EventLoop loop)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def address():
    '''returns InetAddress\n\n
    address()\n
    '''
def cause():
    '''returns Throwable\n\n
    cause()\n
    '''
