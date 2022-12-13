def LoginProfile():
    '''public LoginProfile(final long session, final String usrname, final GregorianCalendar expiry, final int invalidlogins, final Properties attrs)
    public LoginProfile(final long session, final String usrname, final GregorianCalendar expiry, final int invalidlogins, final Properties attrs, final Set groups)
    public LoginProfile(final long session, final String usrname, final GregorianCalendar expiry, final int invalidlogins, final Properties attrs, final Set groups, final SerializableCookie SSOToken)
    '''
def getSession():
    '''public SessionContext getSession()
    '''
def getUser():
    '''public String getUser()
    '''
def getPasswordExpiry():
    '''public GregorianCalendar getPasswordExpiry()
    '''
def getInvalidLoginAttempts():
    '''public int getInvalidLoginAttempts()
    '''
def getAttributes():
    '''public Properties getAttributes()
    '''
def getGroupMembership():
    '''public Set getGroupMembership()
    '''
def getSSOToken():
    '''public SerializableCookie getSSOToken()
    '''
