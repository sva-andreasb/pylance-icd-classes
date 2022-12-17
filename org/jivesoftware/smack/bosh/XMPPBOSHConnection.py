XMPP_BOSH_NS = "String  \"urn:xmpp:xbosh\""
BOSH_URI = "String  \"http://jabber.org/protocol/httpbind\""
def ():
    '''returns XMPPBOSHConnection\n\n
    (final String username, final String password, final boolean https, final String host, final int port, final String filePath, final DomainBareJid xmppServiceDomain)\n
    (final BOSHConfiguration config)\n
    '''
def isSecureConnection():
    '''returns boolean\n\n
    isSecureConnection()\n
    '''
def isUsingCompression():
    '''returns boolean\n\n
    isUsingCompression()\n
    '''
def sendNonza():
    '''returns None\n\n
    sendNonza(final Nonza element)\n
    '''
def instantShutdown():
    '''returns None\n\n
    instantShutdown()\n
    '''
def write():
    '''returns None\n\n
    write(final char[] cbuf, final int off, final int len)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def responseReceived():
    '''returns None\n\n
    responseReceived(final BOSHMessageEvent event)\n
    responseReceived(final BOSHMessageEvent event)\n
    '''
def requestSent():
    '''returns None\n\n
    requestSent(final BOSHMessageEvent event)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def connectionEvent():
    '''returns None\n\n
    connectionEvent(final BOSHClientConnEvent connEvent)\n
    '''
