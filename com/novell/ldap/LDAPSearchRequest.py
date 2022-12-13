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
def LDAPSearchRequest():
    '''public LDAPSearchRequest()
    public LDAPSearchRequest(final String s, final int n, final String s2, final String[] array, final int n2, final int n3, final int n4, final boolean b, final LDAPControl[] array2)
    public LDAPSearchRequest(final String s, final int n, final RfcFilter rfcFilter, final String[] array, final int n2, final int n3, final int n4, final boolean b, final LDAPControl[] array2)
    '''
def getDN():
    '''public String getDN()
    '''
def getScope():
    '''public int getScope()
    '''
def getDereference():
    '''public int getDereference()
    '''
def getMaxResults():
    '''public int getMaxResults()
    '''
def getServerTimeLimit():
    '''public int getServerTimeLimit()
    '''
def isTypesOnly():
    '''public boolean isTypesOnly()
    '''
def getAttributes():
    '''public String[] getAttributes()
    '''
def getStringFilter():
    '''public String getStringFilter()
    '''
def getSearchFilter():
    '''public Iterator getSearchFilter()
    '''
