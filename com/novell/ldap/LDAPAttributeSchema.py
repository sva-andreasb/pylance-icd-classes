USER_APPLICATIONS = "int  0"
DIRECTORY_OPERATION = "int  1"
DISTRIBUTED_OPERATION = "int  2"
DSA_OPERATION = "int  3"
def LDAPAttributeSchema():
'''public LDAPAttributeSchema()
public LDAPAttributeSchema(final String[] names, final String oid, final String description, final String syntaxString, final boolean single, final String s, final boolean obsolete, final String equality, final String ordering, final String substring, final boolean collective, final boolean userMod, final int usage)
public LDAPAttributeSchema(final String s)
'''
pass
def getSyntaxString():
'''public String getSyntaxString()
'''
pass
def getSuperior():
'''public String getSuperior()
'''
pass
def isSingleValued():
'''public boolean isSingleValued()
'''
pass
def getEqualityMatchingRule():
'''public String getEqualityMatchingRule()
'''
pass
def getOrderingMatchingRule():
'''public String getOrderingMatchingRule()
'''
pass
def getSubstringMatchingRule():
'''public String getSubstringMatchingRule()
'''
pass
def isCollective():
'''public boolean isCollective()
'''
pass
def isUserModifiable():
'''public boolean isUserModifiable()
'''
pass
def getUsage():
'''public int getUsage()
'''
pass
def readDSML():
'''public static Object readDSML(final InputStream inputStream)
'''
pass
