#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
import random
import string

DOCUMENTATION = r'''
---
module: password_generator
short_description: Génère un mot de passe aléatoire
description:
  - Génère un mot de passe aléatoire avec les options spécifiées.
options:
  chars:
    description:
      - Type de caractères à utiliser.
      - Choix possibles : num, alpha, alphanum, special
    type: str
    default: special
  length:
    description:
      - Longueur du mot de passe (entre 1 et 100).
    type: int
    default: 20
  var_name:
    description:
      - Nom de la variable dans laquelle enregistrer le mot de passe.
    type: str
    required: false
'''

EXAMPLES = r'''
- name: Générer un mot de passe spécial de 28 caractères
  password_generator:
    chars: special
    length: 28
'''

def generate_password(chars, length):
    if chars == "num":
        char_set = string.digits
    elif chars == "alpha":
        char_set = string.ascii_letters
    elif chars == "alphanum":
        char_set = string.ascii_letters + string.digits
    elif chars == "special":
        char_set = string.ascii_letters + string.digits + string.punctuation
    else:
        return None

    return ''.join(random.choice(char_set) for _ in range(length))

def main():
    module = AnsibleModule(
        argument_spec=dict(
            chars=dict(type='str', default='special', choices=['num', 'alpha', 'alphanum', 'special']),
            length=dict(type='int', default=20),
            var_name=dict(type='str', required=False),
        ),
        supports_check_mode=True,
    )

    chars = module.params['chars']
    length = module.params['length']
    var_name = module.params.get('var_name')

    if length < 1 or length > 100:
        module.fail_json(msg="La longueur doit être comprise entre 1 et 100.")

    password = generate_password(chars, length)

    result = dict(
        changed=True,
        password=password,
    )

    if var_name:
        result[var_name] = password

    module.exit_json(**result)

if __name__ == '__main__':
    main()
