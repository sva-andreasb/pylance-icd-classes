def ():
    '''returns CommonShell\n\n
    ()\n
    (final MXServer server)\n
    '''
def doSql():
    '''returns None\n\n
    doSql(final List list)\n
    doSql(final List list, final Util util)\n
    doSql(final String sql)\n
    doSql(final String sql, final Util util)\n
    '''
def doCall():
    '''returns None\n\n
    doCall(final String sql)\n
    '''
def doDB2TextSearchCall():
    '''returns None\n\n
    doDB2TextSearchCall(final String sql)\n
    '''
def doWait():
    '''returns None\n\n
    doWait(final int milli)\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String propName)\n
    '''
def execRuntime():
    '''returns None\n\n
    execRuntime(final String arg)\n
    '''
def showMXException():
    '''returns None\n\n
    showMXException(final MXApplicationException e, final boolean infoOnly, final boolean hideErrorKey)\n
    showMXException(final MXApplicationException e)\n
    '''
def getDisplayMessage():
    '''returns String\n\n
    getDisplayMessage(final String errorkey, final Object[] params)\n
    getDisplayMessage(final String errorkey)\n
    '''
def showMsg():
    '''returns None\n\n
    showMsg(String str)\n
    '''
def setup():
    '''returns None\n\n
    setup(final HashMap params)\n
    '''
def getRootDirName():
    '''returns String\n\n
    getRootDirName()\n
    '''
def setupInstance():
    '''returns None\n\n
    setupInstance(final HashMap params)\n
    '''
def setupFromPropfile():
    '''returns String\n\n
    setupFromPropfile(String propfile, String user, String password, final String tempUrl, final String rootDirName, String propdir)\n
    '''
def setupNested():
    '''returns None\n\n
    setupNested(final Connection con, final Util util, final String schemaOwner, final Driver driver, final String outdir, final boolean logparam, final boolean execparam, final HashMap params, final String nestedUrl)\n
    '''
def setupNestedInstance():
    '''returns None\n\n
    setupNestedInstance(final HashMap params)\n
    '''
def endSetup():
    '''returns None\n\n
    endSetup(final String outdir, String outfile, final HashMap params)\n
    '''
def createOutfile():
    '''returns None\n\n
    createOutfile(final String outdir, final String outfile)\n
    '''
def getOutfile():
    '''returns File\n\n
    getOutfile()\n
    '''
def getOutstream():
    '''returns PrintStream\n\n
    getOutstream()\n
    '''
def endSetupInstance():
    '''returns None\n\n
    endSetupInstance(final String outdir, final String outfile, final HashMap params)\n
    '''
def endProcess():
    '''returns None\n\n
    endProcess(final boolean errors)\n
    '''
def endProcessInstance():
    '''returns None\n\n
    endProcessInstance()\n
    '''
def setDB2TextOutput():
    '''returns None\n\n
    setDB2TextOutput(final PrintStream out1, final PrintStream out2)\n
    '''
def setUserLangCode():
    '''returns None\n\n
    setUserLangCode(final String value)\n
    '''
def setConnection():
    '''returns None\n\n
    setConnection(final Connection inCon)\n
    '''
