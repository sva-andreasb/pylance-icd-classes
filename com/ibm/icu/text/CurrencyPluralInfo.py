def CurrencyPluralInfo():
'''public CurrencyPluralInfo()
public CurrencyPluralInfo(final Locale locale)
public CurrencyPluralInfo(final ULocale locale)
'''
pass
def getInstance():
'''public static CurrencyPluralInfo getInstance()
public static CurrencyPluralInfo getInstance(final Locale locale)
public static CurrencyPluralInfo getInstance(final ULocale locale)
'''
pass
def getPluralRules():
'''public PluralRules getPluralRules()
'''
pass
def getCurrencyPluralPattern():
'''public String getCurrencyPluralPattern(final String pluralCount)
'''
pass
def getLocale():
'''public ULocale getLocale()
'''
pass
def setPluralRules():
'''public void setPluralRules(final String ruleDescription)
'''
pass
def setCurrencyPluralPattern():
'''public void setCurrencyPluralPattern(final String pluralCount, final String pattern)
'''
pass
def setLocale():
'''public void setLocale(final ULocale loc)
'''
pass
def clone():
'''public Object clone()
'''
pass
def equals():
'''public boolean equals(final Object a)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def select():
'''public String select(final PluralRules.FixedDecimal numberInfo)
'''
pass
def pluralPatternIterator():
'''public Iterator<String> pluralPatternIterator()
'''
pass
