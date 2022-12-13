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
def equals():
    '''public static boolean equals(final RBBIStateTable left, final RBBIStateTable right)
    public boolean equals(final Object other)
    '''
def getRowIndex():
    '''public int getRowIndex(final int state)
    '''
def get():
    '''public static RBBIDataWrapper get(final ByteBuffer bytes)
    '''
def dump():
    '''public void dump(final PrintStream out)
    '''
def intToString():
    '''public static String intToString(final int n, final int width)
    '''
def intToHexString():
    '''public static String intToHexString(final int n, final int width)
    '''
def put():
    '''public int put(final DataOutputStream bytes)
    '''
def isDataVersionAcceptable():
    '''public boolean isDataVersionAcceptable(final byte[] version)
    '''
def RBBIDataHeader():
    '''public RBBIDataHeader()
    '''
