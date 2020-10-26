#!/bin/sh
DIR=`dirname $0`
cd $DIR
rules_location="regels/algemeen/"
rule_file="validation_shape_label"
rule_full_path="$rules_location/$rule_file.ttl"
for f in `find ontology -type f -name "*.ttl"`; do 
  echo ""
  echo "validating file: $f"
  f_name_only="$(basename -s .ttl $f)"
  result="validation-output/$f_name_only-$rule_file.ttl"
  java -jar tools/validation/validation-1.0-SNAPSHOT-jar-with-dependencies.jar -t $f -r $rule_full_path -o $result
done
