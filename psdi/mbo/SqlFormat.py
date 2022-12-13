OLD_PREFIX = "String  $old_""
OWNER = "String  &OWNER&""
APPNAME = "String  &APPNAME&""
MBONAME = "String  &MBONAME&""
OWNERNAME = "String  &OWNERNAME&""
PERSONID = "String  &PERSONID&""
USER = "String  &USERNAME&""
DATE = "String  &DATE&""
DATETIME = "String  &DATETIME&""
SEQUENCE = "String  &SEQUENCE&""
HOSTNAME = "String  &HOSTNAME&""
UNIQUEID = "String  &UNIQUEID&""
DOMAINFILTERINGPREFIX = "String  &domainfilter&_""
SYNONYMLISTPREFIX = "String  &synonymlist&_""
TIMEZONEPREFIX = "String  &timezone&_""
LOCALEPREFIX = "String  &locale&_""
def hasNullBoundValue():
'''public boolean hasNullBoundValue()
'''
pass
def getDBProperties():
'''public static Properties getDBProperties()
'''
pass
def setDBProperties():
'''public static void setDBProperties(final Properties p)
'''
pass
def getUpperFunction():
'''public static String getUpperFunction(final String param)
'''
pass
def getTimestampFunction():
'''public static String getTimestampFunction(final Date param)
'''
pass
def getTimeFunction():
'''public static String getTimeFunction(final Date param)
'''
pass
def getNullValueFunction():
'''public static String getNullValueFunction(final String param, final String nullVal)
'''
pass
def getDateFunction():
'''public static String getDateFunction(final Date param)
'''
pass
def getDateHistogramFunction():
'''public static String getDateHistogramFunction(final String funcName, final String attr)
'''
pass
def SqlFormat():
'''public SqlFormat(final String stmt)
public SqlFormat(final Locale locale, final TimeZone timeZone, final String stmt)
public SqlFormat(final MboRemote mr, final String stmt)
public SqlFormat(final UserInfo uInfo, final String stmt)
'''
pass
def appendStatement():
'''public SqlFormat appendStatement(final String statement)
'''
pass
def setBoolean():
'''public void setBoolean(final int col, final boolean val)
'''
pass
def setLong():
'''public void setLong(final int col, final long val)
'''
pass
def setInt():
'''public void setInt(final int col, final int val)
'''
pass
def setFloat():
'''public void setFloat(final int col, final float val)
'''
pass
def setDouble():
'''public void setDouble(final int col, final double val)
'''
pass
def setDate():
'''public void setDate(final int col, final Date val)
'''
pass
def setTime():
'''public void setTime(final int col, final Date val)
'''
pass
def setTimestamp():
'''public void setTimestamp(final int col, final Date val)
'''
pass
def setBytes():
'''public void setBytes(final int col, final byte[] val)
'''
pass
def setObject():
'''public void setObject(final int col, final String tbName, final String colName, final String val)
public void setObject(final int col, final String type, final String val)
'''
pass
def simpleFormat():
'''public String simpleFormat()
'''
pass
def validateFormat():
'''public String validateFormat()
'''
pass
def format():
'''public String format()
public String format(final MboSetInfo msi, final MboSetRemote set)
'''
pass
def formatRaw():
'''public String formatRaw()
'''
pass
def getEncounteredError():
'''public MXException getEncounteredError()
'''
pass
def getFieldValue():
'''public String getFieldValue(final String field, final MboRemote mbo)
public String getFieldValue(final String field, final MboRemote mbo, final boolean useLocale)
public String getFieldValue(String field, final MboRemote mbo, final boolean useLocale, final int indexAfter)
'''
pass
def setNoSpaces():
'''public void setNoSpaces(final boolean b)
'''
pass
def setRealNumericNulls():
'''public void setRealNumericNulls(final boolean b)
'''
pass
def getSQLString():
'''public static String getSQLString(final String s)
'''
pass
def reverseSQLString():
'''public static String reverseSQLString(final String s)
'''
pass
def resolveContent():
'''public String resolveContent()
'''
pass
def setIgnoreUnresolved():
'''public void setIgnoreUnresolved(final boolean b)
'''
pass
def expressionToQueryWhere():
'''public String expressionToQueryWhere()
'''
pass
def isStrReservedKey():
'''public static boolean isStrReservedKey(String str)
'''
pass
def limitInClause():
'''public String limitInClause(final String where)
public StringBuffer limitInClause(final StringBuffer where)
public String limitInClause(final String where, final String lastWord, final int numOfBraces, final boolean isInClause)
'''
pass
def checkForString():
'''public boolean checkForString(final char c)
'''
pass
def reset():
'''public void reset()
'''
pass
