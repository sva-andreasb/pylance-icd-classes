def MaximoRegistry():
    '''public MaximoRegistry()
    '''
def initialize():
    '''public void initialize(final Properties props)
    '''
def checkPassword():
    '''public String checkPassword(String userSecurityName, final String passwd)
    '''
def mapCertificate():
    '''public String mapCertificate(final X509Certificate[] cert)
    '''
def getRealm():
    '''public String getRealm()
    '''
def getUsers():
    '''public Result getUsers(final String pattern, final int limit)
    '''
def getUserDisplayName():
    '''public String getUserDisplayName(final String userSecurityName)
    '''
def getUniqueUserId():
    '''public String getUniqueUserId(final String userSecurityName)
    '''
def getUserSecurityName():
    '''public String getUserSecurityName(final String uniqueUserId)
    '''
def isValidUser():
    '''public boolean isValidUser(final String userSecurityName)
    '''
def getGroups():
    '''public Result getGroups(final String pattern, final int limit)
    '''
def getGroupDisplayName():
    '''public String getGroupDisplayName(final String groupSecurityName)
    '''
def getUniqueGroupId():
    '''public String getUniqueGroupId(final String groupSecurityName)
    '''
def getUniqueGroupIds():
    '''public List getUniqueGroupIds(final String uniqueUserId)
    '''
def getGroupSecurityName():
    '''public String getGroupSecurityName(final String uniqueGroupId)
    '''
def isValidGroup():
    '''public boolean isValidGroup(final String groupSecurityName)
    '''
def getGroupsForUser():
    '''public List getGroupsForUser(final String userSecurityName)
    '''
def getUsersForGroup():
    '''public Result getUsersForGroup(final String groupSecurityName, final int limit)
    '''
def createCredential():
    '''public WSCredential createCredential(final String userSecurityName)
    '''
