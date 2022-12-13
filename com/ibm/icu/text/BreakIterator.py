DONE = "int  -1"
WORD_NONE = "int  0"
WORD_NONE_LIMIT = "int  100"
WORD_NUMBER = "int  100"
WORD_NUMBER_LIMIT = "int  200"
WORD_LETTER = "int  200"
WORD_LETTER_LIMIT = "int  300"
WORD_KANA = "int  300"
WORD_KANA_LIMIT = "int  400"
WORD_IDEO = "int  400"
WORD_IDEO_LIMIT = "int  500"
KIND_CHARACTER = "int  0"
KIND_WORD = "int  1"
KIND_LINE = "int  2"
KIND_SENTENCE = "int  3"
KIND_TITLE = "int  4"
def clone():
    '''    public Object clone()
    '''
def preceding():
    '''    public int preceding(final int offset)
    '''
def isBoundary():
    '''    public boolean isBoundary(final int offset)
    '''
def getRuleStatus():
    '''    public int getRuleStatus()
    '''
def getRuleStatusVec():
    '''    public int getRuleStatusVec(final int[] fillInArray)
    '''
def setText():
    '''    public void setText(final String newText)
    public void setText(final CharSequence newText)
    '''
def getWordInstance():
    '''    public static BreakIterator getWordInstance()
    public static BreakIterator getWordInstance(final Locale where)
    public static BreakIterator getWordInstance(final ULocale where)
    '''
def getLineInstance():
    '''    public static BreakIterator getLineInstance()
    public static BreakIterator getLineInstance(final Locale where)
    public static BreakIterator getLineInstance(final ULocale where)
    '''
def getCharacterInstance():
    '''    public static BreakIterator getCharacterInstance()
    public static BreakIterator getCharacterInstance(final Locale where)
    public static BreakIterator getCharacterInstance(final ULocale where)
    '''
def getSentenceInstance():
    '''    public static BreakIterator getSentenceInstance()
    public static BreakIterator getSentenceInstance(final Locale where)
    public static BreakIterator getSentenceInstance(final ULocale where)
    '''
def getTitleInstance():
    '''    public static BreakIterator getTitleInstance()
    public static BreakIterator getTitleInstance(final Locale where)
    public static BreakIterator getTitleInstance(final ULocale where)
    '''
def registerInstance():
    '''    public static Object registerInstance(final BreakIterator iter, final Locale locale, final int kind)
    public static Object registerInstance(final BreakIterator iter, final ULocale locale, final int kind)
    '''
def unregister():
    '''    public static boolean unregister(final Object key)
    '''
def getBreakInstance():
    '''    public static BreakIterator getBreakInstance(final ULocale where, final int kind)
    '''
def getAvailableLocales():
    '''    public static synchronized Locale[] getAvailableLocales()
    '''
def getAvailableULocales():
    '''    public static synchronized ULocale[] getAvailableULocales()
    '''
def getLocale():
    '''    public final ULocale getLocale(final ULocale.Type type)
    '''
