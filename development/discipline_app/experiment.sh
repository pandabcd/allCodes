# I am sorry for commenting on every line but I am a shell noob and dont want take chances for future.

field_arr=()
											
export IFS=","										# Specifying the delimiter
while  read -r line || [[ -n "$line" ]]; do    		# [[-n "$line"]] used to read from the last line
    read -ra vals <<< "$line";						#Converts $line to array called vals(has one line from the csv)
    index=${vals[0]};								# Meta.csv has format index,field,check frequency, next check(date)
    field=${vals[1]};
    freq=${vals[2]};
    next_check=${vals[3]};
    
    field_arr+=($field)								#Creating an array of all the fields
    # echo "Enter input for $field!"
    # read -e value;
    # echo "Value entered = $value";
done < $TEMP/data/Meta.csv

# Deleting previous content if any(or creating an empty file)
echo "Creating empty log file for today..."
echo
echo -n > $TEMP/last_log.txt

# Give an option of changing the entered values
# Reading value for all the fields
len=${#field_arr[@]};
for (( i=1; i<$len; i++ )); do 
	echo "Enter value for: ${field_arr[$i]}" ; 
	read value
	echo "${field_arr[$i]},$value">>$TEMP/last_log.txt
done

echo "Log file for today updated"
echo "Updating main log file now..."
echo

# python $TEMP/update_log.py