def isEntityJid():
    '''public final boolean isEntityJid()
    '''
def isEntityBareJid():
    '''public final boolean isEntityBareJid()
    '''
def isEntityFullJid():
    '''public final boolean isEntityFullJid()
    '''
def isDomainBareJid():
    '''public final boolean isDomainBareJid()
    '''
def isDomainFullJid():
    '''public final boolean isDomainFullJid()
    '''
def hasResource():
    '''public final boolean hasResource()
    '''
def hasLocalpart():
    '''public final boolean hasLocalpart()
    '''
def downcast():
    '''public final <T extends Jid> T downcast(final Class<T> jidClass)
    '''
def length():
    '''public int length()
    '''
def charAt():
    '''public char charAt(final int index)
    '''
def subSequence():
    '''public CharSequence subSequence(final int start, final int end)
    '''
def asEntityBareJidOrThrow():
    '''public final EntityBareJid asEntityBareJidOrThrow()
    '''
def asEntityFullJidOrThrow():
    '''public EntityFullJid asEntityFullJidOrThrow()
    '''
def asEntityJidOrThrow():
    '''public EntityJid asEntityJidOrThrow()
    '''
def asFullJidOrThrow():
    '''public EntityFullJid asFullJidOrThrow()
    '''
def asDomainFullJidOrThrow():
    '''public DomainFullJid asDomainFullJidOrThrow()
    '''
def getResourceOrEmpty():
    '''public final Resourcepart getResourceOrEmpty()
    '''
def getResourceOrThrow():
    '''public final Resourcepart getResourceOrThrow()
    '''
def getLocalpartOrThrow():
    '''public final Localpart getLocalpartOrThrow()
    '''
def isParentOf():
    '''public final boolean isParentOf(final Jid jid)
    '''
def hashCode():
    '''public final int hashCode()
    '''
def equals():
    '''public final boolean equals(final Object other)
    public final boolean equals(final CharSequence charSequence)
    public final boolean equals(final String string)
    '''
def compareTo():
    '''public final int compareTo(final Jid other)
    '''
def intern():
    '''public final String intern()
    '''
def asUrlEncodedString():
    '''public final String asUrlEncodedString()
    '''
