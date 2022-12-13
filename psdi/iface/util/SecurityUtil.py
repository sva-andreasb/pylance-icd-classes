ALLOWDFLTLOGIN = "String  \"ALLOWDFLTLOGIN\""
APIKEYLOGIN = "String  \"@@$$--APIKEY--$$@@\""
def setTenantUserInfo():
    '''    public static void setTenantUserInfo(final UserInfo userInfo)
    '''
def cleanTenantUserInfo():
    '''    public static void cleanTenantUserInfo()
    '''
def setTenantCodeContext():
    '''    public static void setTenantCodeContext(final String tenantCode)
    '''
def clearTenantCodeContext():
    '''    public static void clearTenantCodeContext()
    '''
def getTenantCodeContext():
    '''    public static String getTenantCodeContext()
    '''
def getUserInfo():
    '''    public static UserInfo getUserInfo(String loginid, final String password, final Principal principal)
    public static UserInfo getUserInfo()
    '''
def getUserInfoFromApiKey():
    '''    public static UserInfo getUserInfoFromApiKey(String apikey)
    '''
def isAllowDefaultLogin():
    '''    public static boolean isAllowDefaultLogin()
    '''
def getNewUserInfo():
    '''    public static UserInfo getNewUserInfo()
    public static UserInfo getNewUserInfo(final String loginid, final String password)
    public static UserInfo getNewUserInfo(final String[] loginid, final String password)
    public static UserInfo getNewUserInfo(final String loginid)
    public static UserInfo getNewUserInfo(final String[] loginDet)
    '''
def disconnectUser():
    '''    public static void disconnectUser(final UserInfo userInfo)
    '''
def isDisconnectUser():
    '''    public static boolean isDisconnectUser()
    '''
def getNewUserInfoWithTenantID():
    '''    public static UserInfo getNewUserInfoWithTenantID(final String[] loginDet)
    '''
def invalidateSSOSession():
    '''    public static void invalidateSSOSession(final HttpServletRequest request, final HttpServletResponse response)
    '''
