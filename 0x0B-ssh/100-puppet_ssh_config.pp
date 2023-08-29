# Use puppet to change a configuration file for ssh

include stdlib

file_line {'append_config':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile  ~/.ssh/school',
  ensure => present
  }

file_line {'append_config2':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication  no',
  ensure => present
  }
