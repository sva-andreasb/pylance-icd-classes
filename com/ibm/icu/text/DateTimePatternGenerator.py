ERA = "int 0"
YEAR = "int 1"
QUARTER = "int 2"
MONTH = "int 3"
WEEK_OF_YEAR = "int 4"
WEEK_OF_MONTH = "int 5"
WEEKDAY = "int 6"
DAY = "int 7"
DAY_OF_YEAR = "int 8"
DAY_OF_WEEK_IN_MONTH = "int 9"
DAYPERIOD = "int 10"
HOUR = "int 11"
MINUTE = "int 12"
SECOND = "int 13"
FRACTIONAL_SECOND = "int 14"
ZONE = "int 15"
TYPE_LIMIT = "int 16"
MATCH_NO_OPTIONS = "int 0"
MATCH_HOUR_FIELD_LENGTH = "int 2048"
MATCH_MINUTE_FIELD_LENGTH = "int 4096"
MATCH_SECOND_FIELD_LENGTH = "int 8192"
MATCH_ALL_FIELDS_LENGTH = "int 65535"
OK = "int 0"
BASE_CONFLICT = "int 1"
CONFLICT = "int 2"
def getEmptyInstance():
'''public static DateTimePatternGenerator getEmptyInstance()
'''
pass
def getInstance():
'''public static DateTimePatternGenerator getInstance()
public static DateTimePatternGenerator getInstance(final ULocale uLocale)
public static DateTimePatternGenerator getInstance(final Locale locale)
'''
pass
def getFrozenInstance():
'''public static DateTimePatternGenerator getFrozenInstance(final ULocale uLocale)
'''
pass
def getDefaultHourFormatChar():
'''public char getDefaultHourFormatChar()
'''
pass
def setDefaultHourFormatChar():
'''public void setDefaultHourFormatChar(final char defaultHourFormatChar)
'''
pass
def getAppendFormatNumber():
'''public static int getAppendFormatNumber(final UResource.Key key)
public static int getAppendFormatNumber(final String string)
'''
pass
def getBestPattern():
'''public String getBestPattern(final String skeleton)
public String getBestPattern(final String skeleton, final int options)
'''
pass
def addPattern():
'''public DateTimePatternGenerator addPattern(final String pattern, final boolean override, final PatternInfo returnInfo)
'''
pass
def addPatternWithSkeleton():
'''public DateTimePatternGenerator addPatternWithSkeleton(final String pattern, final String skeletonToUse, final boolean override, final PatternInfo returnInfo)
'''
pass
def getSkeleton():
'''public String getSkeleton(final String pattern)
'''
pass
def getSkeletonAllowingDuplicates():
'''public String getSkeletonAllowingDuplicates(final String pattern)
'''
pass
def getCanonicalSkeletonAllowingDuplicates():
'''public String getCanonicalSkeletonAllowingDuplicates(final String pattern)
'''
pass
def getBaseSkeleton():
'''public String getBaseSkeleton(final String pattern)
'''
pass
def getSkeletons():
'''public Map<String, String> getSkeletons(Map<String, String> result)
'''
pass
def getBaseSkeletons():
'''public Set<String> getBaseSkeletons(Set<String> result)
'''
pass
def replaceFieldTypes():
'''public String replaceFieldTypes(final String pattern, final String skeleton)
public String replaceFieldTypes(final String pattern, final String skeleton, final int options)
'''
pass
def setDateTimeFormat():
'''public void setDateTimeFormat(final String dateTimeFormat)
'''
pass
def getDateTimeFormat():
'''public String getDateTimeFormat()
'''
pass
def setDecimal():
'''public void setDecimal(final String decimal)
'''
pass
def getDecimal():
'''public String getDecimal()
'''
pass
def getRedundants():
'''public Collection<String> getRedundants(Collection<String> output)
'''
pass
def setAppendItemFormat():
'''public void setAppendItemFormat(final int field, final String value)
'''
pass
def getAppendItemFormat():
'''public String getAppendItemFormat(final int field)
'''
pass
def setAppendItemName():
'''public void setAppendItemName(final int field, final String value)
'''
pass
def getAppendItemName():
'''public String getAppendItemName(final int field)
'''
pass
def getFieldDisplayName():
'''public String getFieldDisplayName(final int field, final DisplayWidth width)
'''
pass
def isSingleField():
'''public static boolean isSingleField(final String skeleton)
'''
pass
def isFrozen():
'''public boolean isFrozen()
'''
pass
def freeze():
'''public DateTimePatternGenerator freeze()
'''
pass
def cloneAsThawed():
'''public DateTimePatternGenerator cloneAsThawed()
'''
pass
def clone():
'''public Object clone()
'''
pass
def skeletonsAreSimilar():
'''public boolean skeletonsAreSimilar(final String id, final String skeleton)
'''
pass
def getFields():
'''public String getFields(final String pattern)
'''
pass
def put():
'''public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
public void put(final UResource.Key key, final UResource.Value value, final boolean isRoot)
public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
'''
pass
def AvailableFormatsSink():
'''public AvailableFormatsSink(final PatternInfo returnInfo)
'''
pass
def VariableField():
'''public VariableField(final String string)
public VariableField(final String string, final boolean strict)
'''
pass
def getType():
'''public int getType()
'''
pass
def getCanonicalCode():
'''public static String getCanonicalCode(final int type)
'''
pass
def isNumeric():
'''public boolean isNumeric()
'''
pass
def toString():
'''public String toString()
public String toString()
public String toString(final int start, final int limit)
public String toString()
public String toString()
public String toString(final boolean skipDayPeriod)
public String toString()
public String toString()
'''
pass
def FormatParser():
'''public FormatParser()
'''
pass
def set():
'''public final FormatParser set(final String string)
public FormatParser set(final String string, final boolean strict)
'''
pass
def getItems():
'''public List<Object> getItems()
'''
pass
def hasDateAndTimeFields():
'''public boolean hasDateAndTimeFields()
'''
pass
def quoteLiteral():
'''public Object quoteLiteral(final String string)
'''
pass
def PatternWithMatcher():
'''public PatternWithMatcher(final String pat, final DateTimeMatcher matcher)
'''
pass
def PatternWithSkeletonFlag():
'''public PatternWithSkeletonFlag(final String pat, final boolean skelSpecified)
'''
pass
def clear():
'''public void clear()
'''
pass
def isFieldEmpty():
'''public boolean isFieldEmpty(final int field)
'''
pass
def toCanonicalString():
'''public String toCanonicalString()
public String toCanonicalString(final boolean skipDayPeriod)
public String toCanonicalString()
'''
pass
def appendTo():
'''public StringBuilder appendTo(final StringBuilder sb)
'''
pass
def appendFieldTo():
'''public StringBuilder appendFieldTo(final int field, final StringBuilder sb)
'''
pass
def compareTo():
'''public int compareTo(final SkeletonFields other)
public int compareTo(final DateTimeMatcher that)
'''
pass
def equals():
'''public boolean equals(final Object other)
public boolean equals(final Object other)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
'''
pass
def fieldIsNumeric():
'''public boolean fieldIsNumeric(final int field)
'''
pass
