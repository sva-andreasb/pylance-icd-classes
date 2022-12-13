def getDebug():
'''public synchronized boolean getDebug()
'''
pass
def setDebug():
'''public synchronized void setDebug(final boolean debug)
'''
pass
def getDebugOut():
'''public synchronized PrintStream getDebugOut()
'''
pass
def setDebugOut():
'''public synchronized void setDebugOut(final PrintStream out)
'''
pass
def load():
'''public void load(final InputStream is)
public void load(final InputStream is)
'''
pass
def getProperties():
'''public Properties getProperties()
'''
pass
def getProviders():
'''public synchronized Provider[] getProviders()
'''
pass
def setProvider():
'''public synchronized void setProvider(final Provider provider)
'''
pass
def getStore():
'''public Store getStore()
public Store getStore(final String protocol)
public Store getStore(final Provider provider)
public Store getStore(final URLName url)
'''
pass
def getTransport():
'''public Transport getTransport()
public Transport getTransport(final String protocol)
public Transport getTransport(final Address address)
public Transport getTransport(final Provider provider)
public Transport getTransport(final URLName url)
'''
pass
def getProperty():
'''public String getProperty(final String name)
'''
pass
def getFolder():
'''public Folder getFolder(final URLName url)
'''
pass
def getPasswordAuthentication():
'''public PasswordAuthentication getPasswordAuthentication(final URLName url)
'''
pass
def setPasswordAuthentication():
'''public void setPasswordAuthentication(final URLName url, final PasswordAuthentication pw)
'''
pass
def getProvider():
'''public synchronized Provider getProvider(final String protocol)
'''
pass
def getDefaultInstance():
'''public static Session getDefaultInstance(final Properties props)
public static synchronized Session getDefaultInstance(final Properties props, final Authenticator authenticator)
'''
pass
def getInstance():
'''public static Session getInstance(final Properties props)
public static Session getInstance(final Properties props, final Authenticator authenticator)
'''
pass
def requestPasswordAuthentication():
'''public PasswordAuthentication requestPasswordAuthentication(final InetAddress addr, final int port, final String protocol, final String prompt, final String defaultUserName)
'''
pass
