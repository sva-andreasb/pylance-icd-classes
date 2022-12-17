AND = "int  0"
OR = "int  1"
NOT = "int  2"
EQUALITY_MATCH = "int  3"
SUBSTRINGS = "int  4"
GREATER_OR_EQUAL = "int  5"
LESS_OR_EQUAL = "int  6"
PRESENT = "int  7"
APPROX_MATCH = "int  8"
EXTENSIBLE_MATCH = "int  9"
INITIAL = "int  0"
ANY = "int  1"
FINAL = "int  2"
def ():
    '''returns LDAPSearchRequest\n\n
    ()\n
    (final String s, final int n, final String s2, final String[] array, final int n2, final int n3, final int n4, final boolean b, final LDAPControl[] array2)\n
    (final String s, final int n, final RfcFilter rfcFilter, final String[] array, final int n2, final int n3, final int n4, final boolean b, final LDAPControl[] array2)\n
    '''
def getDN():
    '''returns String\n\n
    getDN()\n
    '''
def getScope():
    '''returns int\n\n
    getScope()\n
    '''
def getDereference():
    '''returns int\n\n
    getDereference()\n
    '''
def getMaxResults():
    '''returns int\n\n
    getMaxResults()\n
    '''
def getServerTimeLimit():
    '''returns int\n\n
    getServerTimeLimit()\n
    '''
def isTypesOnly():
    '''returns boolean\n\n
    isTypesOnly()\n
    '''
def getAttributes():
    '''returns String[]\n\n
    getAttributes()\n
    '''
def getStringFilter():
    '''returns String\n\n
    getStringFilter()\n
    '''
def getSearchFilter():
    '''returns Iterator\n\n
    getSearchFilter()\n
    '''
