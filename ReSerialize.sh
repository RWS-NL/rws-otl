#!/bin/sh

for f in ontology/*.ttl; do
    echo "ReSerializing file: $f"
    tools/ReSerialize/bin/ReSerialize -f $f -r
    if [ $? -gt 0 ]; then
        echo "> Modified file: $f"
    fi
done
