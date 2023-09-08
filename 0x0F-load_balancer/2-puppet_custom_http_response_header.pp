# configure Nginx server to display custom HTTP header

$old_line = "root \/var\/www\/html;"
$new_line = "$old_line\n\n\tadd_header X-Served-By "
$file_path = "/ALX_SE/alx-system_engineering-devops/0x0F-load_balancer/test"

exec { 'capture_host':
  command     => "host=$(/usr/bin/hostname) && sed 's/$old_line/$new_line$host/' $file_path",
  logoutput   => true,
  path        => '/usr/bin/sed'
}

#file_line {'add custom header':
#  line  => "\n\t#Add custom HTTP header\n\tadd_header X-Served-By $host",
#  after => 'root \/var\/www\/html;',
#path => '/ALX_SE/alx-system_engineering-devops/0x0F-load_balancer/test',
#  require => Exec['capture_host']
#}
