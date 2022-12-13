def PeriodFormatterBuilder():
'''public PeriodFormatterBuilder()
'''
pass
def toFormatter():
'''public PeriodFormatter toFormatter()
'''
pass
def toPrinter():
'''public PeriodPrinter toPrinter()
'''
pass
def toParser():
'''public PeriodParser toParser()
'''
pass
def clear():
'''public void clear()
'''
pass
def append():
'''public PeriodFormatterBuilder append(final PeriodFormatter periodFormatter)
public PeriodFormatterBuilder append(final PeriodPrinter periodPrinter, final PeriodParser periodParser)
'''
pass
def appendLiteral():
'''public PeriodFormatterBuilder appendLiteral(final String s)
'''
pass
def minimumPrintedDigits():
'''public PeriodFormatterBuilder minimumPrintedDigits(final int iMinPrintedDigits)
'''
pass
def maximumParsedDigits():
'''public PeriodFormatterBuilder maximumParsedDigits(final int iMaxParsedDigits)
'''
pass
def rejectSignedValues():
'''public PeriodFormatterBuilder rejectSignedValues(final boolean iRejectSignedValues)
'''
pass
def printZeroRarelyLast():
'''public PeriodFormatterBuilder printZeroRarelyLast()
'''
pass
def printZeroRarelyFirst():
'''public PeriodFormatterBuilder printZeroRarelyFirst()
'''
pass
def printZeroIfSupported():
'''public PeriodFormatterBuilder printZeroIfSupported()
'''
pass
def printZeroAlways():
'''public PeriodFormatterBuilder printZeroAlways()
'''
pass
def printZeroNever():
'''public PeriodFormatterBuilder printZeroNever()
'''
pass
def appendPrefix():
'''public PeriodFormatterBuilder appendPrefix(final String s)
public PeriodFormatterBuilder appendPrefix(final String s, final String s2)
public PeriodFormatterBuilder appendPrefix(final String[] array, final String[] array2)
'''
pass
def appendYears():
'''public PeriodFormatterBuilder appendYears()
'''
pass
def appendMonths():
'''public PeriodFormatterBuilder appendMonths()
'''
pass
def appendWeeks():
'''public PeriodFormatterBuilder appendWeeks()
'''
pass
def appendDays():
'''public PeriodFormatterBuilder appendDays()
'''
pass
def appendHours():
'''public PeriodFormatterBuilder appendHours()
'''
pass
def appendMinutes():
'''public PeriodFormatterBuilder appendMinutes()
'''
pass
def appendSeconds():
'''public PeriodFormatterBuilder appendSeconds()
'''
pass
def appendSecondsWithMillis():
'''public PeriodFormatterBuilder appendSecondsWithMillis()
'''
pass
def appendSecondsWithOptionalMillis():
'''public PeriodFormatterBuilder appendSecondsWithOptionalMillis()
'''
pass
def appendMillis():
'''public PeriodFormatterBuilder appendMillis()
'''
pass
def appendMillis3Digit():
'''public PeriodFormatterBuilder appendMillis3Digit()
'''
pass
def appendSuffix():
'''public PeriodFormatterBuilder appendSuffix(final String s)
public PeriodFormatterBuilder appendSuffix(final String s, final String s2)
public PeriodFormatterBuilder appendSuffix(final String[] array, final String[] array2)
'''
pass
def appendSeparator():
'''public PeriodFormatterBuilder appendSeparator(final String s)
public PeriodFormatterBuilder appendSeparator(final String s, final String s2)
public PeriodFormatterBuilder appendSeparator(final String s, final String s2, final String[] array)
'''
pass
def appendSeparatorIfFieldsAfter():
'''public PeriodFormatterBuilder appendSeparatorIfFieldsAfter(final String s)
'''
pass
def appendSeparatorIfFieldsBefore():
'''public PeriodFormatterBuilder appendSeparatorIfFieldsBefore(final String s)
'''
pass
def finish():
'''public void finish(final Set<PeriodFieldAffix> set)
public void finish(final FieldFormatter[] array)
'''
pass
def calculatePrintedLength():
'''public int calculatePrintedLength(final int n)
public int calculatePrintedLength(final int n)
public int calculatePrintedLength(final int n)
public int calculatePrintedLength(final int n)
public int calculatePrintedLength(final ReadablePeriod readablePeriod, final Locale locale)
public int calculatePrintedLength(final ReadablePeriod readablePeriod, final Locale locale)
public int calculatePrintedLength(final ReadablePeriod readablePeriod, final Locale locale)
public int calculatePrintedLength(final ReadablePeriod readablePeriod, final Locale locale)
'''
pass
def printTo():
'''public void printTo(final StringBuffer sb, final int n)
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
pass
def parse():
'''public int parse(final String s, final int toffset)
public int parse(final String s, final int n)
public int parse(final String s, final int toffset)
public int parse(final String s, final int n)
'''
pass
def scan():
'''public int scan(final String s, final int n)
public int scan(final String s, final int n)
public int scan(final String s, final int n)
public int scan(final String s, final int n)
'''
pass
def getAffixes():
'''public String[] getAffixes()
public String[] getAffixes()
public String[] getAffixes()
public String[] getAffixes()
'''
pass
def compare():
'''public int compare(final String s, final String s2)
'''
pass
def countFieldsToPrint():
'''public int countFieldsToPrint(final ReadablePeriod readablePeriod, final int n, final Locale locale)
public int countFieldsToPrint(final ReadablePeriod readablePeriod, final int n, final Locale locale)
public int countFieldsToPrint(final ReadablePeriod readablePeriod, final int n, final Locale locale)
public int countFieldsToPrint(final ReadablePeriod readablePeriod, final int n, final Locale locale)
'''
pass
def parseInto():
'''public int parseInto(final ReadWritablePeriod readWritablePeriod, final String s, int n, final Locale locale)
public int parseInto(final ReadWritablePeriod readWritablePeriod, final String s, final int toffset, final Locale locale)
public int parseInto(final ReadWritablePeriod readWritablePeriod, final String s, int toffset, final Locale locale)
public int parseInto(final ReadWritablePeriod readWritablePeriod, final String s, int into, final Locale locale)
'''
pass
