#fix nginx error 24: too many files open by increasing nginx worker_preocesses limit to 1000
exec {'increase nginx worker_processes':
          command => "/bin/sed -i 's/^worker_processes[[:space:]]4;$/worker_processes 1000;/' /etc/nginx/nginx.conf"
}

exec {'restart nginx':
  command => '/usr/sbin/service nginx restart'
  }
