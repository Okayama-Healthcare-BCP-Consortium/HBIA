# 医療ビジネスインパクト分析システム（Healthcare BIA System）

## Usage

### コードのクローン

以下のコマンドをターミナルで実行して下さい．
```shell
git clone git@github.com:Okayama-Healthcare-BCP-Consortium/HBIA.git
```

### 基準・業務・必要物一覧データの準備

<root>/data/input/基準・業務・必要物リスト.xlsxに基準と業務一覧を入力してください．

### 入力データの生成

以下のコマンドをターミナルで実行して下さい．
```shell
python <root>/src/data/dump_ahp_data.py
```

### AHPアンケートの記入

<root>/data/input/AHPアンケート.xlsxという自動生成されたアンケートに答えてください．

### 必要物フィルタのための入力データの記入

<root>/data/input/必要物フィルタのための入力データ.xlsxに必要事項を入力してください．

### 階層分析（AHP）と必要物フィルタの実行

以下のコマンドをターミナルで実行して下さい．
```shell
python <root>/main.py
```

### 結果の場所

<root>/result/AHP・必要物フィルタによる解析結果.xlsxを開いて確認してください．

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

## Requirement Filter Module Rule

各業務が実行可能（1）か実行不可能（0）かを判定する．

1. 各業務の「必要物」を三段階のスコア（十分→2，やや不十分→1，不十分→0）に変換
2. 1つでも不十分な「必要物」があれば，実行不可能（0）
3. スコアの算術平均が閾値（今回は1）を超えていれば，実行可能（1）
4. スコアの算術平均が閾値（今回は1）を超えていなければ，実行不可能（0）

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)
