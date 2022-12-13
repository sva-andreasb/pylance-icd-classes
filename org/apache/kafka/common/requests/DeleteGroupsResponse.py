def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def DeleteGroupsResponse():
'''public DeleteGroupsResponse(final Map<String, Errors> errors)
public DeleteGroupsResponse(final int throttleTimeMs, final Map<String, Errors> errors)
public DeleteGroupsResponse(final Struct struct)
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def errors():
'''public Map<String, Errors> errors()
'''
pass
def hasError():
'''public boolean hasError(final String group)
'''
pass
def get():
'''public Errors get(final String group)
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def parse():
'''public static DeleteGroupsResponse parse(final ByteBuffer buffer, final short version)
'''
pass
