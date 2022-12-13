COMMAND_NODE = "String  http://jabber.org/protocol/admin""
def getInstanceFor():
'''public static synchronized ServiceAdministrationManager getInstanceFor(final XMPPConnection connection)
'''
pass
def ServiceAdministrationManager():
'''public ServiceAdministrationManager(final XMPPConnection connection)
'''
pass
def addUser():
'''public RemoteCommand addUser()
public RemoteCommand addUser(final Jid service)
public void addUser(final EntityBareJid userJid, final String password)
'''
pass
def deleteUser():
'''public RemoteCommand deleteUser()
public RemoteCommand deleteUser(final Jid service)
public void deleteUser(final EntityBareJid userJidToDelete)
public void deleteUser(final Set<EntityBareJid> jidsToDelete)
'''
pass
