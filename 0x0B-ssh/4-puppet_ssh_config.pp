# Modify client config file
file_line { "/etc/ssh/ssh_config":
  ensure => present,
  line   => 'PasswordAuthentication no'
}

file_line { "/etc/ssh/ssh_config":
  ensure => present
  line   => 'IdentityFile ~/.ssh/holberton'
}
