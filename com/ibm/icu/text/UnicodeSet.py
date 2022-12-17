MIN_VALUE = "int  0"
MAX_VALUE = "int  1114111"
IGNORE_SPACE = "int  1"
CASE = "int  2"
CASE_INSENSITIVE = "int  2"
ADD_CASE_MAPPINGS = "int  4"
def ():
    '''returns UnicodeSet\n\n
    ()\n
    (final UnicodeSet other)\n
    (final int start, final int end)\n
    (final int... pairs)\n
    (final String pattern)\n
    (final String pattern, final boolean ignoreWhitespace)\n
    (final String pattern, final int options)\n
    (final String pattern, final ParsePosition pos, final SymbolTable symbols)\n
    (final String pattern, final ParsePosition pos, final SymbolTable symbols, final int options)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def set():
    '''returns UnicodeSet\n\n
    set(final int start, final int end)\n
    set(final UnicodeSet other)\n
    '''
def applyPattern():
    '''returns UnicodeSet\n\n
    applyPattern(final String pattern, final boolean ignoreWhitespace)\n
    applyPattern(final String pattern, final int options)\n
    applyPattern(final String pattern, ParsePosition pos, final SymbolTable symbols, final int options)\n
    '''
def toPattern():
    '''returns String\n\n
    toPattern(final boolean escapeUnprintable)\n
    '''
def _generatePattern():
    '''returns StringBuffer\n\n
    _generatePattern(final StringBuffer result, final boolean escapeUnprintable)\n
    _generatePattern(final StringBuffer result, final boolean escapeUnprintable, final boolean includeStrings)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def matchesIndexValue():
    '''returns boolean\n\n
    matchesIndexValue(final int v)\n
    '''
def matches():
    '''returns int\n\n
    matches(final Replaceable text, final int[] offset, final int limit, final boolean incremental)\n
    '''
def matchesAt():
    '''returns int\n\n
    matchesAt(final CharSequence text, final int offset)\n
    '''
def addMatchSetTo():
    '''returns None\n\n
    addMatchSetTo(final UnicodeSet toUnionTo)\n
    '''
def indexOf():
    '''returns int\n\n
    indexOf(final int c)\n
    '''
def charAt():
    '''returns int\n\n
    charAt(int index)\n
    '''
def add():
    '''returns UnicodeSet\n\n
    add(final int start, final int end)\n
    add(final Collection<?> source)\n
    '''
def addAll():
    '''returns UnicodeSet\n\n
    addAll(final int start, final int end)\n
    addAll(final UnicodeSet c)\n
    addAll(final Collection<?> source)\n
    addAll(final String... collection)\n
    '''
def retain():
    '''returns UnicodeSet\n\n
    retain(final int start, final int end)\n
    '''
def remove():
    '''returns None\n\n
    remove(final int start, final int end)\n
    remove()\n
    '''
def complement():
    '''returns UnicodeSet\n\n
    complement(final int start, final int end)\n
    complement()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final int c)\n
    contains(final int start, final int end)\n
    contains(final int ch)\n
    contains(final int ch)\n
    contains(final int ch)\n
    contains(final int ch)\n
    '''
def containsAll():
    '''returns boolean\n\n
    containsAll(final UnicodeSet b)\n
    containsAll(final String s)\n
    containsAll(final Collection<String> collection)\n
    '''
def getRegexEquivalent():
    '''returns String\n\n
    getRegexEquivalent()\n
    '''
def containsNone():
    '''returns boolean\n\n
    containsNone(final int start, final int end)\n
    containsNone(final UnicodeSet b)\n
    containsNone(final String s)\n
    containsNone(final Collection<String> collection)\n
    '''
def retainAll():
    '''returns UnicodeSet\n\n
    retainAll(final UnicodeSet c)\n
    retainAll(final Collection<String> collection)\n
    '''
def removeAll():
    '''returns UnicodeSet\n\n
    removeAll(final UnicodeSet c)\n
    removeAll(final Collection<String> collection)\n
    '''
def complementAll():
    '''returns UnicodeSet\n\n
    complementAll(final UnicodeSet c)\n
    '''
def clear():
    '''returns UnicodeSet\n\n
    clear()\n
    '''
def getRangeCount():
    '''returns int\n\n
    getRangeCount()\n
    '''
def getRangeStart():
    '''returns int\n\n
    getRangeStart(final int index)\n
    '''
def getRangeEnd():
    '''returns int\n\n
    getRangeEnd(final int index)\n
    '''
def compact():
    '''returns UnicodeSet\n\n
    compact()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def addAllTo():
    '''returns String[]\n\n
    addAllTo(final String[] target)\n
    '''
def applyIntPropertyValue():
    '''returns UnicodeSet\n\n
    applyIntPropertyValue(final int prop, final int value)\n
    '''
def applyPropertyAlias():
    '''returns boolean\n\n
    applyPropertyAlias(final String propertyAlias, final String valueAlias)\n
    applyPropertyAlias(final String propertyAlias, final String valueAlias, final SymbolTable symbols)\n
    applyPropertyAlias(final String propertyName, final String propertyValue, final UnicodeSet result)\n
    '''
def closeOver():
    '''returns UnicodeSet\n\n
    closeOver(final int attribute)\n
    '''
def isFrozen():
    '''returns boolean\n\n
    isFrozen()\n
    '''
def freeze():
    '''returns UnicodeSet\n\n
    freeze()\n
    '''
def span():
    '''returns int\n\n
    span(final CharSequence s, final SpanCondition spanCondition)\n
    span(final CharSequence s, int start, final SpanCondition spanCondition)\n
    '''
def spanBack():
    '''returns int\n\n
    spanBack(final CharSequence s, final SpanCondition spanCondition)\n
    spanBack(final CharSequence s, int fromIndex, final SpanCondition spanCondition)\n
    '''
def cloneAsThawed():
    '''returns UnicodeSet\n\n
    cloneAsThawed()\n
    '''
def iterator():
    '''returns Iterator<String>\n\n
    iterator()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final UnicodeSet o)\n
    compareTo(final UnicodeSet o, final ComparisonStyle style)\n
    compareTo(final Iterable<String> other)\n
    '''
def strings():
    '''returns Iterable<String>\n\n
    strings()\n
    '''
def addBridges():
    '''returns UnicodeSet\n\n
    addBridges(final UnicodeSet dontCare)\n
    '''
def findIn():
    '''returns int\n\n
    findIn(final CharSequence value, int fromIndex, final boolean findNot)\n
    '''
def findLastIn():
    '''returns int\n\n
    findLastIn(final CharSequence value, int fromIndex, final boolean findNot)\n
    '''
def stripFrom():
    '''returns String\n\n
    stripFrom(final CharSequence source, final boolean matches)\n
    '''
def lookupMatcher():
    '''returns UnicodeMatcher\n\n
    lookupMatcher(final int i)\n
    '''
def lookup():
    '''returns char[]\n\n
    lookup(final String s)\n
    '''
def parseReference():
    '''returns String\n\n
    parseReference(final String text, final ParsePosition pos, final int limit)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns String\n\n
    next()\n
    '''
