DEFAULT_PORT = "int  119"
def ():
    '''returns NNTP\n\n
    ()\n
    '''
def addProtocolCommandListener():
    '''returns None\n\n
    addProtocolCommandListener(final ProtocolCommandListener listener)\n
    '''
def removeProtocolCommandListener():
    '''returns None\n\n
    removeProtocolCommandListener(final ProtocolCommandListener listener)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def isAllowedToPost():
    '''returns boolean\n\n
    isAllowedToPost()\n
    '''
def sendCommand():
    '''returns int\n\n
    sendCommand(final String command, final String args)\n
    sendCommand(final int command, final String args)\n
    sendCommand(final String command)\n
    sendCommand(final int command)\n
    '''
def getReplyCode():
    '''returns int\n\n
    getReplyCode()\n
    '''
def getReply():
    '''returns int\n\n
    getReply()\n
    '''
def getReplyString():
    '''returns String\n\n
    getReplyString()\n
    '''
def article():
    '''returns int\n\n
    article(final String messageId)\n
    article(final int articleNumber)\n
    article()\n
    '''
def body():
    '''returns int\n\n
    body(final String messageId)\n
    body(final int articleNumber)\n
    body()\n
    '''
def head():
    '''returns int\n\n
    head(final String messageId)\n
    head(final int articleNumber)\n
    head()\n
    '''
def stat():
    '''returns int\n\n
    stat(final String messageId)\n
    stat(final int articleNumber)\n
    stat()\n
    '''
def group():
    '''returns int\n\n
    group(final String newsgroup)\n
    '''
def help():
    '''returns int\n\n
    help()\n
    '''
def ihave():
    '''returns int\n\n
    ihave(final String messageId)\n
    '''
def last():
    '''returns int\n\n
    last()\n
    '''
def list():
    '''returns int\n\n
    list()\n
    '''
def next():
    '''returns int\n\n
    next()\n
    '''
def newgroups():
    '''returns int\n\n
    newgroups(final String date, final String time, final boolean GMT, final String distributions)\n
    '''
def newnews():
    '''returns int\n\n
    newnews(final String newsgroups, final String date, final String time, final boolean GMT, final String distributions)\n
    '''
def post():
    '''returns int\n\n
    post()\n
    '''
def quit():
    '''returns int\n\n
    quit()\n
    '''
def authinfoUser():
    '''returns int\n\n
    authinfoUser(final String username)\n
    '''
def authinfoPass():
    '''returns int\n\n
    authinfoPass(final String password)\n
    '''
def xover():
    '''returns int\n\n
    xover(final String selectedArticles)\n
    '''
def xhdr():
    '''returns int\n\n
    xhdr(final String header, final String selectedArticles)\n
    '''
def listActive():
    '''returns int\n\n
    listActive(final String wildmat)\n
    '''
