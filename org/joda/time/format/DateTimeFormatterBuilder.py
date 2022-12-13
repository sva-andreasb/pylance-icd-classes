def DateTimeFormatterBuilder():
'''public DateTimeFormatterBuilder()
'''
pass
def toFormatter():
'''public DateTimeFormatter toFormatter()
'''
pass
def toPrinter():
'''public DateTimePrinter toPrinter()
'''
pass
def toParser():
'''public DateTimeParser toParser()
'''
pass
def canBuildFormatter():
'''public boolean canBuildFormatter()
'''
pass
def canBuildPrinter():
'''public boolean canBuildPrinter()
'''
pass
def canBuildParser():
'''public boolean canBuildParser()
'''
pass
def clear():
'''public void clear()
'''
pass
def append():
'''public DateTimeFormatterBuilder append(final DateTimeFormatter dateTimeFormatter)
public DateTimeFormatterBuilder append(final DateTimePrinter dateTimePrinter)
public DateTimeFormatterBuilder append(final DateTimeParser dateTimeParser)
public DateTimeFormatterBuilder append(final DateTimePrinter dateTimePrinter, final DateTimeParser dateTimeParser)
public DateTimeFormatterBuilder append(final DateTimePrinter dateTimePrinter, final DateTimeParser[] array)
'''
pass
def appendOptional():
'''public DateTimeFormatterBuilder appendOptional(final DateTimeParser dateTimeParser)
'''
pass
def appendLiteral():
'''public DateTimeFormatterBuilder appendLiteral(final char c)
public DateTimeFormatterBuilder appendLiteral(final String s)
'''
pass
def appendDecimal():
'''public DateTimeFormatterBuilder appendDecimal(final DateTimeFieldType dateTimeFieldType, final int n, int n2)
'''
pass
def appendFixedDecimal():
'''public DateTimeFormatterBuilder appendFixedDecimal(final DateTimeFieldType dateTimeFieldType, final int i)
'''
pass
def appendSignedDecimal():
'''public DateTimeFormatterBuilder appendSignedDecimal(final DateTimeFieldType dateTimeFieldType, final int n, int n2)
'''
pass
def appendFixedSignedDecimal():
'''public DateTimeFormatterBuilder appendFixedSignedDecimal(final DateTimeFieldType dateTimeFieldType, final int i)
'''
pass
def appendText():
'''public DateTimeFormatterBuilder appendText(final DateTimeFieldType dateTimeFieldType)
'''
pass
def appendShortText():
'''public DateTimeFormatterBuilder appendShortText(final DateTimeFieldType dateTimeFieldType)
'''
pass
def appendFraction():
'''public DateTimeFormatterBuilder appendFraction(final DateTimeFieldType dateTimeFieldType, final int n, int n2)
'''
pass
def appendFractionOfSecond():
'''public DateTimeFormatterBuilder appendFractionOfSecond(final int n, final int n2)
'''
pass
def appendFractionOfMinute():
'''public DateTimeFormatterBuilder appendFractionOfMinute(final int n, final int n2)
'''
pass
def appendFractionOfHour():
'''public DateTimeFormatterBuilder appendFractionOfHour(final int n, final int n2)
'''
pass
def appendFractionOfDay():
'''public DateTimeFormatterBuilder appendFractionOfDay(final int n, final int n2)
'''
pass
def appendMillisOfSecond():
'''public DateTimeFormatterBuilder appendMillisOfSecond(final int n)
'''
pass
def appendMillisOfDay():
'''public DateTimeFormatterBuilder appendMillisOfDay(final int n)
'''
pass
def appendSecondOfMinute():
'''public DateTimeFormatterBuilder appendSecondOfMinute(final int n)
'''
pass
def appendSecondOfDay():
'''public DateTimeFormatterBuilder appendSecondOfDay(final int n)
'''
pass
def appendMinuteOfHour():
'''public DateTimeFormatterBuilder appendMinuteOfHour(final int n)
'''
pass
def appendMinuteOfDay():
'''public DateTimeFormatterBuilder appendMinuteOfDay(final int n)
'''
pass
def appendHourOfDay():
'''public DateTimeFormatterBuilder appendHourOfDay(final int n)
'''
pass
def appendClockhourOfDay():
'''public DateTimeFormatterBuilder appendClockhourOfDay(final int n)
'''
pass
def appendHourOfHalfday():
'''public DateTimeFormatterBuilder appendHourOfHalfday(final int n)
'''
pass
def appendClockhourOfHalfday():
'''public DateTimeFormatterBuilder appendClockhourOfHalfday(final int n)
'''
pass
def appendDayOfWeek():
'''public DateTimeFormatterBuilder appendDayOfWeek(final int n)
'''
pass
def appendDayOfMonth():
'''public DateTimeFormatterBuilder appendDayOfMonth(final int n)
'''
pass
def appendDayOfYear():
'''public DateTimeFormatterBuilder appendDayOfYear(final int n)
'''
pass
def appendWeekOfWeekyear():
'''public DateTimeFormatterBuilder appendWeekOfWeekyear(final int n)
'''
pass
def appendWeekyear():
'''public DateTimeFormatterBuilder appendWeekyear(final int n, final int n2)
'''
pass
def appendMonthOfYear():
'''public DateTimeFormatterBuilder appendMonthOfYear(final int n)
'''
pass
def appendYear():
'''public DateTimeFormatterBuilder appendYear(final int n, final int n2)
'''
pass
def appendTwoDigitYear():
'''public DateTimeFormatterBuilder appendTwoDigitYear(final int n)
public DateTimeFormatterBuilder appendTwoDigitYear(final int n, final boolean b)
'''
pass
def appendTwoDigitWeekyear():
'''public DateTimeFormatterBuilder appendTwoDigitWeekyear(final int n)
public DateTimeFormatterBuilder appendTwoDigitWeekyear(final int n, final boolean b)
'''
pass
def appendYearOfEra():
'''public DateTimeFormatterBuilder appendYearOfEra(final int n, final int n2)
'''
pass
def appendYearOfCentury():
'''public DateTimeFormatterBuilder appendYearOfCentury(final int n, final int n2)
'''
pass
def appendCenturyOfEra():
'''public DateTimeFormatterBuilder appendCenturyOfEra(final int n, final int n2)
'''
pass
def appendHalfdayOfDayText():
'''public DateTimeFormatterBuilder appendHalfdayOfDayText()
'''
pass
def appendDayOfWeekText():
'''public DateTimeFormatterBuilder appendDayOfWeekText()
'''
pass
def appendDayOfWeekShortText():
'''public DateTimeFormatterBuilder appendDayOfWeekShortText()
'''
pass
def appendMonthOfYearText():
'''public DateTimeFormatterBuilder appendMonthOfYearText()
'''
pass
def appendMonthOfYearShortText():
'''public DateTimeFormatterBuilder appendMonthOfYearShortText()
'''
pass
def appendEraText():
'''public DateTimeFormatterBuilder appendEraText()
'''
pass
def appendTimeZoneName():
'''public DateTimeFormatterBuilder appendTimeZoneName()
public DateTimeFormatterBuilder appendTimeZoneName(final Map<String, DateTimeZone> map)
'''
pass
def appendTimeZoneShortName():
'''public DateTimeFormatterBuilder appendTimeZoneShortName()
public DateTimeFormatterBuilder appendTimeZoneShortName(final Map<String, DateTimeZone> map)
'''
pass
def appendTimeZoneId():
'''public DateTimeFormatterBuilder appendTimeZoneId()
'''
pass
def appendTimeZoneOffset():
'''public DateTimeFormatterBuilder appendTimeZoneOffset(final String s, final boolean b, final int n, final int n2)
public DateTimeFormatterBuilder appendTimeZoneOffset(final String s, final String s2, final boolean b, final int n, final int n2)
'''
pass
def appendPattern():
'''public DateTimeFormatterBuilder appendPattern(final String s)
'''
pass
def estimatePrintedLength():
'''public int estimatePrintedLength()
public int estimatePrintedLength()
public int estimatePrintedLength()
public int estimatePrintedLength()
public int estimatePrintedLength()
public int estimatePrintedLength()
public int estimatePrintedLength()
public int estimatePrintedLength()
public int estimatePrintedLength()
public int estimatePrintedLength()
public int estimatePrintedLength()
'''
pass
def printTo():
'''public void printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)
public void printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)
public void printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)
public void printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)
public void printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)
public void printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)
public void printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)
public void printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)
public void printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)
public void printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)
public void printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)
public void printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)
public void printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)
public void printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)
public void printTo(final Appendable appendable, final long n, final Chronology chronology, int n2, final DateTimeZone dateTimeZone, final Locale locale)
public void printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)
public void printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)
public void printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)
public void printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)
public void printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)
public void printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, Locale default1)
public void printTo(final Appendable appendable, final ReadablePartial readablePartial, Locale default1)
'''
pass
def estimateParsedLength():
'''public int estimateParsedLength()
public int estimateParsedLength()
public int estimateParsedLength()
public int estimateParsedLength()
public int estimateParsedLength()
public int estimateParsedLength()
public int estimateParsedLength()
public int estimateParsedLength()
public int estimateParsedLength()
public int estimateParsedLength()
public int estimateParsedLength()
'''
pass
def parseInto():
'''public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)
public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)
public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, int n)
public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)
public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, int n)
public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)
public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)
public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, int n)
public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)
public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)
public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, int into)
public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)
'''
pass
