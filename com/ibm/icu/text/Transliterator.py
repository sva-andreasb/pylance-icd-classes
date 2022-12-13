FORWARD = "int  0"
REVERSE = "int  1"
def transliterate():
    '''    public final int transliterate(final Replaceable text, final int start, final int limit)
    public final void transliterate(final Replaceable text)
    public final String transliterate(final String text)
    public final void transliterate(final Replaceable text, final Position index, final String insertion)
    public final void transliterate(final Replaceable text, final Position index, final int insertion)
    public final void transliterate(final Replaceable text, final Position index)
    '''
def finishTransliteration():
    '''    public final void finishTransliteration(final Replaceable text, final Position index)
    '''
def filteredTransliterate():
    '''    public void filteredTransliterate(final Replaceable text, final Position index, final boolean incremental)
    '''
def getMaximumContextLength():
    '''    public final int getMaximumContextLength()
    '''
def getID():
    '''    public final String getID()
    '''
def getDisplayName():
    '''    public static final String getDisplayName(final String ID)
    public static String getDisplayName(final String id, final Locale inLocale)
    public static String getDisplayName(final String id, final ULocale inLocale)
    '''
def getFilter():
    '''    public final UnicodeFilter getFilter()
    '''
def setFilter():
    '''    public void setFilter(final UnicodeFilter filter)
    '''
def getInstance():
    '''    public static final Transliterator getInstance(final String ID)
    public static Transliterator getInstance(final String ID, final int dir)
    '''
def createFromRules():
    '''    public static final Transliterator createFromRules(final String ID, final String rules, final int dir)
    '''
def toRules():
    '''    public String toRules(final boolean escapeUnprintable)
    '''
def getElements():
    '''    public Transliterator[] getElements()
    '''
def getSourceSet():
    '''    public final UnicodeSet getSourceSet()
    '''
def getTargetSet():
    '''    public UnicodeSet getTargetSet()
    '''
def addSourceTargetSet():
    '''    public void addSourceTargetSet(final UnicodeSet inputFilter, final UnicodeSet sourceSet, final UnicodeSet targetSet)
    '''
def getFilterAsUnicodeSet():
    '''    public UnicodeSet getFilterAsUnicodeSet(final UnicodeSet externalFilter)
    '''
def getInverse():
    '''    public final Transliterator getInverse()
    '''
def registerClass():
    '''    public static void registerClass(final String ID, final Class<? extends Transliterator> transClass, final String displayName)
    '''
def registerFactory():
    '''    public static void registerFactory(final String ID, final Factory factory)
    '''
def registerInstance():
    '''    public static void registerInstance(final Transliterator trans)
    '''
def registerAlias():
    '''    public static void registerAlias(final String aliasID, final String realID)
    '''
def unregister():
    '''    public static void unregister(final String ID)
    '''
def getAvailableIDs():
    '''    public static final Enumeration<String> getAvailableIDs()
    '''
def getAvailableSources():
    '''    public static final Enumeration<String> getAvailableSources()
    '''
def getAvailableTargets():
    '''    public static final Enumeration<String> getAvailableTargets(final String source)
    '''
def getAvailableVariants():
    '''    public static final Enumeration<String> getAvailableVariants(final String source, final String target)
    '''
def registerAny():
    '''    public static void registerAny()
    '''
def transform():
    '''    public String transform(final String source)
    '''
def Position():
    '''    public Position()
    public Position(final int contextStart, final int contextLimit, final int start)
    public Position(final int contextStart, final int contextLimit, final int start, final int limit)
    public Position(final Position pos)
    '''
def set():
    '''    public void set(final Position pos)
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def toString():
    '''    public String toString()
    '''
def validate():
    '''    public final void validate(final int length)
    '''
