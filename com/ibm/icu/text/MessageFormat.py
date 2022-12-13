def MessageFormat():
'''public MessageFormat(final String pattern)
public MessageFormat(final String pattern, final Locale locale)
public MessageFormat(final String pattern, final ULocale locale)
'''
pass
def setLocale():
'''public void setLocale(final Locale locale)
public void setLocale(final ULocale locale)
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def getULocale():
'''public ULocale getULocale()
'''
pass
def applyPattern():
'''public void applyPattern(final String pttrn)
public void applyPattern(final String pattern, final MessagePattern.ApostropheMode aposMode)
'''
pass
def toPattern():
'''public String toPattern()
'''
pass
def setFormatsByArgumentIndex():
'''public void setFormatsByArgumentIndex(final Format[] newFormats)
'''
pass
def setFormatsByArgumentName():
'''public void setFormatsByArgumentName(final Map<String, Format> newFormats)
'''
pass
def setFormats():
'''public void setFormats(final Format[] newFormats)
'''
pass
def setFormatByArgumentIndex():
'''public void setFormatByArgumentIndex(final int argumentIndex, final Format newFormat)
'''
pass
def setFormatByArgumentName():
'''public void setFormatByArgumentName(final String argumentName, final Format newFormat)
'''
pass
def setFormat():
'''public void setFormat(final int formatElementIndex, final Format newFormat)
'''
pass
def getFormatsByArgumentIndex():
'''public Format[] getFormatsByArgumentIndex()
'''
pass
def getFormats():
'''public Format[] getFormats()
'''
pass
def getArgumentNames():
'''public Set<String> getArgumentNames()
'''
pass
def getFormatByArgumentName():
'''public Format getFormatByArgumentName(final String argumentName)
'''
pass
def format():
'''public final StringBuffer format(final Object[] arguments, final StringBuffer result, final FieldPosition pos)
public final StringBuffer format(final Map<String, Object> arguments, final StringBuffer result, final FieldPosition pos)
public static String format(final String pattern, final Object... arguments)
public static String format(final String pattern, final Map<String, Object> arguments)
public final StringBuffer format(final Object arguments, final StringBuffer result, final FieldPosition pos)
'''
pass
def usesNamedArguments():
'''public boolean usesNamedArguments()
'''
pass
def formatToCharacterIterator():
'''public AttributedCharacterIterator formatToCharacterIterator(final Object arguments)
'''
pass
def parse():
'''public Object[] parse(final String source, final ParsePosition pos)
public Object[] parse(final String source)
'''
pass
def parseToMap():
'''public Map<String, Object> parseToMap(final String source, final ParsePosition pos)
public Map<String, Object> parseToMap(final String source)
'''
pass
def parseObject():
'''public Object parseObject(final String source, final ParsePosition pos)
'''
pass
def clone():
'''public Object clone()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def autoQuoteApostrophe():
'''public static String autoQuoteApostrophe(final String pattern)
'''
pass
def toString():
'''public String toString()
'''
pass
def PluralSelectorProvider():
'''public PluralSelectorProvider(final MessageFormat mf, final PluralRules.PluralType type)
'''
pass
def select():
'''public String select(final Object ctx, final double number)
'''
pass
def AppendableWrapper():
'''public AppendableWrapper(final StringBuilder sb)
public AppendableWrapper(final StringBuffer sb)
'''
pass
def useAttributes():
'''public void useAttributes()
'''
pass
def append():
'''public void append(final CharSequence s)
public void append(final CharSequence s, final int start, final int limit)
public void append(final CharacterIterator iterator)
public static int append(final Appendable result, final CharacterIterator iterator)
'''
pass
def formatAndAppend():
'''public void formatAndAppend(final Format formatter, final Object arg)
public void formatAndAppend(final Format formatter, final Object arg, final String argString)
'''
pass
def AttributeAndPosition():
'''public AttributeAndPosition(final Object fieldValue, final int startIndex, final int limitIndex)
public AttributeAndPosition(final AttributedCharacterIterator.Attribute field, final Object fieldValue, final int startIndex, final int limitIndex)
'''
pass
def init():
'''public void init(final AttributedCharacterIterator.Attribute field, final Object fieldValue, final int startIndex, final int limitIndex)
'''
pass
