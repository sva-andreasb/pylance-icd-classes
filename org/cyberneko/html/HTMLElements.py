A = "short  0"
ABBR = "short  1"
ACRONYM = "short  2"
ADDRESS = "short  3"
APPLET = "short  4"
AREA = "short  5"
B = "short  6"
BASE = "short  7"
BASEFONT = "short  8"
BDO = "short  9"
BGSOUND = "short  10"
BIG = "short  11"
BLINK = "short  12"
BLOCKQUOTE = "short  13"
BODY = "short  14"
BR = "short  15"
BUTTON = "short  16"
CAPTION = "short  17"
CENTER = "short  18"
CITE = "short  19"
CODE = "short  20"
COL = "short  21"
COLGROUP = "short  22"
COMMENT = "short  23"
DEL = "short  24"
DFN = "short  25"
DIR = "short  26"
DIV = "short  27"
DD = "short  28"
DL = "short  29"
DT = "short  30"
EM = "short  31"
EMBED = "short  32"
FIELDSET = "short  33"
FONT = "short  34"
FORM = "short  35"
FRAME = "short  36"
FRAMESET = "short  37"
H1 = "short  38"
H2 = "short  39"
H3 = "short  40"
H4 = "short  41"
H5 = "short  42"
H6 = "short  43"
HEAD = "short  44"
HR = "short  45"
HTML = "short  46"
I = "short  47"
IFRAME = "short  48"
ILAYER = "short  49"
IMG = "short  50"
INPUT = "short  51"
INS = "short  52"
ISINDEX = "short  53"
KBD = "short  54"
KEYGEN = "short  55"
LABEL = "short  56"
LAYER = "short  57"
LEGEND = "short  58"
LI = "short  59"
LINK = "short  60"
LISTING = "short  61"
MAP = "short  62"
MARQUEE = "short  63"
MENU = "short  64"
META = "short  65"
MULTICOL = "short  66"
NEXTID = "short  67"
NOBR = "short  68"
NOEMBED = "short  69"
NOFRAMES = "short  70"
NOLAYER = "short  71"
NOSCRIPT = "short  72"
OBJECT = "short  73"
OL = "short  74"
OPTION = "short  75"
OPTGROUP = "short  76"
P = "short  77"
PARAM = "short  78"
PLAINTEXT = "short  79"
PRE = "short  80"
Q = "short  81"
RB = "short  82"
RBC = "short  83"
RP = "short  84"
RT = "short  85"
RTC = "short  86"
RUBY = "short  87"
S = "short  88"
SAMP = "short  89"
SCRIPT = "short  90"
SECTION = "short  91"
SELECT = "short  92"
SMALL = "short  93"
SOUND = "short  94"
SPACER = "short  95"
SPAN = "short  96"
STRIKE = "short  97"
STRONG = "short  98"
STYLE = "short  99"
SUB = "short  100"
SUP = "short  101"
TABLE = "short  102"
TBODY = "short  103"
TD = "short  104"
TEXTAREA = "short  105"
TFOOT = "short  106"
TH = "short  107"
THEAD = "short  108"
TITLE = "short  109"
TR = "short  110"
TT = "short  111"
U = "short  112"
UL = "short  113"
VAR = "short  114"
WBR = "short  115"
XML = "short  116"
XMP = "short  117"
UNKNOWN = "short  118"
INLINE = "int  1"
BLOCK = "int  2"
EMPTY = "int  4"
CONTAINER = "int  8"
SPECIAL = "int  16"
def getElement():
    '''public static final Element getElement(final short code)
    public static final Element getElement(final String ename)
    public static final Element getElement(final String ename, final Element element)
    '''
def Element():
    '''public Element(final short code, final String name, final int flags, final short parent, final short[] closes)
    public Element(final short code, final String name, final int flags, final short parent, final short bounds, final short[] closes)
    public Element(final short code, final String name, final int flags, final short[] parents, final short[] closes)
    public Element(final short code, final String name, final int flags, final short[] parents, final short bounds, final short[] closes)
    '''
def isInline():
    '''public final boolean isInline()
    '''
def isBlock():
    '''public final boolean isBlock()
    '''
def isEmpty():
    '''public final boolean isEmpty()
    '''
def isContainer():
    '''public final boolean isContainer()
    '''
def isSpecial():
    '''public final boolean isSpecial()
    '''
def closes():
    '''public boolean closes(final short tag)
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def toString():
    '''public String toString()
    '''
def isParent():
    '''public boolean isParent(final Element element)
    '''
def ElementList():
    '''public ElementList()
    '''
def addElement():
    '''public void addElement(final Element element)
    '''
