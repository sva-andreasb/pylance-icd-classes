def getInstance():
    '''    public static RelativeDateTimeFormatter getInstance()
    public static RelativeDateTimeFormatter getInstance(final ULocale locale)
    public static RelativeDateTimeFormatter getInstance(final Locale locale)
    public static RelativeDateTimeFormatter getInstance(final ULocale locale, final NumberFormat nf)
    public static RelativeDateTimeFormatter getInstance(final ULocale locale, NumberFormat nf, final Style style, final DisplayContext capitalizationContext)
    public static RelativeDateTimeFormatter getInstance(final Locale locale, final NumberFormat nf)
    '''
def format():
    '''    public String format(final double quantity, final Direction direction, final RelativeUnit unit)
    public String format(final Direction direction, final AbsoluteUnit unit)
    public String format(final double offset, final RelativeDateTimeUnit unit)
    '''
def formatToValue():
    '''    public FormattedRelativeDateTime formatToValue(final double quantity, final Direction direction, final RelativeUnit unit)
    public FormattedRelativeDateTime formatToValue(final Direction direction, final AbsoluteUnit unit)
    public FormattedRelativeDateTime formatToValue(final double offset, final RelativeDateTimeUnit unit)
    '''
def formatNumeric():
    '''    public String formatNumeric(final double offset, final RelativeDateTimeUnit unit)
    '''
def formatNumericToValue():
    '''    public FormattedRelativeDateTime formatNumericToValue(final double offset, final RelativeDateTimeUnit unit)
    '''
def combineDateAndTime():
    '''    public String combineDateAndTime(final String relativeDateString, final String timeString)
    '''
def getNumberFormat():
    '''    public NumberFormat getNumberFormat()
    '''
def getCapitalizationContext():
    '''    public DisplayContext getCapitalizationContext()
    '''
def getFormatStyle():
    '''    public Style getFormatStyle()
    '''
def toString():
    '''    public String toString()
    '''
def length():
    '''    public int length()
    '''
def charAt():
    '''    public char charAt(final int index)
    '''
def subSequence():
    '''    public CharSequence subSequence(final int start, final int end)
    '''
def appendTo():
    '''    public <A extends Appendable> A appendTo(final A appendable)
    '''
def nextPosition():
    '''    public boolean nextPosition(final ConstrainedFieldPosition cfpos)
    '''
def toCharacterIterator():
    '''    public AttributedCharacterIterator toCharacterIterator()
    '''
def RelativeDateTimeFormatterData():
    '''    public RelativeDateTimeFormatterData(final EnumMap<Style, EnumMap<AbsoluteUnit, EnumMap<Direction, String>>> qualitativeUnitMap, final EnumMap<Style, EnumMap<RelativeUnit, String[][]>> relUnitPatternMap, final String dateTimePattern)
    '''
def get():
    '''    public RelativeDateTimeFormatterData get(final ULocale locale)
    '''
def consumeTableRelative():
    '''    public void consumeTableRelative(final UResource.Key key, final UResource.Value value)
    '''
def consumeTableRelativeTime():
    '''    public void consumeTableRelativeTime(final UResource.Key key, final UResource.Value value)
    '''
def consumeTimeDetail():
    '''    public void consumeTimeDetail(final UResource.Key key, final UResource.Value value)
    '''
def consumeTimeUnit():
    '''    public void consumeTimeUnit(final UResource.Key key, final UResource.Value value)
    '''
def put():
    '''    public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
    '''
def Loader():
    '''    public Loader(final ULocale ulocale)
    '''
def load():
    '''    public RelativeDateTimeFormatterData load()
    '''
