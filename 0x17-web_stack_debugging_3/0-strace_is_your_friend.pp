# Manifest to fix 500 server error in a wordpress site

exec {'enable wordpress':
  command => 'sudo a2ensite wordpress'
}

exec {'enable URL rewriting':
  command => 'sudo a2enmod rewrite'
}

exec{'restart apache':
  command => 'sudo service apache2 restart'
  }
