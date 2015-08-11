import os

secrets_list = [
    'ONENAME_API_ID', 'ONENAME_API_SECRET'
]

for env_variable in os.environ:
    if env_variable in secrets_list:
        env_value = os.environ[env_variable]
        exec(env_variable + " = \"\"\"" + env_value + "\"\"\"")
