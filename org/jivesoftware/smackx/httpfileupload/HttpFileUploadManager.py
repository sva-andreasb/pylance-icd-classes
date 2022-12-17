NAMESPACE = "String  \"urn:xmpp:http:upload:0\""
NAMESPACE_0_2 = "String  \"urn:xmpp:http:upload\""
def authenticated():
    '''returns None\n\n
    authenticated(final XMPPConnection connection, final boolean resumed)\n
    '''
def discoverUploadService():
    '''returns boolean\n\n
    discoverUploadService()\n
    '''
def isUploadServiceDiscovered():
    '''returns boolean\n\n
    isUploadServiceDiscovered()\n
    '''
def getDefaultUploadService():
    '''returns UploadService\n\n
    getDefaultUploadService()\n
    '''
def uploadFile():
    '''returns URL\n\n
    uploadFile(final File file)\n
    uploadFile(final File file, final UploadProgressListener listener)\n
    '''
def requestSlot():
    '''returns Slot\n\n
    requestSlot(final String filename, final long fileSize)\n
    requestSlot(final String filename, final long fileSize, final String contentType)\n
    requestSlot(final String filename, final long fileSize, final String contentType, final DomainBareJid uploadServiceAddress)\n
    '''
def setTlsContext():
    '''returns None\n\n
    setTlsContext(final SSLContext tlsContext)\n
    '''
def useTlsSettingsFrom():
    '''returns None\n\n
    useTlsSettingsFrom(final ConnectionConfiguration connectionConfiguration)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
