def getInstance():
'''public static CurrencyMetaInfo getInstance()
public static CurrencyMetaInfo getInstance(final boolean noSubstitute)
'''
pass
def hasData():
'''public static boolean hasData()
'''
pass
def currencyInfo():
'''public List<CurrencyInfo> currencyInfo(final CurrencyFilter filter)
'''
pass
def currencies():
'''public List<String> currencies(final CurrencyFilter filter)
'''
pass
def regions():
'''public List<String> regions(final CurrencyFilter filter)
'''
pass
def currencyDigits():
'''public CurrencyDigits currencyDigits(final String isoCode)
public CurrencyDigits currencyDigits(final String isoCode, final Currency.CurrencyUsage currencyUsage)
'''
pass
def all():
'''public static CurrencyFilter all()
'''
pass
def now():
'''public static CurrencyFilter now()
'''
pass
def onRegion():
'''public static CurrencyFilter onRegion(final String region)
'''
pass
def onCurrency():
'''public static CurrencyFilter onCurrency(final String currency)
'''
pass
def onDate():
'''public static CurrencyFilter onDate(final Date date)
public static CurrencyFilter onDate(final long date)
'''
pass
def onDateRange():
'''public static CurrencyFilter onDateRange(final Date from, final Date to)
public static CurrencyFilter onDateRange(final long from, final long to)
'''
pass
def onTender():
'''public static CurrencyFilter onTender()
'''
pass
def withRegion():
'''public CurrencyFilter withRegion(final String region)
'''
pass
def withCurrency():
'''public CurrencyFilter withCurrency(final String currency)
'''
pass
def withDate():
'''public CurrencyFilter withDate(final Date date)
public CurrencyFilter withDate(final long date)
'''
pass
def withDateRange():
'''public CurrencyFilter withDateRange(final Date from, final Date to)
public CurrencyFilter withDateRange(final long from, final long to)
'''
pass
def withTender():
'''public CurrencyFilter withTender()
'''
pass
def equals():
'''public boolean equals(final Object rhs)
public boolean equals(final CurrencyFilter rhs)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def toString():
'''public String toString()
public String toString()
public String toString()
'''
pass
def CurrencyDigits():
'''public CurrencyDigits(final int fractionDigits, final int roundingIncrement)
'''
pass
def CurrencyInfo():
'''public CurrencyInfo(final String region, final String code, final long from, final long to, final int priority)
public CurrencyInfo(final String region, final String code, final long from, final long to, final int priority, final boolean tender)
'''
pass
def isTender():
'''public boolean isTender()
'''
pass
