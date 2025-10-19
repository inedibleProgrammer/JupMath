
# Make this script's context its own directory no matter where it is
# called from
cd "$(dirname "${BASH_SOURCE[0]}")"

# Move up a directory
cd ..


docker run \
      --rm \
      -v "$(pwd)":/app \
      -it \
      --privileged \
      --env=DISPLAY \
      pythondummy \
