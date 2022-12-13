TITLECASE_WHOLE_STRING = "int  32"
TITLECASE_SENTENCES = "int  64"
TITLECASE_ADJUST_TO_CASED = "int  1024"
OMIT_UNCHANGED_TEXT = "int  16384"
def addTitleAdjustmentOption():
'''public static int addTitleAdjustmentOption(final int options, final int newOption)
'''
pass
def addTitleIteratorOption():
'''public static int addTitleIteratorOption(final int options, final int newOption)
'''
pass
def getTitleBreakIterator():
'''public static BreakIterator getTitleBreakIterator(final Locale locale, int options, BreakIterator iter)
public static BreakIterator getTitleBreakIterator(final ULocale locale, int options, BreakIterator iter)
'''
pass
def toLower():
'''public static String toLower(final int caseLocale, final int options, final CharSequence src)
public static <A extends Appendable> A toLower(final int caseLocale, final int options, final CharSequence src, final A dest, final Edits edits)
'''
pass
def toUpper():
'''public static String toUpper(final int caseLocale, final int options, final CharSequence src)
public static <A extends Appendable> A toUpper(final int caseLocale, final int options, final CharSequence src, final A dest, final Edits edits)
'''
pass
def toTitle():
'''public static String toTitle(final int caseLocale, final int options, final BreakIterator iter, final CharSequence src)
public static <A extends Appendable> A toTitle(final int caseLocale, final int options, final BreakIterator titleIter, final CharSequence src, final A dest, final Edits edits)
'''
pass
def fold():
'''public static String fold(final int options, final CharSequence src)
public static <A extends Appendable> A fold(final int options, final CharSequence src, final A dest, final Edits edits)
'''
pass
def StringContextIterator():
'''public StringContextIterator(final CharSequence src)
public StringContextIterator(final CharSequence src, final int cpStart, final int cpLimit)
'''
pass
def setLimit():
'''public void setLimit(final int lim)
'''
pass
def moveToLimit():
'''public void moveToLimit()
'''
pass
def nextCaseMapCP():
'''public int nextCaseMapCP()
'''
pass
def setCPStartAndLimit():
'''public void setCPStartAndLimit(final int s, final int l)
'''
pass
def getCPStart():
'''public int getCPStart()
'''
pass
def getCPLimit():
'''public int getCPLimit()
'''
pass
def getCPLength():
'''public int getCPLength()
'''
pass
def reset():
'''public void reset(final int direction)
'''
pass
def next():
'''public int next()
public int next(final int n)
public int next()
'''
pass
def first():
'''public int first()
'''
pass
def last():
'''public int last()
'''
pass
def previous():
'''public int previous()
'''
pass
def following():
'''public int following(final int offset)
'''
pass
def current():
'''public int current()
'''
pass
def getText():
'''public CharacterIterator getText()
'''
pass
def setText():
'''public void setText(final CharacterIterator newText)
public void setText(final CharSequence newText)
public void setText(final String newText)
'''
pass
