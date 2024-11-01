from ansible.module_utils.basic import AnsibleModule

import sys
import time
import jwt

# @see https://medium.com/@mj.vishweshwaran/custom-module-ansible-fcdeb9b48a0c
def main():
    parameters = {
        'client_id': {"required": True, "type": 'str'},
        'client_secret': {"required": True, "type": 'str'},
        'signing_key': {"required": True, "type": 'str'},
    }

    module = AnsibleModule(argument_spec=parameters)

    client_id = module.params['client_id']
    client_secret = module.params['client_secret']
    signing_key = module.params['signing_key']

    # @see https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-json-web-token-jwt-for-a-github-app#example-using-python-to-generate-a-jwt
    #with open(pem, 'rb') as pem_file:
    #    signing_key = pem_file.read()

    payload = {
        # Issued at time
        'iat': int(time.time()),
        # JWT expiration time (10 minutes maximum)
        'exp': int(time.time()) + 600,

        # GitHub App's client ID
        'iss': client_id
    }

    # Create JWT
    encoded_jwt = jwt.encode(payload, signing_key, algorithm='RS256')

    output = {
        'token': encoded_jwt
    }

    module.exit_json(changed=False, **output)

if __name__ == '__main__':
    main()