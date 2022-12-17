def ():
    '''returns ChangesBuilder\n\n
    ()\n
    (final Map data)\n
    '''
def Changes():
    '''returns JSONArray\n\n
    Changes()\n
    '''
def addDeleted():
    '''returns JSONObject\n\n
    addDeleted(final String id)\n
    addDeleted(final String id, final boolean newRow)\n
    '''
def addChange():
    '''returns JSONObject\n\n
    addChange(final String id)\n
    addChange(final String id, final String field, final Object value)\n
    addChange(final String id, final JSONObject change)\n
    '''
def addNewRow():
    '''returns JSONObject\n\n
    addNewRow(final String id, final JSONObject change)\n
    addNewRow(final String id, final boolean forceNewRow)\n
    addNewRow(final String id)\n
    '''
def findChange():
    '''returns JSONObject\n\n
    findChange(final String id)\n
    '''
