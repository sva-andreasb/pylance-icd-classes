def getLiteralReplacedSql():
    '''returns String\n\n
    getLiteralReplacedSql()\n
    '''
def setLiteralReplacedSql():
    '''returns None\n\n
    setLiteralReplacedSql(final String literalReplacedSql_)\n
    '''
def getLiteralType():
    '''returns short\n\n
    getLiteralType(final int n)\n
    '''
def getParameterMappedIndex():
    '''returns Integer\n\n
    getParameterMappedIndex(final int i)\n
    '''
def getMappedParameterCount():
    '''returns int\n\n
    getMappedParameterCount()\n
    '''
def getLiteralValueforIndex():
    '''returns String\n\n
    getLiteralValueforIndex(final int i)\n
    '''
def allowLiteralSubstitution():
    '''returns None\n\n
    allowLiteralSubstitution()\n
    '''
def disallowLiteralSubstitution():
    '''returns None\n\n
    disallowLiteralSubstitution(final boolean b, final Throwable thrown, final String reasonForDisallowLiteralSubstitution_)\n
    '''
def addLiteralType():
    '''returns None\n\n
    addLiteralType(final int i, final short value)\n
    '''
def addLiteralValue():
    '''returns None\n\n
    addLiteralValue(final int i, final String value)\n
    '''
def setLiteralsInformation():
    '''returns None\n\n
    setLiteralsInformation(final HashMap<Integer, String> literals_)\n
    '''
def isLiteralSubstitutionAllowed():
    '''returns boolean\n\n
    isLiteralSubstitutionAllowed()\n
    '''
def isStatementUsingParamterMarker():
    '''returns boolean\n\n
    isStatementUsingParamterMarker()\n
    '''
def setStatementUsingParamterMarker():
    '''returns None\n\n
    setStatementUsingParamterMarker(final boolean isStatementUsingParamterMarker_)\n
    '''
def disallowedDueToException():
    '''returns boolean\n\n
    disallowedDueToException()\n
    '''
def getReasonForDisallowLiteralSubstitution():
    '''returns String\n\n
    getReasonForDisallowLiteralSubstitution()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getCurrentSql():
    '''returns String\n\n
    getCurrentSql()\n
    '''
def isLiteralSubstitutionAllowedForTheseTokens():
    '''returns boolean\n\n
    isLiteralSubstitutionAllowedForTheseTokens(final String s)\n
    '''
def verifyAndSetActualLiteralsDataType():
    '''returns boolean\n\n
    verifyAndSetActualLiteralsDataType(final PreparedStatement preparedStatement, final PreparedStatementExecutionHandler preparedStatementExecutionHandler)\n
    '''
def isSuccessfulLiteralReplacement():
    '''returns boolean\n\n
    isSuccessfulLiteralReplacement(final String s, final short n, final StringBuilder sb, final char c, final EscapeLexer.ParenthesizedLevelDetail parenthesizedLevelDetail)\n
    '''
def recordParameterMarkerUse():
    '''returns None\n\n
    recordParameterMarkerUse()\n
    '''
def testIsTimestampSubstitutionOK():
    '''returns boolean\n\n
    testIsTimestampSubstitutionOK(final String s)\n
    '''
def isTimezonePresent():
    '''returns boolean\n\n
    isTimezonePresent(final String s)\n
    '''
def needsDBTimestamp():
    '''returns boolean\n\n
    needsDBTimestamp(final String s)\n
    '''
def setRecoveryPoint():
    '''returns None\n\n
    setRecoveryPoint()\n
    '''
def returnToRecoveryPoint():
    '''returns None\n\n
    returnToRecoveryPoint()\n
    '''
