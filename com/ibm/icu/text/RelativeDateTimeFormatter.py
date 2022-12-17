def format():
    '''returns String\n\n
    format(final double quantity, final Direction direction, final RelativeUnit unit)\n
    format(final Direction direction, final AbsoluteUnit unit)\n
    format(final double offset, final RelativeDateTimeUnit unit)\n
    '''
def formatToValue():
    '''returns FormattedRelativeDateTime\n\n
    formatToValue(final double quantity, final Direction direction, final RelativeUnit unit)\n
    formatToValue(final Direction direction, final AbsoluteUnit unit)\n
    formatToValue(final double offset, final RelativeDateTimeUnit unit)\n
    '''
def formatNumeric():
    '''returns String\n\n
    formatNumeric(final double offset, final RelativeDateTimeUnit unit)\n
    '''
def formatNumericToValue():
    '''returns FormattedRelativeDateTime\n\n
    formatNumericToValue(final double offset, final RelativeDateTimeUnit unit)\n
    '''
def combineDateAndTime():
    '''returns String\n\n
    combineDateAndTime(final String relativeDateString, final String timeString)\n
    '''
def getNumberFormat():
    '''returns NumberFormat\n\n
    getNumberFormat()\n
    '''
def getCapitalizationContext():
    '''returns DisplayContext\n\n
    getCapitalizationContext()\n
    '''
def getFormatStyle():
    '''returns Style\n\n
    getFormatStyle()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def charAt():
    '''returns char\n\n
    charAt(final int index)\n
    '''
def subSequence():
    '''returns CharSequence\n\n
    subSequence(final int start, final int end)\n
    '''
def nextPosition():
    '''returns boolean\n\n
    nextPosition(final ConstrainedFieldPosition cfpos)\n
    '''
def toCharacterIterator():
    '''returns AttributedCharacterIterator\n\n
    toCharacterIterator()\n
    '''
def ():
    '''returns Loader\n\n
    (final EnumMap<Style, EnumMap<AbsoluteUnit, EnumMap<Direction, String>>> qualitativeUnitMap, final EnumMap<Style, EnumMap<RelativeUnit, String[][]>> relUnitPatternMap, final String dateTimePattern)\n
    (final ULocale ulocale)\n
    '''
def get():
    '''returns RelativeDateTimeFormatterData\n\n
    get(final ULocale locale)\n
    '''
def consumeTableRelative():
    '''returns None\n\n
    consumeTableRelative(final UResource.Key key, final UResource.Value value)\n
    '''
def consumeTableRelativeTime():
    '''returns None\n\n
    consumeTableRelativeTime(final UResource.Key key, final UResource.Value value)\n
    '''
def consumeTimeDetail():
    '''returns None\n\n
    consumeTimeDetail(final UResource.Key key, final UResource.Value value)\n
    '''
def consumeTimeUnit():
    '''returns None\n\n
    consumeTimeUnit(final UResource.Key key, final UResource.Value value)\n
    '''
def put():
    '''returns None\n\n
    put(final UResource.Key key, final UResource.Value value, final boolean noFallback)\n
    '''
def load():
    '''returns RelativeDateTimeFormatterData\n\n
    load()\n
    '''
