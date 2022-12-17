HOLDS_MESSAGES = "int  1"
HOLDS_FOLDERS = "int  2"
READ_ONLY = "int  1"
READ_WRITE = "int  2"
def getMode():
    '''returns int\n\n
    getMode()\n
    '''
def dispatch():
    '''returns None\n\n
    dispatch(final Object listener)\n
    '''
def isSubscribed():
    '''returns boolean\n\n
    isSubscribed()\n
    '''
def setSubscribed():
    '''returns None\n\n
    setSubscribed(final boolean subscribe)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def list():
    '''returns Folder[]\n\n
    list()\n
    '''
def listSubscribed():
    '''returns Folder[]\n\n
    listSubscribed()\n
    listSubscribed(final String pattern)\n
    '''
def getStore():
    '''returns Store\n\n
    getStore()\n
    '''
def getURLName():
    '''returns URLName\n\n
    getURLName()\n
    '''
def fetch():
    '''returns None\n\n
    fetch(final Message[] msgs, final FetchProfile fp)\n
    '''
def copyMessages():
    '''returns None\n\n
    copyMessages(final Message[] msgs, final Folder folder)\n
    '''
def search():
    '''returns Message[]\n\n
    search(final SearchTerm term)\n
    search(final SearchTerm term, final Message[] msgs)\n
    '''
