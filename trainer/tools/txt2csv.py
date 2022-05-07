import re
import pandas as pd


txt_path = "sample_data/test.txt"
csv_path = "sample_data/test/labels.csv"

data_dict = {
    "filename": [],
    "words": [],
}
with open(txt_path, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        infos = re.split(r'[\t, ]+', line.strip())
        # print(infos)
        ## other operations
        import os
        infos[0] = os.path.basename(infos[0])
        infos[1] = infos[1][1:-1]
        ###################
        data_dict["filename"].append(infos[0])
        data_dict["words"].append(infos[1])

data_pd = pd.DataFrame(data_dict)
data_pd.to_csv(csv_path, index=False)

