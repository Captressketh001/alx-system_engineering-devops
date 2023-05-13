# Fix apache 500 internal server error using strace

exec {'500 error fix':
  command   => '/bin/sed',
  arguments => ['-i', 's/phpp/php/g', '/var/www/html/wp-settings.php'],
  path      => '/usr/bin:/bin',
}
