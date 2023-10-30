#!/bin/bash
port=8000
project_dir=$(pwd)

echo "project_dir: $project_dir"

# Change to the project directory
cd $project_dir

# Extract the first IP address and start Django on the specified port
ip_address=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -n 1)
if [ -n "$ip_address" ]; then
  # Check if a process is running on the port
  if [[ $(lsof -i :$port) ]]; then
    echo "Killing processes running on port $port"
    # Kill processes running on the port
    kill $(lsof -t -i :$port)
  fi

  # Start Django on the specified IP address and port
  echo "Starting Django on IP address $ip_address, port $port"
  python3 manage.py runserver $ip_address:$port
else
  echo "No valid IP address found for Django."
fi
