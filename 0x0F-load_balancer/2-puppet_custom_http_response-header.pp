# Configures a custom response header
include stdlib

file_line { 'custom response header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => '        error_page 404 /custom_404.html;',
  line   => "        add_header X-Served-By ${hostname};",
}
