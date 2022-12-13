def DefaultDnsCnameCache():
    '''public DefaultDnsCnameCache()
    public DefaultDnsCnameCache(final int minTtl, final int maxTtl)
    '''
def get():
    '''public String get(final String hostname)
    '''
def cache():
    '''public void cache(final String hostname, final String cname, final long originalTtl, final EventLoop loop)
    '''
def clear():
    '''public void clear()
    public boolean clear(final String hostname)
    '''
