# creates a file in /tmp
file {'/tmp':
  path       => '/tmp/holberton',
  permission => '0774',
  owner      => 'www-data',
  group      => 'www-data',
  content    => 'I love Puppet',
}