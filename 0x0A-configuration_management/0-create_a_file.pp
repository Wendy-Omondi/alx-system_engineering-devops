# creates a file in /tmp
file {'holberton':
  ensure  => 'present'
  path    => '/tmp/holberton',
  mode    => '0774',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}