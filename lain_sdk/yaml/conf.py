from lain_sdk.yaml.lain_user_config import LainUserConfig

DOCKER_APP_ROOT = '/lain/app'

user_config = LainUserConfig.create()
etc = user_config.get_config()

PRIVATE_REGISTRY = None if etc is None else etc.get(
    'private_docker_registry', None)
DOMAIN = None if not etc else etc.get('domain', 'lain.local')
