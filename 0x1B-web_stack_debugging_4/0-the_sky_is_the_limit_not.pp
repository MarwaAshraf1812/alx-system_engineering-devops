# Fix NGINX to accept and serve more requests

#increase the ULIMIT of the default file
exec { 'fix nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
}

exec { 'restart nginx':
  command => 'sudo service nginx restart',
  path    => ['/etc/init.d'],
}
