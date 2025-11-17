#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os

def main():
    module = AnsibleModule(
        argument_spec={
            'path': {'type': 'str', 'required': True}
        }
    )

    path = module.params['path']

    # Vérification de l'existence du fichier
    if os.path.exists(path):
        module.exit_json(changed=False, msg=f"Le fichier {path} existe.")
    else:
        module.fail_json(msg=f"Le fichier {path} n'existe pas.")

if __name__ == '__main__':
    main()
