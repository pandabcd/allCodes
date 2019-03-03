# export IFS=","
# while  read -r line || [[ -n "$line" ]]; do
#     # echo "Text read from file: $line"
#     for i in $line;
#     	do echo $i;
#     done
#     echo ;
# done < data/Meta.csv

# I am sorry for commenting on every line but I am a shell noob and dont want take chances for future.

field_arr=()
											
export IFS=","										# Specifying the delimiter
while  read -r line || [[ -n "$line" ]]; do    		# [[-n "$line"]] used to read from the last line
    read -ra vals <<< "$line";						#Converts $line to array called vals(has one line from the csv)
    index=${vals[0]};								# Meta.csv has format index,field,check frequency, next check(date)
    field=${vals[1]};
    freq=${vals[2]};
    next_check=${vals[3]};
    
    field_arr+=($field)
    # echo "Enter input for $field!"
    # read -e value;
    # echo "Value entered = $value";
done < data/Meta.csv

len=${#field_arr[@]};

echo $len;
for (( i=0; i<$len; i++ )); do 
	echo "Enter value for: ${field_arr[$i]}" ; 
done

# echo ${field_arr[0]};
# echo ${field_arr[1]};
# echo ${field_arr[2]};
# echo ${field_arr[3]};

# for val in field_arr;do
# 	echo "$val";
# done
