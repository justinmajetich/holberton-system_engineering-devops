# Fix typo in WordPress settings file
exec { 'Fix typo in filename':
  command  => 'sudo sed -i "137s@.*@require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );@" /var/www/html/wp-settings.php',
  provider => shell,
}
