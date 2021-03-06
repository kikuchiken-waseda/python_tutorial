======================================================
統計学基礎 (重回帰分析/因子分析)
======================================================

.. contents:: 目次

統計学とは
===========================

統計という言葉の意味をご存知でしょうか？
Wikipedia に よりますと以下のような意味だそうです．

| 統計（とうけい, statistic）は, 現象を調査することによって数量で把握すること,
| または, 調査によって得られた数量データ(統計量)のことである.
|
| - 出典: フリー百科事典『ウィキペディア（Wikipedia）』
| - https://ja.wikipedia.org/wiki/%E7%B5%B1%E8%A8%88

身長や体重を始めとした数値などをデータにすることを「統計」と言い,
そのデータを整理したり比較したりして,
手持ちのデータから持っていないデータについて議論する方法を学ぶことを
「統計学」と呼びます.

今回のセミナーでは, :code:`R` の基本的な操作と,
統計学のうち, 「重回帰分析」「因子分析」の二つの分析に絞って説明していきたいと
思っています.

R について
===========================

今回の合宿ではデータの分析を行う上で, :code:`R` を用います.
データリテラシーの授業で一度使っていると思うため,
インストールなどの手順は省いて, 実際に動かすところから始めましょう.

データの読み込み
----------------------------------

最初に, :code:`csv` ファイルを読み込みます.
ここでは, 企業の人事評価に関してのデータを扱います.

.. code-block:: R

   > jhk <- read.csv(data.csv”)

読み込んだデータがどのようなものであるのかを確認してみましょう．

.. code-block:: R

   > dim(jhk)  # データの行数列数を確認する
   > colnames(jhk)  # 変数名の確認
   > head(jhk, 3)  # 最初の3行を表示

このデータのヒストグラムを描画させます.
ここでは，パッケージ :code:`lattice` の :code:`histogram` 関数を用います.

.. code-block:: R

   > library(lattice)  # パッケージの読み込み
   > histogram(~stress, data=jhk, breaks=20, type="count")  # ヒストグラムを表示


関数の第 1 引数には, ヒストグラムを描画したい変数名を入れます.
例えば :code:`department` であれば :code:`department` を,
:code:`self_assertion` あれば :code:`self_assertion` を打ち込みます.
第 2 引数にはデータ名, 第 3 引数はヒストグラムの階級数を入力し,
第 4 引数の :code:`type` ではヒストグラムの縦軸を度数としています.

データの代表値, 散布度
----------------------------------

分布の中心位置を表現する指標のことを代表値と言います.
よく使われる代表値には, 平均値, 中央値(メディアン), 最頻値(モード)が挙げられます.
:code:`R` で上記の代表値を求めるには以下のようにします.

.. code-block:: R

   > mean(jhk$stress)  # ストレスの平均値
   > median(jhk$stress)  # ストレスの中央値
   > sort(table(jhk$age))  # 年代の最頻値

最頻値に関しては, 直接最頻値が出てくるわけではなく,
年代の変数名とその数を表示させ, その中で一番多いものを選ぶ, という形になります.

統計的仮説検定
----------------------------------

ここでは, 統計的仮説検定の話をします.
データリテラシーの授業を通して,
:code:`t` 値, :code:`p` 値という言葉は何度も耳にしているのではないかと思います.

では, :code:`t` 値, :code:`p` 値というものはそれぞれ何を表しているか説明できますか？
それぞれの値が何を示しているのかの話をしつつ,
統計的仮説検定の説明をしたいと思います.

統計的仮説検定の意義
===========================

最初にも言いましたが, 統計学とは, 手持ちのデータからまだ持っていないデータについて議論する方法を学ぶ学問です.

言い換えれば，手持ちのデータを分析することで,
データから確率分布を推定し，
まだ，知らないデータの値を予測します.

その上で重要なのは, **正しい確率分布を推定できているか** になります.

これを間違えてしまうと, まだ以後の予測は正しいものになりません.
元のデータから正しい確率分布が推定できているかどうかを判断するためには
統計的仮説検定が有効です.


t 値 と p 値
-----------------------------------

今回説明をする統計的仮説検定は :code:`t` 検定です．

この検定には :code:`t` 値という指標が使われます．
この指標は期待値が 0 ではないことを示すための指標です．

:code:`t` 値はこのように計算できます.

.. math::

   t 値 = \frac{期待値 - 0}{標準誤差}

:code:`t` 値が大きければ, 分子が大きいか, 分母が小さい,
またはその両方が起こっている可能性が考えられます.

分子が大きければ期待値と 0 との差が大きいことが言えますし,
分母が小さければ標準偏差が小さい, サンプル数が大きいことが言えます.

つまり :code:`t` 値が大きければ,
そのデータには期待値は 0 ではないと見なせます.

また, 求められた :code:`t` 値の値を,
偶然超えてしまう確率のことを :code:`p` 値と言います.
統計学上では,  :code:`p` 値が 0.05(5%) を下回れば有意差があると見なすことが多いです.

つまり,  :code:`p` 値が 0.05 以下であると,
偶然求めた :code:`t` 値を上回る可能性が 5% 以下であると言え,
要するにそのデータには有意差があると言えます.

.. warning:: 有意水準に関して

   有意水準の 0.05% という値は，
   慣例的なもので論理的な意味がある値ではないことは，
   常に注意が必要です．

   これは解析者の差別と偏見によって決定するものであるため，
   常に，"有意水準は XXX % と定めた" のように記述をする必要があります．

   10000 回同じ実験をして，5 回までは違う結果になるかもだけど許してねという意味です．


これらの値を求めるために :code:`t` 検定を行います．
例として, 男性と女性からできる二つの母集団で「協調性」の平均に差があるかを統計的に推測してみましょう.

:code:`R` では以下のように求められます.

.. code-block:: R

   > t.test(cooperativeness~gender, data=jhk, var.equal=T)
   t = 3.9599, df = 798, p-value = 8.167e-05

分析の結果,  :code:`t` 値は 3.9599,
自由度は 798, :code:`p` 値：8.167*10^-5 となりました．

少なくとも 0.1％ 水準で有意であると言えます．
つまり, 「母平均に差がない」という帰無仮説が棄却され,
男性と女性の母平均には差があると言えそうです.


様々な分析
==================================

ここまで統計学の基本的なことを復習がてら話してきました.
それでは, 実際に手を動かして(一応今までも動かしていますが)分析に触れて見ましょう.

重回帰分析
-------------------------

重回帰分析とは簡単に言うと,
1 つの目的変数を複数の説明変数で説明しようとする分析のことです.
1 つの目的変数を 1 つの説明変数で説明しようとする単回帰分析よりも,
細かい分析が可能になります.

ここでは, あるフィットネスジムチェーンの企業の顧客満足度のデータを用います.
データを読み込んで見てもらえば分かりますが,
ランダムにふられた店舗番号, 顧客数, 立地満足度, 設備満足度, 店舗面積満足度, トレーナー満足度, トレーナー数, トレーナーの接客研修の有無, 入会特典の有無についてのアンケートです.

一度, 単回帰のモデルを考えてみましょう.
例えば, 「設備満足度」によって「顧客数」を説明する場合には,
以下の式を立てることができます．

.. math::

   顧客数 = \alpha + \beta \times 設備満足度 + e

ここで単回帰式は一次関数ですので，
:math:`\alpha` は切片, :math:`\beta` は傾きです．
この :math:`\beta` のことを単回帰係数と呼びます.

この式は, 顧客数という目的変数を立地満足度という説明変数できる部分を表すものですが,
顧客数を立地満足度のみで説明できるとは思えません.
その説明できなかった部分が誤差 :math:`e` として表現されています.

では, 重回帰分析とはどのようなものでしょうか？

重回帰分析は, 複数の説明変数を用いて目的変数を説明するものだと述べました.
例えば, 「立地満足度」と「設備満足度」説明するならば,
以下の式で表現できます．

.. math::

   顧客数 = \alpha + \beta_{1} \times 立地満足度 + \beta_{2} \times 設備満足度 + e

説明変数が増えていることから, 傾きも二種類あります.
説明変数が 2 個以上ある場合には, これらの傾きを偏回帰係数と呼びます.

一通り言葉で説明したので, 実際に分析を始めましょう.
重回帰分析の具体的な手順は以下の通りです.

1. 回帰モデルの作成(どのような説明変数を入れるかの検討)
2. モデルにおける母数の推定(各説明変数に付与された偏回帰係数の値を推定)
3. モデルの診断と評価(重回帰モデルの評価)
4. 偏回帰係数の解釈(モデルの評価が良好であれば, 偏回帰係数を解釈)


今回は, 「顧客数」という目的変数を「立地満足度」「設備満足度」「店舗面積満足度」「トレーナー満足度」の4つの説明変数によって説明するモデルを作成し,
R を用いた重回帰分析の基本的な手順を踏んでいきます.

重回帰モデルを以下のように仮定します．

.. math::

  顧客数 = \alpha + \beta_{1} \times 立地満足度 + \beta_{2} \times 設備満足度 + \beta_{3} \times 店舗面積満足度 + \beta_{4} \times トレーナー満足度 + e


:code:`R` を用いて重回帰分析を行うときは関数 :code:`lm` 関数を用います.

.. code-block:: R

   > csdat <- read.csv("data2.csv")  # データの読み込み
   > head(cedar, 3)  # 最初の 3 行を確認する
   > res1 <- lm(num ~ location + facility + area + trainer, data=csdat)

見てわかるとは思いますが, 関数 :code:`lm` は第 1 引数にモデルの式を与えます.
:code:`~` の左側に目的変数, 右側に用いる説明変数を + で繋いでいくだけです.

重回帰分析の結果が含まれた :code:`res1` に対して関数 :code:`summary` を用いると,
主要な値が表示されます．

.. code-block:: R

   > summary(res1)

結果の :code:`Estimate` というのが各変数の偏回帰係数となっており,
傾きを示したもので, :code:`intercept` は切片を意味します.

時間の関係上, モデルの診断・評価ができないため,
今回はこのモデルがいい評価を得た前提で話を進めます.

.. warning:: モデルは仮説

   ここで重回帰式というのは解析者が勝手に考えた，
   仮説を試してみた結果に過ぎないことに注意が必要です．

   ようはモデルを作成しただけでは，
   それがうまくいっていたものなのか，
   そうじゃないのかはわかりません．

   実際の研究では，
   今回飛ばしたモデルの診断・評価こそが重要になります．

上記の結果をまとめると，
顧客数は以下の式で予測を行うことが出来そうです．

.. math::

   顧客数 = \alpha + 29.105 \times 立地満足度 + 21.640 \times 設備満足度 + 23.803 \times店舗面積満足度 + 32.421 \times トレーナー満足度 + e

因子分析
-------------------------

因子分析は, 質問紙等のアンケートに含まれている項目の間の相関関係を元に,
ある項目群に共通している成分(因子)を見つけるための手法となっています.

主に心理尺度を利用した調査研究で扱われます.因子分析には探索的因子分析と確認的因子分析の二種類がありますが, 本セミナーでは探索的因子分析の身の説明をさせていただきます.

人がある行動を起こす際,
その理由には大きく分けて内発的動機づけと外発的動機づけの2つがあると言われています.

内発的動機づけとは, その物事を「面白いからやる」と活動そのものに興味を持っている状態で, 外発的動機づけとは, 「褒美がもらえるから」「やらないと怒られるから」など報酬の獲得, 罰の回避など, 活動そのものとは関係のない目的を達成するための手段としての動機づけとなっています.

因子分析を行う上で, 今回は中学生が学習をする理由について調査するため, 内発的, 外発的共に4つずつの項目に答えてもらったデータを用います.

内発的動機づけの項目は

- I1. 問題を解くことは面白いから
- I2. 勉強すること自体が好きだから
- I3. わかるようになるのが嬉しいから
- I4. 好奇心が満たされるから

外発的動機づけの項目は

- E1. 成績が下がると怒られるから
- E2. 勉強することは規則のようなものだから
- E3. みんなが勉強しているから
- E4. 周りの人がやりなさいと言うから

となっています.

それぞれに 1 (全く当てはまらない) から 4 (かなり当てはまる) までの評価をしてもらいました.

では, 最初にデータを読み込んで見ましょう

.. code-block:: R

   > mtv <- read.csv("data3.csv")
   > head(mtv)

これらの回答に得点を与え, 合計点を内発的動機づけ,
外発的動機づけのそれぞれの得点とすることで,
動機づけの程度を表すことができます.
このように, 対象に数値を与える規則のことを尺度と言います.

さて, 探索的因子分析を行う上で, 踏む手順は以下の通りとなります.
一つずつ見ていきましょう.

1. 因子数の決定
2. 因子負荷の推定
3. 因子軸の回転 (因子が二つ以上の場合)
4. 因子の解釈

まず, 因子数の決定を行いましょう.
因子数の決定には何種類かありますが, 今回はスクリーテストを用いて見ましょう.
固有値を縦軸, 因子の番号を横軸に取り,
固有値の変化をプロットした折れ線グラフのことをスクリープロットと言います.

スクリーテストでは, 固有値の推移がなだらかになる直前までの固有値の数を因子数とします.
スクリープロットは, :code:`psych` というパッケージの :code:`VSS.scree` を用いることで出力できます.

.. code-block:: R

   > library(psych)
   > VSS.scree(dkk)

ここで出力されたスクリープロットを見ると,
第 3 因子以降でなだらかになっています.

したがって, 因子数は 2 までと決めてみることができそうです．

仮に第 4 因子以降でなだらかになるようであれば因子数は3となりますので,
臨機応変に対応してください.

次に, 因子負荷の推定を行います.

因子負荷は, それぞれの観測変数が各因子をどの程度反映しているかを示します.
探索的因子分析による因子負荷の推定は,
パッケージ :code:`psych` の :code:`fa` という関数により行うことができます.
先ほどのスクリーテストにより, 因子数は 2 として分析していきましょう.

因子数が 2 つであるため, 因子軸を回転させる必要がありますが,
まず最初に回転する前の因子負荷の値を推定しましょう.

.. code-block:: R

   > fa.mtv <- ca(mtv, nfactors=2, fm=“ml”, rotate=“none”)
   > print(fa.mtv, sort=T, digits=3)

因子分析の結果を変数 :code:`fa.mtv` に保存します.

関数 :code:`fa` では, 第一引数でデータを指定, 第二引数で因子数の指定, 第三引数では推定法を記述します.

今回は心理学研究で最もよく使われている最尤法を用いています.

第四引数では回転の方向を決めるものですが, 今回はなしにしております.
出力画面に出てくる結果ですが,
ML1, ML2の列はそれぞれ第一因子, 第二因子の因子負荷を大きい順に
並び替えたものとなっております.

下に出てくる :code:`SS loadings` は因子寄与と呼ばれるもので,
各因子が説明できる観測変数の分散の大きさを表します.

:code:`Proportion Var` は各因子の寄与率を合計した値であり,
累積寄与率と呼ばれることが多いです.

では, 因子軸の回転について考えて見ましょう.

因子を解釈する際、その因子が単純構造であるほうが簡単に解釈できます。単純構造家とは、観測変数が一つの因子だけから高い因子負荷を受けて、それ以外はほぼ0である状態のことを指します。しかし、先ほどの例で推定されたような観測変数にかかる因子負荷は単純構造とは言えません。例えば、観測変数「I3」は第一因子の因子負荷が0.630、第二因子の因子負荷が0.425であり、いずれの因子からも高い因子負荷を受けているため、第一因子を反映した変数なのか、第二因子を反映した変数なのかを判断することが難しくなっています。そこで単純構造になるように因子軸の回転を行います。ここでは、斜交回転として最も使われている、プロマックス回転を利用します。みなさん、名前は聞いたことがあるのではないでしょうか。因子軸の回転を利用するには、パッケージGPArotationが必要です。

.. code-block:: R

   > library(GPArotation)
   > fa.mtv2 <-fa(mtv, nfactors=2, fm="ml", rotate="prom")
   > print(fa.mtv2, sort=T, ditgits=3)

最初に求めた因子分析と違うのは第四引数であるrotateがnoneからpromaxに変わっているところです。これで、プロマックス回転を行った上での因子負荷が想定されます。開店後の因子負荷は最初とは異な理、単純構造に近づいていることがわかります。観測変数「I3」は第一因子からの因子負荷が0.791、第二因子からの因子負荷が0.061であり、メリハリがつきました。また、出力結果の違いとして、因子間相関が求められています。今回の場合は-0.54ということで、中程度の負の相関があると言えます。

因子負荷の想定が終わったので、解釈に入ります。因子の解釈とは、各因子が強く反映する変数の内容から、その因子の内容を推測することです。具体的にいうと、その因子がどのような概念を表しているかについて、因子名をつけます。

今回の場合、第一因子を見ると、「好奇心が満たされるから」や「わかるようになるのが嬉しいから」などが高い因子負荷を示しています。これは、学習すること自体に興味を持っている人が高い得点を取ると考えられる変数であることから、第一因子は「内発的動機づけ」因子と因子名をつけられます。次に、第二因子を見ると、
「皆が勉強しているから」や「勉強することは規則のようなものだから」などが高い因子負荷を示しています。これらは学習自体ではなく、別の目的を達成するための手段として学習を行っている人が高い得点と取ると考えられる変数であること方、第二因子は「外発的動機づけ」と因子名をつけられます。

最後に
===========================

みなさん、お疲れ様でした。今回のセミナーはデータリテラシーの復習を基本としていますが、おそらくこれだけで完全に理解できる人はいないと思います。自分の手で分析をしてみる、ということを何度も繰り返しやることで身につくものだと思うので、試してみてください。何か困ったことがあれば髙田をはじめ、院生が答えてくれると思います。これから一緒に頑張っていきましょう。
