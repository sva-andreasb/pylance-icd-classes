def login():
    '''returns boolean\n\n
    login(final String username, final String password)\n
    login(final String username, String timestamp, final String secret)\n
    '''
def logout():
    '''returns boolean\n\n
    logout()\n
    '''
def noop():
    '''returns boolean\n\n
    noop()\n
    '''
def deleteMessage():
    '''returns boolean\n\n
    deleteMessage(final int messageId)\n
    '''
def reset():
    '''returns boolean\n\n
    reset()\n
    '''
def status():
    '''returns POP3MessageInfo\n\n
    status()\n
    '''
def listMessage():
    '''returns POP3MessageInfo\n\n
    listMessage(final int messageId)\n
    '''
def listMessages():
    '''returns POP3MessageInfo[]\n\n
    listMessages()\n
    '''
def listUniqueIdentifier():
    '''returns POP3MessageInfo\n\n
    listUniqueIdentifier(final int messageId)\n
    '''
def listUniqueIdentifiers():
    '''returns POP3MessageInfo[]\n\n
    listUniqueIdentifiers()\n
    '''
def retrieveMessage():
    '''returns Reader\n\n
    retrieveMessage(final int messageId)\n
    '''
def retrieveMessageTop():
    '''returns Reader\n\n
    retrieveMessageTop(final int messageId, final int numLines)\n
    '''
