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
def getEmptyInstance():
    '''    public static DateTimePatternGenerator getEmptyInstance()
    '''
def getInstance():
    '''    public static DateTimePatternGenerator getInstance()
    public static DateTimePatternGenerator getInstance(final ULocale uLocale)
    public static DateTimePatternGenerator getInstance(final Locale locale)
    '''
def getFrozenInstance():
    '''    public static DateTimePatternGenerator getFrozenInstance(final ULocale uLocale)
    '''
def getDefaultHourFormatChar():
    '''    public char getDefaultHourFormatChar()
    '''
def setDefaultHourFormatChar():
    '''    public void setDefaultHourFormatChar(final char defaultHourFormatChar)
    '''
def getAppendFormatNumber():
    '''    public static int getAppendFormatNumber(final UResource.Key key)
    public static int getAppendFormatNumber(final String string)
    '''
def getBestPattern():
    '''    public String getBestPattern(final String skeleton)
    public String getBestPattern(final String skeleton, final int options)
    '''
def addPattern():
    '''    public DateTimePatternGenerator addPattern(final String pattern, final boolean override, final PatternInfo returnInfo)
    '''
def addPatternWithSkeleton():
    '''    public DateTimePatternGenerator addPatternWithSkeleton(final String pattern, final String skeletonToUse, final boolean override, final PatternInfo returnInfo)
    '''
def getSkeleton():
    '''    public String getSkeleton(final String pattern)
    '''
def getSkeletonAllowingDuplicates():
    '''    public String getSkeletonAllowingDuplicates(final String pattern)
    '''
def getCanonicalSkeletonAllowingDuplicates():
    '''    public String getCanonicalSkeletonAllowingDuplicates(final String pattern)
    '''
def getBaseSkeleton():
    '''    public String getBaseSkeleton(final String pattern)
    '''
def getSkeletons():
    '''    public Map<String, String> getSkeletons(Map<String, String> result)
    '''
def getBaseSkeletons():
    '''    public Set<String> getBaseSkeletons(Set<String> result)
    '''
def replaceFieldTypes():
    '''    public String replaceFieldTypes(final String pattern, final String skeleton)
    public String replaceFieldTypes(final String pattern, final String skeleton, final int options)
    '''
def setDateTimeFormat():
    '''    public void setDateTimeFormat(final String dateTimeFormat)
    '''
def getDateTimeFormat():
    '''    public String getDateTimeFormat()
    '''
def setDecimal():
    '''    public void setDecimal(final String decimal)
    '''
def getDecimal():
    '''    public String getDecimal()
    '''
def getRedundants():
    '''    public Collection<String> getRedundants(Collection<String> output)
    '''
def setAppendItemFormat():
    '''    public void setAppendItemFormat(final int field, final String value)
    '''
def getAppendItemFormat():
    '''    public String getAppendItemFormat(final int field)
    '''
def setAppendItemName():
    '''    public void setAppendItemName(final int field, final String value)
    '''
def getAppendItemName():
    '''    public String getAppendItemName(final int field)
    '''
def getFieldDisplayName():
    '''    public String getFieldDisplayName(final int field, final DisplayWidth width)
    '''
def isSingleField():
    '''    public static boolean isSingleField(final String skeleton)
    '''
def isFrozen():
    '''    public boolean isFrozen()
    '''
def freeze():
    '''    public DateTimePatternGenerator freeze()
    '''
def cloneAsThawed():
    '''    public DateTimePatternGenerator cloneAsThawed()
    '''
def clone():
    '''    public Object clone()
    '''
def skeletonsAreSimilar():
    '''    public boolean skeletonsAreSimilar(final String id, final String skeleton)
    '''
def getFields():
    '''    public String getFields(final String pattern)
    '''
def put():
    '''    public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
    public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
    public void put(final UResource.Key key, final UResource.Value value, final boolean isRoot)
    public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
    '''
def AvailableFormatsSink():
    '''    public AvailableFormatsSink(final PatternInfo returnInfo)
    '''
def VariableField():
    '''    public VariableField(final String string)
    public VariableField(final String string, final boolean strict)
    '''
def getType():
    '''    public int getType()
    '''
def getCanonicalCode():
    '''    public static String getCanonicalCode(final int type)
    '''
def isNumeric():
    '''    public boolean isNumeric()
    '''
def toString():
    '''    public String toString()
    public String toString()
    public String toString(final int start, final int limit)
    public String toString()
    public String toString()
    public String toString(final boolean skipDayPeriod)
    public String toString()
    public String toString()
    '''
def FormatParser():
    '''    public FormatParser()
    '''
def set():
    '''    public final FormatParser set(final String string)
    public FormatParser set(final String string, final boolean strict)
    '''
def getItems():
    '''    public List<Object> getItems()
    '''
def hasDateAndTimeFields():
    '''    public boolean hasDateAndTimeFields()
    '''
def quoteLiteral():
    '''    public Object quoteLiteral(final String string)
    '''
def PatternWithMatcher():
    '''    public PatternWithMatcher(final String pat, final DateTimeMatcher matcher)
    '''
def PatternWithSkeletonFlag():
    '''    public PatternWithSkeletonFlag(final String pat, final boolean skelSpecified)
    '''
def clear():
    '''    public void clear()
    '''
def isFieldEmpty():
    '''    public boolean isFieldEmpty(final int field)
    '''
def toCanonicalString():
    '''    public String toCanonicalString()
    public String toCanonicalString(final boolean skipDayPeriod)
    public String toCanonicalString()
    '''
def appendTo():
    '''    public StringBuilder appendTo(final StringBuilder sb)
    '''
def appendFieldTo():
    '''    public StringBuilder appendFieldTo(final int field, final StringBuilder sb)
    '''
def compareTo():
    '''    public int compareTo(final SkeletonFields other)
    public int compareTo(final DateTimeMatcher that)
    '''
def equals():
    '''    public boolean equals(final Object other)
    public boolean equals(final Object other)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    '''
def fieldIsNumeric():
    '''    public boolean fieldIsNumeric(final int field)
    '''
