NAMESPACE = "String  \"urn:xmpp:http:upload:0\""
NAMESPACE_0_2 = "String  \"urn:xmpp:http:upload\""
def getInstanceFor():
    '''public static synchronized HttpFileUploadManager getInstanceFor(final XMPPConnection connection)
    '''
def authenticated():
    '''public void authenticated(final XMPPConnection connection, final boolean resumed)
    '''
def discoverUploadService():
    '''public boolean discoverUploadService()
    '''
def isUploadServiceDiscovered():
    '''public boolean isUploadServiceDiscovered()
    '''
def getDefaultUploadService():
    '''public UploadService getDefaultUploadService()
    '''
def uploadFile():
    '''public URL uploadFile(final File file)
    public URL uploadFile(final File file, final UploadProgressListener listener)
    '''
def requestSlot():
    '''public Slot requestSlot(final String filename, final long fileSize)
    public Slot requestSlot(final String filename, final long fileSize, final String contentType)
    public Slot requestSlot(final String filename, final long fileSize, final String contentType, final DomainBareJid uploadServiceAddress)
    '''
def setTlsContext():
    '''public void setTlsContext(final SSLContext tlsContext)
    '''
def useTlsSettingsFrom():
    '''public void useTlsSettingsFrom(final ConnectionConfiguration connectionConfiguration)
    '''
def connectionCreated():
    '''public void connectionCreated(final XMPPConnection connection)
    '''
