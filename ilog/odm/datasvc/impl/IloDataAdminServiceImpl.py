COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
RIGHT_MULTI_SESSION = "String  \"MULTI_SESSION\""
def ():
    '''returns IloDataAdminServiceImpl\n\n
    (final IloSystemDataManager system_data_manager)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def getAppDataId():
    '''returns String\n\n
    getAppDataId()\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def getOrCreateTechnicalUser():
    '''returns IloUser\n\n
    getOrCreateTechnicalUser(final String technicalUserName)\n
    '''
def getUser():
    '''returns IloUser\n\n
    getUser(final String name)\n
    '''
def getRecycleBin():
    '''returns IloRecycleBin\n\n
    getRecycleBin()\n
    '''
def removeUser():
    '''returns None\n\n
    removeUser(final ilog.odm.datasvc.IloUser user)\n
    '''
def changeUserName():
    '''returns None\n\n
    changeUserName(final ilog.odm.datasvc.IloUser user, final String value)\n
    '''
def addUserRight():
    '''returns None\n\n
    addUserRight(final ilog.odm.datasvc.IloUser user, final String rightId)\n
    '''
def removeUserRight():
    '''returns None\n\n
    removeUserRight(final ilog.odm.datasvc.IloUser user, final String rightId)\n
    '''
def addUserRole():
    '''returns None\n\n
    addUserRole(final ilog.odm.datasvc.IloUser user, final String role)\n
    '''
def getUserRoles():
    '''returns Set<String>\n\n
    getUserRoles(final ilog.odm.datasvc.IloUser user)\n
    '''
def removeUserRole():
    '''returns None\n\n
    removeUserRole(final ilog.odm.datasvc.IloUser user, final String role)\n
    '''
def getPossibleUserRights():
    '''returns Set<String>\n\n
    getPossibleUserRights(final boolean includeSystemRights)\n
    '''
def getResources():
    '''returns IloResourceBundle\n\n
    getResources()\n
    '''
def getConnectionPerformance():
    '''returns IloConnectionPerformance\n\n
    getConnectionPerformance()\n
    '''
def getSaveRatio():
    '''returns int\n\n
    getSaveRatio()\n
    '''
def getSaveQuality():
    '''returns Quality\n\n
    getSaveQuality()\n
    '''
def getLoadRatio():
    '''returns int\n\n
    getLoadRatio()\n
    '''
def getLoadQuality():
    '''returns Quality\n\n
    getLoadQuality()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
