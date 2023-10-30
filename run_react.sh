#!/bin/bash
port=3000
host=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}')
project_dir=$(pwd)/front

# Change to the project directory
cd $project_dir

# Check if a process is running on the port
if [[ $(lsof -i :$port) ]]; then
  echo "Killing processes running on port $port"
  # Kill processes running on the port
  kill $(lsof -t -i :$port)
fi

# Check if react-scripts is installed globally
if ! npm list -g react-scripts > /dev/null; then
  echo "react-scripts is not installed globally. Installing it locally..."
  npm install react-scripts
fi

# Start React on the specified port and host
echo "Starting React on port $port and host $host"
npm start --port $port --host $host
