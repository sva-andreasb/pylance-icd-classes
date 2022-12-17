def ():
    '''returns SysDataElementMAXMESSAGES\n\n
    ()\n
    (final String name)\n
    (final String name, final Namespace namespace)\n
    (final String name, final String uri)\n
    (final String name, final String prefix, final String uri)\n
    (final String tbname, final TreeMap newCol, final TreeMap oldCol, final TreeMap newData, final TreeMap oldData, final TreeMap newDataOldKeys, final TreeMap keyCols, final File codefile)\n
    '''
def getDeleteSql():
    '''returns ArrayList\n\n
    getDeleteSql(final String tbname, final Connection con, final Util util, final TreeMap oldCol, final TreeMap keyCols)\n
    '''
def deleteRow():
    '''returns ArrayList<String>\n\n
    deleteRow(final Element row, final TreeMap colsColno)\n
    '''
