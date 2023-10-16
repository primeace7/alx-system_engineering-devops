#increase open files limit for user holberton

$uri1 = "/bin/sed -i 's/holberton hard nofile [[:digit:]]/holberton hard nofile 150/' /etc/security/limits.conf"
$uri2 = "/bin/sed -i 's/holberton soft nofile [[:digit:]]/holberton soft nofile 140/' /etc/security/limits.conf"

exec {'increase open files hard limit':
  command => $uri1
}

exec {'increase open files soft limit':
  command => $uri2
}
