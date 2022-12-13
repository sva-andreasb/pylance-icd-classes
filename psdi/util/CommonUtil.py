def vectorToStringArray():
    '''    public static String[] vectorToStringArray(final Vector vector)
    '''
def commaSepStringToVector():
    '''    public static Vector<String> commaSepStringToVector(final String tokens)
    public static Vector<String> commaSepStringToVector(final String tokens, final boolean toUpper)
    '''
def getCombineDateTime():
    '''    public static Date getCombineDateTime(final Date date, final Date time)
    '''
def getNextTaskID():
    '''    public static int getNextTaskID(final int maxTask, final String seedName, final String intervalName, final String siteOrOrg)
    '''
def getEmailOfPerson():
    '''    public static String getEmailOfPerson(final MboRemote person)
    '''
def getGroupPeople():
    '''    public static PersonSetRemote getGroupPeople(final PersonGroupRemote group, final MboRemote mbo, final boolean isBroadcast)
    public static PersonSetRemote getGroupPeople(final PersonGroupRemote group, final MboRemote mbo, final boolean isBroadcast, final boolean treatNoCalAsAvailable)
    '''
def getEmailsOfPersonGroup():
    '''    public static String[] getEmailsOfPersonGroup(final PersonGroupRemote personGroup, final MboRemote mbo, final boolean broadcast)
    '''
def getEmailsOfPersonSet():
    '''    public static String[] getEmailsOfPersonSet(final PersonSetRemote personSet)
    '''
def getSMSPhonesOfPersonSet():
    '''    public static HashSet<String> getSMSPhonesOfPersonSet(final PersonSetRemote personSet)
    '''
def getSMSNumOfPerson():
    '''    public static String getSMSNumOfPerson(final MboRemote person)
    '''
def csvStringFromArray():
    '''    public static String csvStringFromArray(final Object[] values)
    '''
def inClauseFromArray():
    '''    public static String inClauseFromArray(final Object[] values)
    '''
def inClauseFromSet():
    '''    public static String inClauseFromSet(final Set values)
    '''
def calcWebUrl():
    '''    public static String calcWebUrl(final MboRemote doc)
    public static String calcWebUrl(final MboRemote doc, final MboRemote doclinkMbo)
    '''
def calEncodedValue():
    '''    public static String calEncodedValue(String filepathvalue)
    '''
def EncodeDocLink():
    '''    public static String EncodeDocLink(String docpath)
    '''
def EncodeFilePath():
    '''    public static String EncodeFilePath(String filepathvalue)
    '''
def getDomainValDescription():
    '''    public static String getDomainValDescription(final String domainid, final String maxvalue, final MboRemote tktotal)
    '''
def arrayToString():
    '''    public static String arrayToString(final String[] list)
    '''
def copyDocStoreFile():
    '''    public static void copyDocStoreFile(final AttachmentStorage docStore, final String in, final String out)
    '''
def copyFile():
    '''    public static void copyFile(final String in, final String out)
    '''
def getWASLoginContext():
    '''    public static LoginContext getWASLoginContext()
    '''
def getDeploymentMgrURL():
    '''    public static String getDeploymentMgrURL()
    '''
def run():
    '''    public Object run()
    public Object run()
    '''
def getAppServerPorts():
    '''    public static String getAppServerPorts()
    '''
def getWASPorts():
    '''    public static String getWASPorts()
    '''
def removeSpaces():
    '''    public static String removeSpaces(final String inStr)
    '''
def removeNewLines():
    '''    public static String removeNewLines(String inStr)
    '''
def isRepairFacilityEnabled():
    '''    public static boolean isRepairFacilityEnabled(final MboRemote mbo, final MXServerRemote mxServer)
    public static boolean isRepairFacilityEnabled(final String orgSite, MXServerRemote mxServer)
    '''
def isBypassSiteMismatchWarningEnabled():
    '''    public static boolean isBypassSiteMismatchWarningEnabled(final MboRemote mbo, final MXServerRemote mxServer)
    public static boolean isBypassSiteMismatchWarningEnabled(final String orgSite, MXServerRemote mxServer)
    '''
def convertGregorianDateToIslamicString():
    '''    public static String convertGregorianDateToIslamicString(Date date, final TimeZone sourceTimeZone, final TimeZone targetTimeZone, final Locale l)
    '''
def isEmail():
    '''    public static boolean isEmail(final String notfType)
    '''
def isSMS():
    '''    public static boolean isSMS(final String notfType)
    '''
def useSQLServerSequence():
    '''    public static boolean useSQLServerSequence()
    '''
