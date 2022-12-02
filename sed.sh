while IFS= read -r line; do sed -i "s/10.18.0.18/app.qa.wus.internal.corestack.io/g" $line; done < /home/kalaivani/conf-files
while IFS= read -r line; do sed -i "s/10.18.0.14/dp.qa.wus.internal.corestack.io/g" $line; done < /home/kalaivani/conf-files 
while IFS= read -r line; do sed -i "s/10.18.0.4/mongodbprimary.qa.wus.internal.corestack.io/g" $line; done < /home/kalaivani/conf-files 
while IFS= read -r line; do sed -i "s/10.18.0.7/mongodbsecondary1.qa.wus.internal.corestack.io/g" $line; done < /home/kalaivani/conf-files
while IFS= read -r line; do sed -i "s/10.18.0.21/mongodbsecondary2.qa.wus.internal.corestack.io/g" $line; done < /home/kalaivani/conf-files
while IFS= read -r line; do sed -i "s/10.18.0.15/policy.qa.wus.internal.corestack.io/g" $line; done < /home/kalaivani/conf-files

