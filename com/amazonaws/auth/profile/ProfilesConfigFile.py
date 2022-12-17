AWS_PROFILE_ENVIRONMENT_VARIABLE = "String  \"AWS_PROFILE\""
AWS_PROFILE_SYSTEM_PROPERTY = "String  \"aws.profile\""
DEFAULT_PROFILE_NAME = "String  \"default\""
def ():
    '''returns ProfilesConfigFile\n\n
    ()\n
    (final String filePath)\n
    (final String filePath, final ProfileCredentialsService credentialsService)\n
    (final File file)\n
    (final File file, final ProfileCredentialsService credentialsService)\n
    '''
def getCredentials():
    '''returns AWSCredentials\n\n
    getCredentials(final String profile)\n
    '''
def refresh():
    '''returns None\n\n
    refresh()\n
    '''
