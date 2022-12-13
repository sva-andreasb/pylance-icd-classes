def getDebug():
    '''public synchronized boolean getDebug()
    '''
def setDebug():
    '''public synchronized void setDebug(final boolean debug)
    '''
def getDebugOut():
    '''public synchronized PrintStream getDebugOut()
    '''
def setDebugOut():
    '''public synchronized void setDebugOut(final PrintStream out)
    '''
def load():
    '''public void load(final InputStream is)
    public void load(final InputStream is)
    '''
def getProperties():
    '''public Properties getProperties()
    '''
def getProviders():
    '''public synchronized Provider[] getProviders()
    '''
def setProvider():
    '''public synchronized void setProvider(final Provider provider)
    '''
def getStore():
    '''public Store getStore()
    public Store getStore(final String protocol)
    public Store getStore(final Provider provider)
    public Store getStore(final URLName url)
    '''
def getTransport():
    '''public Transport getTransport()
    public Transport getTransport(final String protocol)
    public Transport getTransport(final Address address)
    public Transport getTransport(final Provider provider)
    public Transport getTransport(final URLName url)
    '''
def getProperty():
    '''public String getProperty(final String name)
    '''
def getFolder():
    '''public Folder getFolder(final URLName url)
    '''
def getPasswordAuthentication():
    '''public PasswordAuthentication getPasswordAuthentication(final URLName url)
    '''
def setPasswordAuthentication():
    '''public void setPasswordAuthentication(final URLName url, final PasswordAuthentication pw)
    '''
def getProvider():
    '''public synchronized Provider getProvider(final String protocol)
    '''
def getDefaultInstance():
    '''public static Session getDefaultInstance(final Properties props)
    public static synchronized Session getDefaultInstance(final Properties props, final Authenticator authenticator)
    '''
def getInstance():
    '''public static Session getInstance(final Properties props)
    public static Session getInstance(final Properties props, final Authenticator authenticator)
    '''
def requestPasswordAuthentication():
    '''public PasswordAuthentication requestPasswordAuthentication(final InetAddress addr, final int port, final String protocol, final String prompt, final String defaultUserName)
    '''
