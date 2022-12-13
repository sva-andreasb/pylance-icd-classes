INTERACTION_OBJECT_GROUP = "String  INTERACTION_OBJ""
INTERACTION_INT_GROUP = "String  INTERACTION_INT""
INTERACTION_OBJECT_PKGDEF = "String  INTERACTION_OBJ""
INTERACTION_INT_PKGDEF = "String  INTERACTION_INT""
def InteractionMigrator():
'''public InteractionMigrator(final String name, final MXTransaction trans, final UserInfo userInfo)
'''
pass
def migrateInteraction():
'''public void migrateInteraction()
'''
pass
def migrate():
'''public void migrate(final String groupName, final String defName, final Map<String, String> whereMap)
'''
pass
def buildObjectDMWhereList():
'''public List<Map<String, String>> buildObjectDMWhereList()
'''
pass
def buildIntDMWhereClause():
'''public Map<String, String> buildIntDMWhereClause()
'''
pass
def buildChildrenWhereClause():
'''public Map<String, Map<String, String>> buildChildrenWhereClause()
'''
pass
def setDMWhereClause():
'''public void setDMWhereClause(final MboRemote packageDef, final String groupName, final String defName, final Map<String, String> whereMap)
'''
pass
def breakRelationWhere():
'''public List<String> breakRelationWhere(final String where, final int maxLength, final List<String> allWheres)
'''
pass
def breakObjectWhere():
'''public List<String> breakObjectWhere(final String where, final int maxLength, final List<String> allWheres)
'''
pass
def buildCombineWhere():
'''public List<Map<String, String>> buildCombineWhere(final List<String> domainWhere, final List<String> objectWhere, final List<String> relationWhere, final String intObjectWhere)
'''
pass
