#!/bin/sh
for f in `find ontology -type f -name "*.ttl"`; do 
  echo "ReSerializing file: $f"
  tools/ReSerialize/bin/ReSerialize -f $f -r
done
