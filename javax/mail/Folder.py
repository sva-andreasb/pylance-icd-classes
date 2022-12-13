HOLDS_MESSAGES = "int  1"
HOLDS_FOLDERS = "int  2"
READ_ONLY = "int  1"
READ_WRITE = "int  2"
def getDeletedMessageCount():
    '''public synchronized int getDeletedMessageCount()
    '''
def getMode():
    '''public int getMode()
    '''
def getNewMessageCount():
    '''public synchronized int getNewMessageCount()
    '''
def getUnreadMessageCount():
    '''public synchronized int getUnreadMessageCount()
    '''
def dispatch():
    '''public void dispatch(final Object listener)
    '''
def isSubscribed():
    '''public boolean isSubscribed()
    '''
def setSubscribed():
    '''public void setSubscribed(final boolean subscribe)
    '''
def toString():
    '''public String toString()
    '''
def setFlags():
    '''public synchronized void setFlags(final int start, final int end, final Flags flag, final boolean value)
    public synchronized void setFlags(final int[] msgnums, final Flags flag, final boolean value)
    public synchronized void setFlags(final Message[] msgs, final Flags flag, final boolean value)
    '''
def list():
    '''public Folder[] list()
    '''
def listSubscribed():
    '''public Folder[] listSubscribed()
    public Folder[] listSubscribed(final String pattern)
    '''
def getMessages():
    '''public synchronized Message[] getMessages()
    public synchronized Message[] getMessages(final int start, final int end)
    public synchronized Message[] getMessages(final int[] msgnums)
    '''
def getStore():
    '''public Store getStore()
    '''
def getURLName():
    '''public URLName getURLName()
    '''
def addConnectionListener():
    '''public synchronized void addConnectionListener(final ConnectionListener l)
    '''
def removeConnectionListener():
    '''public synchronized void removeConnectionListener(final ConnectionListener l)
    '''
def addFolderListener():
    '''public synchronized void addFolderListener(final FolderListener l)
    '''
def removeFolderListener():
    '''public synchronized void removeFolderListener(final FolderListener l)
    '''
def addMessageChangedListener():
    '''public synchronized void addMessageChangedListener(final MessageChangedListener l)
    '''
def removeMessageChangedListener():
    '''public synchronized void removeMessageChangedListener(final MessageChangedListener l)
    '''
def addMessageCountListener():
    '''public synchronized void addMessageCountListener(final MessageCountListener l)
    '''
def removeMessageCountListener():
    '''public synchronized void removeMessageCountListener(final MessageCountListener l)
    '''
def fetch():
    '''public void fetch(final Message[] msgs, final FetchProfile fp)
    '''
def copyMessages():
    '''public void copyMessages(final Message[] msgs, final Folder folder)
    '''
def search():
    '''public Message[] search(final SearchTerm term)
    public Message[] search(final SearchTerm term, final Message[] msgs)
    '''
