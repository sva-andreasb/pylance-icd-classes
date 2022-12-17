OSLC_PROVIDER_GROUP = "String  \"OSLCPROVIDER\""
OSLC_PROVIDER_PKGDEF = "String  \"OSLCPROVIDER\""
def ():
    '''returns OslcProviderMigrator\n\n
    (final MXTransaction trans, final UserInfo userInfo)\n
    '''
def migrateProvider():
    '''returns None\n\n
    migrateProvider(final String name)\n
    '''
def migrate():
    '''returns None\n\n
    migrate(final String groupName, final String defName, final Map<String, String> whereMap)\n
    '''
def buildChildrenWhereClause():
    '''returns None\n\n
    buildChildrenWhereClause(final String authWhere, final String optionWhere, final String presentWhere)\n
    '''
def setDMWhereClause():
    '''returns None\n\n
    setDMWhereClause(final MboRemote packageDef, final String groupName, final String defName, final Map<String, String> whereMap)\n
    '''
