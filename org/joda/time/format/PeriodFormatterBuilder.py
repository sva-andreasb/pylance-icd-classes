def ():
    '''returns PeriodFormatterBuilder\n\n
    ()\n
    '''
def toFormatter():
    '''returns PeriodFormatter\n\n
    toFormatter()\n
    '''
def toPrinter():
    '''returns PeriodPrinter\n\n
    toPrinter()\n
    '''
def toParser():
    '''returns PeriodParser\n\n
    toParser()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def append():
    '''returns PeriodFormatterBuilder\n\n
    append(final PeriodFormatter periodFormatter)\n
    append(final PeriodPrinter periodPrinter, final PeriodParser periodParser)\n
    '''
def appendLiteral():
    '''returns PeriodFormatterBuilder\n\n
    appendLiteral(final String s)\n
    '''
def minimumPrintedDigits():
    '''returns PeriodFormatterBuilder\n\n
    minimumPrintedDigits(final int iMinPrintedDigits)\n
    '''
def maximumParsedDigits():
    '''returns PeriodFormatterBuilder\n\n
    maximumParsedDigits(final int iMaxParsedDigits)\n
    '''
def rejectSignedValues():
    '''returns PeriodFormatterBuilder\n\n
    rejectSignedValues(final boolean iRejectSignedValues)\n
    '''
def printZeroRarelyLast():
    '''returns PeriodFormatterBuilder\n\n
    printZeroRarelyLast()\n
    '''
def printZeroRarelyFirst():
    '''returns PeriodFormatterBuilder\n\n
    printZeroRarelyFirst()\n
    '''
def printZeroIfSupported():
    '''returns PeriodFormatterBuilder\n\n
    printZeroIfSupported()\n
    '''
def printZeroAlways():
    '''returns PeriodFormatterBuilder\n\n
    printZeroAlways()\n
    '''
def printZeroNever():
    '''returns PeriodFormatterBuilder\n\n
    printZeroNever()\n
    '''
def appendPrefix():
    '''returns PeriodFormatterBuilder\n\n
    appendPrefix(final String s)\n
    appendPrefix(final String s, final String s2)\n
    appendPrefix(final String[] array, final String[] array2)\n
    '''
def appendYears():
    '''returns PeriodFormatterBuilder\n\n
    appendYears()\n
    '''
def appendMonths():
    '''returns PeriodFormatterBuilder\n\n
    appendMonths()\n
    '''
def appendWeeks():
    '''returns PeriodFormatterBuilder\n\n
    appendWeeks()\n
    '''
def appendDays():
    '''returns PeriodFormatterBuilder\n\n
    appendDays()\n
    '''
def appendHours():
    '''returns PeriodFormatterBuilder\n\n
    appendHours()\n
    '''
def appendMinutes():
    '''returns PeriodFormatterBuilder\n\n
    appendMinutes()\n
    '''
def appendSeconds():
    '''returns PeriodFormatterBuilder\n\n
    appendSeconds()\n
    '''
def appendSecondsWithMillis():
    '''returns PeriodFormatterBuilder\n\n
    appendSecondsWithMillis()\n
    '''
def appendSecondsWithOptionalMillis():
    '''returns PeriodFormatterBuilder\n\n
    appendSecondsWithOptionalMillis()\n
    '''
def appendMillis():
    '''returns PeriodFormatterBuilder\n\n
    appendMillis()\n
    '''
def appendMillis3Digit():
    '''returns PeriodFormatterBuilder\n\n
    appendMillis3Digit()\n
    '''
def appendSuffix():
    '''returns PeriodFormatterBuilder\n\n
    appendSuffix(final String s)\n
    appendSuffix(final String s, final String s2)\n
    appendSuffix(final String[] array, final String[] array2)\n
    '''
def appendSeparator():
    '''returns PeriodFormatterBuilder\n\n
    appendSeparator(final String s)\n
    appendSeparator(final String s, final String s2)\n
    appendSeparator(final String s, final String s2, final String[] array)\n
    '''
def appendSeparatorIfFieldsAfter():
    '''returns PeriodFormatterBuilder\n\n
    appendSeparatorIfFieldsAfter(final String s)\n
    '''
def appendSeparatorIfFieldsBefore():
    '''returns PeriodFormatterBuilder\n\n
    appendSeparatorIfFieldsBefore(final String s)\n
    '''
def finish():
    '''returns None\n\n
    finish(final Set<PeriodFieldAffix> set)\n
    finish(final FieldFormatter[] array)\n
    '''
def calculatePrintedLength():
    '''returns int\n\n
    calculatePrintedLength(final int n)\n
    calculatePrintedLength(final int n)\n
    calculatePrintedLength(final int n)\n
    calculatePrintedLength(final int n)\n
    calculatePrintedLength(final ReadablePeriod readablePeriod, final Locale locale)\n
    calculatePrintedLength(final ReadablePeriod readablePeriod, final Locale locale)\n
    calculatePrintedLength(final ReadablePeriod readablePeriod, final Locale locale)\n
    calculatePrintedLength(final ReadablePeriod readablePeriod, final Locale locale)\n
    '''
def printTo():
    '''returns None\n\n
    printTo(final StringBuffer sb, final int n)\n
    printTo(final Writer writer, final int n)\n
    printTo(final StringBuffer sb, final int n)\n
    printTo(final Writer writer, final int n)\n
    printTo(final StringBuffer sb, final int n)\n
    printTo(final Writer writer, final int n)\n
    printTo(final StringBuffer sb, final int n)\n
    printTo(final Writer writer, final int n)\n
    printTo(final StringBuffer sb, final ReadablePeriod readablePeriod, final Locale locale)\n
    printTo(final Writer writer, final ReadablePeriod readablePeriod, final Locale locale)\n
    printTo(final StringBuffer sb, final ReadablePeriod readablePeriod, final Locale locale)\n
    printTo(final Writer writer, final ReadablePeriod readablePeriod, final Locale locale)\n
    printTo(final StringBuffer sb, final ReadablePeriod readablePeriod, final Locale locale)\n
    printTo(final Writer writer, final ReadablePeriod readablePeriod, final Locale locale)\n
    printTo(final StringBuffer sb, final ReadablePeriod readablePeriod, final Locale locale)\n
    printTo(final Writer writer, final ReadablePeriod readablePeriod, final Locale locale)\n
    '''
def parse():
    '''returns int\n\n
    parse(final String s, final int toffset)\n
    parse(final String s, final int n)\n
    parse(final String s, final int toffset)\n
    parse(final String s, final int n)\n
    '''
def scan():
    '''returns int\n\n
    scan(final String s, final int n)\n
    scan(final String s, final int n)\n
    scan(final String s, final int n)\n
    scan(final String s, final int n)\n
    '''
def getAffixes():
    '''returns String[]\n\n
    getAffixes()\n
    getAffixes()\n
    getAffixes()\n
    getAffixes()\n
    '''
def compare():
    '''returns int\n\n
    compare(final String s, final String s2)\n
    '''
def countFieldsToPrint():
    '''returns int\n\n
    countFieldsToPrint(final ReadablePeriod readablePeriod, final int n, final Locale locale)\n
    countFieldsToPrint(final ReadablePeriod readablePeriod, final int n, final Locale locale)\n
    countFieldsToPrint(final ReadablePeriod readablePeriod, final int n, final Locale locale)\n
    countFieldsToPrint(final ReadablePeriod readablePeriod, final int n, final Locale locale)\n
    '''
def parseInto():
    '''returns int\n\n
    parseInto(final ReadWritablePeriod readWritablePeriod, final String s, int n, final Locale locale)\n
    parseInto(final ReadWritablePeriod readWritablePeriod, final String s, final int toffset, final Locale locale)\n
    parseInto(final ReadWritablePeriod readWritablePeriod, final String s, int toffset, final Locale locale)\n
    parseInto(final ReadWritablePeriod readWritablePeriod, final String s, int into, final Locale locale)\n
    '''
