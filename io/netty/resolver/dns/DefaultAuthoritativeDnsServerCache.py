def DefaultAuthoritativeDnsServerCache():
'''public DefaultAuthoritativeDnsServerCache()
public DefaultAuthoritativeDnsServerCache(final int minTtl, final int maxTtl, final Comparator<InetSocketAddress> comparator)
'''
pass
def get():
'''public DnsServerAddressStream get(final String hostname)
'''
pass
def cache():
'''public void cache(final String hostname, final InetSocketAddress address, final long originalTtl, final EventLoop loop)
'''
pass
def clear():
'''public void clear()
public boolean clear(final String hostname)
'''
pass
def toString():
'''public String toString()
'''
pass
