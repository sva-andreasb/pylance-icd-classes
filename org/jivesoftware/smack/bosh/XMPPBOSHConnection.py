XMPP_BOSH_NS = "String  \"urn:xmpp:xbosh\""
BOSH_URI = "String  \"http://jabber.org/protocol/httpbind\""
def XMPPBOSHConnection():
    '''public XMPPBOSHConnection(final String username, final String password, final boolean https, final String host, final int port, final String filePath, final DomainBareJid xmppServiceDomain)
    public XMPPBOSHConnection(final BOSHConfiguration config)
    '''
def isSecureConnection():
    '''public boolean isSecureConnection()
    '''
def isUsingCompression():
    '''public boolean isUsingCompression()
    '''
def sendNonza():
    '''public void sendNonza(final Nonza element)
    '''
def instantShutdown():
    '''public void instantShutdown()
    '''
def write():
    '''public void write(final char[] cbuf, final int off, final int len)
    '''
def close():
    '''public void close()
    '''
def flush():
    '''public void flush()
    '''
def responseReceived():
    '''public void responseReceived(final BOSHMessageEvent event)
    public void responseReceived(final BOSHMessageEvent event)
    '''
def requestSent():
    '''public void requestSent(final BOSHMessageEvent event)
    '''
def run():
    '''public void run()
    '''
def connectionEvent():
    '''public void connectionEvent(final BOSHClientConnEvent connEvent)
    '''
