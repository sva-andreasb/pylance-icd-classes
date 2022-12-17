USER_APPLICATIONS = "int  0"
DIRECTORY_OPERATION = "int  1"
DISTRIBUTED_OPERATION = "int  2"
DSA_OPERATION = "int  3"
def ():
    '''returns LDAPAttributeSchema\n\n
    ()\n
    (final String[] names, final String oid, final String description, final String syntaxString, final boolean single, final String s, final boolean obsolete, final String equality, final String ordering, final String substring, final boolean collective, final boolean userMod, final int usage)\n
    (final String s)\n
    '''
def getSyntaxString():
    '''returns String\n\n
    getSyntaxString()\n
    '''
def getSuperior():
    '''returns String\n\n
    getSuperior()\n
    '''
def isSingleValued():
    '''returns boolean\n\n
    isSingleValued()\n
    '''
def getEqualityMatchingRule():
    '''returns String\n\n
    getEqualityMatchingRule()\n
    '''
def getOrderingMatchingRule():
    '''returns String\n\n
    getOrderingMatchingRule()\n
    '''
def getSubstringMatchingRule():
    '''returns String\n\n
    getSubstringMatchingRule()\n
    '''
def isCollective():
    '''returns boolean\n\n
    isCollective()\n
    '''
def isUserModifiable():
    '''returns boolean\n\n
    isUserModifiable()\n
    '''
def getUsage():
    '''returns int\n\n
    getUsage()\n
    '''
