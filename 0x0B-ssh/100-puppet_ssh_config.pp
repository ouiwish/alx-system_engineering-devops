# Define SSH client configuration file path
$ssh_config_file = '/etc/ssh/ssh_config'

# Ensure SSH client configuration is set to use the private key and refuse password authentication
file_line { 'Declare identity file':
  path  => $ssh_config_file,
  line  => '    IdentityFile ~/.ssh/school',
  match => '^#? *IdentityFile',
}

file_line { 'Turn off passwd auth':
  path  => $ssh_config_file,
  line  => '    PasswordAuthentication no',
  match => '^#? *PasswordAuthentication',
}
