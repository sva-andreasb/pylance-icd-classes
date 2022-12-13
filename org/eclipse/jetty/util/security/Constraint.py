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
def validateMethod():
    '''public static boolean validateMethod(String method)
    '''
def Constraint():
    '''public Constraint()
    public Constraint(final String name, final String role)
    '''
def clone():
    '''public Object clone()
    '''
def setName():
    '''public void setName(final String name)
    '''
def setRoles():
    '''public void setRoles(final String[] roles)
    '''
def isAnyRole():
    '''public boolean isAnyRole()
    '''
def getRoles():
    '''public String[] getRoles()
    '''
def hasRole():
    '''public boolean hasRole(final String role)
    '''
def setAuthenticate():
    '''public void setAuthenticate(final boolean authenticate)
    '''
def getAuthenticate():
    '''public boolean getAuthenticate()
    '''
def isForbidden():
    '''public boolean isForbidden()
    '''
def setDataConstraint():
    '''public void setDataConstraint(final int c)
    '''
def getDataConstraint():
    '''public int getDataConstraint()
    '''
def hasDataConstraint():
    '''public boolean hasDataConstraint()
    '''
def toString():
    '''public String toString()
    '''
