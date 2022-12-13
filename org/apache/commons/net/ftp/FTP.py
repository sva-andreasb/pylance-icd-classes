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
DEFAULT_CONTROL_ENCODING = "String  ISO-8859-1""
def FTP():
'''public FTP()
'''
pass
def setControlEncoding():
'''public void setControlEncoding(final String encoding)
'''
pass
def getControlEncoding():
'''public String getControlEncoding()
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
def getReplyStrings():
'''public String[] getReplyStrings()
'''
pass
def getReplyString():
'''public String getReplyString()
'''
pass
def user():
'''public int user(final String username)
'''
pass
def pass():
'''public int pass(final String password)
'''
pass
def acct():
'''public int acct(final String account)
'''
pass
def abor():
'''public int abor()
'''
pass
def cwd():
'''public int cwd(final String directory)
'''
pass
def cdup():
'''public int cdup()
'''
pass
def quit():
'''public int quit()
'''
pass
def rein():
'''public int rein()
'''
pass
def smnt():
'''public int smnt(final String dir)
'''
pass
def port():
'''public int port(final InetAddress host, final int port)
'''
pass
def pasv():
'''public int pasv()
'''
pass
def type():
'''public int type(final int fileType, final int formatOrByteSize)
public int type(final int fileType)
'''
pass
def stru():
'''public int stru(final int structure)
'''
pass
def mode():
'''public int mode(final int mode)
'''
pass
def retr():
'''public int retr(final String pathname)
'''
pass
def stor():
'''public int stor(final String pathname)
'''
pass
def stou():
'''public int stou()
public int stou(final String pathname)
'''
pass
def appe():
'''public int appe(final String pathname)
'''
pass
def allo():
'''public int allo(final int bytes)
public int allo(final int bytes, final int recordSize)
'''
pass
def rest():
'''public int rest(final String marker)
'''
pass
def rnfr():
'''public int rnfr(final String pathname)
'''
pass
def rnto():
'''public int rnto(final String pathname)
'''
pass
def dele():
'''public int dele(final String pathname)
'''
pass
def rmd():
'''public int rmd(final String pathname)
'''
pass
def mkd():
'''public int mkd(final String pathname)
'''
pass
def pwd():
'''public int pwd()
'''
pass
def list():
'''public int list()
public int list(final String pathname)
'''
pass
def nlst():
'''public int nlst()
public int nlst(final String pathname)
'''
pass
def site():
'''public int site(final String parameters)
'''
pass
def syst():
'''public int syst()
'''
pass
def stat():
'''public int stat()
public int stat(final String pathname)
'''
pass
def help():
'''public int help()
public int help(final String command)
'''
pass
def noop():
'''public int noop()
'''
pass
