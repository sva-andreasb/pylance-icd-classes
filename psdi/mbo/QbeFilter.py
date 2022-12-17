ORACLEDB = "int  1"
SQLSERVERDB = "int  2"
DB2DB = "int  3"
def ():
    '''returns AttributeExpressions\n\n
    (final MboSet set)\n
    (final MboSetInfo ms, final UserInfo userInfo)\n
    (final MboSetInfo ms, final boolean processML, final UserInfo userInfo)\n
    (final MboSetInfo ms, final Locale l, final TimeZone tz, final boolean ml, final UserInfo userInfo)\n
    (final String attrStrg)\n
    '''
def resetQbe():
    '''returns None\n\n
    resetQbe()\n
    '''
def setQbe():
    '''returns None\n\n
    setQbe(final String attrName, final String expr)\n
    '''
def getQbe():
    '''returns String[][]\n\n
    getQbe(final String attrName)\n
    getQbe()\n
    '''
def hasQbe():
    '''returns boolean\n\n
    hasQbe()\n
    '''
def satisfy():
    '''returns boolean\n\n
    satisfy(final MboRemote mbo)\n
    satisfy(final MboRemote mbo)\n
    '''
def setQbeExactMatch():
    '''returns None\n\n
    setQbeExactMatch(final boolean state)\n
    '''
def setQbeCaseSensitive():
    '''returns None\n\n
    setQbeCaseSensitive(final boolean state)\n
    '''
def setOperatorOr():
    '''returns None\n\n
    setOperatorOr()\n
    '''
def isUsingQbeExactMatch():
    '''returns boolean\n\n
    isUsingQbeExactMatch()\n
    '''
def ignoreQbeExactMatchSet():
    '''returns None\n\n
    ignoreQbeExactMatchSet(final boolean flag)\n
    '''
def isIgnoreQbeExactMatchSet():
    '''returns boolean\n\n
    isIgnoreQbeExactMatchSet()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String val)\n
    '''
def isWildCardPresentAtFirst():
    '''returns boolean\n\n
    isWildCardPresentAtFirst(final String expr)\n
    '''
def isWildCardPresentAtLast():
    '''returns boolean\n\n
    isWildCardPresentAtLast(final String expr)\n
    '''
def isWildCardPresent():
    '''returns boolean\n\n
    isWildCardPresent(final String expr)\n
    '''
def getGuiFieldName():
    '''returns String\n\n
    getGuiFieldName()\n
    '''
def getMboName():
    '''returns String\n\n
    getMboName()\n
    '''
def getAttribute():
    '''returns String\n\n
    getAttribute()\n
    '''
def getPrepend():
    '''returns String\n\n
    getPrepend()\n
    '''
def getQbeKey():
    '''returns String\n\n
    getQbeKey()\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    '''
def setUnparsedValue():
    '''returns None\n\n
    setUnparsedValue(final String val)\n
    '''
def setWhereQbe():
    '''returns None\n\n
    setWhereQbe(final boolean isWhereWbe)\n
    '''
def getWhereSnippet():
    '''returns String\n\n
    getWhereSnippet(final String alias)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
