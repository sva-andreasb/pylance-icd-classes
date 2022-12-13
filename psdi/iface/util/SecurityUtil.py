ALLOWDFLTLOGIN = "String  ALLOWDFLTLOGIN""
APIKEYLOGIN = "String  @@$$--APIKEY--$$@@""
def setTenantUserInfo():
'''public static void setTenantUserInfo(final UserInfo userInfo)
'''
pass
def cleanTenantUserInfo():
'''public static void cleanTenantUserInfo()
'''
pass
def setTenantCodeContext():
'''public static void setTenantCodeContext(final String tenantCode)
'''
pass
def clearTenantCodeContext():
'''public static void clearTenantCodeContext()
'''
pass
def getTenantCodeContext():
'''public static String getTenantCodeContext()
'''
pass
def getUserInfo():
'''public static UserInfo getUserInfo(String loginid, final String password, final Principal principal)
public static UserInfo getUserInfo()
'''
pass
def getUserInfoFromApiKey():
'''public static UserInfo getUserInfoFromApiKey(String apikey)
'''
pass
def isAllowDefaultLogin():
'''public static boolean isAllowDefaultLogin()
'''
pass
def getNewUserInfo():
'''public static UserInfo getNewUserInfo()
public static UserInfo getNewUserInfo(final String loginid, final String password)
public static UserInfo getNewUserInfo(final String[] loginid, final String password)
public static UserInfo getNewUserInfo(final String loginid)
public static UserInfo getNewUserInfo(final String[] loginDet)
'''
pass
def disconnectUser():
'''public static void disconnectUser(final UserInfo userInfo)
'''
pass
def isDisconnectUser():
'''public static boolean isDisconnectUser()
'''
pass
def getNewUserInfoWithTenantID():
'''public static UserInfo getNewUserInfoWithTenantID(final String[] loginDet)
'''
pass
def invalidateSSOSession():
'''public static void invalidateSSOSession(final HttpServletRequest request, final HttpServletResponse response)
'''
pass
