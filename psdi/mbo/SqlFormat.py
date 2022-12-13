OLD_PREFIX = "String  \"$old_\""
OWNER = "String  \"&OWNER&\""
APPNAME = "String  \"&APPNAME&\""
MBONAME = "String  \"&MBONAME&\""
OWNERNAME = "String  \"&OWNERNAME&\""
PERSONID = "String  \"&PERSONID&\""
USER = "String  \"&USERNAME&\""
DATE = "String  \"&DATE&\""
DATETIME = "String  \"&DATETIME&\""
SEQUENCE = "String  \"&SEQUENCE&\""
HOSTNAME = "String  \"&HOSTNAME&\""
UNIQUEID = "String  \"&UNIQUEID&\""
DOMAINFILTERINGPREFIX = "String  \"&domainfilter&_\""
SYNONYMLISTPREFIX = "String  \"&synonymlist&_\""
TIMEZONEPREFIX = "String  \"&timezone&_\""
LOCALEPREFIX = "String  \"&locale&_\""
def hasNullBoundValue():
    '''    public boolean hasNullBoundValue()
    '''
def getDBProperties():
    '''    public static Properties getDBProperties()
    '''
def setDBProperties():
    '''    public static void setDBProperties(final Properties p)
    '''
def getUpperFunction():
    '''    public static String getUpperFunction(final String param)
    '''
def getTimestampFunction():
    '''    public static String getTimestampFunction(final Date param)
    '''
def getTimeFunction():
    '''    public static String getTimeFunction(final Date param)
    '''
def getNullValueFunction():
    '''    public static String getNullValueFunction(final String param, final String nullVal)
    '''
def getDateFunction():
    '''    public static String getDateFunction(final Date param)
    '''
def getDateHistogramFunction():
    '''    public static String getDateHistogramFunction(final String funcName, final String attr)
    '''
def SqlFormat():
    '''    public SqlFormat(final String stmt)
    public SqlFormat(final Locale locale, final TimeZone timeZone, final String stmt)
    public SqlFormat(final MboRemote mr, final String stmt)
    public SqlFormat(final UserInfo uInfo, final String stmt)
    '''
def appendStatement():
    '''    public SqlFormat appendStatement(final String statement)
    '''
def setBoolean():
    '''    public void setBoolean(final int col, final boolean val)
    '''
def setLong():
    '''    public void setLong(final int col, final long val)
    '''
def setInt():
    '''    public void setInt(final int col, final int val)
    '''
def setFloat():
    '''    public void setFloat(final int col, final float val)
    '''
def setDouble():
    '''    public void setDouble(final int col, final double val)
    '''
def setDate():
    '''    public void setDate(final int col, final Date val)
    '''
def setTime():
    '''    public void setTime(final int col, final Date val)
    '''
def setTimestamp():
    '''    public void setTimestamp(final int col, final Date val)
    '''
def setBytes():
    '''    public void setBytes(final int col, final byte[] val)
    '''
def setObject():
    '''    public void setObject(final int col, final String tbName, final String colName, final String val)
    public void setObject(final int col, final String type, final String val)
    '''
def simpleFormat():
    '''    public String simpleFormat()
    '''
def validateFormat():
    '''    public String validateFormat()
    '''
def format():
    '''    public String format()
    public String format(final MboSetInfo msi, final MboSetRemote set)
    '''
def formatRaw():
    '''    public String formatRaw()
    '''
def getEncounteredError():
    '''    public MXException getEncounteredError()
    '''
def getFieldValue():
    '''    public String getFieldValue(final String field, final MboRemote mbo)
    public String getFieldValue(final String field, final MboRemote mbo, final boolean useLocale)
    public String getFieldValue(String field, final MboRemote mbo, final boolean useLocale, final int indexAfter)
    '''
def setNoSpaces():
    '''    public void setNoSpaces(final boolean b)
    '''
def setRealNumericNulls():
    '''    public void setRealNumericNulls(final boolean b)
    '''
def getSQLString():
    '''    public static String getSQLString(final String s)
    '''
def reverseSQLString():
    '''    public static String reverseSQLString(final String s)
    '''
def resolveContent():
    '''    public String resolveContent()
    '''
def setIgnoreUnresolved():
    '''    public void setIgnoreUnresolved(final boolean b)
    '''
def expressionToQueryWhere():
    '''    public String expressionToQueryWhere()
    '''
def isStrReservedKey():
    '''    public static boolean isStrReservedKey(String str)
    '''
def limitInClause():
    '''    public String limitInClause(final String where)
    public StringBuffer limitInClause(final StringBuffer where)
    public String limitInClause(final String where, final String lastWord, final int numOfBraces, final boolean isInClause)
    '''
def checkForString():
    '''    public boolean checkForString(final char c)
    '''
def reset():
    '''    public void reset()
    '''
