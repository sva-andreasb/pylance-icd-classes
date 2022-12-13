def completePendingCommand():
    '''public boolean completePendingCommand()
    '''
def login():
    '''public boolean login(final String hostname)
    public boolean login()
    '''
def setSender():
    '''public boolean setSender(final RelayPath path)
    public boolean setSender(final String address)
    '''
def addRecipient():
    '''public boolean addRecipient(final RelayPath path)
    public boolean addRecipient(final String address)
    '''
def sendMessageData():
    '''public Writer sendMessageData()
    '''
def sendShortMessageData():
    '''public boolean sendShortMessageData(final String message)
    '''
def sendSimpleMessage():
    '''public boolean sendSimpleMessage(final String sender, final String recipient, final String message)
    public boolean sendSimpleMessage(final String sender, final String[] recipients, final String message)
    '''
def logout():
    '''public boolean logout()
    '''
def reset():
    '''public boolean reset()
    '''
def verify():
    '''public boolean verify(final String username)
    '''
def listHelp():
    '''public String listHelp()
    public String listHelp(final String command)
    '''
def sendNoOp():
    '''public boolean sendNoOp()
    '''
