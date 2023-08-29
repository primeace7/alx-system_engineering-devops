# Use puppet to change a configuration file for ssh

include stdlib

  file_line {'ssh_config':
    path     => '/etc/ssh/ssh_config',
    line     => 'IdentityFile = ~/.ssh/school',
    multiple => 'false'
  }

  file_line {'ssh_config2':
    path     => '/etc/ssh/ssh_config',
    line     => 'PasswordAuthentication = no',
    multiple => 'false'
  }
