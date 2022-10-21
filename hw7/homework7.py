## Homework7
import re

## [a-zA-Z0-9]

string = 'S123_Miami_hostname1_filer_FC1, S14_Tampa_hostname2_switch_FC4, S3991_Boston_hostname3_windows2K_FC0, S44_Raleigh_hostname4_solaris_FC1'
result = re.findall(r"\w", string)
print(result)