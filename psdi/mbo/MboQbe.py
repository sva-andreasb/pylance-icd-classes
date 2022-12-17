def ():
    '''returns AttributeExpressions\n\n
    (final MboSetInfo ms, final boolean processML, final UserInfo userInfo)\n
    (final MboSetInfo ms, final Locale l, final TimeZone tz, final boolean ml, final UserInfo userInfo)\n
    (final String attrStrg)\n
    '''
def addSubQbe():
    '''returns None\n\n
    addSubQbe(final String name, final String[] attributes, final String op, final boolean exactMatch)\n
    addSubQbe(final String name, final String[] attributes, final String operator)\n
    '''
def setCaseSensitive():
    '''returns None\n\n
    setCaseSensitive(final boolean state)\n
    '''
def isCaseSensitive():
    '''returns boolean\n\n
    isCaseSensitive()\n
    '''
def setOperatorOr():
    '''returns None\n\n
    setOperatorOr()\n
    '''
def setOperatorAnd():
    '''returns None\n\n
    setOperatorAnd()\n
    '''
def getOperator():
    '''returns String\n\n
    getOperator()\n
    '''
def setExactMatch():
    '''returns None\n\n
    setExactMatch(final boolean state)\n
    '''
def isExactMatch():
    '''returns boolean\n\n
    isExactMatch()\n
    '''
def ignoreQbeExactMatchSet():
    '''returns None\n\n
    ignoreQbeExactMatchSet(final boolean flag)\n
    '''
def isIgnoreQbeExactMatchSet():
    '''returns boolean\n\n
    isIgnoreQbeExactMatchSet()\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale l, final TimeZone t)\n
    '''
def setQbe():
    '''returns None\n\n
    setQbe(final String[] attr, final String exp)\n
    setQbe(final String[] attr, final String[] exp)\n
    setQbe(final String attr, final String[] exp)\n
    setQbe(final String attr, final String expr)\n
    '''
def setWhereQbe():
    '''returns None\n\n
    setWhereQbe(final String attrStr, final String value, final String clause)\n
    setWhereQbe(final boolean isWhereWbe)\n
    '''
def getAllQbeKeys():
    '''returns Enumeration\n\n
    getAllQbeKeys()\n
    '''
def getQbe():
    '''returns String[][]\n\n
    getQbe(final String attrStr)\n
    getQbe()\n
    '''
def resetQbe():
    '''returns None\n\n
    resetQbe()\n
    '''
def getWhere():
    '''returns String\n\n
    getWhere()\n
    getWhere(final String alias)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String val)\n
    setValue(final String[] val)\n
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
def getWhereSnippet():
    '''returns String\n\n
    getWhereSnippet(final String alias)\n
    '''
def sZettUpperCase():
    '''returns String\n\n
    sZettUpperCase(final String str)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
