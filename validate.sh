#!/bin/sh
DIR=`dirname $0`
cd $DIR
if [ "$1" == "--help" ]; then
  echo "Without arguments it will validate all rulesets against all files in ontology folder"
  echo "With one argument that argument will be used as a filter for the files in ontology folder"
  echo "With two arguments the second argument will be used as a filter for the rulesets"
  echo "PUT FILTERS IN \"\""
  echo "Example: validate.sh \"*otl*\" \"*label*\" "
  exit
fi
file_filter=$1
rule_filter=$2
if [ "$file_filter" == "" ]; then
  file_filter="*"
fi
if [ "$rule_filter" == "" ]; then
  rule_filter="*"
fi
echo "Files: $file_filter"
echo "Rulesets: $rule_filter"
validation_output_folder="validation-output"
rm -f $validation_output_folder/*
for rule_file in `find regels -type f -name "$rule_filter.ttl"`; do 
  rule_file_name_only="$(basename -s .ttl $rule_file)"
  echo ""
  echo "----------------- ruleset: $rule_file --------------------------"
  for f in `find ontology -type f -name "$file_filter.ttl"`; do 
    echo ""
    echo "validating file: $f"
    f_name_only="$(basename -s .ttl $f)"
    result="$validation_output_folder/$f_name_only-$rule_file_name_only.ttl"
    java -jar tools/validation/validation-1.0-SNAPSHOT-jar-with-dependencies.jar -t $f -r $rule_file -o $result
  done
done
