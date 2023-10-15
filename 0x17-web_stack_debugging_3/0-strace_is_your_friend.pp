# Manifest to fix 500 server error in a wordpress site

exec {'fix wordpress':
  command => "/bin/sed -i 's/**.phpp/.php/' /var/www/html/wp-settings.php"
}
