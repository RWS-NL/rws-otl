#!/bin/sh
DIR=`dirname $0`
cd $DIR
target="ontology/otl/brug.ttl"
rules="regels/algemeen/validation_shape_label.ttl"
result="validation-output/brug-report.tt"
java -jar tools/validation/validation-1.0-SNAPSHOT-jar-with-dependencies.jar -t $target -r $rules -o $result
