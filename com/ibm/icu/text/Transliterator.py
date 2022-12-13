FORWARD = "int 0"
REVERSE = "int 1"
def transliterate():
'''public final int transliterate(final Replaceable text, final int start, final int limit)
public final void transliterate(final Replaceable text)
public final String transliterate(final String text)
public final void transliterate(final Replaceable text, final Position index, final String insertion)
public final void transliterate(final Replaceable text, final Position index, final int insertion)
public final void transliterate(final Replaceable text, final Position index)
'''
pass
def finishTransliteration():
'''public final void finishTransliteration(final Replaceable text, final Position index)
'''
pass
def filteredTransliterate():
'''public void filteredTransliterate(final Replaceable text, final Position index, final boolean incremental)
'''
pass
def getMaximumContextLength():
'''public final int getMaximumContextLength()
'''
pass
def getID():
'''public final String getID()
'''
pass
def getDisplayName():
'''public static final String getDisplayName(final String ID)
public static String getDisplayName(final String id, final Locale inLocale)
public static String getDisplayName(final String id, final ULocale inLocale)
'''
pass
def getFilter():
'''public final UnicodeFilter getFilter()
'''
pass
def setFilter():
'''public void setFilter(final UnicodeFilter filter)
'''
pass
def getInstance():
'''public static final Transliterator getInstance(final String ID)
public static Transliterator getInstance(final String ID, final int dir)
'''
pass
def createFromRules():
'''public static final Transliterator createFromRules(final String ID, final String rules, final int dir)
'''
pass
def toRules():
'''public String toRules(final boolean escapeUnprintable)
'''
pass
def getElements():
'''public Transliterator[] getElements()
'''
pass
def getSourceSet():
'''public final UnicodeSet getSourceSet()
'''
pass
def getTargetSet():
'''public UnicodeSet getTargetSet()
'''
pass
def addSourceTargetSet():
'''public void addSourceTargetSet(final UnicodeSet inputFilter, final UnicodeSet sourceSet, final UnicodeSet targetSet)
'''
pass
def getFilterAsUnicodeSet():
'''public UnicodeSet getFilterAsUnicodeSet(final UnicodeSet externalFilter)
'''
pass
def getInverse():
'''public final Transliterator getInverse()
'''
pass
def registerClass():
'''public static void registerClass(final String ID, final Class<? extends Transliterator> transClass, final String displayName)
'''
pass
def registerFactory():
'''public static void registerFactory(final String ID, final Factory factory)
'''
pass
def registerInstance():
'''public static void registerInstance(final Transliterator trans)
'''
pass
def registerAlias():
'''public static void registerAlias(final String aliasID, final String realID)
'''
pass
def unregister():
'''public static void unregister(final String ID)
'''
pass
def getAvailableIDs():
'''public static final Enumeration<String> getAvailableIDs()
'''
pass
def getAvailableSources():
'''public static final Enumeration<String> getAvailableSources()
'''
pass
def getAvailableTargets():
'''public static final Enumeration<String> getAvailableTargets(final String source)
'''
pass
def getAvailableVariants():
'''public static final Enumeration<String> getAvailableVariants(final String source, final String target)
'''
pass
def registerAny():
'''public static void registerAny()
'''
pass
def transform():
'''public String transform(final String source)
'''
pass
def Position():
'''public Position()
public Position(final int contextStart, final int contextLimit, final int start)
public Position(final int contextStart, final int contextLimit, final int start, final int limit)
public Position(final Position pos)
'''
pass
def set():
'''public void set(final Position pos)
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def toString():
'''public String toString()
'''
pass
def validate():
'''public final void validate(final int length)
'''
pass
