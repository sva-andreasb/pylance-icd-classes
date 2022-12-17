DATA_FORMAT = "int  1114794784"
FORMAT_VERSION = "int  83886080"
DH_SIZE = "int  20"
DH_MAGIC = "int  0"
DH_FORMATVERSION = "int  1"
DH_LENGTH = "int  2"
DH_CATCOUNT = "int  3"
DH_FTABLE = "int  4"
DH_FTABLELEN = "int  5"
DH_RTABLE = "int  6"
DH_RTABLELEN = "int  7"
DH_TRIE = "int  8"
DH_TRIELEN = "int  9"
DH_RULESOURCE = "int  10"
DH_RULESOURCELEN = "int  11"
DH_STATUSTABLE = "int  12"
DH_STATUSTABLELEN = "int  13"
ACCEPTING = "int  0"
LOOKAHEAD = "int  1"
TAGIDX = "int  2"
RESERVED = "int  3"
NEXTSTATES = "int  4"
RBBI_LOOKAHEAD_HARD_BREAK = "int  1"
RBBI_BOF_REQUIRED = "int  2"
def getRowIndex():
    '''returns int\n\n
    getRowIndex(final int state)\n
    '''
def dump():
    '''returns None\n\n
    dump(final PrintStream out)\n
    '''
def put():
    '''returns int\n\n
    put(final DataOutputStream bytes)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def isDataVersionAcceptable():
    '''returns boolean\n\n
    isDataVersionAcceptable(final byte[] version)\n
    '''
def ():
    '''returns RBBIDataHeader\n\n
    ()\n
    '''
