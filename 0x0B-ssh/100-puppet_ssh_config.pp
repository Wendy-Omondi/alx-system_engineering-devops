#!/usr/bin/env bash
#sets up your client SSH configuration file so that you can connect to a server without typing a password.

file_line {'USE priivate key':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line {'TURN OFF Password Auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
