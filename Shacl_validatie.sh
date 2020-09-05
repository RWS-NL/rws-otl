#!/bin/sh

for f in ontology/shacl/*.ttl; do
    echo "Valdiation f: $f"
    Filename=$(basename $f .ttl)
    echo "Validation filename: $Filename"
    output=$(tools/apache-jena/bin/shacl v -d $f -s ./shacl/validation_shape_label.ttl --text)
    echo "output: $output"
    if [$output="Conforms"]; then
    		echo "Validation file $f SUCCEEDED"
    	else
    		echo "Validation file $f FAILED"
    		tailfilename="_validation_shape_def_label.rdf"
    		headfilename="./output/$Filename"
    		outputfilename="${headfilename}${tailfilename}"
    		touch $outputfilename
    		#echo "outputfile: $outputfilename"
    		echo $output | tee $outputfilename
    	fi
done
