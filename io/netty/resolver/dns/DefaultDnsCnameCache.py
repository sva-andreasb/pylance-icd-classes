def ():
    '''returns DefaultDnsCnameCache\n\n
    ()\n
    (final int minTtl, final int maxTtl)\n
    '''
def get():
    '''returns String\n\n
    get(final String hostname)\n
    '''
def cache():
    '''returns None\n\n
    cache(final String hostname, final String cname, final long originalTtl, final EventLoop loop)\n
    '''
def clear():
    '''returns boolean\n\n
    clear()\n
    clear(final String hostname)\n
    '''
