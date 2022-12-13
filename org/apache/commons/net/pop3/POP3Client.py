def login():
    '''public boolean login(final String username, final String password)
    public boolean login(final String username, String timestamp, final String secret)
    '''
def logout():
    '''public boolean logout()
    '''
def noop():
    '''public boolean noop()
    '''
def deleteMessage():
    '''public boolean deleteMessage(final int messageId)
    '''
def reset():
    '''public boolean reset()
    '''
def status():
    '''public POP3MessageInfo status()
    '''
def listMessage():
    '''public POP3MessageInfo listMessage(final int messageId)
    '''
def listMessages():
    '''public POP3MessageInfo[] listMessages()
    '''
def listUniqueIdentifier():
    '''public POP3MessageInfo listUniqueIdentifier(final int messageId)
    '''
def listUniqueIdentifiers():
    '''public POP3MessageInfo[] listUniqueIdentifiers()
    '''
def retrieveMessage():
    '''public Reader retrieveMessage(final int messageId)
    '''
def retrieveMessageTop():
    '''public Reader retrieveMessageTop(final int messageId, final int numLines)
    '''
