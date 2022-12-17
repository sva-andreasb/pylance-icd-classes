MaxProjectNamesInGroup = "int  10"
MaxGroupNamesInCall = "int  5"
versionManifestEntry = "String  \"Schema-Version\""
appNameManifestEntry = "String  \"Application-Name\""
appVersionManifestEntry = "String  \"Application-Version\""
def ():
    '''returns RowIteratorProviderByGroup\n\n
    (final Connection connection, final String s, final String s2, final String s3, final OutputStream outputStream)\n
    (final Connection connection, final String schema, final String s, final String s2, final OutputStream os, TableFormatter formatter)\n
    (final Connection c, final String p11, final String p12, final String p13, final String p14, final String p15, final String p16, final String p17, final String p18, final String p19, final String p20)\n
    (final Connection c, final String g1, final String v1, final String g2, final String v2, final String g3, final String v3, final String g4, final String v4, final String g5, final String v5)\n
    '''
def export():
    '''returns None\n\n
    export(final String[] array)\n
    '''
def exportRuntimeGroups():
    '''returns None\n\n
    exportRuntimeGroups(final List<String> list, final List<String> list2)\n
    '''
def getIteratorFor():
    '''returns RowIterator\n\n
    getIteratorFor(final ExportTable exportTable)\n
    getIteratorFor(final ExportTable exportTable)\n
    '''
