def createProcessRequest():
'''public String createProcessRequest(final MboRemote mbo, final MXServer mxserver, final UserInfo userinfo)
'''
pass
def createSolution():
'''public MboRemote createSolution(final MboRemote pmIncident, final MboRemote solutionMbo)
'''
pass
def setAttributesInSolution():
'''public void setAttributesInSolution(final MboRemote origMbo, final MboRemote solutionMbo)
'''
pass
def findLatest():
'''public static TKStatusRemote findLatest(final MboSetRemote tkStatuses)
'''
pass
def cumulativeTimeSpent():
'''public static long cumulativeTimeSpent(final String timeSpent)
'''
pass
def timeToString():
'''public static String timeToString(final long cumulativeTime)
'''
pass
def simpleElapseTime():
'''public static String simpleElapseTime(final Date current, final Date last)
'''
pass
def elapseTime():
'''public static String elapseTime(final long dtime)
'''
pass
def canEnterMeterReadings():
'''public void canEnterMeterReadings(final Mbo mbo)
'''
pass
def canReportDowntime():
'''public void canReportDowntime(final Mbo pmIncident)
'''
pass
def setTicketInternalPriority():
'''public static TSDCommonMessage setTicketInternalPriority(final MboRemote ticketMbo, final boolean validate_null)
'''
pass
def ticketAppValidate():
'''public static void ticketAppValidate(final Mbo ticket)
'''
pass
def takeTicketOwnership():
'''public static void takeTicketOwnership(final TicketRemote ticket)
'''
pass
def findDefaultTicketStatusForSite():
'''public static String findDefaultTicketStatusForSite(final MboRemote ticketMbo, final String siteId)
'''
pass
def ticketAdd():
'''public static void ticketAdd(final Ticket ticket)
'''
pass
def accountForPreviousStatus():
'''public static void accountForPreviousStatus(final MboSetRemote tkStatuses, final MboRemote ticketRemote)
'''
pass
def findOrCreatePersistStatusForStatus():
'''public static MboRemote findOrCreatePersistStatusForStatus(final String status, final MboRemote ticketRemote)
'''
pass
def createPersistStatus():
'''public static MboRemote createPersistStatus(final String status, final MboRemote ticketRemote)
'''
pass
def accountForCurrentStatus():
'''public static void accountForCurrentStatus(final MboRemote ticketRemote)
'''
pass
def populateOwnershipInformation():
'''public static void populateOwnershipInformation(final Mbo pmTkStatus)
'''
pass
def validateApplyTKTemplate():
'''public void validateApplyTKTemplate(final MboRemote templateMbo, final MboRemote tk)
'''
pass
def applyTKTemplateRemoveActivities():
'''public void applyTKTemplateRemoveActivities(final MboRemote tk)
'''
pass
def ticketCanRemoveActivities():
'''public void ticketCanRemoveActivities(final MboRemote tk)
'''
pass
def ticketCanTemplateApply():
'''public void ticketCanTemplateApply(final MboRemote tk)
'''
pass
def isSRfromCatalog():
'''public static boolean isSRfromCatalog(final TicketRemote ticket)
'''
pass
