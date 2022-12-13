def DateTimeFormatterBuilder():
    '''    public DateTimeFormatterBuilder()
    '''
def toFormatter():
    '''    public DateTimeFormatter toFormatter()
    '''
def toPrinter():
    '''    public DateTimePrinter toPrinter()
    '''
def toParser():
    '''    public DateTimeParser toParser()
    '''
def canBuildFormatter():
    '''    public boolean canBuildFormatter()
    '''
def canBuildPrinter():
    '''    public boolean canBuildPrinter()
    '''
def canBuildParser():
    '''    public boolean canBuildParser()
    '''
def clear():
    '''    public void clear()
    '''
def append():
    '''    public DateTimeFormatterBuilder append(final DateTimeFormatter dateTimeFormatter)
    public DateTimeFormatterBuilder append(final DateTimePrinter dateTimePrinter)
    public DateTimeFormatterBuilder append(final DateTimeParser dateTimeParser)
    public DateTimeFormatterBuilder append(final DateTimePrinter dateTimePrinter, final DateTimeParser dateTimeParser)
    public DateTimeFormatterBuilder append(final DateTimePrinter dateTimePrinter, final DateTimeParser[] array)
    '''
def appendOptional():
    '''    public DateTimeFormatterBuilder appendOptional(final DateTimeParser dateTimeParser)
    '''
def appendLiteral():
    '''    public DateTimeFormatterBuilder appendLiteral(final char c)
    public DateTimeFormatterBuilder appendLiteral(final String s)
    '''
def appendDecimal():
    '''    public DateTimeFormatterBuilder appendDecimal(final DateTimeFieldType dateTimeFieldType, final int n, int n2)
    '''
def appendFixedDecimal():
    '''    public DateTimeFormatterBuilder appendFixedDecimal(final DateTimeFieldType dateTimeFieldType, final int i)
    '''
def appendSignedDecimal():
    '''    public DateTimeFormatterBuilder appendSignedDecimal(final DateTimeFieldType dateTimeFieldType, final int n, int n2)
    '''
def appendFixedSignedDecimal():
    '''    public DateTimeFormatterBuilder appendFixedSignedDecimal(final DateTimeFieldType dateTimeFieldType, final int i)
    '''
def appendText():
    '''    public DateTimeFormatterBuilder appendText(final DateTimeFieldType dateTimeFieldType)
    '''
def appendShortText():
    '''    public DateTimeFormatterBuilder appendShortText(final DateTimeFieldType dateTimeFieldType)
    '''
def appendFraction():
    '''    public DateTimeFormatterBuilder appendFraction(final DateTimeFieldType dateTimeFieldType, final int n, int n2)
    '''
def appendFractionOfSecond():
    '''    public DateTimeFormatterBuilder appendFractionOfSecond(final int n, final int n2)
    '''
def appendFractionOfMinute():
    '''    public DateTimeFormatterBuilder appendFractionOfMinute(final int n, final int n2)
    '''
def appendFractionOfHour():
    '''    public DateTimeFormatterBuilder appendFractionOfHour(final int n, final int n2)
    '''
def appendFractionOfDay():
    '''    public DateTimeFormatterBuilder appendFractionOfDay(final int n, final int n2)
    '''
def appendMillisOfSecond():
    '''    public DateTimeFormatterBuilder appendMillisOfSecond(final int n)
    '''
def appendMillisOfDay():
    '''    public DateTimeFormatterBuilder appendMillisOfDay(final int n)
    '''
def appendSecondOfMinute():
    '''    public DateTimeFormatterBuilder appendSecondOfMinute(final int n)
    '''
def appendSecondOfDay():
    '''    public DateTimeFormatterBuilder appendSecondOfDay(final int n)
    '''
def appendMinuteOfHour():
    '''    public DateTimeFormatterBuilder appendMinuteOfHour(final int n)
    '''
def appendMinuteOfDay():
    '''    public DateTimeFormatterBuilder appendMinuteOfDay(final int n)
    '''
def appendHourOfDay():
    '''    public DateTimeFormatterBuilder appendHourOfDay(final int n)
    '''
def appendClockhourOfDay():
    '''    public DateTimeFormatterBuilder appendClockhourOfDay(final int n)
    '''
def appendHourOfHalfday():
    '''    public DateTimeFormatterBuilder appendHourOfHalfday(final int n)
    '''
def appendClockhourOfHalfday():
    '''    public DateTimeFormatterBuilder appendClockhourOfHalfday(final int n)
    '''
def appendDayOfWeek():
    '''    public DateTimeFormatterBuilder appendDayOfWeek(final int n)
    '''
def appendDayOfMonth():
    '''    public DateTimeFormatterBuilder appendDayOfMonth(final int n)
    '''
def appendDayOfYear():
    '''    public DateTimeFormatterBuilder appendDayOfYear(final int n)
    '''
def appendWeekOfWeekyear():
    '''    public DateTimeFormatterBuilder appendWeekOfWeekyear(final int n)
    '''
def appendWeekyear():
    '''    public DateTimeFormatterBuilder appendWeekyear(final int n, final int n2)
    '''
def appendMonthOfYear():
    '''    public DateTimeFormatterBuilder appendMonthOfYear(final int n)
    '''
def appendYear():
    '''    public DateTimeFormatterBuilder appendYear(final int n, final int n2)
    '''
def appendTwoDigitYear():
    '''    public DateTimeFormatterBuilder appendTwoDigitYear(final int n)
    public DateTimeFormatterBuilder appendTwoDigitYear(final int n, final boolean b)
    '''
def appendTwoDigitWeekyear():
    '''    public DateTimeFormatterBuilder appendTwoDigitWeekyear(final int n)
    public DateTimeFormatterBuilder appendTwoDigitWeekyear(final int n, final boolean b)
    '''
def appendYearOfEra():
    '''    public DateTimeFormatterBuilder appendYearOfEra(final int n, final int n2)
    '''
def appendYearOfCentury():
    '''    public DateTimeFormatterBuilder appendYearOfCentury(final int n, final int n2)
    '''
def appendCenturyOfEra():
    '''    public DateTimeFormatterBuilder appendCenturyOfEra(final int n, final int n2)
    '''
def appendHalfdayOfDayText():
    '''    public DateTimeFormatterBuilder appendHalfdayOfDayText()
    '''
def appendDayOfWeekText():
    '''    public DateTimeFormatterBuilder appendDayOfWeekText()
    '''
def appendDayOfWeekShortText():
    '''    public DateTimeFormatterBuilder appendDayOfWeekShortText()
    '''
def appendMonthOfYearText():
    '''    public DateTimeFormatterBuilder appendMonthOfYearText()
    '''
def appendMonthOfYearShortText():
    '''    public DateTimeFormatterBuilder appendMonthOfYearShortText()
    '''
def appendEraText():
    '''    public DateTimeFormatterBuilder appendEraText()
    '''
def appendTimeZoneName():
    '''    public DateTimeFormatterBuilder appendTimeZoneName()
    public DateTimeFormatterBuilder appendTimeZoneName(final Map<String, DateTimeZone> map)
    '''
def appendTimeZoneShortName():
    '''    public DateTimeFormatterBuilder appendTimeZoneShortName()
    public DateTimeFormatterBuilder appendTimeZoneShortName(final Map<String, DateTimeZone> map)
    '''
def appendTimeZoneId():
    '''    public DateTimeFormatterBuilder appendTimeZoneId()
    '''
def appendTimeZoneOffset():
    '''    public DateTimeFormatterBuilder appendTimeZoneOffset(final String s, final boolean b, final int n, final int n2)
    public DateTimeFormatterBuilder appendTimeZoneOffset(final String s, final String s2, final boolean b, final int n, final int n2)
    '''
def appendPattern():
    '''    public DateTimeFormatterBuilder appendPattern(final String s)
    '''
def estimatePrintedLength():
    '''    public int estimatePrintedLength()
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
def printTo():
    '''    public void printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)
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
def estimateParsedLength():
    '''    public int estimateParsedLength()
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
def parseInto():
    '''    public int parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)
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
