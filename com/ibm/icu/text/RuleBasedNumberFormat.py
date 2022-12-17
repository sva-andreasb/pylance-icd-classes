SPELLOUT = "int  1"
ORDINAL = "int  2"
DURATION = "int  3"
NUMBERING_SYSTEM = "int  4"
def ():
    '''returns RuleBasedNumberFormat\n\n
    (final String description)\n
    (final String description, final String[][] localizations)\n
    (final String description, final Locale locale)\n
    (final String description, final ULocale locale)\n
    (final String description, final String[][] localizations, final ULocale locale)\n
    (final Locale locale, final int format)\n
    (final ULocale locale, final int format)\n
    (final int format)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object that)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getRuleSetNames():
    '''returns String[]\n\n
    getRuleSetNames()\n
    '''
def getRuleSetDisplayNameLocales():
    '''returns ULocale[]\n\n
    getRuleSetDisplayNameLocales()\n
    '''
def getRuleSetDisplayNames():
    '''returns String[]\n\n
    getRuleSetDisplayNames(final ULocale loc)\n
    getRuleSetDisplayNames()\n
    '''
def getRuleSetDisplayName():
    '''returns String\n\n
    getRuleSetDisplayName(final String ruleSetName, final ULocale loc)\n
    getRuleSetDisplayName(final String ruleSetName)\n
    '''
def format():
    '''returns StringBuffer\n\n
    format(final double number, final String ruleSet)\n
    format(final long number, final String ruleSet)\n
    format(final double number, final StringBuffer toAppendTo, final FieldPosition ignore)\n
    format(final long number, final StringBuffer toAppendTo, final FieldPosition ignore)\n
    format(final BigInteger number, final StringBuffer toAppendTo, final FieldPosition pos)\n
    format(final java.math.BigDecimal number, final StringBuffer toAppendTo, final FieldPosition pos)\n
    format(final BigDecimal number, final StringBuffer toAppendTo, final FieldPosition pos)\n
    '''
def parse():
    '''returns Number\n\n
    parse(final String text, final ParsePosition parsePosition)\n
    '''
def setLenientParseMode():
    '''returns None\n\n
    setLenientParseMode(final boolean enabled)\n
    '''
def lenientParseEnabled():
    '''returns boolean\n\n
    lenientParseEnabled()\n
    '''
def setLenientScannerProvider():
    '''returns None\n\n
    setLenientScannerProvider(final RbnfLenientScannerProvider scannerProvider)\n
    '''
def getLenientScannerProvider():
    '''returns RbnfLenientScannerProvider\n\n
    getLenientScannerProvider()\n
    '''
def setDefaultRuleSet():
    '''returns None\n\n
    setDefaultRuleSet(final String ruleSetName)\n
    '''
def getDefaultRuleSetName():
    '''returns String\n\n
    getDefaultRuleSetName()\n
    '''
