# Using Puppet, install flask from pip3

exec {'install flask':
  command => '/usr/bin/pip3 install python3-flask=2.1.0'
  }
