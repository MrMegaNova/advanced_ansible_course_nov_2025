## Advanced ansible course
advanced_ansible_course Novembre 2025


# Installation avec uv

### Nouveau projet
```(sh)
uv init
uv add ansible ansible-lint
un run ansible-lint --version
```

### Projet existant
```(sh)
uv sync
un run ansible-lint --version
```

# Usefull Links

- [Doc ansible](https://docs.ansible.com/)

- [UV](https://docs.astral.sh/uv/getting-started/installation/)

- [Ansible Realease & maintenance](https://docs.ansible.com/projects/ansible/latest/reference_appendices/release_and_maintenance.html)

- [Doc jinja2](https://jinja.palletsprojects.com/en/stable/nativetypes/#examples)

- [Templating ansible](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_templating.html)

- [Templating Jinja ansible (outdated)](https://docs.ansible.com/projects/ansible/2.9/user_guide/playbooks_templating.html)

- [Ansible var precedence](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_variables.html#ansible-variable-precedence)

- [Ansible inventory](https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_inventory.html)

- [Use ansible filters](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_filters.html)

- [Ansible filters list](https://docs.ansible.com/projects/ansible/2.9/user_guide/playbooks_filters.html)

- [Delegation](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_delegation.html)

- [Block](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_blocks.html)

- [Speed up ansible runtime - mitogen](https://mitogen.networkgenomics.com/ansible_detailed.html)

- [Ansible role](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_reuse_roles.html)

- [Molecule](https://docs.ansible.com/projects/molecule/)

#### Modules: 
- [Module lineinfile](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/lineinfile_module.html)

- [Module apt](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/apt_module.html)

- [Package facts](https://docs.ansible.com/projects/ansible/3/collections/ansible/builtin/package_facts_module.html)