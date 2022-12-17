__BASIC_AUTH = "String  \"BASIC\""
__FORM_AUTH = "String  \"FORM\""
__DIGEST_AUTH = "String  \"DIGEST\""
__CERT_AUTH = "String  \"CLIENT_CERT\""
__CERT_AUTH2 = "String  \"CLIENT-CERT\""
__SPNEGO_AUTH = "String  \"SPNEGO\""
DC_UNSET = "int  -1"
DC_NONE = "int  0"
DC_INTEGRAL = "int  1"
DC_CONFIDENTIAL = "int  2"
DC_FORBIDDEN = "int  3"
NONE = "String  \"NONE\""
ANY_ROLE = "String  \"*\""
def ():
    '''returns Constraint\n\n
    ()\n
    (final String name, final String role)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def setRoles():
    '''returns None\n\n
    setRoles(final String[] roles)\n
    '''
def isAnyRole():
    '''returns boolean\n\n
    isAnyRole()\n
    '''
def getRoles():
    '''returns String[]\n\n
    getRoles()\n
    '''
def hasRole():
    '''returns boolean\n\n
    hasRole(final String role)\n
    '''
def setAuthenticate():
    '''returns None\n\n
    setAuthenticate(final boolean authenticate)\n
    '''
def getAuthenticate():
    '''returns boolean\n\n
    getAuthenticate()\n
    '''
def isForbidden():
    '''returns boolean\n\n
    isForbidden()\n
    '''
def setDataConstraint():
    '''returns None\n\n
    setDataConstraint(final int c)\n
    '''
def getDataConstraint():
    '''returns int\n\n
    getDataConstraint()\n
    '''
def hasDataConstraint():
    '''returns boolean\n\n
    hasDataConstraint()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
