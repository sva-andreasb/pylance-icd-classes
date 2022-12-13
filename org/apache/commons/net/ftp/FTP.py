DEFAULT_DATA_PORT = "int  20"
DEFAULT_PORT = "int  21"
ASCII_FILE_TYPE = "int  0"
EBCDIC_FILE_TYPE = "int  1"
IMAGE_FILE_TYPE = "int  2"
BINARY_FILE_TYPE = "int  2"
LOCAL_FILE_TYPE = "int  3"
NON_PRINT_TEXT_FORMAT = "int  4"
TELNET_TEXT_FORMAT = "int  5"
CARRIAGE_CONTROL_TEXT_FORMAT = "int  6"
FILE_STRUCTURE = "int  7"
RECORD_STRUCTURE = "int  8"
PAGE_STRUCTURE = "int  9"
STREAM_TRANSFER_MODE = "int  10"
BLOCK_TRANSFER_MODE = "int  11"
COMPRESSED_TRANSFER_MODE = "int  12"
DEFAULT_CONTROL_ENCODING = "String  \"ISO-8859-1\""
def FTP():
    '''public FTP()
    '''
def setControlEncoding():
    '''public void setControlEncoding(final String encoding)
    '''
def getControlEncoding():
    '''public String getControlEncoding()
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
def getReplyStrings():
    '''public String[] getReplyStrings()
    '''
def getReplyString():
    '''public String getReplyString()
    '''
def user():
    '''public int user(final String username)
    '''
def pass():
    '''public int pass(final String password)
    '''
def acct():
    '''public int acct(final String account)
    '''
def abor():
    '''public int abor()
    '''
def cwd():
    '''public int cwd(final String directory)
    '''
def cdup():
    '''public int cdup()
    '''
def quit():
    '''public int quit()
    '''
def rein():
    '''public int rein()
    '''
def smnt():
    '''public int smnt(final String dir)
    '''
def port():
    '''public int port(final InetAddress host, final int port)
    '''
def pasv():
    '''public int pasv()
    '''
def type():
    '''public int type(final int fileType, final int formatOrByteSize)
    public int type(final int fileType)
    '''
def stru():
    '''public int stru(final int structure)
    '''
def mode():
    '''public int mode(final int mode)
    '''
def retr():
    '''public int retr(final String pathname)
    '''
def stor():
    '''public int stor(final String pathname)
    '''
def stou():
    '''public int stou()
    public int stou(final String pathname)
    '''
def appe():
    '''public int appe(final String pathname)
    '''
def allo():
    '''public int allo(final int bytes)
    public int allo(final int bytes, final int recordSize)
    '''
def rest():
    '''public int rest(final String marker)
    '''
def rnfr():
    '''public int rnfr(final String pathname)
    '''
def rnto():
    '''public int rnto(final String pathname)
    '''
def dele():
    '''public int dele(final String pathname)
    '''
def rmd():
    '''public int rmd(final String pathname)
    '''
def mkd():
    '''public int mkd(final String pathname)
    '''
def pwd():
    '''public int pwd()
    '''
def list():
    '''public int list()
    public int list(final String pathname)
    '''
def nlst():
    '''public int nlst()
    public int nlst(final String pathname)
    '''
def site():
    '''public int site(final String parameters)
    '''
def syst():
    '''public int syst()
    '''
def stat():
    '''public int stat()
    public int stat(final String pathname)
    '''
def help():
    '''public int help()
    public int help(final String command)
    '''
def noop():
    '''public int noop()
    '''
