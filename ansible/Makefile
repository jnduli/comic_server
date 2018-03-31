ANSIBLE_SUDO = ansible-playbook --ask-become-pass

update:
	$(ANSIBLE_SUDO) updates.yml

setup:
	$(ANSIBLE_SUDO) initial_setup.yml

update_project:
	$(ANSIBLE_SUDO) -i 'jnduli.co.ke,' -u 'rookie' update_project.yml
