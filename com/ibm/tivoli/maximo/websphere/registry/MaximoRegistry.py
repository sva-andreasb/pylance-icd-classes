def MaximoRegistry():
'''public MaximoRegistry()
'''
pass
def initialize():
'''public void initialize(final Properties props)
'''
pass
def checkPassword():
'''public String checkPassword(String userSecurityName, final String passwd)
'''
pass
def mapCertificate():
'''public String mapCertificate(final X509Certificate[] cert)
'''
pass
def getRealm():
'''public String getRealm()
'''
pass
def getUsers():
'''public Result getUsers(final String pattern, final int limit)
'''
pass
def getUserDisplayName():
'''public String getUserDisplayName(final String userSecurityName)
'''
pass
def getUniqueUserId():
'''public String getUniqueUserId(final String userSecurityName)
'''
pass
def getUserSecurityName():
'''public String getUserSecurityName(final String uniqueUserId)
'''
pass
def isValidUser():
'''public boolean isValidUser(final String userSecurityName)
'''
pass
def getGroups():
'''public Result getGroups(final String pattern, final int limit)
'''
pass
def getGroupDisplayName():
'''public String getGroupDisplayName(final String groupSecurityName)
'''
pass
def getUniqueGroupId():
'''public String getUniqueGroupId(final String groupSecurityName)
'''
pass
def getUniqueGroupIds():
'''public List getUniqueGroupIds(final String uniqueUserId)
'''
pass
def getGroupSecurityName():
'''public String getGroupSecurityName(final String uniqueGroupId)
'''
pass
def isValidGroup():
'''public boolean isValidGroup(final String groupSecurityName)
'''
pass
def getGroupsForUser():
'''public List getGroupsForUser(final String userSecurityName)
'''
pass
def getUsersForGroup():
'''public Result getUsersForGroup(final String groupSecurityName, final int limit)
'''
pass
def createCredential():
'''public WSCredential createCredential(final String userSecurityName)
'''
pass
