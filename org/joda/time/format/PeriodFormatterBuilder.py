def PeriodFormatterBuilder():
    '''    public PeriodFormatterBuilder()
    '''
def toFormatter():
    '''    public PeriodFormatter toFormatter()
    '''
def toPrinter():
    '''    public PeriodPrinter toPrinter()
    '''
def toParser():
    '''    public PeriodParser toParser()
    '''
def clear():
    '''    public void clear()
    '''
def append():
    '''    public PeriodFormatterBuilder append(final PeriodFormatter periodFormatter)
    public PeriodFormatterBuilder append(final PeriodPrinter periodPrinter, final PeriodParser periodParser)
    '''
def appendLiteral():
    '''    public PeriodFormatterBuilder appendLiteral(final String s)
    '''
def minimumPrintedDigits():
    '''    public PeriodFormatterBuilder minimumPrintedDigits(final int iMinPrintedDigits)
    '''
def maximumParsedDigits():
    '''    public PeriodFormatterBuilder maximumParsedDigits(final int iMaxParsedDigits)
    '''
def rejectSignedValues():
    '''    public PeriodFormatterBuilder rejectSignedValues(final boolean iRejectSignedValues)
    '''
def printZeroRarelyLast():
    '''    public PeriodFormatterBuilder printZeroRarelyLast()
    '''
def printZeroRarelyFirst():
    '''    public PeriodFormatterBuilder printZeroRarelyFirst()
    '''
def printZeroIfSupported():
    '''    public PeriodFormatterBuilder printZeroIfSupported()
    '''
def printZeroAlways():
    '''    public PeriodFormatterBuilder printZeroAlways()
    '''
def printZeroNever():
    '''    public PeriodFormatterBuilder printZeroNever()
    '''
def appendPrefix():
    '''    public PeriodFormatterBuilder appendPrefix(final String s)
    public PeriodFormatterBuilder appendPrefix(final String s, final String s2)
    public PeriodFormatterBuilder appendPrefix(final String[] array, final String[] array2)
    '''
def appendYears():
    '''    public PeriodFormatterBuilder appendYears()
    '''
def appendMonths():
    '''    public PeriodFormatterBuilder appendMonths()
    '''
def appendWeeks():
    '''    public PeriodFormatterBuilder appendWeeks()
    '''
def appendDays():
    '''    public PeriodFormatterBuilder appendDays()
    '''
def appendHours():
    '''    public PeriodFormatterBuilder appendHours()
    '''
def appendMinutes():
    '''    public PeriodFormatterBuilder appendMinutes()
    '''
def appendSeconds():
    '''    public PeriodFormatterBuilder appendSeconds()
    '''
def appendSecondsWithMillis():
    '''    public PeriodFormatterBuilder appendSecondsWithMillis()
    '''
def appendSecondsWithOptionalMillis():
    '''    public PeriodFormatterBuilder appendSecondsWithOptionalMillis()
    '''
def appendMillis():
    '''    public PeriodFormatterBuilder appendMillis()
    '''
def appendMillis3Digit():
    '''    public PeriodFormatterBuilder appendMillis3Digit()
    '''
def appendSuffix():
    '''    public PeriodFormatterBuilder appendSuffix(final String s)
    public PeriodFormatterBuilder appendSuffix(final String s, final String s2)
    public PeriodFormatterBuilder appendSuffix(final String[] array, final String[] array2)
    '''
def appendSeparator():
    '''    public PeriodFormatterBuilder appendSeparator(final String s)
    public PeriodFormatterBuilder appendSeparator(final String s, final String s2)
    public PeriodFormatterBuilder appendSeparator(final String s, final String s2, final String[] array)
    '''
def appendSeparatorIfFieldsAfter():
    '''    public PeriodFormatterBuilder appendSeparatorIfFieldsAfter(final String s)
    '''
def appendSeparatorIfFieldsBefore():
    '''    public PeriodFormatterBuilder appendSeparatorIfFieldsBefore(final String s)
    '''
def finish():
    '''    public void finish(final Set<PeriodFieldAffix> set)
    public void finish(final FieldFormatter[] array)
    '''
def calculatePrintedLength():
    '''    public int calculatePrintedLength(final int n)
    public int calculatePrintedLength(final int n)
    public int calculatePrintedLength(final int n)
    public int calculatePrintedLength(final int n)
    public int calculatePrintedLength(final ReadablePeriod readablePeriod, final Locale locale)
    public int calculatePrintedLength(final ReadablePeriod readablePeriod, final Locale locale)
    public int calculatePrintedLength(final ReadablePeriod readablePeriod, final Locale locale)
    public int calculatePrintedLength(final ReadablePeriod readablePeriod, final Locale locale)
    '''
def printTo():
    '''    public void printTo(final StringBuffer sb, final int n)
    public void printTo(final Writer writer, final int n)
    public void printTo(final StringBuffer sb, final int n)
    public void printTo(final Writer writer, final int n)
    public void printTo(final StringBuffer sb, final int n)
    public void printTo(final Writer writer, final int n)
    public void printTo(final StringBuffer sb, final int n)
    public void printTo(final Writer writer, final int n)
    public void printTo(final StringBuffer sb, final ReadablePeriod readablePeriod, final Locale locale)
    public void printTo(final Writer writer, final ReadablePeriod readablePeriod, final Locale locale)
    public void printTo(final StringBuffer sb, final ReadablePeriod readablePeriod, final Locale locale)
    public void printTo(final Writer writer, final ReadablePeriod readablePeriod, final Locale locale)
    public void printTo(final StringBuffer sb, final ReadablePeriod readablePeriod, final Locale locale)
    public void printTo(final Writer writer, final ReadablePeriod readablePeriod, final Locale locale)
    public void printTo(final StringBuffer sb, final ReadablePeriod readablePeriod, final Locale locale)
    public void printTo(final Writer writer, final ReadablePeriod readablePeriod, final Locale locale)
    '''
def parse():
    '''    public int parse(final String s, final int toffset)
    public int parse(final String s, final int n)
    public int parse(final String s, final int toffset)
    public int parse(final String s, final int n)
    '''
def scan():
    '''    public int scan(final String s, final int n)
    public int scan(final String s, final int n)
    public int scan(final String s, final int n)
    public int scan(final String s, final int n)
    '''
def getAffixes():
    '''    public String[] getAffixes()
    public String[] getAffixes()
    public String[] getAffixes()
    public String[] getAffixes()
    '''
def compare():
    '''    public int compare(final String s, final String s2)
    '''
def countFieldsToPrint():
    '''    public int countFieldsToPrint(final ReadablePeriod readablePeriod, final int n, final Locale locale)
    public int countFieldsToPrint(final ReadablePeriod readablePeriod, final int n, final Locale locale)
    public int countFieldsToPrint(final ReadablePeriod readablePeriod, final int n, final Locale locale)
    public int countFieldsToPrint(final ReadablePeriod readablePeriod, final int n, final Locale locale)
    '''
def parseInto():
    '''    public int parseInto(final ReadWritablePeriod readWritablePeriod, final String s, int n, final Locale locale)
    public int parseInto(final ReadWritablePeriod readWritablePeriod, final String s, final int toffset, final Locale locale)
    public int parseInto(final ReadWritablePeriod readWritablePeriod, final String s, int toffset, final Locale locale)
    public int parseInto(final ReadWritablePeriod readWritablePeriod, final String s, int into, final Locale locale)
    '''
