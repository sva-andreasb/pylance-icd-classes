COPYRIGHT = "String  \"IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.\""
def TIMIMService():
    '''    public TIMIMService()
    '''
def init():
    '''    public void init(final Preferences prefs, final String itimAdmistrator, final String itimAdmistratorPwd, final String itimURL, final String tenant, final String org, final String beanUser, final String beanPwd, final String profile)
    '''
def destroy():
    '''    public void destroy()
    '''
def getPlatform():
    '''    public PlatformContext getPlatform()
    '''
def getSubject():
    '''    public Subject getSubject(final PlatformContext platform)
    public Subject getSubject(final PlatformContext platform, final String user, final String password)
    '''
def getAccount():
    '''    public Account getAccount(final String filter, final PlatformContext platform, final Subject subject)
    '''
def getNotesAccounts():
    '''    public Collection getNotesAccounts(final String filter, final PlatformContext platform, final Subject subject, final String NOTESPROFILENAME)
    '''
def getAccounts():
    '''    public Collection getAccounts(final String filter, final PlatformContext platform, final Subject subject)
    '''
def getPerson():
    '''    public Person getPerson(final String filter, final PlatformContext platform, final Subject subject)
    '''
def getDivision():
    '''    public Collection getDivision(final String filter, final PlatformContext platform, final Subject subject)
    '''
def getDepartment():
    '''    public Collection getDepartment(final String divisionDN, final String filter, final PlatformContext platform, final Subject subject)
    '''
def getRole():
    '''    public Collection getRole(final DistinguishedName dn, final String filter, final PlatformContext platform, final Subject subject)
    '''
def getEmpRolesNames():
    '''    public String getEmpRolesNames(final PlatformContext platform, final Subject subject, final DistinguishedName dnRole)
    '''
def changePassword():
    '''    public String changePassword(final String userid, final String oldPassword, final String newPassword, final String confirmPassword)
    '''
def changeNotesPassword():
    '''    public String changeNotesPassword(final String userid, final String oldPassword, final String newPassword, final String confirmPassword, final String NOTESPROFILENAME)
    '''
def resetNotesPassword():
    '''    public String resetNotesPassword(final String userid, final String NOTESPROFILENAME)
    '''
def getLotusNewPwd():
    '''    public String getLotusNewPwd()
    '''
