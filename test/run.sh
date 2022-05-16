echo "Output of first script:" > output.txt
python3 ../interpreter.py -s script.bl | tee output.txt
echo "Output of second script:" >> output.txt
python3 ../interpreter.py -s blk.bl | tee -a output.txt
echo "Output of third script:" >> output.txt
python3 ../interpreter.py -s import.bl | tee -a output.txt
