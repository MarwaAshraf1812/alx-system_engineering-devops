# Puppet manifest for configuring SSH client

include stdlib

file_line { 'Turn off passwd auth':
  ensure => present,
  path    => '/etc/ssh/sshd_config',
  line    => 'PasswordAuthentication no',
  match   => '^#?PasswordAuthentication',
  replace => true,
}

file_line { 'Declare identity file':
  ensure => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
  replace => true,
}
