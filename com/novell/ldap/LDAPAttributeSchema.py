USER_APPLICATIONS = "int  0"
DIRECTORY_OPERATION = "int  1"
DISTRIBUTED_OPERATION = "int  2"
DSA_OPERATION = "int  3"
def LDAPAttributeSchema():
    '''    public LDAPAttributeSchema()
    public LDAPAttributeSchema(final String[] names, final String oid, final String description, final String syntaxString, final boolean single, final String s, final boolean obsolete, final String equality, final String ordering, final String substring, final boolean collective, final boolean userMod, final int usage)
    public LDAPAttributeSchema(final String s)
    '''
def getSyntaxString():
    '''    public String getSyntaxString()
    '''
def getSuperior():
    '''    public String getSuperior()
    '''
def isSingleValued():
    '''    public boolean isSingleValued()
    '''
def getEqualityMatchingRule():
    '''    public String getEqualityMatchingRule()
    '''
def getOrderingMatchingRule():
    '''    public String getOrderingMatchingRule()
    '''
def getSubstringMatchingRule():
    '''    public String getSubstringMatchingRule()
    '''
def isCollective():
    '''    public boolean isCollective()
    '''
def isUserModifiable():
    '''    public boolean isUserModifiable()
    '''
def getUsage():
    '''    public int getUsage()
    '''
def readDSML():
    '''    public static Object readDSML(final InputStream inputStream)
    '''
