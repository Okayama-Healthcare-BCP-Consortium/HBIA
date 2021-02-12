# 医療ビジネスインパクト分析システム（Healthcare BIA System）

## Usage

### コードのクローン

以下のコマンドをターミナルで実行して下さい．
```shell
git clone git@github.com:Okayama-Healthcare-BCP-Consortium/HBIA.git
```

### 基準・業務一覧データの準備

<root>/data/input/基準・業務リスト.xlsxに基準と業務一覧を入力してください．

### アンケートの作成

以下のコマンドをターミナルで実行して下さい．
```shell
cd <root>/src/data
python dump_ahp_data.py
```

### アンケートの記入

<root>/data/input/AHPアンケート.xlsxという自動作成されたアンケートに答えてください．

### 階層分析（AHP）

以下のコマンドをターミナルで実行して下さい．
```shell
cd <root>/src/module/
python ahp.py
```

### 結果の場所

<root>/result/AHPによる解析結果.xlsxを開いて確認してください．

## AHP Module Rules

### 重要度ルール

重要度はアンケート中の「○」を指す．

| 尺度 | 重要度 |
| ------------- | ------------- |
| 絶対的  | 9  |
| かなり  | 7  |
| その他  | 5  |
| やや  | 3  |
| 同じ  | 1  |

### Priorityルール

Priorityは最終結果の離散値（1~5）を指す．

1. AHPの総合評価値が高い順に業務をソート
2. ソートされた業務群を均等に5分割
3. 分割された業務群にPriorityをそれぞれつける

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)
