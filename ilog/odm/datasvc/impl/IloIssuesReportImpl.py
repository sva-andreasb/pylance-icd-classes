COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
COMMON_ISSUES_CATEGORY = "String  \"category\""
COMMON_ISSUES_TYPE = "String  \"type\""
COMMON_ISSUES_MESSAGE_KEY = "String  \"msg_key\""
COMMON_ISSUES_MESSAGE_PARAM = "String  \"msg_param\""
COMMON_ISSUES_TABLE_ID = "String  \"table_id\""
COMMON_ISSUES_ROW_ID = "String  \"row_id\""
COMMON_ISSUES_COLUMN_NAME = "String  \"column_name\""
COMMON_ISSUES_ACKNOWLEGED = "String  \"acknowledged\""
COMMON_ISSUES_CATEGORY_INDEX = "int  0"
COMMON_ISSUES_TYPE_INDEX = "int  1"
COMMON_ISSUES_MESSAGE_KEY_INDEX = "int  2"
COMMON_ISSUES_MESSAGE_PARAM_INDEX = "int  3"
COMMON_ISSUES_TABLE_ID_INDEX = "int  4"
COMMON_ISSUES_ROW_ID_INDEX = "int  5"
COMMON_ISSUES_COLUMN_NAME_INDEX = "int  6"
COMMON_ISSUES_ACKNOWLEGED_INDEX = "int  7"
def ():
    '''returns IloRowMapKey\n\n
    (final IloScenario scenario)\n
    (final IloTableContainer table_container)\n
    (final String schema_id, final Long row_id)\n
    '''
def notifyStateChanged():
    '''returns None\n\n
    notifyStateChanged(final IloTableEvent evt)\n
    notifyStateChanged(final IloTableEvent evt)\n
    '''
def notifyRowDeleted():
    '''returns None\n\n
    notifyRowDeleted(final IloRowDeletedEvent evt)\n
    notifyRowDeleted(final IloRowDeletedEvent evt)\n
    '''
def notifyRowChanged():
    '''returns None\n\n
    notifyRowChanged(final IloRowChangedEvent evt)\n
    notifyRowChanged(final IloRowChangedEvent evt)\n
    '''
def notifyRowAdded():
    '''returns None\n\n
    notifyRowAdded(final IloRowAddedEvent evt)\n
    notifyRowAdded(final IloRowAddedEvent evt)\n
    '''
def notifyContentLoaded():
    '''returns None\n\n
    notifyContentLoaded(final IloTableEvent evt)\n
    notifyContentLoaded(final IloTableEvent evt)\n
    '''
def notifyContentChanged():
    '''returns None\n\n
    notifyContentChanged(final IloTableEvent evt)\n
    notifyContentChanged(final IloTableEvent evt)\n
    '''
def notifyChanges():
    '''returns None\n\n
    notifyChanges(final List<IloTableEvent> events)\n
    notifyChanges(final List<IloTableEvent> events)\n
    '''
def addIssue():
    '''returns IloIssueImpl\n\n
    addIssue(final String categoryId, final IloIssue.IssueType type, final String message, final Object[] params)\n
    addIssue(final String categoryId, final IloIssue.IssueType type, final String message, final Object[] params, final IloDataLocation location)\n
    addIssue(final IloRow issueRow)\n
    '''
def clearReport():
    '''returns None\n\n
    clearReport(final String categoryId, final boolean acknowledged)\n
    '''
def getIssuesCount():
    '''returns int\n\n
    getIssuesCount(final String categoryId, final IloIssue.IssueType type, final IloTable table, final IloRow row)\n
    '''
def getIssues():
    '''returns List<IloIssue>\n\n
    getIssues(final String categoryId, final IloTable table, final IloRow row)\n
    '''
def enableIssueOverflow():
    '''returns None\n\n
    enableIssueOverflow(final int issue_overflow)\n
    '''
def disableIssueOverflow():
    '''returns None\n\n
    disableIssueOverflow()\n
    '''
def hasErrors():
    '''returns boolean\n\n
    hasErrors()\n
    '''
def hasWarnings():
    '''returns boolean\n\n
    hasWarnings()\n
    '''
def invalidate():
    '''returns None\n\n
    invalidate()\n
    '''
def isFeatureSupported():
    '''returns boolean\n\n
    isFeatureSupported()\n
    '''
def addIssuesReportListener():
    '''returns None\n\n
    addIssuesReportListener(final IloIssuesReportListener listener)\n
    '''
def removeIssuesReportListener():
    '''returns None\n\n
    removeIssuesReportListener(final IloIssuesReportListener listener)\n
    '''
def beginModifications():
    '''returns None\n\n
    beginModifications()\n
    '''
def endModifications():
    '''returns None\n\n
    endModifications()\n
    '''
def getRowId():
    '''returns Long\n\n
    getRowId()\n
    '''
def getVersion():
    '''returns Long\n\n
    getVersion()\n
    '''
def getCategory():
    '''returns String\n\n
    getCategory()\n
    '''
def getLocation():
    '''returns IloDataLocation\n\n
    getLocation()\n
    '''
def getLocalizedMessage():
    '''returns String\n\n
    getLocalizedMessage()\n
    '''
def getMessageKey():
    '''returns String\n\n
    getMessageKey()\n
    '''
def getMessageParameters():
    '''returns Object[]\n\n
    getMessageParameters()\n
    '''
def getType():
    '''returns IssueType\n\n
    getType()\n
    '''
def getAcknowledged():
    '''returns boolean\n\n
    getAcknowledged()\n
    '''
def setAcknowledged():
    '''returns None\n\n
    setAcknowledged(final boolean acknowleged)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
