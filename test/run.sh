echo "Which tests do you want to run?"
echo "1. Variables"
echo "2. Variables in MAINBLOCK"
echo "3. Variables in MAINBLOCK of imported module"
echo "4. Blocks"
echo "5. Loops"
echo "6. Setres"
echo "7. Print in Block"
echo "[1-7]/all: "
read ans

declare -a mapping=( ["1"]="variables.bl" ["2"]="variablesmb.bl" ["3"]="variablesimpmb.bl" ["4"]="block.bl" ["5"]="import.bl" ["6"]="loops.bl" ["7"]="prnblk.bl" )

> output.txt

if [ "${ans}" != "all" ]; then
	echo "Code and output for ${mapping[${ans}]}:" > output.txt
	python3 ../interpreter.py -s ${mapping[${ans}]} | tee -a output.txt
else
	for i in `seq 7`
	do
		echo "Code and output for ${mapping[${i}]}:" >> output.txt
		python3 ../interpreter.py -s ${mapping[${i}]} | tee -a output.txt
	done
fi
