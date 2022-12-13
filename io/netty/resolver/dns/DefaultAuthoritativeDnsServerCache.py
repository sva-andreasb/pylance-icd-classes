def DefaultAuthoritativeDnsServerCache():
    '''public DefaultAuthoritativeDnsServerCache()
    public DefaultAuthoritativeDnsServerCache(final int minTtl, final int maxTtl, final Comparator<InetSocketAddress> comparator)
    '''
def get():
    '''public DnsServerAddressStream get(final String hostname)
    '''
def cache():
    '''public void cache(final String hostname, final InetSocketAddress address, final long originalTtl, final EventLoop loop)
    '''
def clear():
    '''public void clear()
    public boolean clear(final String hostname)
    '''
def toString():
    '''public String toString()
    '''
