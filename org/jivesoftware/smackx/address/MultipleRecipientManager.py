def send():
    '''public static void send(final XMPPConnection connection, final Stanza packet, final Collection<? extends Jid> to, final Collection<? extends Jid> cc, final Collection<? extends Jid> bcc)
    public static void send(final XMPPConnection connection, final Stanza packet, final Collection<? extends Jid> to, final Collection<? extends Jid> cc, final Collection<? extends Jid> bcc, final Jid replyTo, final Jid replyRoom, final boolean noReply)
    '''
def reply():
    '''public static void reply(final XMPPConnection connection, final Message original, final Message reply)
    '''
def getMultipleRecipientInfo():
    '''public static MultipleRecipientInfo getMultipleRecipientInfo(final Stanza packet)
    '''
def toXML():
    '''public CharSequence toXML(final String enclosingNamespace)
    '''
def toString():
    '''public String toString()
    '''
