def ReportDialogBean():
    '''    public ReportDialogBean()
    '''
def initialize():
    '''    public void initialize()
    '''
def setValue():
    '''    public void setValue(final int nRow, final String attribute, final String value, final long accessModifier)
    public synchronized void setValue(final String attribute, final MboRemote mboRemote)
    '''
def runrequestpage():
    '''    public int runrequestpage()
    '''
def displayRequestDialog():
    '''    public int displayRequestDialog(final String pageName)
    '''
def isLookupMultiSelect():
    '''    public boolean isLookupMultiSelect(final BoundComponentInstance component, final boolean isQueryInput)
    '''
def requestreportrun():
    '''    public int requestreportrun()
    '''
def editadhocreport():
    '''    public int editadhocreport()
    '''
def createScheduleRecord():
    '''    public void createScheduleRecord(final Hashtable reportParams, final DataBean rptParmBean, final MboRemote thisRpt)
    '''
def validateSchedFields():
    '''    public boolean validateSchedFields(final DataBean rptParmBean, final Hashtable reportParams)
    '''
def getEmailSchedParams():
    '''    public Hashtable getEmailSchedParams(final Hashtable reportParams, final DataBean rptParmBean, final String reportType)
    '''
def setRedirect():
    '''    public Hashtable setRedirect(final Hashtable reportParams, final String reportType, final String overridePath, final String quickPrintType)
    '''
def getWhereParams():
    '''    public Hashtable getWhereParams(final Hashtable reportParams, final MXSession mxsession, final DataBean rptParmBean, final String reportNum, final boolean useWhere)
    public Hashtable getWhereParams(Hashtable reportParams, final MXSession mxsession, final DataBean rptParmBean, final String reportNum, final boolean useWhere, final boolean isdetail)
    '''
def getStdParams():
    '''    public Hashtable getStdParams(final Hashtable reportParams, final MXSession mxsession)
    '''
def getRptRecordParams():
    '''    public Hashtable getRptRecordParams(final Hashtable reportParams, final MXSession mxsession, final MboSetRemote reportData)
    '''
def getMaxPropRptParams():
    '''    public Hashtable getMaxPropRptParams(final Hashtable reportParams, final MXSession mxsession)
    '''
def fetchProperty():
    '''    public String fetchProperty(final Properties maxProps, final String propName)
    '''
def getCustomReportProps():
    '''    public void getCustomReportProps(final Properties maxProps, final Hashtable reportParams)
    '''
def noDef():
    '''    public String noDef(final String val)
    '''
def spcDef():
    '''    public String spcDef(final String val)
    '''
def nsDef():
    '''    public String nsDef(final String val)
    '''
def getMaxProps():
    '''    public Properties getMaxProps()
    '''
def qualifyWhere():
    '''    public String qualifyWhere(final MXSession mxsession, final String where, final String baseTable)
    '''
def getFileDesc():
    '''    public String getFileDesc(final String appName, final String filename)
    '''
def linkFileDesc():
    '''    public MboRemote linkFileDesc(String destfoldername, String filename, final String ext)
    '''
def sortDate():
    '''    public Integer[] sortDate(final Hashtable fileList)
    '''
def setReportMaxRows():
    '''    public void setReportMaxRows(final int maxrows)
    '''
def getSelectionWhere():
    '''    public String getSelectionWhere(final DataBean resultsBean)
    '''
def setQbe():
    '''    public synchronized void setQbe(final String attribute, String expression)
    '''
def setvalue():
    '''    public int setvalue()
    '''
def setDate():
    '''    public synchronized void setDate(final String controlId, final String attribute, final Date value)
    '''
def handleQuickReporting():
    '''    public int handleQuickReporting(final String reportType, final WebClientEvent event, final Hashtable reportParams, final String reportNum, final boolean attachdoc, final String rptParmKey, final String brosDPUrl)
    '''
def submitWOChangePrintJob():
    '''    public int submitWOChangePrintJob(final String repKey)
    '''
def getSearchFolder():
    '''    public String getSearchFolder()
    '''
