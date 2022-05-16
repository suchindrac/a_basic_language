echo "Output of first script:" > output.txt
python3 interpreter.py -s test/script.bl | tee output.txt
echo "Output of second script:" >> output.txt
python3 interpreter.py -s test/blk.bl | tee -a output.txt
