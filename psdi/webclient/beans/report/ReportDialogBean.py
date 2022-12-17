def ():
    '''returns ReportDialogBean\n\n
    ()\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final int nRow, final String attribute, final String value, final long accessModifier)\n
    '''
def runrequestpage():
    '''returns int\n\n
    runrequestpage()\n
    '''
def displayRequestDialog():
    '''returns int\n\n
    displayRequestDialog(final String pageName)\n
    '''
def isLookupMultiSelect():
    '''returns boolean\n\n
    isLookupMultiSelect(final BoundComponentInstance component, final boolean isQueryInput)\n
    '''
def requestreportrun():
    '''returns int\n\n
    requestreportrun()\n
    '''
def editadhocreport():
    '''returns int\n\n
    editadhocreport()\n
    '''
def createScheduleRecord():
    '''returns None\n\n
    createScheduleRecord(final Hashtable reportParams, final DataBean rptParmBean, final MboRemote thisRpt)\n
    '''
def validateSchedFields():
    '''returns boolean\n\n
    validateSchedFields(final DataBean rptParmBean, final Hashtable reportParams)\n
    '''
def getEmailSchedParams():
    '''returns Hashtable\n\n
    getEmailSchedParams(final Hashtable reportParams, final DataBean rptParmBean, final String reportType)\n
    '''
def setRedirect():
    '''returns Hashtable\n\n
    setRedirect(final Hashtable reportParams, final String reportType, final String overridePath, final String quickPrintType)\n
    '''
def getWhereParams():
    '''returns Hashtable\n\n
    getWhereParams(final Hashtable reportParams, final MXSession mxsession, final DataBean rptParmBean, final String reportNum, final boolean useWhere)\n
    getWhereParams(Hashtable reportParams, final MXSession mxsession, final DataBean rptParmBean, final String reportNum, final boolean useWhere, final boolean isdetail)\n
    '''
def getStdParams():
    '''returns Hashtable\n\n
    getStdParams(final Hashtable reportParams, final MXSession mxsession)\n
    '''
def getRptRecordParams():
    '''returns Hashtable\n\n
    getRptRecordParams(final Hashtable reportParams, final MXSession mxsession, final MboSetRemote reportData)\n
    '''
def getMaxPropRptParams():
    '''returns Hashtable\n\n
    getMaxPropRptParams(final Hashtable reportParams, final MXSession mxsession)\n
    '''
def fetchProperty():
    '''returns String\n\n
    fetchProperty(final Properties maxProps, final String propName)\n
    '''
def getCustomReportProps():
    '''returns None\n\n
    getCustomReportProps(final Properties maxProps, final Hashtable reportParams)\n
    '''
def noDef():
    '''returns String\n\n
    noDef(final String val)\n
    '''
def spcDef():
    '''returns String\n\n
    spcDef(final String val)\n
    '''
def nsDef():
    '''returns String\n\n
    nsDef(final String val)\n
    '''
def getMaxProps():
    '''returns Properties\n\n
    getMaxProps()\n
    '''
def qualifyWhere():
    '''returns String\n\n
    qualifyWhere(final MXSession mxsession, final String where, final String baseTable)\n
    '''
def getFileDesc():
    '''returns String\n\n
    getFileDesc(final String appName, final String filename)\n
    '''
def linkFileDesc():
    '''returns MboRemote\n\n
    linkFileDesc(String destfoldername, String filename, final String ext)\n
    '''
def sortDate():
    '''returns Integer[]\n\n
    sortDate(final Hashtable fileList)\n
    '''
def setReportMaxRows():
    '''returns None\n\n
    setReportMaxRows(final int maxrows)\n
    '''
def getSelectionWhere():
    '''returns String\n\n
    getSelectionWhere(final DataBean resultsBean)\n
    '''
def setvalue():
    '''returns int\n\n
    setvalue()\n
    '''
def handleQuickReporting():
    '''returns int\n\n
    handleQuickReporting(final String reportType, final WebClientEvent event, final Hashtable reportParams, final String reportNum, final boolean attachdoc, final String rptParmKey, final String brosDPUrl)\n
    '''
def submitWOChangePrintJob():
    '''returns int\n\n
    submitWOChangePrintJob(final String repKey)\n
    '''
def getSearchFolder():
    '''returns String\n\n
    getSearchFolder()\n
    '''
