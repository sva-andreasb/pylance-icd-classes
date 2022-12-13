TITLECASE_WHOLE_STRING = "int  32"
TITLECASE_SENTENCES = "int  64"
TITLECASE_ADJUST_TO_CASED = "int  1024"
OMIT_UNCHANGED_TEXT = "int  16384"
def addTitleAdjustmentOption():
    '''    public static int addTitleAdjustmentOption(final int options, final int newOption)
    '''
def addTitleIteratorOption():
    '''    public static int addTitleIteratorOption(final int options, final int newOption)
    '''
def getTitleBreakIterator():
    '''    public static BreakIterator getTitleBreakIterator(final Locale locale, int options, BreakIterator iter)
    public static BreakIterator getTitleBreakIterator(final ULocale locale, int options, BreakIterator iter)
    '''
def toLower():
    '''    public static String toLower(final int caseLocale, final int options, final CharSequence src)
    public static <A extends Appendable> A toLower(final int caseLocale, final int options, final CharSequence src, final A dest, final Edits edits)
    '''
def toUpper():
    '''    public static String toUpper(final int caseLocale, final int options, final CharSequence src)
    public static <A extends Appendable> A toUpper(final int caseLocale, final int options, final CharSequence src, final A dest, final Edits edits)
    '''
def toTitle():
    '''    public static String toTitle(final int caseLocale, final int options, final BreakIterator iter, final CharSequence src)
    public static <A extends Appendable> A toTitle(final int caseLocale, final int options, final BreakIterator titleIter, final CharSequence src, final A dest, final Edits edits)
    '''
def fold():
    '''    public static String fold(final int options, final CharSequence src)
    public static <A extends Appendable> A fold(final int options, final CharSequence src, final A dest, final Edits edits)
    '''
def StringContextIterator():
    '''    public StringContextIterator(final CharSequence src)
    public StringContextIterator(final CharSequence src, final int cpStart, final int cpLimit)
    '''
def setLimit():
    '''    public void setLimit(final int lim)
    '''
def moveToLimit():
    '''    public void moveToLimit()
    '''
def nextCaseMapCP():
    '''    public int nextCaseMapCP()
    '''
def setCPStartAndLimit():
    '''    public void setCPStartAndLimit(final int s, final int l)
    '''
def getCPStart():
    '''    public int getCPStart()
    '''
def getCPLimit():
    '''    public int getCPLimit()
    '''
def getCPLength():
    '''    public int getCPLength()
    '''
def reset():
    '''    public void reset(final int direction)
    '''
def next():
    '''    public int next()
    public int next(final int n)
    public int next()
    '''
def first():
    '''    public int first()
    '''
def last():
    '''    public int last()
    '''
def previous():
    '''    public int previous()
    '''
def following():
    '''    public int following(final int offset)
    '''
def current():
    '''    public int current()
    '''
def getText():
    '''    public CharacterIterator getText()
    '''
def setText():
    '''    public void setText(final CharacterIterator newText)
    public void setText(final CharSequence newText)
    public void setText(final String newText)
    '''
