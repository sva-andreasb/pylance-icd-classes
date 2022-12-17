DEREF_NEVER = "int  0"
DEREF_SEARCHING = "int  1"
DEREF_FINDING = "int  2"
DEREF_ALWAYS = "int  3"
def ():
    '''returns LDAPSearchConstraints\n\n
    ()\n
    (final LDAPConstraints ldapConstraints)\n
    (final int n, final int serverTimeLimit, final int dereference, final int maxResults, final boolean b, final int batchSize, final LDAPReferralHandler ldapReferralHandler, final int n2)\n
    '''
def getBatchSize():
    '''returns int\n\n
    getBatchSize()\n
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
def setBatchSize():
    '''returns None\n\n
    setBatchSize(final int batchSize)\n
    '''
def setDereference():
    '''returns None\n\n
    setDereference(final int dereference)\n
    '''
def setMaxResults():
    '''returns None\n\n
    setMaxResults(final int maxResults)\n
    '''
def setServerTimeLimit():
    '''returns None\n\n
    setServerTimeLimit(final int serverTimeLimit)\n
    '''
