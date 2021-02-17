import pandas as pd
from src.module import ahp, reqfil


if __name__ == '__main__':

    tsk2prio = ahp.calc()
    tsk2bool = reqfil.calc()

    tsks = list(pd.read_excel('./data/input/基準・業務・必要物リスト.xlsx')['業務一覧'].dropna())
    df = pd.DataFrame({
        '業務名': tsks,
        'Priority': [tsk2prio[tsk] for tsk in tsks],
        '可否（可→1，否→0）': [tsk2bool[tsk] for tsk in tsks],
    })
    print(df)
    df.to_excel('./data/result/AHP・必要物フィルタによる解析結果.xlsx')