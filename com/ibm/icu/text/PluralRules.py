KEYWORD_ZERO = "String zero""
KEYWORD_ONE = "String one""
KEYWORD_TWO = "String two""
KEYWORD_FEW = "String few""
KEYWORD_MANY = "String many""
KEYWORD_OTHER = "String other""
NO_UNIQUE_VALUE = "double -0.00123456777"
def parseDescription():
'''public static PluralRules parseDescription(String description)
'''
pass
def createRules():
'''public static PluralRules createRules(final String description)
'''
pass
def forLocale():
'''public static PluralRules forLocale(final ULocale locale)
public static PluralRules forLocale(final Locale locale)
public static PluralRules forLocale(final ULocale locale, final PluralType type)
public static PluralRules forLocale(final Locale locale, final PluralType type)
public final PluralRules forLocale(final ULocale locale)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
public int hashCode()
'''
pass
def select():
'''public String select(final double number)
public String select(final FormattedNumber number)
public String select(final double number, final int countVisibleFractionDigits, final long fractionaldigits)
public String select(final IFixedDecimal number)
public String select(final IFixedDecimal n)
public boolean select(final IFixedDecimal sample, final String keyword)
'''
pass
def matches():
'''public boolean matches(final FixedDecimal sample, final String keyword)
'''
pass
def getKeywords():
'''public Set<String> getKeywords()
public Set<String> getKeywords()
'''
pass
def getUniqueKeywordValue():
'''public double getUniqueKeywordValue(final String keyword)
'''
pass
def getAllKeywordValues():
'''public Collection<Double> getAllKeywordValues(final String keyword)
public Collection<Double> getAllKeywordValues(final String keyword, final SampleType type)
'''
pass
def getSamples():
'''public Collection<Double> getSamples(final String keyword)
public Collection<Double> getSamples(final String keyword, final SampleType sampleType)
public Set<FixedDecimalRange> getSamples()
'''
pass
def getDecimalSamples():
'''public FixedDecimalSamples getDecimalSamples(final String keyword, final SampleType sampleType)
public FixedDecimalSamples getDecimalSamples(final String keyword, final SampleType sampleType)
'''
pass
def getAvailableULocales():
'''public static ULocale[] getAvailableULocales()
'''
pass
def getFunctionalEquivalent():
'''public static ULocale getFunctionalEquivalent(final ULocale locale, final boolean[] isAvailable)
'''
pass
def toString():
'''public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
'''
pass
def equals():
'''public boolean equals(final Object rhs)
public boolean equals(final PluralRules rhs)
public boolean equals(final Object arg0)
'''
pass
def getKeywordStatus():
'''public KeywordStatus getKeywordStatus(final String keyword, final int offset, final Set<Double> explicits, final Output<Double> uniqueValue)
public KeywordStatus getKeywordStatus(final String keyword, final int offset, Set<Double> explicits, final Output<Double> uniqueValue, final SampleType sampleType)
'''
pass
def getRules():
'''public String getRules(final String keyword)
public String getRules(final String keyword)
'''
pass
def compareTo():
'''public int compareTo(final PluralRules other)
public int compareTo(final FixedDecimal other)
'''
pass
def isLimited():
'''public boolean isLimited(final String keyword, final SampleType sampleType)
public boolean isLimited(final SampleType sampleType)
public boolean isLimited(final SampleType sampleType)
public boolean isLimited(final SampleType sampleType)
public boolean isLimited(final SampleType sampleType)
public boolean isLimited(final SampleType sampleType)
public boolean isLimited(final String keyword, final SampleType sampleType)
'''
pass
def computeLimited():
'''public boolean computeLimited(final String keyword, final SampleType sampleType)
public boolean computeLimited(final String keyword, final SampleType sampleType)
'''
pass
def isFulfilled():
'''public boolean isFulfilled(final IFixedDecimal n)
public boolean isFulfilled(final IFixedDecimal number)
public boolean isFulfilled(final IFixedDecimal n)
public boolean isFulfilled(final IFixedDecimal n)
'''
pass
def getDefaultFactory():
'''public static PluralRulesLoader getDefaultFactory()
'''
pass
def getSource():
'''public double getSource()
'''
pass
def getVisibleDecimalDigitCount():
'''public int getVisibleDecimalDigitCount()
'''
pass
def getVisibleDecimalDigitCountWithoutTrailingZeros():
'''public int getVisibleDecimalDigitCountWithoutTrailingZeros()
'''
pass
def getDecimalDigits():
'''public long getDecimalDigits()
'''
pass
def getDecimalDigitsWithoutTrailingZeros():
'''public long getDecimalDigitsWithoutTrailingZeros()
'''
pass
def getIntegerValue():
'''public long getIntegerValue()
'''
pass
def isHasIntegerValue():
'''public boolean isHasIntegerValue()
'''
pass
def isNegative():
'''public boolean isNegative()
'''
pass
def getBaseFactor():
'''public int getBaseFactor()
'''
pass
def FixedDecimal():
'''public FixedDecimal(final double n, final int v, final long f)
public FixedDecimal(final double n, final int v)
public FixedDecimal(final double n)
public FixedDecimal(final long n)
public FixedDecimal(final String n)
'''
pass
def decimals():
'''public static int decimals(double n)
'''
pass
def getPluralOperand():
'''public double getPluralOperand(final Operand operand)
'''
pass
def getOperand():
'''public static Operand getOperand(final String t)
'''
pass
def hasIntegerValue():
'''public boolean hasIntegerValue()
'''
pass
def intValue():
'''public int intValue()
'''
pass
def longValue():
'''public long longValue()
'''
pass
def floatValue():
'''public float floatValue()
'''
pass
def doubleValue():
'''public double doubleValue()
'''
pass
def getShiftedValue():
'''public long getShiftedValue()
'''
pass
def isNaN():
'''public boolean isNaN()
'''
pass
def isInfinite():
'''public boolean isInfinite()
'''
pass
def FixedDecimalRange():
'''public FixedDecimalRange(final FixedDecimal start, final FixedDecimal end)
'''
pass
def addSamples():
'''public Set<Double> addSamples(final Set<Double> result)
'''
pass
def getStartEndSamples():
'''public void getStartEndSamples(final Set<FixedDecimal> target)
'''
pass
def Rule():
'''public Rule(final String keyword, final Constraint constraint, final FixedDecimalSamples integerSamples, final FixedDecimalSamples decimalSamples)
'''
pass
def and():
'''public Rule and(final Constraint c)
'''
pass
def or():
'''public Rule or(final Constraint c)
'''
pass
def getKeyword():
'''public String getKeyword()
'''
pass
def appliesTo():
'''public boolean appliesTo(final IFixedDecimal n)
'''
pass
def getConstraint():
'''public String getConstraint()
'''
pass
def addRule():
'''public RuleList addRule(final Rule nextRule)
'''
pass
def finish():
'''public RuleList finish()
'''
pass
