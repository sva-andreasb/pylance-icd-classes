def DefaultDnsCache():
    '''public DefaultDnsCache()
    public DefaultDnsCache(final int minTtl, final int maxTtl, final int negativeTtl)
    '''
def minTtl():
    '''public int minTtl()
    '''
def maxTtl():
    '''public int maxTtl()
    '''
def negativeTtl():
    '''public int negativeTtl()
    '''
def clear():
    '''public void clear()
    public boolean clear(final String hostname)
    '''
def cache():
    '''public DnsCacheEntry cache(final String hostname, final DnsRecord[] additionals, final InetAddress address, final long originalTtl, final EventLoop loop)
    public DnsCacheEntry cache(final String hostname, final DnsRecord[] additionals, final Throwable cause, final EventLoop loop)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def address():
    '''public InetAddress address()
    '''
def cause():
    '''public Throwable cause()
    '''
