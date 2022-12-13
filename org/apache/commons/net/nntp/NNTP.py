DEFAULT_PORT = "int  119"
def NNTP():
'''public NNTP()
'''
pass
def addProtocolCommandListener():
'''public void addProtocolCommandListener(final ProtocolCommandListener listener)
'''
pass
def removeProtocolCommandListener():
'''public void removeProtocolCommandListener(final ProtocolCommandListener listener)
'''
pass
def disconnect():
'''public void disconnect()
'''
pass
def isAllowedToPost():
'''public boolean isAllowedToPost()
'''
pass
def sendCommand():
'''public int sendCommand(final String command, final String args)
public int sendCommand(final int command, final String args)
public int sendCommand(final String command)
public int sendCommand(final int command)
'''
pass
def getReplyCode():
'''public int getReplyCode()
'''
pass
def getReply():
'''public int getReply()
'''
pass
def getReplyString():
'''public String getReplyString()
'''
pass
def article():
'''public int article(final String messageId)
public int article(final int articleNumber)
public int article()
'''
pass
def body():
'''public int body(final String messageId)
public int body(final int articleNumber)
public int body()
'''
pass
def head():
'''public int head(final String messageId)
public int head(final int articleNumber)
public int head()
'''
pass
def stat():
'''public int stat(final String messageId)
public int stat(final int articleNumber)
public int stat()
'''
pass
def group():
'''public int group(final String newsgroup)
'''
pass
def help():
'''public int help()
'''
pass
def ihave():
'''public int ihave(final String messageId)
'''
pass
def last():
'''public int last()
'''
pass
def list():
'''public int list()
'''
pass
def next():
'''public int next()
'''
pass
def newgroups():
'''public int newgroups(final String date, final String time, final boolean GMT, final String distributions)
'''
pass
def newnews():
'''public int newnews(final String newsgroups, final String date, final String time, final boolean GMT, final String distributions)
'''
pass
def post():
'''public int post()
'''
pass
def quit():
'''public int quit()
'''
pass
def authinfoUser():
'''public int authinfoUser(final String username)
'''
pass
def authinfoPass():
'''public int authinfoPass(final String password)
'''
pass
def xover():
'''public int xover(final String selectedArticles)
'''
pass
def xhdr():
'''public int xhdr(final String header, final String selectedArticles)
'''
pass
def listActive():
'''public int listActive(final String wildmat)
'''
pass
