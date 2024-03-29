# install and configure and nginx webserver

  exec {'update package repo':
    command => '/usr/bin/apt update' }

  package {'nginx':
    ensure => installed }

  file {'/var/www/html/index.html':
    ensure  => present,
    content => "Hello World!\n" }

  service {'nginx':
    ensure => running }

  file_line {'enable redirect':
    path  => '/etc/nginx/sites-available/default',
    line  => "\n\tlocation /redirect_me {\n\t\treturn 301 https://youtube.com;\n\t}\n",
    after => 'root\s+/var/www/html;' }

  exec {'restart nginx':
    command => '/usr/sbin/service nginx restart' }
