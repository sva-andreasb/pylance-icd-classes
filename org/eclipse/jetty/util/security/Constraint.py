__BASIC_AUTH = "String  BASIC""
__FORM_AUTH = "String  FORM""
__DIGEST_AUTH = "String  DIGEST""
__CERT_AUTH = "String  CLIENT_CERT""
__CERT_AUTH2 = "String  CLIENT-CERT""
__SPNEGO_AUTH = "String  SPNEGO""
DC_UNSET = "int  -1"
DC_NONE = "int  0"
DC_INTEGRAL = "int  1"
DC_CONFIDENTIAL = "int  2"
DC_FORBIDDEN = "int  3"
NONE = "String  NONE""
ANY_ROLE = "String  *""
def validateMethod():
'''public static boolean validateMethod(String method)
'''
pass
def Constraint():
'''public Constraint()
public Constraint(final String name, final String role)
'''
pass
def clone():
'''public Object clone()
'''
pass
def setName():
'''public void setName(final String name)
'''
pass
def setRoles():
'''public void setRoles(final String[] roles)
'''
pass
def isAnyRole():
'''public boolean isAnyRole()
'''
pass
def getRoles():
'''public String[] getRoles()
'''
pass
def hasRole():
'''public boolean hasRole(final String role)
'''
pass
def setAuthenticate():
'''public void setAuthenticate(final boolean authenticate)
'''
pass
def getAuthenticate():
'''public boolean getAuthenticate()
'''
pass
def isForbidden():
'''public boolean isForbidden()
'''
pass
def setDataConstraint():
'''public void setDataConstraint(final int c)
'''
pass
def getDataConstraint():
'''public int getDataConstraint()
'''
pass
def hasDataConstraint():
'''public boolean hasDataConstraint()
'''
pass
def toString():
'''public String toString()
'''
pass
