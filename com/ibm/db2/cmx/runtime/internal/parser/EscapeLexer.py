isLexingPossibleCastFunctionBit_ = "char  '\u0001'"
isLabeledDurationBit_ = "char  '\u0010'"
delimitersThatDontPrecedeUnaryOperators_ = "String  \")]}\\"'\""
delimitersThatMightEndSelectExpressionList_ = "String  \"*)]}\\"'\""
def getSqlStatementType():
    '''returns SqlStatementType\n\n
    getSqlStatementType()\n
    '''
def foundSearchedValue():
    '''returns boolean\n\n
    foundSearchedValue()\n
    '''
def ():
    '''returns ParenthesizedLevelDetail\n\n
    (final String s)\n
    (final String s, final boolean b)\n
    (final String s, final String s2)\n
    (final ParenthesizedLevelDetail parenthesizedLevelDetail, final String openParensPreviousToken_)\n
    (final ParenthesizedLevelDetail parenthesizedLevelDetail)\n
    '''
def reinit():
    '''returns None\n\n
    reinit()\n
    '''
def getCurrentPos():
    '''returns int\n\n
    getCurrentPos()\n
    '''
def getUpToNextNotInQuotedStringOrRemainder():
    '''returns String\n\n
    getUpToNextNotInQuotedStringOrRemainder(final char c, final char c2, final boolean b, final boolean b2)\n
    '''
def getUpToNextNotInSingleQuotedStringOrRemainder():
    '''returns String\n\n
    getUpToNextNotInSingleQuotedStringOrRemainder(final char c, final boolean b)\n
    '''
def parseSql():
    '''returns String\n\n
    parseSql(final ParameterInfoArray parameterInfoArray, final int n)\n
    '''
def handleHostVariable():
    '''returns None\n\n
    handleHostVariable(final StringBuilder sb, final SqlParameterInfo sqlParameterInfo, final String s, final ParameterInfoArray parameterInfoArray)\n
    '''
def parseSqlAndGetSqlType():
    '''returns SqlStatementType\n\n
    parseSqlAndGetSqlType()\n
    '''
def parseSqlAndGetStoredProcParamIndexes():
    '''returns Integer[]\n\n
    parseSqlAndGetStoredProcParamIndexes()\n
    '''
def isVTIParam():
    '''returns boolean\n\n
    isVTIParam(final TypeInfo typeInfo)\n
    '''
def parseSQLTextForStaticExecution():
    '''returns String\n\n
    parseSQLTextForStaticExecution()\n
    '''
def upperCaseSQLNotInQuotedString():
    '''returns String\n\n
    upperCaseSQLNotInQuotedString()\n
    '''
def escapeUnescapedQuotes():
    '''returns String\n\n
    escapeUnescapedQuotes()\n
    '''
def parseSQLTextForUpdate():
    '''returns boolean\n\n
    parseSQLTextForUpdate()\n
    '''
def parseAndSubstituteParameterMarkersforLiterals():
    '''returns LiteralsInfo\n\n
    parseAndSubstituteParameterMarkersforLiterals(final LiteralsInfo literalsInfo)\n
    '''
