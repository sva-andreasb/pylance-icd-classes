def from():
    '''public static Jid from(final CharSequence localpart, final CharSequence domainpart, final CharSequence resource)
    public static Jid from(final String localpart, final String domainpart, final String resource)
    public static Jid from(final CharSequence jid)
    public static Jid from(final String jidString)
    '''
def fromOrThrowUnchecked():
    '''public static Jid fromOrThrowUnchecked(final CharSequence cs)
    '''
def fromOrNull():
    '''public static Jid fromOrNull(final CharSequence cs)
    '''
def fromUnescapedOrThrowUnchecked():
    '''public static Jid fromUnescapedOrThrowUnchecked(final CharSequence cs)
    '''
def fromUnescaped():
    '''public static Jid fromUnescaped(final CharSequence unescapedJid)
    public static Jid fromUnescaped(final String unescapedJidString)
    '''
def fromUnescapedOrNull():
    '''public static Jid fromUnescapedOrNull(final CharSequence cs)
    '''
def fromUrlEncoded():
    '''public static Jid fromUrlEncoded(final CharSequence cs)
    '''
def bareFromOrThrowUnchecked():
    '''public static BareJid bareFromOrThrowUnchecked(final CharSequence cs)
    '''
def bareFrom():
    '''public static BareJid bareFrom(final CharSequence jid)
    public static BareJid bareFrom(final String jid)
    public static BareJid bareFrom(final Localpart localpart, final DomainBareJid domainBareJid)
    public static BareJid bareFrom(final Localpart localpart, final Domainpart domain)
    '''
def bareFromOrNull():
    '''public static BareJid bareFromOrNull(final CharSequence cs)
    '''
def bareFromUrlEncoded():
    '''public static BareJid bareFromUrlEncoded(final CharSequence cs)
    '''
def fullFromOrThrowUnchecked():
    '''public static FullJid fullFromOrThrowUnchecked(final CharSequence cs)
    '''
def fullFrom():
    '''public static FullJid fullFrom(final CharSequence jid)
    public static FullJid fullFrom(final String jid)
    public static FullJid fullFrom(final String localpart, final String domainpart, final String resource)
    public static FullJid fullFrom(final Localpart localpart, final DomainBareJid domainBareJid, final Resourcepart resource)
    public static FullJid fullFrom(final Localpart localpart, final Domainpart domainpart, final Resourcepart resource)
    public static FullJid fullFrom(final BareJid bareJid, final Resourcepart resource)
    '''
def fullFromOrNull():
    '''public static FullJid fullFromOrNull(final CharSequence cs)
    '''
def fullFromUrlEncoded():
    '''public static FullJid fullFromUrlEncoded(final CharSequence cs)
    '''
def entityFromOrThrowUnchecked():
    '''public static EntityJid entityFromOrThrowUnchecked(final CharSequence cs)
    '''
def entityFrom():
    '''public static EntityJid entityFrom(final CharSequence jid)
    public static EntityJid entityFrom(final String jidString)
    '''
def entityFromUnescapedOrThrowUnchecked():
    '''public static EntityJid entityFromUnescapedOrThrowUnchecked(final CharSequence cs)
    '''
def entityFromUnescaped():
    '''public static EntityJid entityFromUnescaped(final CharSequence jid)
    public static EntityJid entityFromUnescaped(final String jidString)
    '''
def entityFromUnesacpedOrNull():
    '''public static EntityJid entityFromUnesacpedOrNull(final CharSequence cs)
    '''
def entityFromOrNull():
    '''public static EntityJid entityFromOrNull(final CharSequence cs)
    '''
def entityFromUrlEncoded():
    '''public static EntityJid entityFromUrlEncoded(final CharSequence cs)
    '''
def entityBareFromOrThrowUnchecked():
    '''public static EntityBareJid entityBareFromOrThrowUnchecked(final CharSequence cs)
    '''
def entityBareFrom():
    '''public static EntityBareJid entityBareFrom(final CharSequence jid)
    public static EntityBareJid entityBareFrom(final String jid)
    public static EntityBareJid entityBareFrom(final Localpart localpart, final DomainBareJid domainBareJid)
    public static EntityBareJid entityBareFrom(final Localpart localpart, final Domainpart domain)
    '''
def entityBareFromUnescapedOrThrowUnchecked():
    '''public static EntityBareJid entityBareFromUnescapedOrThrowUnchecked(final CharSequence cs)
    '''
def entityBareFromUnescaped():
    '''public static EntityBareJid entityBareFromUnescaped(final CharSequence unescapedJid)
    public static EntityBareJid entityBareFromUnescaped(final String unescapedJidString)
    '''
def entityBareFromUnescapedOrNull():
    '''public static EntityBareJid entityBareFromUnescapedOrNull(final CharSequence cs)
    '''
def entityBareFromOrNull():
    '''public static EntityBareJid entityBareFromOrNull(final CharSequence cs)
    '''
def entityBareFromUrlEncoded():
    '''public static EntityBareJid entityBareFromUrlEncoded(final CharSequence cs)
    '''
def entityFullFromOrThrowUnchecked():
    '''public static EntityFullJid entityFullFromOrThrowUnchecked(final CharSequence cs)
    '''
def entityFullFrom():
    '''public static EntityFullJid entityFullFrom(final CharSequence jid)
    public static EntityFullJid entityFullFrom(final String jid)
    public static EntityFullJid entityFullFrom(final String localpart, final String domainpart, final String resource)
    public static EntityFullJid entityFullFrom(final Localpart localpart, final DomainBareJid domainBareJid, final Resourcepart resource)
    public static EntityFullJid entityFullFrom(final Localpart localpart, final Domainpart domainpart, final Resourcepart resource)
    public static EntityFullJid entityFullFrom(final EntityBareJid bareJid, final Resourcepart resource)
    '''
def entityFullFromOrNull():
    '''public static EntityFullJid entityFullFromOrNull(final CharSequence cs)
    '''
def entityFullFromUnescapedOrThrowUnchecked():
    '''public static EntityFullJid entityFullFromUnescapedOrThrowUnchecked(final CharSequence cs)
    '''
def entityFullFromUnescaped():
    '''public static EntityFullJid entityFullFromUnescaped(final CharSequence unescapedJid)
    public static EntityFullJid entityFullFromUnescaped(final String unescapedJidString)
    '''
def entityFullFromUnescapedOrNull():
    '''public static EntityFullJid entityFullFromUnescapedOrNull(final CharSequence cs)
    '''
def entityFullFromUrlEncoded():
    '''public static EntityFullJid entityFullFromUrlEncoded(final CharSequence cs)
    '''
def domainBareFromOrThrowUnchecked():
    '''public static DomainBareJid domainBareFromOrThrowUnchecked(final CharSequence cs)
    '''
def domainBareFrom():
    '''public static DomainBareJid domainBareFrom(final CharSequence jid)
    public static DomainBareJid domainBareFrom(final String jid)
    public static DomainBareJid domainBareFrom(final Domainpart domainpart)
    '''
def domainBareFromOrNull():
    '''public static DomainBareJid domainBareFromOrNull(final CharSequence cs)
    '''
def domainBareFromUrlEncoded():
    '''public static DomainBareJid domainBareFromUrlEncoded(final CharSequence cs)
    '''
def domainFullFromOrThrowUnchecked():
    '''public static DomainFullJid domainFullFromOrThrowUnchecked(final CharSequence cs)
    '''
def domainFullFrom():
    '''public static DomainFullJid domainFullFrom(final CharSequence jid)
    public static DomainFullJid domainFullFrom(final String jid)
    public static DomainFullJid domainFullFrom(final Domainpart domainpart, final Resourcepart resource)
    public static DomainFullJid domainFullFrom(final DomainBareJid domainBareJid, final Resourcepart resource)
    '''
def domainFullFromOrNull():
    '''public static DomainFullJid domainFullFromOrNull(final CharSequence cs)
    '''
def domainFullFromUrlEncoded():
    '''public static DomainFullJid domainFullFromUrlEncoded(final CharSequence cs)
    '''
