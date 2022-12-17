CONTENTSPECNODE_LEAF = "short  0"
CONTENTSPECNODE_ZERO_OR_ONE = "short  1"
CONTENTSPECNODE_ZERO_OR_MORE = "short  2"
CONTENTSPECNODE_ONE_OR_MORE = "short  3"
CONTENTSPECNODE_CHOICE = "short  4"
CONTENTSPECNODE_SEQ = "short  5"
CONTENTSPECNODE_ANY = "short  6"
CONTENTSPECNODE_ANY_OTHER = "short  7"
CONTENTSPECNODE_ANY_LOCAL = "short  8"
CONTENTSPECNODE_ANY_LAX = "short  22"
CONTENTSPECNODE_ANY_OTHER_LAX = "short  23"
CONTENTSPECNODE_ANY_LOCAL_LAX = "short  24"
CONTENTSPECNODE_ANY_SKIP = "short  38"
CONTENTSPECNODE_ANY_OTHER_SKIP = "short  39"
CONTENTSPECNODE_ANY_LOCAL_SKIP = "short  40"
def ():
    '''returns XMLContentSpec\n\n
    ()\n
    (final short n, final Object o, final Object o2)\n
    (final XMLContentSpec values)\n
    (final Provider provider, final int n)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def setValues():
    '''returns None\n\n
    setValues(final short type, final Object value, final Object otherValue)\n
    setValues(final XMLContentSpec xmlContentSpec)\n
    setValues(final Provider provider, final int n)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
