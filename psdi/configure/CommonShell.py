def CommonShell():
'''public CommonShell()
public CommonShell(final MXServer server)
'''
pass
def doSql():
'''public void doSql(final List list)
public void doSql(final List list, final Util util)
public void doSql(final String sql)
public void doSql(final String sql, final Util util)
'''
pass
def doCall():
'''public void doCall(final String sql)
'''
pass
def doDB2TextSearchCall():
'''public void doDB2TextSearchCall(final String sql)
'''
pass
def doWait():
'''public void doWait(final int milli)
'''
pass
def getProperty():
'''public String getProperty(final String propName)
'''
pass
def reformatForSqlsvr():
'''public static String reformatForSqlsvr(final Connection sqlCon, String sql)
'''
pass
def reformatForDB2():
'''public static String reformatForDB2(final Connection sqlCon, final String sqlIn)
'''
pass
def execRuntime():
'''public void execRuntime(final String arg)
'''
pass
def showMXException():
'''public void showMXException(final MXApplicationException e, final boolean infoOnly, final boolean hideErrorKey)
public void showMXException(final MXApplicationException e)
'''
pass
def getDisplayMessage():
'''public String getDisplayMessage(final String errorkey, final Object[] params)
public String getDisplayMessage(final String errorkey)
'''
pass
def showMsg():
'''public void showMsg(String str)
'''
pass
def logSql():
'''public final void logSql(final String sql)
'''
pass
def setup():
'''public void setup(final HashMap params)
'''
pass
def getRootDirName():
'''public String getRootDirName()
'''
pass
def setupInstance():
'''public void setupInstance(final HashMap params)
'''
pass
def setupFromPropfile():
'''public String setupFromPropfile(String propfile, String user, String password, final String tempUrl, final String rootDirName, String propdir)
'''
pass
def setupNested():
'''public void setupNested(final Connection con, final Util util, final String schemaOwner, final Driver driver, final String outdir, final boolean logparam, final boolean execparam, final HashMap params, final String nestedUrl)
'''
pass
def setupNestedInstance():
'''public void setupNestedInstance(final HashMap params)
'''
pass
def endSetup():
'''public void endSetup(final String outdir, String outfile, final HashMap params)
'''
pass
def createOutfile():
'''public void createOutfile(final String outdir, final String outfile)
'''
pass
def getOutfile():
'''public File getOutfile()
'''
pass
def getOutstream():
'''public PrintStream getOutstream()
'''
pass
def endSetupInstance():
'''public void endSetupInstance(final String outdir, final String outfile, final HashMap params)
'''
pass
def endProcess():
'''public void endProcess(final boolean errors)
'''
pass
def endProcessInstance():
'''public void endProcessInstance()
'''
pass
def setDB2TextOutput():
'''public void setDB2TextOutput(final PrintStream out1, final PrintStream out2)
'''
pass
def setUserLangCode():
'''public void setUserLangCode(final String value)
'''
pass
def setConnection():
'''public void setConnection(final Connection inCon)
'''
pass
