def createProcessRequest():
    '''    public String createProcessRequest(final MboRemote mbo, final MXServer mxserver, final UserInfo userinfo)
    '''
def createSolution():
    '''    public MboRemote createSolution(final MboRemote pmIncident, final MboRemote solutionMbo)
    '''
def setAttributesInSolution():
    '''    public void setAttributesInSolution(final MboRemote origMbo, final MboRemote solutionMbo)
    '''
def findLatest():
    '''    public static TKStatusRemote findLatest(final MboSetRemote tkStatuses)
    '''
def cumulativeTimeSpent():
    '''    public static long cumulativeTimeSpent(final String timeSpent)
    '''
def timeToString():
    '''    public static String timeToString(final long cumulativeTime)
    '''
def simpleElapseTime():
    '''    public static String simpleElapseTime(final Date current, final Date last)
    '''
def elapseTime():
    '''    public static String elapseTime(final long dtime)
    '''
def canEnterMeterReadings():
    '''    public void canEnterMeterReadings(final Mbo mbo)
    '''
def canReportDowntime():
    '''    public void canReportDowntime(final Mbo pmIncident)
    '''
def setTicketInternalPriority():
    '''    public static TSDCommonMessage setTicketInternalPriority(final MboRemote ticketMbo, final boolean validate_null)
    '''
def ticketAppValidate():
    '''    public static void ticketAppValidate(final Mbo ticket)
    '''
def takeTicketOwnership():
    '''    public static void takeTicketOwnership(final TicketRemote ticket)
    '''
def findDefaultTicketStatusForSite():
    '''    public static String findDefaultTicketStatusForSite(final MboRemote ticketMbo, final String siteId)
    '''
def ticketAdd():
    '''    public static void ticketAdd(final Ticket ticket)
    '''
def accountForPreviousStatus():
    '''    public static void accountForPreviousStatus(final MboSetRemote tkStatuses, final MboRemote ticketRemote)
    '''
def findOrCreatePersistStatusForStatus():
    '''    public static MboRemote findOrCreatePersistStatusForStatus(final String status, final MboRemote ticketRemote)
    '''
def createPersistStatus():
    '''    public static MboRemote createPersistStatus(final String status, final MboRemote ticketRemote)
    '''
def accountForCurrentStatus():
    '''    public static void accountForCurrentStatus(final MboRemote ticketRemote)
    '''
def populateOwnershipInformation():
    '''    public static void populateOwnershipInformation(final Mbo pmTkStatus)
    '''
def validateApplyTKTemplate():
    '''    public void validateApplyTKTemplate(final MboRemote templateMbo, final MboRemote tk)
    '''
def applyTKTemplateRemoveActivities():
    '''    public void applyTKTemplateRemoveActivities(final MboRemote tk)
    '''
def ticketCanRemoveActivities():
    '''    public void ticketCanRemoveActivities(final MboRemote tk)
    '''
def ticketCanTemplateApply():
    '''    public void ticketCanTemplateApply(final MboRemote tk)
    '''
def isSRfromCatalog():
    '''    public static boolean isSRfromCatalog(final TicketRemote ticket)
    '''
