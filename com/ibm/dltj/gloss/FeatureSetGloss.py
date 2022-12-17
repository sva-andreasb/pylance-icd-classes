DLT_SIMPLE_DECOMP_FLAG_ALONE = "int  1"
DLT_SIMPLE_DECOMP_FLAG_BEGINNING = "int  2"
DLT_SIMPLE_DECOMP_FLAG_MIDDLE = "int  4"
DLT_SIMPLE_DECOMP_FLAG_END = "int  8"
DLT_SIMPLE_DECOMP_MASK_ANY = "int  15"
DLT_SIMPLE_DECOMP_FLAG_INVALID = "int  16"
POS_UNKNOWN = "int  0"
POS_PRONOUN = "int  1"
POS_VERB = "int  2"
POS_NOUN = "int  3"
POS_ADJECTIVE = "int  4"
POS_ADVERB = "int  5"
POS_ADPOSITION = "int  6"
POS_INTERJECTION = "int  7"
POS_CONJUNCTION = "int  8"
POS_MAX = "int  100"
DECOMP_FLAG_ALONE = "int  101"
DECOMP_FLAG_BEGINNING = "int  102"
DECOMP_FLAG_MIDDLE = "int  103"
DECOMP_FLAG_END = "int  104"
DECOMP_FLAG_INVALID = "int  105"
STOPWORD = "int  200"
DETERMINER = "int  201"
ENDOFSENTENCE = "int  202"
PROPERCASE = "int  203"
ABBREVIATION = "int  204"
ACRONYM = "int  205"
CORRECTLYSPELT = "int  206"
SUGGESTION = "int  207"
COMPOSITIONAL = "int  208"
def ():
    '''returns FeatureSetGloss\n\n
    ()\n
    (final int n, final int n2, final int n3, final int n4, final int n5)\n
    (final int n, final int n2, final boolean b, final boolean b2, final boolean b3, final boolean b4)\n
    (final int n, final int n2, final boolean b, final boolean b2, final boolean b3, final boolean b4, final boolean b5)\n
    '''
def read():
    '''returns None\n\n
    read(final DataInputStream dataInputStream, final int n)\n
    '''
def write():
    '''returns None\n\n
    write(final DataOutputStream dataOutputStream, final GlossMapper glossMapper)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
