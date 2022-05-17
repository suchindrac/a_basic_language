echo "Which tests do you want to run?"
echo "1. Variables"
echo "2. Variables in MAINBLOCK"
echo "3. Blocks"
echo "4. Loops"
echo "5. Setres"
echo "6. Print in Block"
echo "[1-6]/all: "
read ans

declare -a mapping=( ["1"]="variables.bl" ["2"]="variables_mb.bl" ["3"]="block.bl" ["4"]="import.bl" ["5"]="loops.bl" ["6"]="prnblk.bl" )

> output.txt

if [ "${ans}" != "all" ]; then
	echo "Code and output for ${mapping[${ans}]}:" > output.txt
	python3 ../interpreter.py -s ${mapping[${ans}]} | tee -a output.txt
else
	for i in `seq 6`
	do
		echo "Code and output for ${mapping[${i}]}:" >> output.txt
		python3 ../interpreter.py -s ${mapping[${i}]} | tee -a output.txt
	done
fi
