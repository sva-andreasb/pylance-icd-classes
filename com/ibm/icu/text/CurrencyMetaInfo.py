def getInstance():
    '''public static CurrencyMetaInfo getInstance()
    public static CurrencyMetaInfo getInstance(final boolean noSubstitute)
    '''
def hasData():
    '''public static boolean hasData()
    '''
def currencyInfo():
    '''public List<CurrencyInfo> currencyInfo(final CurrencyFilter filter)
    '''
def currencies():
    '''public List<String> currencies(final CurrencyFilter filter)
    '''
def regions():
    '''public List<String> regions(final CurrencyFilter filter)
    '''
def currencyDigits():
    '''public CurrencyDigits currencyDigits(final String isoCode)
    public CurrencyDigits currencyDigits(final String isoCode, final Currency.CurrencyUsage currencyUsage)
    '''
def all():
    '''public static CurrencyFilter all()
    '''
def now():
    '''public static CurrencyFilter now()
    '''
def onRegion():
    '''public static CurrencyFilter onRegion(final String region)
    '''
def onCurrency():
    '''public static CurrencyFilter onCurrency(final String currency)
    '''
def onDate():
    '''public static CurrencyFilter onDate(final Date date)
    public static CurrencyFilter onDate(final long date)
    '''
def onDateRange():
    '''public static CurrencyFilter onDateRange(final Date from, final Date to)
    public static CurrencyFilter onDateRange(final long from, final long to)
    '''
def onTender():
    '''public static CurrencyFilter onTender()
    '''
def withRegion():
    '''public CurrencyFilter withRegion(final String region)
    '''
def withCurrency():
    '''public CurrencyFilter withCurrency(final String currency)
    '''
def withDate():
    '''public CurrencyFilter withDate(final Date date)
    public CurrencyFilter withDate(final long date)
    '''
def withDateRange():
    '''public CurrencyFilter withDateRange(final Date from, final Date to)
    public CurrencyFilter withDateRange(final long from, final long to)
    '''
def withTender():
    '''public CurrencyFilter withTender()
    '''
def equals():
    '''public boolean equals(final Object rhs)
    public boolean equals(final CurrencyFilter rhs)
    '''
def hashCode():
    '''public int hashCode()
    '''
def toString():
    '''public String toString()
    public String toString()
    public String toString()
    '''
def CurrencyDigits():
    '''public CurrencyDigits(final int fractionDigits, final int roundingIncrement)
    '''
def CurrencyInfo():
    '''public CurrencyInfo(final String region, final String code, final long from, final long to, final int priority)
    public CurrencyInfo(final String region, final String code, final long from, final long to, final int priority, final boolean tender)
    '''
def isTender():
    '''public boolean isTender()
    '''
