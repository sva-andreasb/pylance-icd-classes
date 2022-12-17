def ():
    '''returns DateTimeFormatterBuilder\n\n
    ()\n
    '''
def toFormatter():
    '''returns DateTimeFormatter\n\n
    toFormatter()\n
    '''
def toPrinter():
    '''returns DateTimePrinter\n\n
    toPrinter()\n
    '''
def toParser():
    '''returns DateTimeParser\n\n
    toParser()\n
    '''
def canBuildFormatter():
    '''returns boolean\n\n
    canBuildFormatter()\n
    '''
def canBuildPrinter():
    '''returns boolean\n\n
    canBuildPrinter()\n
    '''
def canBuildParser():
    '''returns boolean\n\n
    canBuildParser()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def append():
    '''returns DateTimeFormatterBuilder\n\n
    append(final DateTimeFormatter dateTimeFormatter)\n
    append(final DateTimePrinter dateTimePrinter)\n
    append(final DateTimeParser dateTimeParser)\n
    append(final DateTimePrinter dateTimePrinter, final DateTimeParser dateTimeParser)\n
    append(final DateTimePrinter dateTimePrinter, final DateTimeParser[] array)\n
    '''
def appendOptional():
    '''returns DateTimeFormatterBuilder\n\n
    appendOptional(final DateTimeParser dateTimeParser)\n
    '''
def appendLiteral():
    '''returns DateTimeFormatterBuilder\n\n
    appendLiteral(final char c)\n
    appendLiteral(final String s)\n
    '''
def appendDecimal():
    '''returns DateTimeFormatterBuilder\n\n
    appendDecimal(final DateTimeFieldType dateTimeFieldType, final int n, int n2)\n
    '''
def appendFixedDecimal():
    '''returns DateTimeFormatterBuilder\n\n
    appendFixedDecimal(final DateTimeFieldType dateTimeFieldType, final int i)\n
    '''
def appendSignedDecimal():
    '''returns DateTimeFormatterBuilder\n\n
    appendSignedDecimal(final DateTimeFieldType dateTimeFieldType, final int n, int n2)\n
    '''
def appendFixedSignedDecimal():
    '''returns DateTimeFormatterBuilder\n\n
    appendFixedSignedDecimal(final DateTimeFieldType dateTimeFieldType, final int i)\n
    '''
def appendText():
    '''returns DateTimeFormatterBuilder\n\n
    appendText(final DateTimeFieldType dateTimeFieldType)\n
    '''
def appendShortText():
    '''returns DateTimeFormatterBuilder\n\n
    appendShortText(final DateTimeFieldType dateTimeFieldType)\n
    '''
def appendFraction():
    '''returns DateTimeFormatterBuilder\n\n
    appendFraction(final DateTimeFieldType dateTimeFieldType, final int n, int n2)\n
    '''
def appendFractionOfSecond():
    '''returns DateTimeFormatterBuilder\n\n
    appendFractionOfSecond(final int n, final int n2)\n
    '''
def appendFractionOfMinute():
    '''returns DateTimeFormatterBuilder\n\n
    appendFractionOfMinute(final int n, final int n2)\n
    '''
def appendFractionOfHour():
    '''returns DateTimeFormatterBuilder\n\n
    appendFractionOfHour(final int n, final int n2)\n
    '''
def appendFractionOfDay():
    '''returns DateTimeFormatterBuilder\n\n
    appendFractionOfDay(final int n, final int n2)\n
    '''
def appendMillisOfSecond():
    '''returns DateTimeFormatterBuilder\n\n
    appendMillisOfSecond(final int n)\n
    '''
def appendMillisOfDay():
    '''returns DateTimeFormatterBuilder\n\n
    appendMillisOfDay(final int n)\n
    '''
def appendSecondOfMinute():
    '''returns DateTimeFormatterBuilder\n\n
    appendSecondOfMinute(final int n)\n
    '''
def appendSecondOfDay():
    '''returns DateTimeFormatterBuilder\n\n
    appendSecondOfDay(final int n)\n
    '''
def appendMinuteOfHour():
    '''returns DateTimeFormatterBuilder\n\n
    appendMinuteOfHour(final int n)\n
    '''
def appendMinuteOfDay():
    '''returns DateTimeFormatterBuilder\n\n
    appendMinuteOfDay(final int n)\n
    '''
def appendHourOfDay():
    '''returns DateTimeFormatterBuilder\n\n
    appendHourOfDay(final int n)\n
    '''
def appendClockhourOfDay():
    '''returns DateTimeFormatterBuilder\n\n
    appendClockhourOfDay(final int n)\n
    '''
def appendHourOfHalfday():
    '''returns DateTimeFormatterBuilder\n\n
    appendHourOfHalfday(final int n)\n
    '''
def appendClockhourOfHalfday():
    '''returns DateTimeFormatterBuilder\n\n
    appendClockhourOfHalfday(final int n)\n
    '''
def appendDayOfWeek():
    '''returns DateTimeFormatterBuilder\n\n
    appendDayOfWeek(final int n)\n
    '''
def appendDayOfMonth():
    '''returns DateTimeFormatterBuilder\n\n
    appendDayOfMonth(final int n)\n
    '''
def appendDayOfYear():
    '''returns DateTimeFormatterBuilder\n\n
    appendDayOfYear(final int n)\n
    '''
def appendWeekOfWeekyear():
    '''returns DateTimeFormatterBuilder\n\n
    appendWeekOfWeekyear(final int n)\n
    '''
def appendWeekyear():
    '''returns DateTimeFormatterBuilder\n\n
    appendWeekyear(final int n, final int n2)\n
    '''
def appendMonthOfYear():
    '''returns DateTimeFormatterBuilder\n\n
    appendMonthOfYear(final int n)\n
    '''
def appendYear():
    '''returns DateTimeFormatterBuilder\n\n
    appendYear(final int n, final int n2)\n
    '''
def appendTwoDigitYear():
    '''returns DateTimeFormatterBuilder\n\n
    appendTwoDigitYear(final int n)\n
    appendTwoDigitYear(final int n, final boolean b)\n
    '''
def appendTwoDigitWeekyear():
    '''returns DateTimeFormatterBuilder\n\n
    appendTwoDigitWeekyear(final int n)\n
    appendTwoDigitWeekyear(final int n, final boolean b)\n
    '''
def appendYearOfEra():
    '''returns DateTimeFormatterBuilder\n\n
    appendYearOfEra(final int n, final int n2)\n
    '''
def appendYearOfCentury():
    '''returns DateTimeFormatterBuilder\n\n
    appendYearOfCentury(final int n, final int n2)\n
    '''
def appendCenturyOfEra():
    '''returns DateTimeFormatterBuilder\n\n
    appendCenturyOfEra(final int n, final int n2)\n
    '''
def appendHalfdayOfDayText():
    '''returns DateTimeFormatterBuilder\n\n
    appendHalfdayOfDayText()\n
    '''
def appendDayOfWeekText():
    '''returns DateTimeFormatterBuilder\n\n
    appendDayOfWeekText()\n
    '''
def appendDayOfWeekShortText():
    '''returns DateTimeFormatterBuilder\n\n
    appendDayOfWeekShortText()\n
    '''
def appendMonthOfYearText():
    '''returns DateTimeFormatterBuilder\n\n
    appendMonthOfYearText()\n
    '''
def appendMonthOfYearShortText():
    '''returns DateTimeFormatterBuilder\n\n
    appendMonthOfYearShortText()\n
    '''
def appendEraText():
    '''returns DateTimeFormatterBuilder\n\n
    appendEraText()\n
    '''
def appendTimeZoneName():
    '''returns DateTimeFormatterBuilder\n\n
    appendTimeZoneName()\n
    appendTimeZoneName(final Map<String, DateTimeZone> map)\n
    '''
def appendTimeZoneShortName():
    '''returns DateTimeFormatterBuilder\n\n
    appendTimeZoneShortName()\n
    appendTimeZoneShortName(final Map<String, DateTimeZone> map)\n
    '''
def appendTimeZoneId():
    '''returns DateTimeFormatterBuilder\n\n
    appendTimeZoneId()\n
    '''
def appendTimeZoneOffset():
    '''returns DateTimeFormatterBuilder\n\n
    appendTimeZoneOffset(final String s, final boolean b, final int n, final int n2)\n
    appendTimeZoneOffset(final String s, final String s2, final boolean b, final int n, final int n2)\n
    '''
def appendPattern():
    '''returns DateTimeFormatterBuilder\n\n
    appendPattern(final String s)\n
    '''
def estimatePrintedLength():
    '''returns int\n\n
    estimatePrintedLength()\n
    estimatePrintedLength()\n
    estimatePrintedLength()\n
    estimatePrintedLength()\n
    estimatePrintedLength()\n
    estimatePrintedLength()\n
    estimatePrintedLength()\n
    estimatePrintedLength()\n
    estimatePrintedLength()\n
    estimatePrintedLength()\n
    estimatePrintedLength()\n
    '''
def printTo():
    '''returns None\n\n
    printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)\n
    printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)\n
    printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)\n
    printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)\n
    printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)\n
    printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)\n
    printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)\n
    printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)\n
    printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)\n
    printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)\n
    printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)\n
    printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)\n
    printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)\n
    printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)\n
    printTo(final Appendable appendable, final long n, final Chronology chronology, int n2, final DateTimeZone dateTimeZone, final Locale locale)\n
    printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)\n
    printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)\n
    printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)\n
    printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, final Locale locale)\n
    printTo(final Appendable appendable, final ReadablePartial readablePartial, final Locale locale)\n
    printTo(final Appendable appendable, final long n, final Chronology chronology, final int n2, final DateTimeZone dateTimeZone, Locale default1)\n
    printTo(final Appendable appendable, final ReadablePartial readablePartial, Locale default1)\n
    '''
def estimateParsedLength():
    '''returns int\n\n
    estimateParsedLength()\n
    estimateParsedLength()\n
    estimateParsedLength()\n
    estimateParsedLength()\n
    estimateParsedLength()\n
    estimateParsedLength()\n
    estimateParsedLength()\n
    estimateParsedLength()\n
    estimateParsedLength()\n
    estimateParsedLength()\n
    estimateParsedLength()\n
    '''
def parseInto():
    '''returns int\n\n
    parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)\n
    parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)\n
    parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, int n)\n
    parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)\n
    parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, int n)\n
    parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)\n
    parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)\n
    parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, int n)\n
    parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)\n
    parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)\n
    parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, int into)\n
    parseInto(final DateTimeParserBucket dateTimeParserBucket, final CharSequence charSequence, final int n)\n
    '''
