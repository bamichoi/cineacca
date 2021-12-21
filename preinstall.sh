if [ "$CREDENTIALS" != "" ]; then


echo "Detected credentials. Adding credentials" >&1
  echo "" >&1

  # Ensure we have an gcp folder
  if [ ! -d ./.gcp ]; then
    mkdir -p ./.gcp
    chmod 700 ./.gcp
  fi

  # Load the private key into a file.
  echo $GCP_CREDENTIALS | base64 --decode > ./.gcp/key.json

  # Change the permissions on the file to
  # be read-only for this user.
  chmod 400 ./.gcp/key.json
fi