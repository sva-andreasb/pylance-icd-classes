WS_TCP_CHANNEL_FACTORY_NAME = "String  \"com.ibm.ws.tcp.channel.impl.WSTCPChannelFactory\""
WS_SSL_CHANNEL_FACTORY_NAME = "String  \"com.ibm.ws.ssl.channel.impl.WSSSLChannelFactory\""
TCP_CHANNEL_FACTORY_NAME = "String  \"com.ibm.ws.tcp.channel.impl.TCPChannelFactory\""
APP_CHANNEL_FACTORY_NAME = "String  \"com.ibm.ws.management.connector.ipc.IPCConnectorInboundFactory\""
ZAIO_LOCAL_FACTORY_NAME = "String  \"com.ibm.ws.tcp.channel.impl.ZAioTCPChannelLocalFactory\""
ZAIO_TCP_FACTORY_NAME = "String  \"com.ibm.ws.tcp.channel.impl.ZAioTCPChannelFactory\""
APP_CHANNEL_NAME_BASE = "String  \"IPCCInboundChannel.\""
TCP_CHANNEL_NAME_BASE = "String  \"TCPInboundChannel_ipcc.\""
SSL_CHANNEL_NAME_BASE = "String  \"SSLInboundChannel_ipcc.\""
CHANNEL_CHAIN_NAME_BASE = "String  \"IPCCInboundChain.\""
CHAIN_GROUP_NAME_BASE = "String  \"IPCCInboundGroup.\""
LC_ZAIO_CHANNEL_NAME_BASE = "String  \"LC_ZAioInboundChannel.\""
LC_APP_CHANNEL_NAME_BASE = "String  \"LC_IPCCInboundChannel.\""
LC_CHANNEL_CHAIN_NAME_BASE = "String  \"LC_IPCCInboundChain.\""
DEFAULT_IPC_CONNECTOR_NAME = "String  \"Default_IPC_Connector_Name\""
def ():
    '''returns IPCConnectorServer\n\n
    (final ThreadPool tp, final String pKey)\n
    (final ThreadPool tp)\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final Properties p)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def stop():
    '''returns None\n\n
    stop()\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
def getProperties():
    '''returns Properties\n\n
    getProperties()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
