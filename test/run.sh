echo "Output of script 1:" > output.txt
python3 ../interpreter.py -s script.bl | tee output.txt
echo "Output of script 2:" >> output.txt
python3 ../interpreter.py -s blk.bl | tee -a output.txt
echo "Output of script 3:" >> output.txt
python3 ../interpreter.py -s import.bl | tee -a output.txt
echo "Output of script 4:" >> output.txt
python3 ../interpreter.py -s setres.bl | tee -a output.txt
echo "Output of script 5:" >> output.txt
python3 ../interpreter.py -s prnblk.bl | tee -a output.txt
echo -n -e "NEW <# print abcd #>\r\nexec NEW" | python3 ../command_line.py 2>/dev/null | tee output.txt
