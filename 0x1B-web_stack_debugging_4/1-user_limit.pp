# change system wide limits
exec { 'Change nginx limit':
  command  => 'sudo sed "55 i holberton\tsoft\tnofile\t10048\nholberton\thard\tnofile\t30048" /etc/security/limits.conf && sudo sed -i "$ a\fs.file-max = 100000" /etc/sysctl.conf && sudo sed -i "s/^ULIMIT.*$/ULIMIT=\"-n 4096\"/" /etc/default/nginx && sudo sysctl -p && sudo service nginx restart',
  provider => shell,
}
