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
    '''returns boolean\n\n
    hasNullBoundValue()\n
    '''
def ():
    '''returns SqlFormat\n\n
    (final String stmt)\n
    (final Locale locale, final TimeZone timeZone, final String stmt)\n
    (final MboRemote mr, final String stmt)\n
    (final UserInfo uInfo, final String stmt)\n
    '''
def appendStatement():
    '''returns SqlFormat\n\n
    appendStatement(final String statement)\n
    '''
def setBoolean():
    '''returns None\n\n
    setBoolean(final int col, final boolean val)\n
    '''
def setLong():
    '''returns None\n\n
    setLong(final int col, final long val)\n
    '''
def setInt():
    '''returns None\n\n
    setInt(final int col, final int val)\n
    '''
def setFloat():
    '''returns None\n\n
    setFloat(final int col, final float val)\n
    '''
def setDouble():
    '''returns None\n\n
    setDouble(final int col, final double val)\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final int col, final Date val)\n
    '''
def setTime():
    '''returns None\n\n
    setTime(final int col, final Date val)\n
    '''
def setTimestamp():
    '''returns None\n\n
    setTimestamp(final int col, final Date val)\n
    '''
def setBytes():
    '''returns None\n\n
    setBytes(final int col, final byte[] val)\n
    '''
def setObject():
    '''returns None\n\n
    setObject(final int col, final String tbName, final String colName, final String val)\n
    setObject(final int col, final String type, final String val)\n
    '''
def simpleFormat():
    '''returns String\n\n
    simpleFormat()\n
    '''
def validateFormat():
    '''returns String\n\n
    validateFormat()\n
    '''
def format():
    '''returns String\n\n
    format()\n
    format(final MboSetInfo msi, final MboSetRemote set)\n
    '''
def formatRaw():
    '''returns String\n\n
    formatRaw()\n
    '''
def getEncounteredError():
    '''returns MXException\n\n
    getEncounteredError()\n
    '''
def getFieldValue():
    '''returns String\n\n
    getFieldValue(final String field, final MboRemote mbo)\n
    getFieldValue(final String field, final MboRemote mbo, final boolean useLocale)\n
    getFieldValue(String field, final MboRemote mbo, final boolean useLocale, final int indexAfter)\n
    '''
def setNoSpaces():
    '''returns None\n\n
    setNoSpaces(final boolean b)\n
    '''
def setRealNumericNulls():
    '''returns None\n\n
    setRealNumericNulls(final boolean b)\n
    '''
def resolveContent():
    '''returns String\n\n
    resolveContent()\n
    '''
def setIgnoreUnresolved():
    '''returns None\n\n
    setIgnoreUnresolved(final boolean b)\n
    '''
def expressionToQueryWhere():
    '''returns String\n\n
    expressionToQueryWhere()\n
    '''
def limitInClause():
    '''returns String\n\n
    limitInClause(final String where)\n
    limitInClause(final StringBuffer where)\n
    limitInClause(final String where, final String lastWord, final int numOfBraces, final boolean isInClause)\n
    '''
def checkForString():
    '''returns boolean\n\n
    checkForString(final char c)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
