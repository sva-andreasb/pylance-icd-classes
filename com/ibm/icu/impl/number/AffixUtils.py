TYPE_MINUS_SIGN = "int -1"
TYPE_PLUS_SIGN = "int -2"
TYPE_PERCENT = "int -3"
TYPE_PERMILLE = "int -4"
TYPE_CURRENCY_SINGLE = "int -5"
TYPE_CURRENCY_DOUBLE = "int -6"
TYPE_CURRENCY_TRIPLE = "int -7"
TYPE_CURRENCY_QUAD = "int -8"
TYPE_CURRENCY_QUINT = "int -9"
TYPE_CURRENCY_OVERFLOW = "int -15"
def estimateLength():
'''public static int estimateLength(final CharSequence patternString)
'''
pass
def escape():
'''public static int escape(final CharSequence input, final StringBuilder output)
public static String escape(final CharSequence input)
'''
pass
def unescape():
'''public static int unescape(final CharSequence affixPattern, final FormattedStringBuilder output, final int position, final SymbolProvider provider, final NumberFormat.Field field)
'''
pass
def unescapedCount():
'''public static int unescapedCount(final CharSequence affixPattern, final boolean lengthOrCount, final SymbolProvider provider)
'''
pass
def containsType():
'''public static boolean containsType(final CharSequence affixPattern, final int type)
'''
pass
def hasCurrencySymbols():
'''public static boolean hasCurrencySymbols(final CharSequence affixPattern)
'''
pass
def replaceType():
'''public static String replaceType(final CharSequence affixPattern, final int type, final char replacementChar)
'''
pass
def containsOnlySymbolsAndIgnorables():
'''public static boolean containsOnlySymbolsAndIgnorables(final CharSequence affixPattern, final UnicodeSet ignorables)
'''
pass
def iterateWithConsumer():
'''public static void iterateWithConsumer(final CharSequence affixPattern, final TokenConsumer consumer)
'''
pass
