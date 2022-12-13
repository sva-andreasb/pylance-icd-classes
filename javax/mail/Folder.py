HOLDS_MESSAGES = "int  1"
HOLDS_FOLDERS = "int  2"
READ_ONLY = "int  1"
READ_WRITE = "int  2"
def getDeletedMessageCount():
'''public synchronized int getDeletedMessageCount()
'''
pass
def getMode():
'''public int getMode()
'''
pass
def getNewMessageCount():
'''public synchronized int getNewMessageCount()
'''
pass
def getUnreadMessageCount():
'''public synchronized int getUnreadMessageCount()
'''
pass
def dispatch():
'''public void dispatch(final Object listener)
'''
pass
def isSubscribed():
'''public boolean isSubscribed()
'''
pass
def setSubscribed():
'''public void setSubscribed(final boolean subscribe)
'''
pass
def toString():
'''public String toString()
'''
pass
def setFlags():
'''public synchronized void setFlags(final int start, final int end, final Flags flag, final boolean value)
public synchronized void setFlags(final int[] msgnums, final Flags flag, final boolean value)
public synchronized void setFlags(final Message[] msgs, final Flags flag, final boolean value)
'''
pass
def list():
'''public Folder[] list()
'''
pass
def listSubscribed():
'''public Folder[] listSubscribed()
public Folder[] listSubscribed(final String pattern)
'''
pass
def getMessages():
'''public synchronized Message[] getMessages()
public synchronized Message[] getMessages(final int start, final int end)
public synchronized Message[] getMessages(final int[] msgnums)
'''
pass
def getStore():
'''public Store getStore()
'''
pass
def getURLName():
'''public URLName getURLName()
'''
pass
def addConnectionListener():
'''public synchronized void addConnectionListener(final ConnectionListener l)
'''
pass
def removeConnectionListener():
'''public synchronized void removeConnectionListener(final ConnectionListener l)
'''
pass
def addFolderListener():
'''public synchronized void addFolderListener(final FolderListener l)
'''
pass
def removeFolderListener():
'''public synchronized void removeFolderListener(final FolderListener l)
'''
pass
def addMessageChangedListener():
'''public synchronized void addMessageChangedListener(final MessageChangedListener l)
'''
pass
def removeMessageChangedListener():
'''public synchronized void removeMessageChangedListener(final MessageChangedListener l)
'''
pass
def addMessageCountListener():
'''public synchronized void addMessageCountListener(final MessageCountListener l)
'''
pass
def removeMessageCountListener():
'''public synchronized void removeMessageCountListener(final MessageCountListener l)
'''
pass
def fetch():
'''public void fetch(final Message[] msgs, final FetchProfile fp)
'''
pass
def copyMessages():
'''public void copyMessages(final Message[] msgs, final Folder folder)
'''
pass
def search():
'''public Message[] search(final SearchTerm term)
public Message[] search(final SearchTerm term, final Message[] msgs)
'''
pass
