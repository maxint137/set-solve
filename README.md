# set-solve
Find a set


### How to use X
 1. `open -a XQuartz`
 1. `lsof -i TCP:6000`
 1. `socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\" & lsof -i TCP:6000`

 In the container:
 1. `export DISPLAY=docker.for.mac.host.internal:0`


as shown in https://stackoverflow.com/a/53548183/494308
