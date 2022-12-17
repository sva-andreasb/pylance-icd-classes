def ():
    '''returns BiDnsQueryLifecycleObserver\n\n
    (final DnsQueryLifecycleObserver a, final DnsQueryLifecycleObserver b)\n
    '''
def queryWritten():
    '''returns None\n\n
    queryWritten(final InetSocketAddress dnsServerAddress, final ChannelFuture future)\n
    '''
def queryCancelled():
    '''returns None\n\n
    queryCancelled(final int queriesRemaining)\n
    '''
def queryRedirected():
    '''returns DnsQueryLifecycleObserver\n\n
    queryRedirected(final List<InetSocketAddress> nameServers)\n
    '''
def queryCNAMEd():
    '''returns DnsQueryLifecycleObserver\n\n
    queryCNAMEd(final DnsQuestion cnameQuestion)\n
    '''
def queryNoAnswer():
    '''returns DnsQueryLifecycleObserver\n\n
    queryNoAnswer(final DnsResponseCode code)\n
    '''
def queryFailed():
    '''returns None\n\n
    queryFailed(final Throwable cause)\n
    '''
def querySucceed():
    '''returns None\n\n
    querySucceed()\n
    '''
