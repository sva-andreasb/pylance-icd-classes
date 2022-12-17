def ():
    '''returns DiscoveryAdapter\n\n
    (final ServerInfo info, final String discoveryPort, final int protocol)\n
    (final ServerInfo info, final String discoveryPort, final int protocol, String multicastAddr)\n
    '''
def initialize():
    '''returns boolean\n\n
    initialize(final ThreadPoolMgr tpmgr)\n
    '''
def event():
    '''returns None\n\n
    event(final DiscoveryEvent event)\n
    '''
def discovery():
    '''returns None\n\n
    discovery(final String host, final String port, final int protocol, final ServerInfo target)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def alarm():
    '''returns None\n\n
    alarm(final Object alarmContext)\n
    '''
