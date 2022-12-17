def ():
    '''returns CciTemplate\n\n
    ()\n
    (final ConnectionFactory connectionFactory)\n
    '''
def setConnectionFactory():
    '''returns None\n\n
    setConnectionFactory(final ConnectionFactory connectionFactory)\n
    '''
def getConnectionFactory():
    '''returns ConnectionFactory\n\n
    getConnectionFactory()\n
    '''
def setOutputRecordCreator():
    '''returns None\n\n
    setOutputRecordCreator(final RecordCreator creator)\n
    '''
def getOutputRecordCreator():
    '''returns RecordCreator\n\n
    getOutputRecordCreator()\n
    '''
def afterPropertiesSet():
    '''returns None\n\n
    afterPropertiesSet()\n
    '''
def execute():
    '''returns Object\n\n
    execute(final ConnectionCallback action)\n
    execute(final InteractionCallback action)\n
    execute(final InteractionSpec spec, final Record inputRecord)\n
    execute(final InteractionSpec spec, final Record inputRecord, final Record outputRecord)\n
    execute(final InteractionSpec spec, final RecordCreator inputCreator)\n
    execute(final InteractionSpec spec, final Record inputRecord, final RecordExtractor outputExtractor)\n
    execute(final InteractionSpec spec, final RecordCreator inputCreator, final RecordExtractor outputExtractor)\n
    '''
def doInConnection():
    '''returns Object\n\n
    doInConnection(final Connection connection, final ConnectionFactory connectionFactory)\n
    '''
def doInInteraction():
    '''returns Object\n\n
    doInInteraction(final Interaction interaction, final ConnectionFactory connectionFactory)\n
    '''
def createIndexedRecord():
    '''returns IndexedRecord\n\n
    createIndexedRecord(final String name)\n
    '''
def createMappedRecord():
    '''returns MappedRecord\n\n
    createMappedRecord(final String name)\n
    '''
