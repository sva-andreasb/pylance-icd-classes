def MailcapCommandMap():
    '''    public MailcapCommandMap()
    public MailcapCommandMap(final InputStream is)
    public MailcapCommandMap(final String fileName)
    '''
def addMailcap():
    '''    public synchronized void addMailcap(final String mail_cap)
    '''
def getAllCommands():
    '''    public synchronized CommandInfo[] getAllCommands(final String mimeType)
    '''
def getPreferredCommands():
    '''    public synchronized CommandInfo[] getPreferredCommands(final String mimeType)
    '''
def createDataContentHandler():
    '''    public synchronized DataContentHandler createDataContentHandler(final String mimeType)
    '''
def getCommand():
    '''    public synchronized CommandInfo getCommand(final String mimeType, final String cmdName)
    '''
