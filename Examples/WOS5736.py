'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
RMDL: Random Multimodel Deep Learning for Classification

 * Copyright (C) 2018  Kamran Kowsari <kk7nc@virginia.edu>
 * Last Update: 04/25/2018
 * This file is part of  RMDL project, University of Virginia.
 * Free to use, change, share and distribute source code of RMDL
 * Refrenced paper : RMDL: Random Multimodel Deep Learning for Classification
 * Refrenced paper : An Improvement of Data Classification using Random Multimodel Deep Learning (RMDL)
 * Comments and Error: email: kk7nc@virginia.edu
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


import os
import numpy as np
from RMDL import text_feature_extraction as txt
from RMDL.Download import Download_WOS as WOS
from RMDL import RMDL_Text as RMDL
from sklearn.cross_validation import train_test_split
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



if __name__ == "__main__":
    path_WOS = WOS.download_and_extract()
    fname = os.path.join(path_WOS,"WebOfScience/WOS5736/X.txt")
    fnamek = os.path.join(path_WOS,"WebOfScience/WOS5736/Y.txt")
    with open(fname, encoding="utf-8") as f:
        content = f.readlines()
        content = [txt.text_cleaner(x) for x in content]
    with open(fnamek) as fk:
        contentk = fk.readlines()
    contentk = [x.strip() for x in contentk]
    Label = np.matrix(contentk, dtype=int)
    Label = np.transpose(Label)
    np.random.seed(7)
    print(Label.shape)
    X_train, X_test, y_train, y_test = train_test_split(content, Label, test_size=0.2, random_state=42)

    batch_size = 100
    sparse_categorical = 0
    n_epochs = [10, 10, 10]  ## DNN--RNN-CNN
    Random_Deep = [1, 1, 1]  ## DNN--RNN-CNN

    RMDL.Text_Classification(X_train, y_train, X_test, y_test,
                             batch_size=batch_size,
                             sparse_categorical=True,
                             random_deep=Random_Deep,
                             epochs=n_epochs)
