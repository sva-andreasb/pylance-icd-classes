def toLower():
    '''    public static Lower toLower()
    '''
def toUpper():
    '''    public static Upper toUpper()
    '''
def toTitle():
    '''    public static Title toTitle()
    '''
def fold():
    '''    public static Fold fold()
    '''
def omitUnchangedText():
    '''    public Lower omitUnchangedText()
    public Upper omitUnchangedText()
    public Title omitUnchangedText()
    public Fold omitUnchangedText()
    '''
def apply():
    '''    public String apply(final Locale locale, final CharSequence src)
    public <A extends Appendable> A apply(final Locale locale, final CharSequence src, final A dest, final Edits edits)
    public String apply(final Locale locale, final CharSequence src)
    public <A extends Appendable> A apply(final Locale locale, final CharSequence src, final A dest, final Edits edits)
    public String apply(Locale locale, BreakIterator iter, final CharSequence src)
    public <A extends Appendable> A apply(Locale locale, BreakIterator iter, final CharSequence src, final A dest, final Edits edits)
    public String apply(final CharSequence src)
    public <A extends Appendable> A apply(final CharSequence src, final A dest, final Edits edits)
    '''
def wholeString():
    '''    public Title wholeString()
    '''
def sentences():
    '''    public Title sentences()
    '''
def noLowercase():
    '''    public Title noLowercase()
    '''
def noBreakAdjustment():
    '''    public Title noBreakAdjustment()
    '''
def adjustToCased():
    '''    public Title adjustToCased()
    '''
def turkic():
    '''    public Fold turkic()
    '''
