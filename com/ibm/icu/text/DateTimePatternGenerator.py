ERA = "int  0"
YEAR = "int  1"
QUARTER = "int  2"
MONTH = "int  3"
WEEK_OF_YEAR = "int  4"
WEEK_OF_MONTH = "int  5"
WEEKDAY = "int  6"
DAY = "int  7"
DAY_OF_YEAR = "int  8"
DAY_OF_WEEK_IN_MONTH = "int  9"
DAYPERIOD = "int  10"
HOUR = "int  11"
MINUTE = "int  12"
SECOND = "int  13"
FRACTIONAL_SECOND = "int  14"
ZONE = "int  15"
TYPE_LIMIT = "int  16"
MATCH_NO_OPTIONS = "int  0"
MATCH_HOUR_FIELD_LENGTH = "int  2048"
MATCH_MINUTE_FIELD_LENGTH = "int  4096"
MATCH_SECOND_FIELD_LENGTH = "int  8192"
MATCH_ALL_FIELDS_LENGTH = "int  65535"
OK = "int  0"
BASE_CONFLICT = "int  1"
CONFLICT = "int  2"
def getBestPattern():
    '''returns String\n\n
    getBestPattern(final String skeleton)\n
    getBestPattern(final String skeleton, final int options)\n
    '''
def addPattern():
    '''returns DateTimePatternGenerator\n\n
    addPattern(final String pattern, final boolean override, final PatternInfo returnInfo)\n
    '''
def getSkeleton():
    '''returns String\n\n
    getSkeleton(final String pattern)\n
    '''
def getBaseSkeleton():
    '''returns String\n\n
    getBaseSkeleton(final String pattern)\n
    '''
def getBaseSkeletons():
    '''returns Set<String>\n\n
    getBaseSkeletons(Set<String> result)\n
    '''
def replaceFieldTypes():
    '''returns String\n\n
    replaceFieldTypes(final String pattern, final String skeleton)\n
    replaceFieldTypes(final String pattern, final String skeleton, final int options)\n
    '''
def setDateTimeFormat():
    '''returns None\n\n
    setDateTimeFormat(final String dateTimeFormat)\n
    '''
def getDateTimeFormat():
    '''returns String\n\n
    getDateTimeFormat()\n
    '''
def setDecimal():
    '''returns None\n\n
    setDecimal(final String decimal)\n
    '''
def getDecimal():
    '''returns String\n\n
    getDecimal()\n
    '''
def getRedundants():
    '''returns Collection<String>\n\n
    getRedundants(Collection<String> output)\n
    '''
def setAppendItemFormat():
    '''returns None\n\n
    setAppendItemFormat(final int field, final String value)\n
    '''
def getAppendItemFormat():
    '''returns String\n\n
    getAppendItemFormat(final int field)\n
    '''
def setAppendItemName():
    '''returns None\n\n
    setAppendItemName(final int field, final String value)\n
    '''
def getAppendItemName():
    '''returns String\n\n
    getAppendItemName(final int field)\n
    '''
def isFrozen():
    '''returns boolean\n\n
    isFrozen()\n
    '''
def freeze():
    '''returns DateTimePatternGenerator\n\n
    freeze()\n
    '''
def cloneAsThawed():
    '''returns DateTimePatternGenerator\n\n
    cloneAsThawed()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def skeletonsAreSimilar():
    '''returns boolean\n\n
    skeletonsAreSimilar(final String id, final String skeleton)\n
    '''
def getFields():
    '''returns String\n\n
    getFields(final String pattern)\n
    '''
def ():
    '''returns PatternWithSkeletonFlag\n\n
    (final String string)\n
    (final String string, final boolean strict)\n
    ()\n
    (final String pat, final DateTimeMatcher matcher)\n
    (final String pat, final boolean skelSpecified)\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString(final int start, final int limit)\n
    toString()\n
    toString()\n
    '''
def set():
    '''returns FormatParser\n\n
    set(final String string, final boolean strict)\n
    '''
def getItems():
    '''returns List<Object>\n\n
    getItems()\n
    '''
def hasDateAndTimeFields():
    '''returns boolean\n\n
    hasDateAndTimeFields()\n
    '''
def quoteLiteral():
    '''returns Object\n\n
    quoteLiteral(final String string)\n
    '''
def origStringForField():
    '''returns String\n\n
    origStringForField(final int field)\n
    '''
def fieldIsNumeric():
    '''returns boolean\n\n
    fieldIsNumeric(final int field)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final DateTimeMatcher that)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
