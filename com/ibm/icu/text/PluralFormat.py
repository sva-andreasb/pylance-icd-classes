def PluralFormat():
    '''public PluralFormat()
    public PluralFormat(final ULocale ulocale)
    public PluralFormat(final Locale locale)
    public PluralFormat(final PluralRules rules)
    public PluralFormat(final ULocale ulocale, final PluralRules rules)
    public PluralFormat(final Locale locale, final PluralRules rules)
    public PluralFormat(final ULocale ulocale, final PluralRules.PluralType type)
    public PluralFormat(final Locale locale, final PluralRules.PluralType type)
    public PluralFormat(final String pattern)
    public PluralFormat(final ULocale ulocale, final String pattern)
    public PluralFormat(final PluralRules rules, final String pattern)
    public PluralFormat(final ULocale ulocale, final PluralRules rules, final String pattern)
    public PluralFormat(final ULocale ulocale, final PluralRules.PluralType type, final String pattern)
    '''
def applyPattern():
    '''public void applyPattern(final String pattern)
    '''
def toPattern():
    '''public String toPattern()
    '''
def format():
    '''public final String format(final double number)
    public StringBuffer format(final Object number, final StringBuffer toAppendTo, final FieldPosition pos)
    '''
def parse():
    '''public Number parse(final String text, final ParsePosition parsePosition)
    '''
def parseObject():
    '''public Object parseObject(final String source, final ParsePosition pos)
    '''
def setLocale():
    '''public void setLocale(ULocale ulocale)
    '''
def setNumberFormat():
    '''public void setNumberFormat(final NumberFormat format)
    '''
def equals():
    '''public boolean equals(final Object rhs)
    public boolean equals(final PluralFormat rhs)
    '''
def hashCode():
    '''public int hashCode()
    '''
def toString():
    '''public String toString()
    '''
def select():
    '''public String select(final Object context, final double number)
    '''
