#!/bin/sh
DIR=`dirname $0`
cd $DIR
if [ "$1" == "--help" ]; then
  echo "Without arguments it will reserialize all files in ontology folder"
  echo "With argument that argument will be used as a filter for the files in ontology folder"
  echo "PUT FILTERS IN \"\""
  echo "Example: reserialize.sh \"*otl*\" "
  exit
fi
file_filter=$1
if [ "$file_filter" == "" ]; then
  file_filter="*"
fi
echo "File filter: $file_filter"
for f in `find ontology -type f -name "$file_filter.ttl"`; do 
  echo "ReSerializing file: $f"
  tools/ReSerialize/bin/ReSerialize -f $f -r
  if [ $? -gt 0 ]; then
    echo "> Modified file: $f"
  fi
done
