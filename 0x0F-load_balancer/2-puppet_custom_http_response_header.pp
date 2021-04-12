# custom HTTP header response, but with Puppet.
exec { 'http':
  command  => 'sudo apt-get update 
              && sudo apt-get -y install nginx
              && var="add_header X-Served-By: $HOSTNAME"
              && sudo sed -i "50i$var" /etc/nginx/sites-available/default
              && sudo service nginx start',
  provider => shell
}
