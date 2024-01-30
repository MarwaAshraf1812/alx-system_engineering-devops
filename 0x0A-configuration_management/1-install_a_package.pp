# installs the flask package 

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command  => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  provider => 'shell',
  require  => Package['python3-pip'],
}
