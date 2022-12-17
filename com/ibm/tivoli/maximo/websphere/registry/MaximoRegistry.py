def ():
    '''returns MaximoRegistry\n\n
    ()\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final Properties props)\n
    '''
def checkPassword():
    '''returns String\n\n
    checkPassword(String userSecurityName, final String passwd)\n
    '''
def mapCertificate():
    '''returns String\n\n
    mapCertificate(final X509Certificate[] cert)\n
    '''
def getRealm():
    '''returns String\n\n
    getRealm()\n
    '''
def getUsers():
    '''returns Result\n\n
    getUsers(final String pattern, final int limit)\n
    '''
def getUserDisplayName():
    '''returns String\n\n
    getUserDisplayName(final String userSecurityName)\n
    '''
def getUniqueUserId():
    '''returns String\n\n
    getUniqueUserId(final String userSecurityName)\n
    '''
def getUserSecurityName():
    '''returns String\n\n
    getUserSecurityName(final String uniqueUserId)\n
    '''
def isValidUser():
    '''returns boolean\n\n
    isValidUser(final String userSecurityName)\n
    '''
def getGroups():
    '''returns Result\n\n
    getGroups(final String pattern, final int limit)\n
    '''
def getGroupDisplayName():
    '''returns String\n\n
    getGroupDisplayName(final String groupSecurityName)\n
    '''
def getUniqueGroupId():
    '''returns String\n\n
    getUniqueGroupId(final String groupSecurityName)\n
    '''
def getUniqueGroupIds():
    '''returns List\n\n
    getUniqueGroupIds(final String uniqueUserId)\n
    '''
def getGroupSecurityName():
    '''returns String\n\n
    getGroupSecurityName(final String uniqueGroupId)\n
    '''
def isValidGroup():
    '''returns boolean\n\n
    isValidGroup(final String groupSecurityName)\n
    '''
def getGroupsForUser():
    '''returns List\n\n
    getGroupsForUser(final String userSecurityName)\n
    '''
def getUsersForGroup():
    '''returns Result\n\n
    getUsersForGroup(final String groupSecurityName, final int limit)\n
    '''
def createCredential():
    '''returns WSCredential\n\n
    createCredential(final String userSecurityName)\n
    '''
