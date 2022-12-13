def createSimpleParser():
    '''public static NumberParserImpl createSimpleParser(final ULocale locale, final String pattern, final int parseFlags)
    '''
def parseStatic():
    '''public static Number parseStatic(final String input, final ParsePosition ppos, final DecimalFormatProperties properties, final DecimalFormatSymbols symbols)
    '''
def parseStaticCurrency():
    '''public static CurrencyAmount parseStaticCurrency(final String input, final ParsePosition ppos, final DecimalFormatProperties properties, final DecimalFormatSymbols symbols)
    '''
def createDefaultParserForLocale():
    '''public static NumberParserImpl createDefaultParserForLocale(final ULocale loc)
    '''
def createParserFromProperties():
    '''public static NumberParserImpl createParserFromProperties(final DecimalFormatProperties properties, final DecimalFormatSymbols symbols, final boolean parseCurrency)
    '''
def NumberParserImpl():
    '''public NumberParserImpl(final int parseFlags)
    '''
def addMatcher():
    '''public void addMatcher(final NumberParseMatcher matcher)
    '''
def addMatchers():
    '''public void addMatchers(final Collection<? extends NumberParseMatcher> matchers)
    '''
def freeze():
    '''public void freeze()
    '''
def getParseFlags():
    '''public int getParseFlags()
    '''
def parse():
    '''public void parse(final String input, final boolean greedy, final ParsedNumber result)
    public void parse(final String input, final int start, final boolean greedy, final ParsedNumber result)
    '''
def toString():
    '''public String toString()
    '''
