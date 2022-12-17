def load():
    '''returns None\n\n
    load(final InputStream is)\n
    load(final InputStream is)\n
    '''
def getProperties():
    '''returns Properties\n\n
    getProperties()\n
    '''
def getStore():
    '''returns Store\n\n
    getStore()\n
    getStore(final String protocol)\n
    getStore(final Provider provider)\n
    getStore(final URLName url)\n
    '''
def getTransport():
    '''returns Transport\n\n
    getTransport()\n
    getTransport(final String protocol)\n
    getTransport(final Address address)\n
    getTransport(final Provider provider)\n
    getTransport(final URLName url)\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String name)\n
    '''
def getFolder():
    '''returns Folder\n\n
    getFolder(final URLName url)\n
    '''
def getPasswordAuthentication():
    '''returns PasswordAuthentication\n\n
    getPasswordAuthentication(final URLName url)\n
    '''
def setPasswordAuthentication():
    '''returns None\n\n
    setPasswordAuthentication(final URLName url, final PasswordAuthentication pw)\n
    '''
def requestPasswordAuthentication():
    '''returns PasswordAuthentication\n\n
    requestPasswordAuthentication(final InetAddress addr, final int port, final String protocol, final String prompt, final String defaultUserName)\n
    '''
