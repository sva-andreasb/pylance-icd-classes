def getInstance():
'''public static RelativeDateTimeFormatter getInstance()
public static RelativeDateTimeFormatter getInstance(final ULocale locale)
public static RelativeDateTimeFormatter getInstance(final Locale locale)
public static RelativeDateTimeFormatter getInstance(final ULocale locale, final NumberFormat nf)
public static RelativeDateTimeFormatter getInstance(final ULocale locale, NumberFormat nf, final Style style, final DisplayContext capitalizationContext)
public static RelativeDateTimeFormatter getInstance(final Locale locale, final NumberFormat nf)
'''
pass
def format():
'''public String format(final double quantity, final Direction direction, final RelativeUnit unit)
public String format(final Direction direction, final AbsoluteUnit unit)
public String format(final double offset, final RelativeDateTimeUnit unit)
'''
pass
def formatToValue():
'''public FormattedRelativeDateTime formatToValue(final double quantity, final Direction direction, final RelativeUnit unit)
public FormattedRelativeDateTime formatToValue(final Direction direction, final AbsoluteUnit unit)
public FormattedRelativeDateTime formatToValue(final double offset, final RelativeDateTimeUnit unit)
'''
pass
def formatNumeric():
'''public String formatNumeric(final double offset, final RelativeDateTimeUnit unit)
'''
pass
def formatNumericToValue():
'''public FormattedRelativeDateTime formatNumericToValue(final double offset, final RelativeDateTimeUnit unit)
'''
pass
def combineDateAndTime():
'''public String combineDateAndTime(final String relativeDateString, final String timeString)
'''
pass
def getNumberFormat():
'''public NumberFormat getNumberFormat()
'''
pass
def getCapitalizationContext():
'''public DisplayContext getCapitalizationContext()
'''
pass
def getFormatStyle():
'''public Style getFormatStyle()
'''
pass
def toString():
'''public String toString()
'''
pass
def length():
'''public int length()
'''
pass
def charAt():
'''public char charAt(final int index)
'''
pass
def subSequence():
'''public CharSequence subSequence(final int start, final int end)
'''
pass
def appendTo():
'''public <A extends Appendable> A appendTo(final A appendable)
'''
pass
def nextPosition():
'''public boolean nextPosition(final ConstrainedFieldPosition cfpos)
'''
pass
def toCharacterIterator():
'''public AttributedCharacterIterator toCharacterIterator()
'''
pass
def RelativeDateTimeFormatterData():
'''public RelativeDateTimeFormatterData(final EnumMap<Style, EnumMap<AbsoluteUnit, EnumMap<Direction, String>>> qualitativeUnitMap, final EnumMap<Style, EnumMap<RelativeUnit, String[][]>> relUnitPatternMap, final String dateTimePattern)
'''
pass
def get():
'''public RelativeDateTimeFormatterData get(final ULocale locale)
'''
pass
def consumeTableRelative():
'''public void consumeTableRelative(final UResource.Key key, final UResource.Value value)
'''
pass
def consumeTableRelativeTime():
'''public void consumeTableRelativeTime(final UResource.Key key, final UResource.Value value)
'''
pass
def consumeTimeDetail():
'''public void consumeTimeDetail(final UResource.Key key, final UResource.Value value)
'''
pass
def consumeTimeUnit():
'''public void consumeTimeUnit(final UResource.Key key, final UResource.Value value)
'''
pass
def put():
'''public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
'''
pass
def Loader():
'''public Loader(final ULocale ulocale)
'''
pass
def load():
'''public RelativeDateTimeFormatterData load()
'''
pass
