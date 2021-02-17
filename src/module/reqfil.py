import pandas as pd
import numpy as np


def calc(inp_path='./data/input/必要物フィルタのための入力データ.xlsx', ts_v=1):

    sheet2df = pd.read_excel(inp_path, sheet_name=None)

    for sheet, df in sheet2df.items(): 

        if '必要物の現況' == sheet:

            req2score = {row['必要物']: int(row['スコア（十分→2，やや不十分→1，不十分→0）']) for _, row in df.iterrows()}

        else:

            tsk2bool = dict()

            for _, row in df.iterrows():

                scores = [req2score[req] for req in row['必要物'].split(',')]

                if 0 in scores:

                    tsk2bool[row['業務']] = 0

                else:

                    tsk2bool[row['業務']] = 1 if np.mean(scores) >= ts_v else 0

    return tsk2bool