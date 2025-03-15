for var in `head list.txt`
do
python3 test.py $var >> ../results/result.txt
done
