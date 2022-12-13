KEYWORD_ZERO = "String  \"zero\""
KEYWORD_ONE = "String  \"one\""
KEYWORD_TWO = "String  \"two\""
KEYWORD_FEW = "String  \"few\""
KEYWORD_MANY = "String  \"many\""
KEYWORD_OTHER = "String  \"other\""
NO_UNIQUE_VALUE = "double  -0.00123456777"
def parseDescription():
    '''    public static PluralRules parseDescription(String description)
    '''
def createRules():
    '''    public static PluralRules createRules(final String description)
    '''
def forLocale():
    '''    public static PluralRules forLocale(final ULocale locale)
    public static PluralRules forLocale(final Locale locale)
    public static PluralRules forLocale(final ULocale locale, final PluralType type)
    public static PluralRules forLocale(final Locale locale, final PluralType type)
    public final PluralRules forLocale(final ULocale locale)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    public int hashCode()
    '''
def select():
    '''    public String select(final double number)
    public String select(final FormattedNumber number)
    public String select(final double number, final int countVisibleFractionDigits, final long fractionaldigits)
    public String select(final IFixedDecimal number)
    public String select(final IFixedDecimal n)
    public boolean select(final IFixedDecimal sample, final String keyword)
    '''
def matches():
    '''    public boolean matches(final FixedDecimal sample, final String keyword)
    '''
def getKeywords():
    '''    public Set<String> getKeywords()
    public Set<String> getKeywords()
    '''
def getUniqueKeywordValue():
    '''    public double getUniqueKeywordValue(final String keyword)
    '''
def getAllKeywordValues():
    '''    public Collection<Double> getAllKeywordValues(final String keyword)
    public Collection<Double> getAllKeywordValues(final String keyword, final SampleType type)
    '''
def getSamples():
    '''    public Collection<Double> getSamples(final String keyword)
    public Collection<Double> getSamples(final String keyword, final SampleType sampleType)
    public Set<FixedDecimalRange> getSamples()
    '''
def getDecimalSamples():
    '''    public FixedDecimalSamples getDecimalSamples(final String keyword, final SampleType sampleType)
    public FixedDecimalSamples getDecimalSamples(final String keyword, final SampleType sampleType)
    '''
def getAvailableULocales():
    '''    public static ULocale[] getAvailableULocales()
    '''
def getFunctionalEquivalent():
    '''    public static ULocale getFunctionalEquivalent(final ULocale locale, final boolean[] isAvailable)
    '''
def toString():
    '''    public String toString()
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
def equals():
    '''    public boolean equals(final Object rhs)
    public boolean equals(final PluralRules rhs)
    public boolean equals(final Object arg0)
    '''
def getKeywordStatus():
    '''    public KeywordStatus getKeywordStatus(final String keyword, final int offset, final Set<Double> explicits, final Output<Double> uniqueValue)
    public KeywordStatus getKeywordStatus(final String keyword, final int offset, Set<Double> explicits, final Output<Double> uniqueValue, final SampleType sampleType)
    '''
def getRules():
    '''    public String getRules(final String keyword)
    public String getRules(final String keyword)
    '''
def compareTo():
    '''    public int compareTo(final PluralRules other)
    public int compareTo(final FixedDecimal other)
    '''
def isLimited():
    '''    public boolean isLimited(final String keyword, final SampleType sampleType)
    public boolean isLimited(final SampleType sampleType)
    public boolean isLimited(final SampleType sampleType)
    public boolean isLimited(final SampleType sampleType)
    public boolean isLimited(final SampleType sampleType)
    public boolean isLimited(final SampleType sampleType)
    public boolean isLimited(final String keyword, final SampleType sampleType)
    '''
def computeLimited():
    '''    public boolean computeLimited(final String keyword, final SampleType sampleType)
    public boolean computeLimited(final String keyword, final SampleType sampleType)
    '''
def isFulfilled():
    '''    public boolean isFulfilled(final IFixedDecimal n)
    public boolean isFulfilled(final IFixedDecimal number)
    public boolean isFulfilled(final IFixedDecimal n)
    public boolean isFulfilled(final IFixedDecimal n)
    '''
def getDefaultFactory():
    '''    public static PluralRulesLoader getDefaultFactory()
    '''
def getSource():
    '''    public double getSource()
    '''
def getVisibleDecimalDigitCount():
    '''    public int getVisibleDecimalDigitCount()
    '''
def getVisibleDecimalDigitCountWithoutTrailingZeros():
    '''    public int getVisibleDecimalDigitCountWithoutTrailingZeros()
    '''
def getDecimalDigits():
    '''    public long getDecimalDigits()
    '''
def getDecimalDigitsWithoutTrailingZeros():
    '''    public long getDecimalDigitsWithoutTrailingZeros()
    '''
def getIntegerValue():
    '''    public long getIntegerValue()
    '''
def isHasIntegerValue():
    '''    public boolean isHasIntegerValue()
    '''
def isNegative():
    '''    public boolean isNegative()
    '''
def getBaseFactor():
    '''    public int getBaseFactor()
    '''
def FixedDecimal():
    '''    public FixedDecimal(final double n, final int v, final long f)
    public FixedDecimal(final double n, final int v)
    public FixedDecimal(final double n)
    public FixedDecimal(final long n)
    public FixedDecimal(final String n)
    '''
def decimals():
    '''    public static int decimals(double n)
    '''
def getPluralOperand():
    '''    public double getPluralOperand(final Operand operand)
    '''
def getOperand():
    '''    public static Operand getOperand(final String t)
    '''
def hasIntegerValue():
    '''    public boolean hasIntegerValue()
    '''
def intValue():
    '''    public int intValue()
    '''
def longValue():
    '''    public long longValue()
    '''
def floatValue():
    '''    public float floatValue()
    '''
def doubleValue():
    '''    public double doubleValue()
    '''
def getShiftedValue():
    '''    public long getShiftedValue()
    '''
def isNaN():
    '''    public boolean isNaN()
    '''
def isInfinite():
    '''    public boolean isInfinite()
    '''
def FixedDecimalRange():
    '''    public FixedDecimalRange(final FixedDecimal start, final FixedDecimal end)
    '''
def addSamples():
    '''    public Set<Double> addSamples(final Set<Double> result)
    '''
def getStartEndSamples():
    '''    public void getStartEndSamples(final Set<FixedDecimal> target)
    '''
def Rule():
    '''    public Rule(final String keyword, final Constraint constraint, final FixedDecimalSamples integerSamples, final FixedDecimalSamples decimalSamples)
    '''
def and():
    '''    public Rule and(final Constraint c)
    '''
def or():
    '''    public Rule or(final Constraint c)
    '''
def getKeyword():
    '''    public String getKeyword()
    '''
def appliesTo():
    '''    public boolean appliesTo(final IFixedDecimal n)
    '''
def getConstraint():
    '''    public String getConstraint()
    '''
def addRule():
    '''    public RuleList addRule(final Rule nextRule)
    '''
def finish():
    '''    public RuleList finish()
    '''
