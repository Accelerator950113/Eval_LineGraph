i=1
one=""
two=""
for var in `cat SandiAuths.txt`
do
    if [ $i == 1 ]
    then
        one=$var
        i=2
    elif [ $i == 2 ]
    then
        two=$var
        i=3
    elif [ $i == 3 ]
    then
        echo $one $two >> output.txt
        i=1
    fi
done