def CurrencyPluralInfo():
    '''public CurrencyPluralInfo()
    public CurrencyPluralInfo(final Locale locale)
    public CurrencyPluralInfo(final ULocale locale)
    '''
def getInstance():
    '''public static CurrencyPluralInfo getInstance()
    public static CurrencyPluralInfo getInstance(final Locale locale)
    public static CurrencyPluralInfo getInstance(final ULocale locale)
    '''
def getPluralRules():
    '''public PluralRules getPluralRules()
    '''
def getCurrencyPluralPattern():
    '''public String getCurrencyPluralPattern(final String pluralCount)
    '''
def getLocale():
    '''public ULocale getLocale()
    '''
def setPluralRules():
    '''public void setPluralRules(final String ruleDescription)
    '''
def setCurrencyPluralPattern():
    '''public void setCurrencyPluralPattern(final String pluralCount, final String pattern)
    '''
def setLocale():
    '''public void setLocale(final ULocale loc)
    '''
def clone():
    '''public Object clone()
    '''
def equals():
    '''public boolean equals(final Object a)
    '''
def hashCode():
    '''public int hashCode()
    '''
def select():
    '''public String select(final PluralRules.FixedDecimal numberInfo)
    '''
def pluralPatternIterator():
    '''public Iterator<String> pluralPatternIterator()
    '''
