docker run \
      --rm \
      -v "$(pwd)":/app \
      -it \
      --privileged \
      --env=DISPLAY \
      pythondummy \
