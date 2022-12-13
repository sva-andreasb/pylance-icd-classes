NAMESPACE = "String  urn:xmpp:http:upload:0""
NAMESPACE_0_2 = "String  urn:xmpp:http:upload""
def getInstanceFor():
'''public static synchronized HttpFileUploadManager getInstanceFor(final XMPPConnection connection)
'''
pass
def authenticated():
'''public void authenticated(final XMPPConnection connection, final boolean resumed)
'''
pass
def discoverUploadService():
'''public boolean discoverUploadService()
'''
pass
def isUploadServiceDiscovered():
'''public boolean isUploadServiceDiscovered()
'''
pass
def getDefaultUploadService():
'''public UploadService getDefaultUploadService()
'''
pass
def uploadFile():
'''public URL uploadFile(final File file)
public URL uploadFile(final File file, final UploadProgressListener listener)
'''
pass
def requestSlot():
'''public Slot requestSlot(final String filename, final long fileSize)
public Slot requestSlot(final String filename, final long fileSize, final String contentType)
public Slot requestSlot(final String filename, final long fileSize, final String contentType, final DomainBareJid uploadServiceAddress)
'''
pass
def setTlsContext():
'''public void setTlsContext(final SSLContext tlsContext)
'''
pass
def useTlsSettingsFrom():
'''public void useTlsSettingsFrom(final ConnectionConfiguration connectionConfiguration)
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
