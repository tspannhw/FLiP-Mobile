bin/pulsar-admin topics create persistent://public/default/transcom

bin/pulsar-admin topics create persistent://public/default/weather

bin/pulsar-admin topics create persistent://public/default/energy

bin/pulsar-admin topics list public/default

bin/pulsar-client consume "persistent://public/default/energy" -s mobile1

python -m SimpleHTTPServer 8000
