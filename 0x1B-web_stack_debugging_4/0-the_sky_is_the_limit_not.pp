#fix nginx error 24: too many files open

$uri = "/bin/sed -i \'s/^ULIMIT=\"-n [[:digit:]]\\{2\\}\"/ULIMIT=\"-n 4090\"/\' /etc/default/nginx"
exec {'increase nginx worker_processes files limit':
          command => $uri
}

exec {'restart nginx':
          command => '/usr/sbin/service nginx restart',
          require => Exec['increase nginx worker_processes files limit']
}
