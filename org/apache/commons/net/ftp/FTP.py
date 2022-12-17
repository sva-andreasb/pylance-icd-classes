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
def ():
    '''returns FTP\n\n
    ()\n
    '''
def setControlEncoding():
    '''returns None\n\n
    setControlEncoding(final String encoding)\n
    '''
def getControlEncoding():
    '''returns String\n\n
    getControlEncoding()\n
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
def getReplyStrings():
    '''returns String[]\n\n
    getReplyStrings()\n
    '''
def getReplyString():
    '''returns String\n\n
    getReplyString()\n
    '''
def user():
    '''returns int\n\n
    user(final String username)\n
    '''
def pass():
    '''returns int\n\n
    pass(final String password)\n
    '''
def acct():
    '''returns int\n\n
    acct(final String account)\n
    '''
def abor():
    '''returns int\n\n
    abor()\n
    '''
def cwd():
    '''returns int\n\n
    cwd(final String directory)\n
    '''
def cdup():
    '''returns int\n\n
    cdup()\n
    '''
def quit():
    '''returns int\n\n
    quit()\n
    '''
def rein():
    '''returns int\n\n
    rein()\n
    '''
def smnt():
    '''returns int\n\n
    smnt(final String dir)\n
    '''
def port():
    '''returns int\n\n
    port(final InetAddress host, final int port)\n
    '''
def pasv():
    '''returns int\n\n
    pasv()\n
    '''
def type():
    '''returns int\n\n
    type(final int fileType, final int formatOrByteSize)\n
    type(final int fileType)\n
    '''
def stru():
    '''returns int\n\n
    stru(final int structure)\n
    '''
def mode():
    '''returns int\n\n
    mode(final int mode)\n
    '''
def retr():
    '''returns int\n\n
    retr(final String pathname)\n
    '''
def stor():
    '''returns int\n\n
    stor(final String pathname)\n
    '''
def stou():
    '''returns int\n\n
    stou()\n
    stou(final String pathname)\n
    '''
def appe():
    '''returns int\n\n
    appe(final String pathname)\n
    '''
def allo():
    '''returns int\n\n
    allo(final int bytes)\n
    allo(final int bytes, final int recordSize)\n
    '''
def rest():
    '''returns int\n\n
    rest(final String marker)\n
    '''
def rnfr():
    '''returns int\n\n
    rnfr(final String pathname)\n
    '''
def rnto():
    '''returns int\n\n
    rnto(final String pathname)\n
    '''
def dele():
    '''returns int\n\n
    dele(final String pathname)\n
    '''
def rmd():
    '''returns int\n\n
    rmd(final String pathname)\n
    '''
def mkd():
    '''returns int\n\n
    mkd(final String pathname)\n
    '''
def pwd():
    '''returns int\n\n
    pwd()\n
    '''
def list():
    '''returns int\n\n
    list()\n
    list(final String pathname)\n
    '''
def nlst():
    '''returns int\n\n
    nlst()\n
    nlst(final String pathname)\n
    '''
def site():
    '''returns int\n\n
    site(final String parameters)\n
    '''
def syst():
    '''returns int\n\n
    syst()\n
    '''
def stat():
    '''returns int\n\n
    stat()\n
    stat(final String pathname)\n
    '''
def help():
    '''returns int\n\n
    help()\n
    help(final String command)\n
    '''
def noop():
    '''returns int\n\n
    noop()\n
    '''
