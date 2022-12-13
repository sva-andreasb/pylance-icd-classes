DEFAULT_PORT = "int  119"
def NNTP():
    '''public NNTP()
    '''
def addProtocolCommandListener():
    '''public void addProtocolCommandListener(final ProtocolCommandListener listener)
    '''
def removeProtocolCommandListener():
    '''public void removeProtocolCommandListener(final ProtocolCommandListener listener)
    '''
def disconnect():
    '''public void disconnect()
    '''
def isAllowedToPost():
    '''public boolean isAllowedToPost()
    '''
def sendCommand():
    '''public int sendCommand(final String command, final String args)
    public int sendCommand(final int command, final String args)
    public int sendCommand(final String command)
    public int sendCommand(final int command)
    '''
def getReplyCode():
    '''public int getReplyCode()
    '''
def getReply():
    '''public int getReply()
    '''
def getReplyString():
    '''public String getReplyString()
    '''
def article():
    '''public int article(final String messageId)
    public int article(final int articleNumber)
    public int article()
    '''
def body():
    '''public int body(final String messageId)
    public int body(final int articleNumber)
    public int body()
    '''
def head():
    '''public int head(final String messageId)
    public int head(final int articleNumber)
    public int head()
    '''
def stat():
    '''public int stat(final String messageId)
    public int stat(final int articleNumber)
    public int stat()
    '''
def group():
    '''public int group(final String newsgroup)
    '''
def help():
    '''public int help()
    '''
def ihave():
    '''public int ihave(final String messageId)
    '''
def last():
    '''public int last()
    '''
def list():
    '''public int list()
    '''
def next():
    '''public int next()
    '''
def newgroups():
    '''public int newgroups(final String date, final String time, final boolean GMT, final String distributions)
    '''
def newnews():
    '''public int newnews(final String newsgroups, final String date, final String time, final boolean GMT, final String distributions)
    '''
def post():
    '''public int post()
    '''
def quit():
    '''public int quit()
    '''
def authinfoUser():
    '''public int authinfoUser(final String username)
    '''
def authinfoPass():
    '''public int authinfoPass(final String password)
    '''
def xover():
    '''public int xover(final String selectedArticles)
    '''
def xhdr():
    '''public int xhdr(final String header, final String selectedArticles)
    '''
def listActive():
    '''public int listActive(final String wildmat)
    '''
