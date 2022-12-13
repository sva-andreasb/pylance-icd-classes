ELEMENT = "String  \"query\""
NAMESPACE = "String  \"jabber:iq:version\""
def Version():
    '''public Version()
    public Version(final Jid to)
    public Version(final String name, final String version)
    public Version(final String name, final String version, final String os)
    public Version(final Version original)
    '''
def getName():
    '''public String getName()
    '''
def getVersion():
    '''public String getVersion()
    '''
def getOs():
    '''public String getOs()
    '''
def setOs():
    '''public void setOs(final String os)
    '''
def createResultFor():
    '''public static Version createResultFor(final Stanza request, final Version version)
    '''
