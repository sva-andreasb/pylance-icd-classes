def ():
    '''returns LoginProfile\n\n
    (final long session, final String usrname, final GregorianCalendar expiry, final int invalidlogins, final Properties attrs)\n
    (final long session, final String usrname, final GregorianCalendar expiry, final int invalidlogins, final Properties attrs, final Set groups)\n
    (final long session, final String usrname, final GregorianCalendar expiry, final int invalidlogins, final Properties attrs, final Set groups, final SerializableCookie SSOToken)\n
    '''
def getSession():
    '''returns SessionContext\n\n
    getSession()\n
    '''
def getUser():
    '''returns String\n\n
    getUser()\n
    '''
def getPasswordExpiry():
    '''returns GregorianCalendar\n\n
    getPasswordExpiry()\n
    '''
def getInvalidLoginAttempts():
    '''returns int\n\n
    getInvalidLoginAttempts()\n
    '''
def getAttributes():
    '''returns Properties\n\n
    getAttributes()\n
    '''
def getGroupMembership():
    '''returns Set\n\n
    getGroupMembership()\n
    '''
def getSSOToken():
    '''returns SerializableCookie\n\n
    getSSOToken()\n
    '''
