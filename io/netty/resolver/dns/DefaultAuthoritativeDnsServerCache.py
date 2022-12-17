def ():
    '''returns DefaultAuthoritativeDnsServerCache\n\n
    ()\n
    (final int minTtl, final int maxTtl, final Comparator<InetSocketAddress> comparator)\n
    '''
def get():
    '''returns DnsServerAddressStream\n\n
    get(final String hostname)\n
    '''
def cache():
    '''returns None\n\n
    cache(final String hostname, final InetSocketAddress address, final long originalTtl, final EventLoop loop)\n
    '''
def clear():
    '''returns boolean\n\n
    clear()\n
    clear(final String hostname)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
