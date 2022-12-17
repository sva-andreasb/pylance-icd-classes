def ():
    '''returns MessageFormat\n\n
    (final String pattern)\n
    (final String pattern, final Locale locale)\n
    (final String pattern, final ULocale locale)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    setLocale(final ULocale locale)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def getULocale():
    '''returns ULocale\n\n
    getULocale()\n
    '''
def applyPattern():
    '''returns None\n\n
    applyPattern(final String pttrn)\n
    '''
def toPattern():
    '''returns String\n\n
    toPattern()\n
    '''
def setFormatsByArgumentIndex():
    '''returns None\n\n
    setFormatsByArgumentIndex(final Format[] newFormats)\n
    '''
def setFormatsByArgumentName():
    '''returns None\n\n
    setFormatsByArgumentName(final Map<String, Format> newFormats)\n
    '''
def setFormats():
    '''returns None\n\n
    setFormats(final Format[] newFormats)\n
    '''
def setFormatByArgumentIndex():
    '''returns None\n\n
    setFormatByArgumentIndex(final int argumentIndex, final Format newFormat)\n
    '''
def setFormatByArgumentName():
    '''returns None\n\n
    setFormatByArgumentName(final String argumentName, final Format newFormat)\n
    '''
def setFormat():
    '''returns None\n\n
    setFormat(final int formatElementIndex, final Format newFormat)\n
    '''
def getFormatsByArgumentIndex():
    '''returns Format[]\n\n
    getFormatsByArgumentIndex()\n
    '''
def getFormats():
    '''returns Format[]\n\n
    getFormats()\n
    '''
def getFormatArgumentNames():
    '''returns Set<String>\n\n
    getFormatArgumentNames()\n
    '''
def getFormatByArgumentName():
    '''returns Format\n\n
    getFormatByArgumentName(final String argumentName)\n
    '''
def usesNamedArguments():
    '''returns boolean\n\n
    usesNamedArguments()\n
    '''
def formatToCharacterIterator():
    '''returns AttributedCharacterIterator\n\n
    formatToCharacterIterator(final Object arguments)\n
    '''
def parse():
    '''returns Object[]\n\n
    parse(final String source, final ParsePosition pos)\n
    parse(final String source)\n
    '''
def parseObject():
    '''returns Object\n\n
    parseObject(final String source, final ParsePosition pos)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
