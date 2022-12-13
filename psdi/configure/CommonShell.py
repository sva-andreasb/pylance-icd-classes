def CommonShell():
    '''public CommonShell()
    public CommonShell(final MXServer server)
    '''
def doSql():
    '''public void doSql(final List list)
    public void doSql(final List list, final Util util)
    public void doSql(final String sql)
    public void doSql(final String sql, final Util util)
    '''
def doCall():
    '''public void doCall(final String sql)
    '''
def doDB2TextSearchCall():
    '''public void doDB2TextSearchCall(final String sql)
    '''
def doWait():
    '''public void doWait(final int milli)
    '''
def getProperty():
    '''public String getProperty(final String propName)
    '''
def reformatForSqlsvr():
    '''public static String reformatForSqlsvr(final Connection sqlCon, String sql)
    '''
def reformatForDB2():
    '''public static String reformatForDB2(final Connection sqlCon, final String sqlIn)
    '''
def execRuntime():
    '''public void execRuntime(final String arg)
    '''
def showMXException():
    '''public void showMXException(final MXApplicationException e, final boolean infoOnly, final boolean hideErrorKey)
    public void showMXException(final MXApplicationException e)
    '''
def getDisplayMessage():
    '''public String getDisplayMessage(final String errorkey, final Object[] params)
    public String getDisplayMessage(final String errorkey)
    '''
def showMsg():
    '''public void showMsg(String str)
    '''
def logSql():
    '''public final void logSql(final String sql)
    '''
def setup():
    '''public void setup(final HashMap params)
    '''
def getRootDirName():
    '''public String getRootDirName()
    '''
def setupInstance():
    '''public void setupInstance(final HashMap params)
    '''
def setupFromPropfile():
    '''public String setupFromPropfile(String propfile, String user, String password, final String tempUrl, final String rootDirName, String propdir)
    '''
def setupNested():
    '''public void setupNested(final Connection con, final Util util, final String schemaOwner, final Driver driver, final String outdir, final boolean logparam, final boolean execparam, final HashMap params, final String nestedUrl)
    '''
def setupNestedInstance():
    '''public void setupNestedInstance(final HashMap params)
    '''
def endSetup():
    '''public void endSetup(final String outdir, String outfile, final HashMap params)
    '''
def createOutfile():
    '''public void createOutfile(final String outdir, final String outfile)
    '''
def getOutfile():
    '''public File getOutfile()
    '''
def getOutstream():
    '''public PrintStream getOutstream()
    '''
def endSetupInstance():
    '''public void endSetupInstance(final String outdir, final String outfile, final HashMap params)
    '''
def endProcess():
    '''public void endProcess(final boolean errors)
    '''
def endProcessInstance():
    '''public void endProcessInstance()
    '''
def setDB2TextOutput():
    '''public void setDB2TextOutput(final PrintStream out1, final PrintStream out2)
    '''
def setUserLangCode():
    '''public void setUserLangCode(final String value)
    '''
def setConnection():
    '''public void setConnection(final Connection inCon)
    '''
