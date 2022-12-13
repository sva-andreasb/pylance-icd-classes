def getName():
    '''    public String getName()
    '''
def getFullName():
    '''    public String getFullName()
    '''
def getParent():
    '''    public Folder getParent()
    '''
def exists():
    '''    public boolean exists()
    '''
def list():
    '''    public Folder[] list(final String s)
    '''
def getSeparator():
    '''    public char getSeparator()
    '''
def getType():
    '''    public int getType()
    '''
def create():
    '''    public boolean create(final int n)
    '''
def hasNewMessages():
    '''    public boolean hasNewMessages()
    '''
def getFolder():
    '''    public Folder getFolder(final String s)
    '''
def delete():
    '''    public boolean delete(final boolean b)
    '''
def renameTo():
    '''    public boolean renameTo(final Folder folder)
    '''
def open():
    '''    public synchronized void open(final int mode)
    '''
def close():
    '''    public synchronized void close(final boolean b)
    '''
def isOpen():
    '''    public boolean isOpen()
    '''
def getPermanentFlags():
    '''    public Flags getPermanentFlags()
    '''
def getMessageCount():
    '''    public int getMessageCount()
    '''
def getMessage():
    '''    public synchronized Message getMessage(final int n)
    '''
def appendMessages():
    '''    public void appendMessages(final Message[] array)
    '''
def expunge():
    '''    public Message[] expunge()
    '''
def fetch():
    '''    public synchronized void fetch(final Message[] array, final FetchProfile fetchProfile)
    '''
def getUID():
    '''    public synchronized String getUID(final Message message)
    '''
def getSize():
    '''    public int getSize()
    '''
def getSizes():
    '''    public synchronized int[] getSizes()
    '''
def listCommand():
    '''    public synchronized InputStream listCommand()
    '''
