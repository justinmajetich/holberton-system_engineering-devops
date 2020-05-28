exec { 'Change nginx limit':
  command  => 'sudo sed -i "s/^ULIMIT.*$/ULIMIT=\"-n 4096\"/" /etc/default/nginx; sudo service nginx restart',
  provider => shell,
}
