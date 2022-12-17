INTERACTION_OBJECT_GROUP = "String  \"INTERACTION_OBJ\""
INTERACTION_INT_GROUP = "String  \"INTERACTION_INT\""
INTERACTION_OBJECT_PKGDEF = "String  \"INTERACTION_OBJ\""
INTERACTION_INT_PKGDEF = "String  \"INTERACTION_INT\""
def ():
    '''returns InteractionMigrator\n\n
    (final String name, final MXTransaction trans, final UserInfo userInfo)\n
    '''
def migrateInteraction():
    '''returns None\n\n
    migrateInteraction()\n
    '''
def migrate():
    '''returns None\n\n
    migrate(final String groupName, final String defName, final Map<String, String> whereMap)\n
    '''
def setDMWhereClause():
    '''returns None\n\n
    setDMWhereClause(final MboRemote packageDef, final String groupName, final String defName, final Map<String, String> whereMap)\n
    '''
def breakRelationWhere():
    '''returns List<String>\n\n
    breakRelationWhere(final String where, final int maxLength, final List<String> allWheres)\n
    '''
def breakObjectWhere():
    '''returns List<String>\n\n
    breakObjectWhere(final String where, final int maxLength, final List<String> allWheres)\n
    '''
