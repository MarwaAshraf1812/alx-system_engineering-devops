# Setup New Ubuntu server with nginx

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

exec { 'redirect_me':
  command => 'sed -i "24i\ rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  require => Package['nginx'],
  path    => ['/bin', '/usr/bin'],
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
