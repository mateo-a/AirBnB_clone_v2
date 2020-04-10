# Task #0 but by using Puppet
exec { 'apt-get':
  command => 'sudo sudo apt-get -y update; sudo apt-get -y install nginx',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'mkdir-shared':
  require => Exec['apt-get'],
  command => 'sudo mkdir -p /data/web_static/shared/',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'mkdir-releases':
  require => Exec['mkdir-shared'],
  command => 'sudo mkdir -p /data/web_static/releases/test/',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'echo':
  require => Exec['mkdir-releases'],
  command => 'echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html > /dev/null',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'link':
  require => Exec['echo'],
  command => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
  returns => [0,1]
}

exec { 'chown':
  require => Exec['link'],
  command => 'sudo chown -R ubuntu:ubuntu /data/',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
  returns => [0,1]
}

exec { 'sed':
  require     => Exec['chown'],
  command     => 'sudo sed -i "38i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n" /etc/nginx/sites-available/default',
  path        => ['/usr/bin', '/bin'],
  returns     => [0,1]
}

exec { 'nginx-restart':
  require => Exec['sed'],
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
  returns => [0,1]
}
