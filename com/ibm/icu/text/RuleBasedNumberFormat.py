SPELLOUT = "int 1"
ORDINAL = "int 2"
DURATION = "int 3"
NUMBERING_SYSTEM = "int 4"
def RuleBasedNumberFormat():
'''public RuleBasedNumberFormat(final String description)
public RuleBasedNumberFormat(final String description, final String[][] localizations)
public RuleBasedNumberFormat(final String description, final Locale locale)
public RuleBasedNumberFormat(final String description, final ULocale locale)
public RuleBasedNumberFormat(final String description, final String[][] localizations, final ULocale locale)
public RuleBasedNumberFormat(final Locale locale, final int format)
public RuleBasedNumberFormat(final ULocale locale, final int format)
public RuleBasedNumberFormat(final int format)
'''
pass
def clone():
'''public Object clone()
'''
pass
def equals():
'''public boolean equals(final Object that)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def toString():
'''public String toString()
'''
pass
def getRuleSetNames():
'''public String[] getRuleSetNames()
'''
pass
def getRuleSetDisplayNameLocales():
'''public ULocale[] getRuleSetDisplayNameLocales()
'''
pass
def getRuleSetDisplayNames():
'''public String[] getRuleSetDisplayNames(final ULocale loc)
public String[] getRuleSetDisplayNames()
'''
pass
def getRuleSetDisplayName():
'''public String getRuleSetDisplayName(final String ruleSetName, final ULocale loc)
public String getRuleSetDisplayName(final String ruleSetName)
'''
pass
def format():
'''public String format(final double number, final String ruleSet)
public String format(final long number, final String ruleSet)
public StringBuffer format(final double number, final StringBuffer toAppendTo, final FieldPosition ignore)
public StringBuffer format(final long number, final StringBuffer toAppendTo, final FieldPosition ignore)
public StringBuffer format(final BigInteger number, final StringBuffer toAppendTo, final FieldPosition pos)
public StringBuffer format(final java.math.BigDecimal number, final StringBuffer toAppendTo, final FieldPosition pos)
public StringBuffer format(final BigDecimal number, final StringBuffer toAppendTo, final FieldPosition pos)
'''
pass
def parse():
'''public Number parse(final String text, final ParsePosition parsePosition)
'''
pass
def setLenientParseMode():
'''public void setLenientParseMode(final boolean enabled)
'''
pass
def lenientParseEnabled():
'''public boolean lenientParseEnabled()
'''
pass
def setLenientScannerProvider():
'''public void setLenientScannerProvider(final RbnfLenientScannerProvider scannerProvider)
'''
pass
def getLenientScannerProvider():
'''public RbnfLenientScannerProvider getLenientScannerProvider()
'''
pass
def setDefaultRuleSet():
'''public void setDefaultRuleSet(final String ruleSetName)
'''
pass
def getDefaultRuleSetName():
'''public String getDefaultRuleSetName()
'''
pass
def setDecimalFormatSymbols():
'''public void setDecimalFormatSymbols(final DecimalFormatSymbols newSymbols)
'''
pass
def setContext():
'''public void setContext(final DisplayContext context)
'''
pass
def getRoundingMode():
'''public int getRoundingMode()
'''
pass
def setRoundingMode():
'''public void setRoundingMode(final int roundingMode)
'''
pass
