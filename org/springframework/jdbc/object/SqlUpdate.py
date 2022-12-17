def ():
    '''returns SqlUpdate\n\n
    ()\n
    (final DataSource ds, final String sql)\n
    (final DataSource ds, final String sql, final int[] types)\n
    (final DataSource ds, final String sql, final int[] types, final int maxRowsAffected)\n
    '''
def setMaxRowsAffected():
    '''returns None\n\n
    setMaxRowsAffected(final int maxRowsAffected)\n
    '''
def setRequiredRowsAffected():
    '''returns None\n\n
    setRequiredRowsAffected(final int requiredRowsAffected)\n
    '''
def update():
    '''returns int\n\n
    update(final Object[] args)\n
    update(final Object[] args, final KeyHolder generatedKeyHolder)\n
    update()\n
    update(final int p1)\n
    update(final int p1, final int p2)\n
    update(final long p1)\n
    update(final long p1, final long p2)\n
    update(final String p)\n
    update(final String p1, final String p2)\n
    '''
