def LoginProfile():
'''public LoginProfile(final long session, final String usrname, final GregorianCalendar expiry, final int invalidlogins, final Properties attrs)
public LoginProfile(final long session, final String usrname, final GregorianCalendar expiry, final int invalidlogins, final Properties attrs, final Set groups)
public LoginProfile(final long session, final String usrname, final GregorianCalendar expiry, final int invalidlogins, final Properties attrs, final Set groups, final SerializableCookie SSOToken)
'''
pass
def getSession():
'''public SessionContext getSession()
'''
pass
def getUser():
'''public String getUser()
'''
pass
def getPasswordExpiry():
'''public GregorianCalendar getPasswordExpiry()
'''
pass
def getInvalidLoginAttempts():
'''public int getInvalidLoginAttempts()
'''
pass
def getAttributes():
'''public Properties getAttributes()
'''
pass
def getGroupMembership():
'''public Set getGroupMembership()
'''
pass
def getSSOToken():
'''public SerializableCookie getSSOToken()
'''
pass
