COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloScenarioUpdateSessionImpl\n\n
    ()\n
    (final IloSessionSchemaRowMap inserted, final IloSessionSchemaRowMap changed, final IloSessionSchemaRowMap deleted, final Collection<IloSchema> all_deleted_tables)\n
    '''
def markAllDeleted():
    '''returns None\n\n
    markAllDeleted(final IloSchema schema)\n
    '''
def unmarkAllDeleted():
    '''returns None\n\n
    unmarkAllDeleted(final IloSchema schema)\n
    '''
def isAllDeleted():
    '''returns boolean\n\n
    isAllDeleted(final IloSchema schema)\n
    '''
def isDeleted():
    '''returns boolean\n\n
    isDeleted(final IloSchema schema, final Long row_id)\n
    '''
def pendingUpdates():
    '''returns boolean\n\n
    pendingUpdates()\n
    pendingUpdates(final IloSchema schema)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def attachAllDeleted():
    '''returns None\n\n
    attachAllDeleted(final Collection<IloSchema> schemas)\n
    '''
def detachAllDeleted():
    '''returns Set<IloSchema>\n\n
    detachAllDeleted()\n
    '''
