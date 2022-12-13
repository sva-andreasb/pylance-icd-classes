AWS_PROFILE_ENVIRONMENT_VARIABLE = "String  AWS_PROFILE""
AWS_PROFILE_SYSTEM_PROPERTY = "String  aws.profile""
DEFAULT_PROFILE_NAME = "String  default""
def ProfilesConfigFile():
'''public ProfilesConfigFile()
public ProfilesConfigFile(final String filePath)
public ProfilesConfigFile(final String filePath, final ProfileCredentialsService credentialsService)
public ProfilesConfigFile(final File file)
public ProfilesConfigFile(final File file, final ProfileCredentialsService credentialsService)
'''
pass
def getCredentials():
'''public AWSCredentials getCredentials(final String profile)
'''
pass
def refresh():
'''public void refresh()
'''
pass
def getAllProfiles():
'''public Map<String, Profile> getAllProfiles()
'''
pass
