KEEPALIVE_SOCKET_TIMEOUT = "String  \"com.ibm.ws.management.connector.soap.keepAliveTimeoutSec\""
KEEPALIVE_SOCKET_TIMEOUT_MIN = "int  5"
def ():
    '''returns SOAPServer\n\n
    (final ThreadPool threadPool)\n
    (final ThreadPool threadPool, final String profileKey)\n
    '''
def stateChanged():
    '''returns None\n\n
    stateChanged(final SSLConfigChangeEvent e)\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final Properties props, final boolean isSecure, final String alias)\n
    '''
def getConfiguredPort():
    '''returns String\n\n
    getConfiguredPort()\n
    '''
