def MessageFormat():
    '''public MessageFormat(final String pattern)
    public MessageFormat(final String pattern, final Locale locale)
    public MessageFormat(final String pattern, final ULocale locale)
    '''
def setLocale():
    '''public void setLocale(final Locale locale)
    public void setLocale(final ULocale locale)
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def getULocale():
    '''public ULocale getULocale()
    '''
def applyPattern():
    '''public void applyPattern(final String pttrn)
    public void applyPattern(final String pattern, final MessagePattern.ApostropheMode aposMode)
    '''
def toPattern():
    '''public String toPattern()
    '''
def setFormatsByArgumentIndex():
    '''public void setFormatsByArgumentIndex(final Format[] newFormats)
    '''
def setFormatsByArgumentName():
    '''public void setFormatsByArgumentName(final Map<String, Format> newFormats)
    '''
def setFormats():
    '''public void setFormats(final Format[] newFormats)
    '''
def setFormatByArgumentIndex():
    '''public void setFormatByArgumentIndex(final int argumentIndex, final Format newFormat)
    '''
def setFormatByArgumentName():
    '''public void setFormatByArgumentName(final String argumentName, final Format newFormat)
    '''
def setFormat():
    '''public void setFormat(final int formatElementIndex, final Format newFormat)
    '''
def getFormatsByArgumentIndex():
    '''public Format[] getFormatsByArgumentIndex()
    '''
def getFormats():
    '''public Format[] getFormats()
    '''
def getArgumentNames():
    '''public Set<String> getArgumentNames()
    '''
def getFormatByArgumentName():
    '''public Format getFormatByArgumentName(final String argumentName)
    '''
def format():
    '''public final StringBuffer format(final Object[] arguments, final StringBuffer result, final FieldPosition pos)
    public final StringBuffer format(final Map<String, Object> arguments, final StringBuffer result, final FieldPosition pos)
    public static String format(final String pattern, final Object... arguments)
    public static String format(final String pattern, final Map<String, Object> arguments)
    public final StringBuffer format(final Object arguments, final StringBuffer result, final FieldPosition pos)
    '''
def usesNamedArguments():
    '''public boolean usesNamedArguments()
    '''
def formatToCharacterIterator():
    '''public AttributedCharacterIterator formatToCharacterIterator(final Object arguments)
    '''
def parse():
    '''public Object[] parse(final String source, final ParsePosition pos)
    public Object[] parse(final String source)
    '''
def parseToMap():
    '''public Map<String, Object> parseToMap(final String source, final ParsePosition pos)
    public Map<String, Object> parseToMap(final String source)
    '''
def parseObject():
    '''public Object parseObject(final String source, final ParsePosition pos)
    '''
def clone():
    '''public Object clone()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def hashCode():
    '''public int hashCode()
    '''
def autoQuoteApostrophe():
    '''public static String autoQuoteApostrophe(final String pattern)
    '''
def toString():
    '''public String toString()
    '''
def PluralSelectorProvider():
    '''public PluralSelectorProvider(final MessageFormat mf, final PluralRules.PluralType type)
    '''
def select():
    '''public String select(final Object ctx, final double number)
    '''
def AppendableWrapper():
    '''public AppendableWrapper(final StringBuilder sb)
    public AppendableWrapper(final StringBuffer sb)
    '''
def useAttributes():
    '''public void useAttributes()
    '''
def append():
    '''public void append(final CharSequence s)
    public void append(final CharSequence s, final int start, final int limit)
    public void append(final CharacterIterator iterator)
    public static int append(final Appendable result, final CharacterIterator iterator)
    '''
def formatAndAppend():
    '''public void formatAndAppend(final Format formatter, final Object arg)
    public void formatAndAppend(final Format formatter, final Object arg, final String argString)
    '''
def AttributeAndPosition():
    '''public AttributeAndPosition(final Object fieldValue, final int startIndex, final int limitIndex)
    public AttributeAndPosition(final AttributedCharacterIterator.Attribute field, final Object fieldValue, final int startIndex, final int limitIndex)
    '''
def init():
    '''public void init(final AttributedCharacterIterator.Attribute field, final Object fieldValue, final int startIndex, final int limitIndex)
    '''
