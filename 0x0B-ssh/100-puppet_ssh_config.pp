#using Puppet to make changes to our configuration file
include stdlib

file_line {'Turn off passwd auth':
    path => '/etc/ssh/sshd_config',
    line => 'passwordAuthentication no',
    match => '^#?PasswordAuthentication',
}

file_line {'Declare identity file':
    path => '/etc/ssh/sshd_config',
    line => 'IdentityFile ~/.ssh/school',
    match => '^#?IdentityFile',
}
