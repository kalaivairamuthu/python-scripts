while IFS= read -r line; do sed -i "s/strg/chgstrg/g" $line; done < <file psth to chnage>
while IFS= read -r line; do sed -i "s/string/chnage_strg/g" $line; done < <conf-files(list of files to change)> 
