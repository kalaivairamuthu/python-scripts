import pandas as pd
import os
 
#file = pandas.read_excel("/home/kalaivani/Downloads/Iron.xlsx")
Sheet_Names = ["heat","mistral"]
for sheets in Sheet_Names:
  df = pd.read_excel('/home/kalaivani/Downloads/Iron.xlsx', sheet_name = sheets)
  kalai=df["url"].tolist()
  print(kalai)
  base_filename = 'harden.yml'
  myfile = open(base_filename, 'w')
  for line in kalai:
    if os.path.exists(base_filename):
      append_write = 'a' # append if already exists
    else:
      append_write = 'w' # make a new file if not

    myfile.write("%s\n" % line)
myfile.close()
#text_file.close()


            
