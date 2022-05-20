echo "Which tests do you want to run?"
echo "1. Test variables"
echo "2. Test variables in MAINBLOCK"
echo "3. Test variables in MAINBLOCK of imported module"
echo "4. Test blocks"
echo "5. Test imports"
echo "6. Test loops"
echo "7. Test printing in a block"
echo "8. Test function input"
echo "[1-8]/all: "
read ans

declare -a mapping=( ["1"]="variables.bl" ["2"]="variablesmb.bl" ["3"]="variablesimpmb.bl" ["4"]="block.bl" ["5"]="import.bl" ["6"]="loops.bl" ["7"]="prnblk.bl" ["8"]="funcinput.bl" )

> output.txt

if [ "${ans}" != "all" ]; then
	echo "Code and output for ${mapping[${ans}]}:" > output.txt
	python3 ../interpreter.py -s ${mapping[${ans}]} | tee -a output.txt
else
	for i in `seq 8`
	do
		echo "Code and output for ${mapping[${i}]}:" >> output.txt
		python3 ../interpreter.py -s ${mapping[${i}]} | tee -a output.txt
	done
fi
