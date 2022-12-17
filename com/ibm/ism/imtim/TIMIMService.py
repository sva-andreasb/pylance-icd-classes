COPYRIGHT = "String  \"IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.\""
def ():
    '''returns TIMIMService\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init(final Preferences prefs, final String itimAdmistrator, final String itimAdmistratorPwd, final String itimURL, final String tenant, final String org, final String beanUser, final String beanPwd, final String profile)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getPlatform():
    '''returns PlatformContext\n\n
    getPlatform()\n
    '''
def getSubject():
    '''returns Subject\n\n
    getSubject(final PlatformContext platform)\n
    getSubject(final PlatformContext platform, final String user, final String password)\n
    '''
def getAccount():
    '''returns Account\n\n
    getAccount(final String filter, final PlatformContext platform, final Subject subject)\n
    '''
def getNotesAccounts():
    '''returns Collection\n\n
    getNotesAccounts(final String filter, final PlatformContext platform, final Subject subject, final String NOTESPROFILENAME)\n
    '''
def getAccounts():
    '''returns Collection\n\n
    getAccounts(final String filter, final PlatformContext platform, final Subject subject)\n
    '''
def getPerson():
    '''returns Person\n\n
    getPerson(final String filter, final PlatformContext platform, final Subject subject)\n
    '''
def getDivision():
    '''returns Collection\n\n
    getDivision(final String filter, final PlatformContext platform, final Subject subject)\n
    '''
def getDepartment():
    '''returns Collection\n\n
    getDepartment(final String divisionDN, final String filter, final PlatformContext platform, final Subject subject)\n
    '''
def getRole():
    '''returns Collection\n\n
    getRole(final DistinguishedName dn, final String filter, final PlatformContext platform, final Subject subject)\n
    '''
def getEmpRolesNames():
    '''returns String\n\n
    getEmpRolesNames(final PlatformContext platform, final Subject subject, final DistinguishedName dnRole)\n
    '''
def changePassword():
    '''returns String\n\n
    changePassword(final String userid, final String oldPassword, final String newPassword, final String confirmPassword)\n
    '''
def changeNotesPassword():
    '''returns String\n\n
    changeNotesPassword(final String userid, final String oldPassword, final String newPassword, final String confirmPassword, final String NOTESPROFILENAME)\n
    '''
def resetNotesPassword():
    '''returns String\n\n
    resetNotesPassword(final String userid, final String NOTESPROFILENAME)\n
    '''
def getLotusNewPwd():
    '''returns String\n\n
    getLotusNewPwd()\n
    '''
