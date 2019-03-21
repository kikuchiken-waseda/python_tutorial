What next
===========================

お疲れさまでした．
以上で， python の tutorial を修了します．

冒頭にも書きました通り，
プログラミングは，
文章を書くことにとても良く似ています．

初学者は，まず道具の練習や単語の練習で，
一杯一杯になります．
これを突破して，初めて文章を作ることができるようになります．
文章構成を考えたり，推敲したり，
色々な練習を経て，初めて，相手（それは python そもものかも知れませんし，他の開発
者かもしれません．あるいは貴方のサービスを使うユーザかもです）に伝わる文章を練り
上げることができるようになります．

ここには特効薬はありません．
ひたすら，書くしか無いのです．
""次になにする"" という項目は多くの技術書に出てくる内容ではありますが，
答えは何時も一つです．

何かを作ろう．
とにかく，書こうです．

フォースと共にあれ というヤツです．

さて，2 つの方針をお渡ししましょう．

ライブラリを極める: ダークサイト
--------------------------------------

python の良い部分の一つには，
質のよいライブラリコミュニティが複数存在することが挙げられます．

もし，貴方が WEB サービスに興味を持つとするのなら,
django というライブラリを調べてみましょう．

- https://docs.djangoproject.com/ja/2.1/intro/tutorial01/

WEB サービスではなく，GUI を作成したい場合，
pyside2 のコミュニティが今は一番, 触りやすいと思います．

- https://www.qt.io/legal-contribution-agreement-qt

そういう物作りではなく，機械学習に興味のある方は，
scikit-learn のドキュメントには一通り目を通すべきます．

- https://scikit-learn.org/stable/

あるいは統計に興味がある場合には，
pandas, scipy, numpy そして Statsmodels などを押さえておくのがよいと思います．

- https://www.statsmodels.org/stable/index.html
- http://pandas.pydata.org/
- https://www.scipy.org://www.scipy.org/
- http://www.numpy.org/

.. note::

   R という言語を知っている方は pandas から始めるのかよいでしょう．
   このライブラリは，筆者が R に必要性を感じなくなった切っ掛けです．

   また matlab という言語を知っているかたは scipy を見て驚くことになるでしょう．
   matlab でできることは全て scipy で実装されています．

python を極める: ライトサイド
--------------------------------------

一方で今回は python その物に関してもほんの一般的な触りだけしか触れていません．
本当に pythonic な部分は，あまり説明をできていないのが現状です．
これら python そのものに関してを探求したい場合には，
何だかんだで公式のドキュメントが一番詳しいです．

例えば今回扱った範囲では，以下のページが役に立ちます

- https://docs.python.org/ja/3/reference/datamodel.html
- https://docs.python.org/ja/3/reference/compound_stmts.html
- https://docs.python.org/ja/3/library/index.html

その他，結局の処，最もよい資料は公式であることを，
筆者は絶対に譲りませんが，初学者はそもそも何を書こうとしているのが
意味不明な部分があることは否めません．

そのため，オススメの書籍を紹介しておきます．

- みんなの python
   - https://www.amazon.co.jp/%E3%81%BF%E3%82%93%E3%81%AA%E3%81%AEPython-%E7%AC%AC4%E7%89%88-%E6%9F%B4%E7%94%B0-%E6%B7%B3/dp/479738946X
   - 一番基本的な python に関する説明が書かれています．
   - 個人的には，勝手まで読むなら，何か手を動かした方が速いと思いますが．
- 実践 Python 3
   - https://www.amazon.co.jp/%E5%AE%9F%E8%B7%B5-Python-3-Mark-Summerfield/dp/4873117399/ref=sr_1_1?ie=UTF8&qid=1552503176&sr=8-1&keywords=%E5%AE%9F%E8%B7%B5python3
   - デザインパターンに関する本です.
   - 文が書けるようになった後のステップとして極めて良書です．
- Fluent Python
   - https://www.amazon.co.jp/Fluent-Python-%E2%80%95Pythonic%E3%81%AA%E6%80%9D%E8%80%83%E3%81%A8%E3%82%B3%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E6%89%8B%E6%B3%95-Luciano-Ramalho/dp/4873118174/ref=sr_1_1?ie=UTF8&qid=1552503310&sr=8-1&keywords=fluent+python
   - 筆者らが言っている通り，中級者以上の人間が読む本です．
   - ただし，必要なことがとてもよく書いてあります．
   - イメージ的には，文章の微妙な言い回しに関する指導書でしょうか？
   - 公式ドキュメントに対する良質な解説書とも言えます．
