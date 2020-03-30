First Python
===========================

実は上の例で，一通り python に関して，
最低限知っておくべきことの実例を示してします.

以後しばらくは，何を伝えたかったのかの説明をします．

.. contents::
   :depth: 3

データモデル
-------------------------------

プログラミングは一種の言葉です．
言葉の構成要素を考えると，
大雑把には二つに分けることができます．

つまり，単語と文です．

python では単語のことをデータモデル,
文のことを制御構文といいます．

.. note::

   この説明に関しては異論を認めます．
   つまり，正確な説明ではありません．

   あくまでもここでの説明のための操作上の定義です.

よい文章を書くためには，
できるだけ多くの単語を使いこなせる方がいいわけで，
ここではまず，単語の話からしていきます．

Python においてデータモデルは，
基本的に 2 つに分けることができます．

- 1 つで意味をもつもの
- いっぱいで意味をもつもの

ここでは python を使う上で必要になる特に重要な単語の使い方を説明していきます．

.. note:: 基本的以外のものは，その両方(変数)か，その両方ではないもの(None)です．

   この内，関数についてだけ先に説明をさせてください．

   イントロダクションの例で変数を使用している部分を紹介します．

   .. code-block:: python
      :linenos:
      :emphasize-lines: 3

      >>> # クリスマスに隠された本当の意味とは
      >>> import itertools
      >>> words = "christmas"
      >>> ["".join(x) for x in itertools.permutations(words, len(words))]

   この例の内変数は 3 行目です．

   イコール記号を使っていますが数学的な意味でのイコールとは少し意味が異なります．

   どちらかというと，ラベル付けという意味です
   (よく箱という風に説明される方がいるのですが，箱よりラベルの方が分かり易いと思います)．

   つまりこの例では,
   :code:`christmas` という文字列に :code:`word` というラベルを貼っているのです．
   それで次に :code:`word` というラベルを見た時には python は
   頑張ってラベルを探し，その内容を返します．

   いくつか例を見てみましょう．

   .. code-block:: python

      >>> word = "christmas"
      >>> print(word)
      christmas
      >>> number = 1
      >>> print(number)
      1

   なんとなくお分かりいただけましたでしょうか？
   これは単なるラベルなので，左辺の文字は何でもよいです．

   .. code-block:: python

      >>> a = "christmas"
      >>> print(a)
      christmas

   だたし，このラベルには注意が必要です．
   以下の結果が如何して，そうなるのか，
   説明できるでしょうか？

   .. code-block:: python
      :emphasize-lines: 3,6

      >>> word = "christmas"
      >>> print(word)
      christmas
      >>> word = "new year"
      >>> print(word)
      new year


数値型: int / float / bool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1 つで意味をもつものに関してを数値型といいます．
大雑把に言えば，数ですね．
代表的なものに以下の 3 つがあります．

- int: 整数
- float: 実数
- bool: 真偽値(True, False)

数値型は数値型同士において四則演算を行うことができます．

.. code-block:: python

   >>> 1 + 1
   2
   >>> 0 - 1
   -1
   >>> 2 * 5
   10
   >>> 10 / 2
   5.0

数値型同士と言いました．
つまり, bool と int も演算を行うことが可能です．

.. code-block:: python

   >>> 1 + True
   2
   >>> 1 + False
   1

さて，では True や False は結局なにものでしょうか？
上の例から考えてみてください．

.. note::

   先の例を見て，あれ？文字は？と感じた方は，
   とても良いです．

   実は文字は，複数で初めて意味を持つので,
   文字列型となり，次の章での説明になります．

   それが証拠に 文字列と int は四則演算できません．

   .. code-block:: python

      >>> "a" + 1
      ----------------------------------------------
      TypeError: can only concatenate str (not "int") to str

大抵の場合，四則演算が可能であれば，
比較を行うことができます．

比較とは以下の操作のことを指します．

.. list-table:: 比較演算
   :widths: 15 10
   :header-rows: 1

   * - 演算子
     - 意味
   * - <
     - より小さい
   * - <=
     - 以下
   * - >
     - より大きい
   * - >=
     - 以上
   * - ==
     - 等しい
   * - !=
     - 等しくない
   * - is
     - 同一のオブジェクトである
   * - is not
     - 同一のオブジェクトでない

例えば以下のような結果になります．

.. code-block:: python

   >>> 1 > 2
   False
   >>> 1 > 1
   False
   >>> 1 < 2
   True
   >>> 1 <= 1
   True
   >>> 1 > False
   True
   >>> 1 == 1
   True
   >>> 1 != 1
   False
   >>> 1 == True
   True
   >>> 1 != True
   False
   >>> 0 == False
   False

ただし, :code:`is` や :code:`is not` は，
今までの説明とは異なる挙動を示します．

.. code-block:: python

   >>> 0 is False
   False
   >>> 1 is not True
   True

もし，貴方がプログラミング経験豊富な方であれば，
この特性が極めて理に適っていることに気が付くと思います．

初学者の方は，まだ，あまり考えなくていいです（いずれ問題が起きたときに思い知るでしょうから）.

この章を通じて説明したかった内容には数値型の扱いがあります．

数値型は四則演算可能で，かつ，
比較可能（ハッシュ可能といいます）であるという特性を持っています．

もう一つこの章で何となく感じて欲しいことがあります．
それは Python において，
データ型は，どんなことができるのか（つまり動詞）との関係で，
定義されているということです．

逆に言えば，どんなことができるのかを決めることで，
全く新しい型を作成した時に，数値にしたり，その他にしたりすることができます（こう
いうプログラミングの方法をダックタイプといいます）．

シーケンス型: list, tuple, str
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

続いてはシークエンス型です．
これはいっぱいで意味をもつものの内，
順番が大事なものです．

これには list, tuple, str が相当します．

ここで, list と tuple ですが，
list は一度作った後に変更可能ですが，
tuple は変更不可能という特徴があります．

- これは一見 list の方が便利だと考えられますが，
  逆に tuple は演算速度が速いです．

一方で list と str を比較すると，
str は文字限定の機能を使うことができます

例えば，こういう風に使います．

.. code-block:: python

   >>> # list
   >>> print([1, 2, 3])
   [1, 2, 3]
   >>> # tuple
   >>> print((1, 2, 3))
   (1, 2, 3)
   >>> # str
   >>> print("apple")
   apple

基本的には, データを何かの記号で囲っていることに注意してください．

順番を持っているので，
特定の順番のデータだけを取り出すこともできます．

.. code-block:: python

   >>> print([1, 2, 3][0])
   1
   >>> print((1, 2, 3)[1])
   2
   >>> print("hello"[-1])
   o

ここで，順番（インデックス）は 0 から始まります．
もちろん，空の箱を作ることもできます．

.. code-block:: python

   >>> print([])
   []

ただし，存在しないインデックスの内容を取り出すことはできません．

.. code-block:: python

   >>> print([1][1])
   -------------------------------------
   IndexError: list index out of range

データの取り出し方は色々あります．

- 以下のような操作をスライスと言います．

.. code-block:: python

   >>> [1,2,3][-1]
   3
   >>> [1,2,3,4][1:3]
   [2, 3]
   >>> [1,2,3,4][1:4:2]
   [2, 4]
   >>> [1,2,3,4][::-1]
   [4, 3, 2, 1]

また, 長さを持っているため，以下のような関数を実行することができます．

.. code-block:: python

   >>> len([1,2,3,4])
   4
   >>> a = [1,2,3,4]
   >>> a[1:len(a)]
   [2, 3, 4]

list 限定操作
++++++++++++++++++++++++

list は和と積が定義されています(差と商は定義されていません)．

.. code-block:: python

   >>> [1,2,3] + [1,2]
   [1, 2, 3, 1, 2]
   >>> [1,2,3] * 2
   [1, 2, 3, 1, 2, 3]

ここで二項目の型は非常に重要です．
つまり，以下の演算はできません．

.. code-block:: python

   >>> [1,2,3] + 1
   TypeError: can only concatenate list (not "int") to list
   >>> [1,2,3] * [2]
   TypeError: can't multiply sequence by non-int of type 'list'

また，以下のような操作を行うことができます．

.. code-block:: python

   >>> numbers = [1,2,3]
   >>> numbers.append(1)
   >>> print(numbers)
   [1, 2, 3, 1]
   >>> a = numbers.pop(-1)
   >>> print(a)
   1
   >>> print(numbers)
   [1, 2, 3]
   >>> numbers.extend([1, 2])
   >>> print(numbers)
   [1, 2, 3, 1, 2]
   >>> numbers.reverse()
   >>> print(numbers)
   [2, 1, 3, 2, 1]
   >>> numbers.sort()
   [1, 1, 2, 2, 3]
   >>> numbers.index(3)
   4
   >>> numbers.count(1)
   2


ここで，何か今までと違うと思った方は，
とてもいいセンスをしています．

list の種々操作の多くは一度変数を使用すると，
その後別の変数に代入することはあまりありません( :code:`pop` の例とか面白いですよね)．
何故かというと， list は可変オブジェクトだからです．

タプル型
+++++++++++++++++++++

list とはうって変わって tuple オブジェクトは非可変です．
これは少し理解が難しいかもしれません．

例えば以下のようなことは可能です．

.. code-block:: python

   >>> tuples = (1, 2, 3, 4, 5)
   >>> new_tuples = tuples + (6, 7)
   >>> print(new_tuples)
   (1, 2, 3, 4, 5, 6, 7)

また，これも可能です．

.. code-block:: python

   >>> tuples = (1, 2, 3, 4, 5)
   >>> new_tuples = tuples[2:4]
   >>> print(new_tuples)
   (3, 4)

つまり, 何か新しい変数にするなら，
リスト型と同じような操作ができるのです．

一方で, :code:`append` 関数や, :code:`pop` 関数のように
一度決まった変数そのものを変更することはできません．

.. code-block:: python

   >>> tuples = (1, 2, 3, 4, 5)
   >>> tuples[0] = 1
   TypeError: 'tuple' object does not support item assignment

この型は初学者の内では，むしろ，種々制御構文内で使用されることが多いです．


str型
+++++++++++++++++++++

文字列型と list 型はとても良く似ています．
つまり，和と積が定義されています．

.. code-block:: python

   >>> x = "apple"
   >>> print(x + "pen")
   applepen
   >>> print(x)
   apple
   >>> x * 2
   'appleapple'

ただし，文字列に特化した様々な操作が用意されています．

.. code-block:: python

   >>> " ".join(["This", "is", "a", "pen"])
   'This is a pen'
   >>> "This is a pen".split()
   ['This', 'is', 'a', 'pen']
   >>> "This is a pen".upper()
   'THIS IS A PEN'
   >>> "This is a pen".lower()
   'this is a pen'
   >>> "This is a pen".find("pen")
   10
   >>> "This is a pen".replace("pen", "pepar")
   'This is a pepar'
   >>> "1 + 1 = {}".format(1 + 1)
   '1 + 1 = 2'

集合型: set, frozenset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

シークエンス型は順番を大事にしますが，
集合型は順番を無視します．

これは同じ値は一つだけという意味を持ちます．

- 例えば，色の種類とか，何かの種類を決める時に便利です．

これは以下のように使います．

.. code-block:: python

   >>> pokemon_set = {"red", "green"}
   >>> print(pokemon_set)
   {'green', 'red'}

基本的な操作は以下の通りです．

.. code-block:: python

   >>> pokemon_set = {"red", "green"}
   >>> pokemon_set.add("blue")
   >>> print(pokemon_set)
   {'red', 'blue', 'green'}
   >>> pokemon_set.add("blue")
   >>> print(pokemon_set)
   {'blue', 'green', 'red'}
   >>> pokemon_set.remove("blue")
   >>> print(pokemon_set)
   {'red', 'green'}
   >>> version = pokemon_set.pop()
   >>> print(version)
   'red'
   >>> print(pokemon_set)
   {'green'}

また， set 型はつまり集合なので，以下の操作が可能です．

.. code-block:: python

   >>> k_pokemon_set = {"Bulbasaur", "Charmander", "Squirtle", "Zubat"}
   >>> j_pokemon_set = {"Chikorita", "Cyndaquil", "Totodile", "Zubat"}
   >>> print(k_pokemon_set | j_pokemon_set)
   {'Bulbasaur', 'Chikorita', 'Zubat', 'Totodile', 'Squirtle', 'Cyndaquil', 'Charmander'}
   >>> print(k_pokemon_set - j_pokemon_set)
   {'Squirtle', 'Bulbasaur', 'Charmander'}
   >>> print(k_pokemon_set & j_pokemon_set)
   {'Zubat'}
   >>> print(k_pokemon_set ^ j_pokemon_set)
   {'Bulbasaur', 'Chikorita', 'Totodile', 'Squirtle', 'Cyndaquil', 'Charmander'}

この辺を使いこなせると，確立や，ニューラルネットワークに強くなります．

また，以下のような作業を行うことも多いです．

.. code-block:: python

   >>> k_pokemons = ["Bulbasaur", "Charmander", "Squirtle", "Zubat"]
   >>> j_pokemons = ["Chikorita", "Cyndaquil", "Totodile", "Zubat"]
   >>> pokemons = list(set(k_pokemons + j_pokemons))

マッピング型: dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

辞書型は, set 型と変数の組み合わせです．
つまり，一つの  key を持ち，それに対応する value を持ちます．

これは以下のように使います．

.. code-block:: python

   >>> b = {'one': 1, 'two': 2, 'three': 3}
   >>> print(b)

これは辞書なので，あるインデックスで検索を行うことができます．

.. code-block:: python

   >>> b = {'one': 1, 'two': 2, 'three': 3}
   >>> b["one"]
   1

リスト型にとても良く似た指定方法ですが，
インデックスは数字ではなく，文字列です．

当然，存在しないインデックスを指定するとエラーになります．

   >>> b = {'one': 1, 'two': 2, 'three': 3}
   >>> b["four"]
   KeyError: 'four'

辞書型はとても作り込まれた型で，
様々なことができます．

   >>> dict = {'one': 1, 'two': 2, 'three': 3}
   >>> print(len(dict))
   3
   >>> dict["four"] = 4
   >>> print(dict)
   {'one': 1, 'two': 2, 'three': 3, 'four': 4}
   >>> print("four" in dict)
   True
   >>> print("five" not in dict)
   True
   >>> print(dict.get("one"))
   1
   >>> print(dict.get("five"))
   None
   >>> print(dict.pop("one"))
   1
   >>> print(dict.pop("five"))
   None
   >>> dict.update({"one": 1, "five": 5})
   >>> print(dict)
   {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
   >>> print(list(dict.keys()))
   ['one', 'two', 'three', 'four']
   >>> print(list(dict.values()))
   [1, 2, 3, 4, 5]
   >>> print(list(dict.items()))
   [('two', 2), ('three', 3), ('four', 4)]

制御構文
-------------------------------

さて，ここまでに色々な単語について説明をしてきました．
ここからはそれらの単語を使った文章について説明をしていきます．

if 文
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if 文とは読んで字の如し,
xx たっだら oo するという意味の文章です．
例えば以下のように使用します．

.. code-block:: python

   >>> val = 100
   >>> if (val > 10):
   >>>     print("いっぱい")
   いっぱい

負例の場合はどうなるのでしょう．

.. code-block:: python

   >>> val = 100
   >>> if (val > 1000):
   >>>     print("いっぱい")

その場合には何も起きません．

ここで :code:`else` というキーワードを使うと，
そうじゃなかったらを表現できます

.. code-block:: python

   >>> val = 100
   >>> if (val > 1000):
   >>>     print("いっぱい")
   >>> else:
   >>>     print("ちょっと")
   ちょっと

xxx か否か以外にも条件を足すことが可能です.

.. code-block:: python

   >>> val = 100
   >>> if (val > 1000):
   >>>     print("いっぱい")
   >>> elif (val > 99):
   >>>     print("ふつう")
   >>> else:
   >>>     print("ちょっと")
   ちょっと

この elif はいくつでもよいです．

- 逆に言えば if や else は一回に一つしかありえません．
    - elif だけということもありえません．

因みに，今回紹介する制御構文の多くはこの if 文から作成されています．
つまり，色々なところに else が出てくるのです．


while 文
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while 文に関しては基本的に,
初学者が使用することはないので単純な例だけを記述します．

.. code-block:: python

   while i < 3:
      print(i)
      i += 1

こうすると, while 以下が三回繰り返されます．
ここにも else が登場します(本質が条件式なので)．

.. code-block:: python

   while i < 3:
       print(i)
       i += 1
   else:
       print('!!FINISH!!')

でも実務上 while を使用する，
最も有意義な例はこれです．

.. code-block:: python

   from time import sleep
   while True:
       print('無限ループって怖くない？')
       sleep(3)

これを実行すると'無限ループって怖くない？'と三秒ごとに永遠に，
表示されます．

-  :kbd:`ctrl + c` で停止されます．

.. note:: 無限ループはいつ使うのか

   初学者に無限ループを教えると，
   何故かみな怖がります．

   でも，実はとても一般的に使用します．
   例えば，何かアプリケーションをイメージしてください．
   word でもいいですし，chrome でもいいです．

   これらは一度起動したら，閉じるボタンを押すまで，
   ずっと起動しています．

   こういう風にずっと起動させておきたい何かを作る際に，
   無限ループは使用されます．


for 文
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python において繰り返し処理を行う，
最も一般的な例は for 文でしょう．

これは以下のように使用します．

.. code-block:: python

   >>> text = "this is a pen."
   >>> for word in text.split():
   >>>     print(word)

基本的にリストや辞書の中身を一つずつ見て行くときに便利です．

プログラミングにおいては，しばしば，いま何回目のデータを見ているのかが知りたくなります．そういうときには以下の記法を覚えておくと便利です．

.. code-block:: python

   >>> text = "this is a pen."
   >>> for i, word in enumerate(text.split()):
   >>>     print("{}: {}".format(i, word))

この制御構文は list や tuple, dict と共に使用されることが多いので，
以下のような書き方も可能です．


.. code-block:: python

   >>> numbers = [i * i for i in range(10)]
   >>> print(numbers)
   >>> numbers = {i: i * i for i in range(10)}
   >>> print(numbers)

また，この書き方は if  文と併用可能です．

   >>> numbers = [i * i for i in range(10) if i % 2 == 0]
   >>> print(numbers)


try 文
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

try 文は何かエラーが起きても頑張るようにする制御構文です．
たとえば以下のコードはエラーが起きます．

.. code-block:: python

   >>> numbers = []
   >>> print(numbers[0])
   IndexError: list index out of range

当たり前ですね．
しかし，以下のようにすると，
エラーが起きた時も何とかすることが可能です．

.. code-block:: python

   >>> numbers = []
   >>> try:
   >>>     print(numbers[0])
   >>> except Exception:
   >>>     print(0)

:code:`except Exception` は何かのエラーが起きた場合には，
それ以下のものを実行してという意味です．

xxx ならば ooo なので，else 文が使用可能です．

.. code-block:: python

   >>> numbers = [1]
   >>> try:
   >>>     v = numbers[0]
   >>> except Exception:
   >>>     v = 0
   >>> else:
   >>>     print(v)

with 文
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

with 文は制御構文の中でもかなり特殊なものです．
イメージ的には，何かを開いてから，閉じるまでという意味です．

これは大変理解しにくいため，まずは以下の事例を覚えてください．

.. code-block:: python

   with open("tmp.txt", "w") as file:
       file.write("some string")

これを実行すると，tmp.txt というファイルが作成されます．
逆にファイルを読み込むには以下のようにします．

.. code-block:: python

   with open("tmp.txt", "r") as file:
       text = file.read()
   print(text)

関数
--------------------------------------------

今から説明する関数と，クラスは，
今回のチュートリアルの中で特に難しく，かつ，大切なものになります．

これらは，単語であるという意味において，
データモデルであり，文章を使うという意味において，制御構文です．

どういうことかというと，自分で新しい単語を作る方法であるという意味です．

今から説明をする関数は，実は今まで使用してきたものです．

.. code-block:: python

   >>> x = "Hello World"
   >>> len(x)

この内の len() の部分がそうですね．
この語は長さを出すという意味を持ちます．

プログラミングの主な仕事の一つは，
このような操作に関係する単語を自分で決めることにあります．

これは以下のようにします．

.. code-block:: python

   >>> def get_word_num(x):
   >>>     return len(x.split())

このように決めた言葉を使うには以下のようにします．

.. code-block:: python

   >>> get_word_num("this is a pen.")
   4

ここで，関数とは何かを，
良く理解しておきましょう．

関数とは, (多くの場合自分で決めた)言葉です.
今回の場合, :code:`get_word_num` という言葉です．
この部分は自分で自由に決めることができます（というか決めなくてはいけません）.
その意味では変数に近いです．

それと同時に，関数とは動詞です．
つまり，目的語が入ります．
今回の場合目的語は x ですね．
この目的語も実は何でもいいです．
単なるラベル(変数)です.

つまり以下のようにしたっていいわけです．

.. code-block:: python

   >>> def x(y):
   >>>     return len(y.split())
   >>> res = x("this is a pen.")
   >>> print(res)
   4

勿論，自動詞のように目的語の存在しない関数だって作れます．

.. code-block:: python

   >>> def x():
   >>>     return 1
   >>> res = x()
   >>> print(res)
   1

すこし，不思議ですね．

じゃあ，今までの例にすべて出て来た :code:`return` は必要なのでしょうか？
実は必須ではありません．

.. code-block:: python

   >>> def x():
   >>>     1
   >>> res = x()
   >>> print(res)
   None

あれ？と思って頂けるとうれしいです．
今まで算数で扱ってきた，関数とは随分違うものですね．

関数とは例えるなら，トンネルです．
それもドラえもんのガリバートンネルみたいなやつです．

入り口があってもいいし，
出口があってもいい(そしてなくてもいい)．

ただ，そこを通すと，通ったものが何か変わる（時もある）.
そんなトンネルなのです．

これは日常でも沢山あります．
例えばどのようなものがあるのでしょうか？
すこし考えてみてください(それは大いにプログラミングの上達を手助けします)．

.. note:: 引数とは何者か

   関数を教えていると，
   しばしば引数に関して混乱する方が多いです．

   初学者の内は，引数とは定義されていない（ことの多い）変数なのだ，と
   理解するのがよいです．

   どういうことでしょうか？

   例えば以下の例で考えてみます::

      >>> def add(a, b):
      >>>     return a + b
      >>>
      >>> add(1, 2)
      3
      >>> add(10, -1)
      9

   関数 :code:`add` は変数 :code:`a` と変数 :code:`b` を
   足しているだけです．

   で実際に使用している際には, :code:`(1, 2)` や :code:`(10, -1)` を使っています．
   では例えば, 1 はどこに入るのでしょうか？
   あるいは -1 はどこに入るのでしょうか？

   これを考えると, 引数とは，後で値が決まる変数の一種だと分かると思います．

   引数が変数であるということを示す例をもう一つおみせします::

      >>> def add(a, b=1):
      >>>     return a + b
      >>>
      >>> add(1)
      2
      >>> add(1, 2)
      3
      >>> add(1, b=4)
      5

   何が起きたのか考えてみましょう．


.. note:: 可変長引数

   引数に関してはもう一つ，
   面白い書き方があります::

      >>> def show(*args):
      >>>     for arg in args:
      >>>         print(arg)
      >>>
      >>> show(1)
      1
      >>> show(1, 2)
      1
      2

   このように引数の前に * をつけると，
   いくつでも後で値を決めることができる引数になります．

   こういうのもあります::

      >>> def show(**kwargs):
      >>>     return ["{}: {}".format(k, v) for k, v in kwargs.items()]
      >>> show(a=1)
      ['a: 1']
      >>> show(a=1, b=2)
      ['a: 1', 'b: 2']

   何が起きたか考えてみてください．

   - これら二つの例にはタプルや辞書型が関わってきます．


クラス
--------------------------------------------

クラスとは，雑に説明すれば，型です．
そう，型，そのものを自分で作ることができるのです．

型とは何かと考えると，基本的には名詞，つまりデータだったはずです．
そして，python の型は, 何ができるのかによって，定義されます．
つまり，その名詞が目的語になる関数をもっています．

TODO アプリ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

例えば，簡単な TODO アプリを作ってみましょう．

TODO アプリには何が必要ですか？
アプリを作成するときには，それが何をすることができるのかを
まず言葉で説明をする習慣をつけましょう．

TODO アプリは何ができますか？

以下に，筆者が考える TODO アプリの最小限の説明を書きます．

- TODO LIST は TODO を管理する
   - TODO LIST は TODO を登録できる
   - TODO LIST は TODO を確認できる
   - TODO LIST は TODO を修了できる
   - TODO LIST は TODO を消せる

まあ，こんなところですかね．
ここで，これらの文章を見てみると，
全て名詞 TODO LIST および TODO が出てきていることに気がつきます
（というかそうしたのです）．

つまり, 今作りたい TODO アプリは 2 つのクラスのみで作成することが出来そうです．
そう, TodoList クラスと Todo クラスです．

TODO クラス
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

まずは Todo クラスに関して，
もう少し詳しく考えてみましょうか．

TODO ってなんですか？

TODO は一般に何をやるのかの情報をまとめたものです．

これは以下のように書きます．

- この辺から，対話環境で記述することが難しくなると思います．
   - 一度スクリプトに書いてから実行してみてください．

.. code-block:: python

   class Todo(object):

       text = ""

       def __init__(self, text):
           self.text = text

   if __name__ == "__main__":
       todo = Todo("TODO")
       print(todo.text)

これで，新しく Todo クラスが使えるようになりました．
使い方は以下の通りです．

.. code-block:: bash

   $ python todo.py
   TODO

さて，ここまでで何をやったのかを説明しましょう．
このスクリプトでは Todo  クラスを作成しています．
:code:`class Todo` から始まる部分です．

ここにやりたいことを書いていきます．
TODO は "何をやるのかの情報" を保存します．
:code:`text=""` と書かれている部分がそれですね．
この :code:`text` に"何をやるのかの情報"が入ります．

インスタンス化
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ん，でも :code:`text` には "" しか入らないじゃんと思った皆様は，
今までの話に付いて来れています．
でも，スクリプトを実行した結果は "TODO" となっています．
なんででしょう？

この謎を解く鍵が, :code:`__init__()` 関数です.
上のコードには以下のように書かれています．

.. code-block:: python

   def __init__(self, text):
       self.text = text

この関数は引数を二つ持ちます．
:code:`self` と :code:`text` です
(python の関数は引数名に制約を持たないので別の名前でもよいのです)．

関数の中身をみると，:code:`text` の値を :code:`self.text` に入れています．
では :code:`self` とは何かというと，クラス Todo そのものです（自分自身だから self ）.
つまりこの関数を実行すると, :code:`__init__(self, text)` の :code:`text` が
クラス :code:`todo` に登録されます．

実際に :code:`text` を登録している場所はどこでしょうか?
これは以下の部分ですね．

.. code-block:: python

   if __name__ == "__main__":
       todo = Todo("TODO")
       print(todo.text)

ここまでで質問ありますか？

... 無いと困ります．

- ん？ :code:`__init__` なんて使っていないけど？ と思った皆様はとても，勘が良いです.
- ん？ :code:`self` は？ と思った皆様もここまでの話によくついて来れています．
- :code:`if __name__ == "__main__":` って何と思った方，後で説明します．

python のクラスにはいくつか特別な名前の関数が存在します．
:code:`__init__()` は正にそれで，クラスをインスタンス化する際に使います．

インスタンス化とは，具体化のことです．

今回作成している Todo クラスは,
ユーザによって毎回異なる内容が登録されるはずです．

でも，今までやってきた用に変数に直接値を入れてしまうと，
その値を変更することができません.

そのような時に（人類が古い歴史の中で編み出した）秘策が抽象化です．

例えば，我々人間は，一人一人，身長も違えば，体重も違います．
髪の色も，皮膚の色も，もしかしたら手の数だって違うのです．

それでも，どんな人間でも身長が存在するし，体重が存在します．
このように，個別具体的なことは一旦わすれて，あるモノが，
どのような属性を持っているのかを考えることをここでは抽象化と言っています．

言い換えれば, 先の :code:`Todo` クラスは，
TODO を一つの属性 :code:`text` を持つものだと抽象化したものです．
で，この属性 :code:`text` に具体的な値を入れることを，
プログラミングの世界では インスタンス化といいます．

.. note:: プログラミングとギリシャ哲学

   ここで，哲学に詳しいかたは，
   きっと，アリストテレスや，プラトンを思い出したことでしょう．
   そう，イディア論です．

   クラス指向のプログラミングは，正しく，イディア論の実戦です．
   ある名詞を，どのように抽象化するのかこそが，
   プログラマの腕の見せ所なのですから．

   だからそこ，プログラミングを行うには，
   それが何であるのかを常に言葉で説明する習慣をつけた方が良いです．

さて，次の疑問．

:code:`__init__()` の第一引数は :code:`self` でした．
しかし， :code:`todo=Todo("TODO")` には :code:`self` がありません．
これはなんででしょう．

これもクラス関数の特殊な事情です．
Python のクラス関数は **第一引数が self である** というルールが存在します．

ちょっと，試してみましょう．

.. code-block:: python

   class Todo(object):

       text = ""

       def __init__(text):
           self.text = text

   if __name__ == "__main__":
       todo = Todo("TODO")
       print(todo.text)

違いは,  :code:`__init__(text):` の様に self を無くしただけです．
実行してみましょう．

.. code-block:: bash

   $ python todo.py
   Traceback (most recent call last):
   File "todo.py", line 68, in <module>
       todo = Todo("TODO")
   TypeError: __init__() takes 1 positional argument but 2 were given

結果はエラーです．
ここでエラーコードをよく読むと（プログラミングが上手くなる人間は何時もエラーを怖
れません.まず英語を読みましょう）.

TypeError: __init__() takes 1 positional argument but 2 were given

どういう意味ですか？
この結果に納得行きますか？

納得できるまで考えてください．

- そして，直すのを忘れないでください．

直したら，次に行きます．

実行カ所
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

最後の疑問は :code:`if __name__ == "__main__":` って何という疑問でした．

これは決まり事なので，簡単に説明します(本当は理由があるけど)．

:code:`if __name__ == "__main__":` はここから先には，
文章を書くよという意味です．

より正確には :code:`python xxx.py` の形でスクリプトを実行した時に，
python さんに実行して貰うカ所になります．

今説明をしているクラスや，いままでに説明をした関数は，
自分で単語を決めている部分です．
でも，誰かに説明をするときには，普通単語だけでやり取りをすることはありません(”んだけでやり取りができるほど，python とは仲良くなれないのです)．
何処かで，自分の決めた単語を使って文として，何をしてほしいのかを書く必要があります．

その，ここから先が文ですよ．という宣言が，
:code:`if __name__ == "__main__":` です．

ここは以下のようになっています．

.. code-block:: python

   if __name__ == "__main__":
       todo = Todo("TODO")
       print(todo.text)

文としては以下のことが書かれていますね．

- まず，Todo クラスをインスタンス化してください．
    - その時には， :code:`"TODO"` という値を属性にいれてください．
- 次に，:code:`todo` インスタンスの :code:`text` という属性を表示してください

こういう文を python に伝えているので，実行結果は "TODO" になりました．

TODO クラスを拡張する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

さて, ここまでで,
class :code:`Todo` を使うと,
何をやりたいのかを管理することができるようになりました.

ただ, TODO アプリというと,
普通はその仕事が終わったのかどうなのかを管理できるはずです.

では, それをできるようにしてみましょう.

.. code-block:: python

   class Todo(object):

       text = ""
       is_finished = False

       def __init__(self, text):
           self.text = text

       def set_is_finish(self, x):
           self.is_finished = x

   if __name__ == "__main__":
       todo = Todo("TODO")
       print(todo.text)
       print(todo.is_finished)

       todo.set_is_finish(True)
       print(todo.is_finished)

実行してみると以下のようになります::

   $ python todo.py
   'TODO'
   False
   True

先の例と同じように, :code:`if __name__ == "__main__":` 以下が,
ユーザの動作です.

今回は, 最初に, :code:`Todo("TODO")` とすることで,
ユーザは TODO の内容を入力しています.

その上で, その内容と, 終わったかどうかを表示しています.
これが一つ目の出力結果と二つ目の出力結果ですね.

それから時間が経って, 最終的にその TODO が終了したとします.
その際の挙動が :code:`todo.set_is_finish(True)` ですね.
そうすると, いままで :code:`False` であった :code:`todo.is_finished` が
:code:`True` に変わりました.
これが三つ目の出力結果です.


実習
~~~~~~~~~~~~~~~~~~~~~~~~

さて，ここからは実習をしましょう．

このスクリプトでは，
一つの TODO を管理できるだけでした.
これでは TODO LIST アプリとは言えないので,
複数の TODO を管理できるようにしてみましょう.

また, 今までは, :code:`if __main__ == __name__:` 以下にユーザの
作業を書いていました.
これでは, 実際のアプリっぽくないので
以下の挙動になるように種々クラスや実行文を書き換えてください．

1. 何も引数を与えずに実行すると今までに登録された全ての todo を表示します::

   # TODO の登録がない場合
   $ python todo.py

   # TODO の登録がある場合
   $ python todo.py
   - [False] TODO 1 (0)
   - [False] TODO 2 (1)
   - [False] TODO 3 (2)
2. --add "内容" を加えると新規 todo を追加します::

   # TODO の登録がない場合
   $ python todo.py --add "やること"
   - [False] やること (0)

   # TODO の登録がすでにあった場合
   $ python todo.py --add "やること"
   - [False] TODO (0)
   - [False] やること (1)
3. --fininish id を加えるとその ID の TODO を修了します::

   $ python todo.py --finish 0
   - [True] TODO 1 (0)
   - [False] TODO 2 (1)
   - [False] TODO 3 (2)
   - [False] やること (3)
4. --delete id を加えるとその ID の TODO を削除します::

   $ python todo.py --delete 1
   - [True] TODO 1 (0)
   - [False] TODO 3 (1)
   - [False] やること (2)

ヒント:
   - 筆者は 1 つのクラスと 3 つの関数でこれを行いました.
   - ユーザの入力部分に関しては, 以下のノートに記載しています.
   - プログラミングではデータを保存する際には基本的にファイルへの入出力が必要です.
      - この方法に関しては with 構文の説明で触れています.
      - ただし, ファイルに保存を行うには, Todo オブジェクトの内容を一度文字列化する必要があります
      - 同様に, ファイルを読み込むと, その内容は文字列型になります.
        これを何とかして Todo オブジェクトに変更する必要があります.

.. note:: 引数入力

   この課題では, 実際にユーザに情報を入力させます.
   この方法に関しては今まで 説明していなかったので,
   ここで説明させてください.

   .. code-block:: python

      class Todo(object):

         text = ""
         is_finished = False

         def __init__(self, text):
            self.text = text

         def set_is_finish(self, x):
            self.is_finished = x

      if __name__ == "__main__":
         from argparse import ArgumentParser
         parser = ArgumentParser()
         parser.add_argument("--add", type=str)
         args = parser.parse_args()

         if args.add:
            todo = Todo(args.add)
            print(todo.text)

   実行してみましょう．

   .. code-block:: bash

      $ python todo.py

   何も出ませんね．
   これは以下のように使用します．

   .. code-block:: bash

      $ python todo.py --add test
      test
      $ python todo.py --add 頑張る
      頑張る

   何が変わったのかというと,
   python を実行する際に, :code:`--add "やりたい内容"` を付け加えているときと,
   そうじゃない時とで実行する内容を変えることができたのです.

   これを決めている部分は :code:`if __name__ -- "__main__":` 以下の行,
   上から4 行目までです.

   特に重要な部分は :code:`parser.add_argument("--add", type=str)` です.
   この関数は, 第一引数に, 実行時にどのようなオプションを使うのかを書きます.
   第二引数は, そのオプションに与えられる値の型がなんなのかを書きます.

   今回の場合では, 実行時に "--add" というオプションが書かれた時には,
   Todo に登録する内容が, その後に続くと決めたいので,
   :code:`parser.add_argument` の第二引数は str 型になります.

   この :code:`parser.add_argument` は :code:`args = parser.parse_args()` を
   書く前であれば何回でも使えます.

   ここで :code:`Todo(args.add)` に注目してくさい.
   ここには, やることの内容がはいるのでした.
   つまり :code:`args.add` にはユーザの入力が入っていることがわかります.

   どうように, 例えば :code:`parser.add_argument("--text", type=str)`
   とした場合にはユーザの入力は :code:`args.text` でとりだすことができます.
