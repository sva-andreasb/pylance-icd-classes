OP_EQ = "int  1"
OP_NEQ = "int  2"
OP_GTEQ = "int  3"
OP_LTEQ = "int  4"
OP_LT = "int  5"
OP_IN = "int  6"
OP_GT = "int  7"
OP_LIKE = "int  8"
def ():
    '''returns RESTQbe\n\n
    (final String resourceName, final UserInfo userInfo)\n
    '''
def hasQbe():
    '''returns boolean\n\n
    hasQbe()\n
    '''
def removeQbe():
    '''returns None\n\n
    removeQbe(final String propName)\n
    '''
def setQbe():
    '''returns None\n\n
    setQbe(final String propName, final int op, final String value)\n
    setQbe(final String propName, final int op, final long value)\n
    setQbe(final String propName, final int op, final boolean value)\n
    setQbe(final String propName, final int op, final double value)\n
    setQbe(final String propName, final int op, final Date dt)\n
    '''
def getQbe():
    '''returns Object\n\n
    getQbe()\n
    getQbe(final String querySeparator)\n
    '''
def resetQbe():
    '''returns None\n\n
    resetQbe()\n
    '''
def setInvalidQbe():
    '''returns None\n\n
    setInvalidQbe(final String propName, final String value)\n
    '''
def hasInvalidQbe():
    '''returns boolean\n\n
    hasInvalidQbe()\n
    '''
