# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2204"
  config.vm.provider "libvirt" do |hv|
    hv.cpus = "2"
    hv.memory = "2048"
  end
  config.vm.synced_folder '.', '/vagrant', disabled: true

  config.vm.define "node1" do |node1|
    node1.vm.hostname = "node1"
  end
  config.vm.define "node2" do |node2|
    node2.vm.hostname = "node2"
  end
  config.vm.define "node3" do |node3|
    node3.vm.hostname = "node3"
    node3.vm.box = "debian/bookworm64"
  end
  config.vm.provision :ansible do |ansible|
    # Disable default limit to connect to all the machines
    ansible.limit = "all"
    ansible.playbook = "set_ssh_key.yml"
  end

end
