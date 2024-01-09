# 1-install_a_package.pp

# Install Flask using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
