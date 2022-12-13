DONE = "int -1"
WORD_NONE = "int 0"
WORD_NONE_LIMIT = "int 100"
WORD_NUMBER = "int 100"
WORD_NUMBER_LIMIT = "int 200"
WORD_LETTER = "int 200"
WORD_LETTER_LIMIT = "int 300"
WORD_KANA = "int 300"
WORD_KANA_LIMIT = "int 400"
WORD_IDEO = "int 400"
WORD_IDEO_LIMIT = "int 500"
KIND_CHARACTER = "int 0"
KIND_WORD = "int 1"
KIND_LINE = "int 2"
KIND_SENTENCE = "int 3"
KIND_TITLE = "int 4"
def clone():
'''public Object clone()
'''
pass
def preceding():
'''public int preceding(final int offset)
'''
pass
def isBoundary():
'''public boolean isBoundary(final int offset)
'''
pass
def getRuleStatus():
'''public int getRuleStatus()
'''
pass
def getRuleStatusVec():
'''public int getRuleStatusVec(final int[] fillInArray)
'''
pass
def setText():
'''public void setText(final String newText)
public void setText(final CharSequence newText)
'''
pass
def getWordInstance():
'''public static BreakIterator getWordInstance()
public static BreakIterator getWordInstance(final Locale where)
public static BreakIterator getWordInstance(final ULocale where)
'''
pass
def getLineInstance():
'''public static BreakIterator getLineInstance()
public static BreakIterator getLineInstance(final Locale where)
public static BreakIterator getLineInstance(final ULocale where)
'''
pass
def getCharacterInstance():
'''public static BreakIterator getCharacterInstance()
public static BreakIterator getCharacterInstance(final Locale where)
public static BreakIterator getCharacterInstance(final ULocale where)
'''
pass
def getSentenceInstance():
'''public static BreakIterator getSentenceInstance()
public static BreakIterator getSentenceInstance(final Locale where)
public static BreakIterator getSentenceInstance(final ULocale where)
'''
pass
def getTitleInstance():
'''public static BreakIterator getTitleInstance()
public static BreakIterator getTitleInstance(final Locale where)
public static BreakIterator getTitleInstance(final ULocale where)
'''
pass
def registerInstance():
'''public static Object registerInstance(final BreakIterator iter, final Locale locale, final int kind)
public static Object registerInstance(final BreakIterator iter, final ULocale locale, final int kind)
'''
pass
def unregister():
'''public static boolean unregister(final Object key)
'''
pass
def getBreakInstance():
'''public static BreakIterator getBreakInstance(final ULocale where, final int kind)
'''
pass
def getAvailableLocales():
'''public static synchronized Locale[] getAvailableLocales()
'''
pass
def getAvailableULocales():
'''public static synchronized ULocale[] getAvailableULocales()
'''
pass
def getLocale():
'''public final ULocale getLocale(final ULocale.Type type)
'''
pass
