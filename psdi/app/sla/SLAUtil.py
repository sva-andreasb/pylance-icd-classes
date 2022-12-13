MAXVARS_SINGLESLA = "String  \"APPLYSINGLESLA\""
MAXVARS_USERANGING = "String  \"USESLARANKING\""
SLARECORDS_RESPONSEDATE = "String  \"responsedate\""
SLARECORDS_RESOLUTIONDATE = "String  \"resolutiondate\""
SLARECORDS_CONTACTDATE = "String  \"contactdate\""
APPLYTO_ORG = "String  \"slaorgid\""
APPLYTO_CALENDAR = "String  \"slacalendar\""
APPLYTO_SHIFT = "String  \"slashift\""
CALC_ORG = "String  \"calcorgid\""
CALC_CALENDAR = "String  \"calccalendar\""
CALC_SHIFT = "String  \"calcshift\""
OWNERTABLE = "String  \"ownertable\""
OWNERID = "String  \"ownerid\""
FIELDNAME_VALUE = "String  \"value\""
FIELDNAME_UOM = "String  \"unitofmeasure\""
def getUniqueKeyFieldName():
    '''public static String getUniqueKeyFieldName(final Mbo mbo)
    public static String getUniqueKeyFieldName(final MboSetInfo mboSetInfo)
    '''
def getSuperType():
    '''public static String getSuperType(final Mbo mbo)
    '''
def singleSLA():
    '''public static boolean singleSLA(final Mbo mbo)
    '''
def useRanking():
    '''public static boolean useRanking(final Mbo mbo)
    '''
def buildExcludingWhere():
    '''public static String buildExcludingWhere(final String keyField, final String checkField, final MboSetRemote set)
    '''
def mboEq():
    '''public static boolean mboEq(final MboRemote mbo1, final MboRemote mbo2)
    '''
def isNull():
    '''public static boolean isNull(final String str)
    '''
def getContractStatusToExclude():
    '''public static String getContractStatusToExclude(final Mbo mbo)
    '''
def getContractStatusToInclude():
    '''public static String getContractStatusToInclude(final Mbo mbo)
    '''
def throwValidationException():
    '''public static void throwValidationException(final MboValue mboValue)
    '''
def getInPhrase():
    '''public static String getInPhrase(final String fieldName, final String in)
    '''
def compareCommitment():
    '''public static int compareCommitment(final MboRemote commitment1, final MboRemote commitment2, final Translate translate)
    '''
def getTargetFieldName():
    '''public static String getTargetFieldName(final String targetMboType, final MboRemote commitment, final Translate translate)
    '''
def getSLARecordsTargetFieldName():
    '''public static String getSLARecordsTargetFieldName(final MboRemote commitment, final Translate translate)
    '''
