def ChangesBuilder():
'''public ChangesBuilder()
public ChangesBuilder(final Map data)
'''
pass
def Changes():
'''public JSONArray Changes()
'''
pass
def addDeleted():
'''public JSONObject addDeleted(final String id)
public JSONObject addDeleted(final String id, final boolean newRow)
'''
pass
def addChange():
'''public JSONObject addChange(final String id)
public JSONObject addChange(final String id, final String field, final Object value)
public JSONObject addChange(final String id, final JSONObject change)
'''
pass
def addNewRow():
'''public JSONObject addNewRow(final String id, final JSONObject change)
public JSONObject addNewRow(final String id, final boolean forceNewRow)
public JSONObject addNewRow(final String id)
'''
pass
def findChange():
'''public JSONObject findChange(final String id)
'''
pass
