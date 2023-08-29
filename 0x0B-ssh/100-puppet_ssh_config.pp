# Use puppet to change a configuration file for ssh

exec {'append_config':
  command => "/usr/bin/echo 'IdentityFile = ~/.ssh/school' >> /etc/ssh/ssh_config"
  }

  exec {'append_config2':
    command => "/usr/bin/echo 'PasswordAuthentication = no' >> /etc/ssh/ssh_config"
  }
