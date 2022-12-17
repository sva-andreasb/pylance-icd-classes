COMMAND_NODE = "String  \"http://jabber.org/protocol/admin\""
def ():
    '''returns ServiceAdministrationManager\n\n
    (final XMPPConnection connection)\n
    '''
def addUser():
    '''returns None\n\n
    addUser()\n
    addUser(final Jid service)\n
    addUser(final EntityBareJid userJid, final String password)\n
    '''
def deleteUser():
    '''returns None\n\n
    deleteUser()\n
    deleteUser(final Jid service)\n
    deleteUser(final EntityBareJid userJidToDelete)\n
    deleteUser(final Set<EntityBareJid> jidsToDelete)\n
    '''
