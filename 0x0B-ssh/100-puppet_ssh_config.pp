# Puppet manifest for configuring SSH client

include stdlib

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/sshd_config',
  line    => 'PasswordAuthentication no',
  match   => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^\s*IdentityFile.*',
}
