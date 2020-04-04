===========================
WEB API 入門: 応用課題
===========================

- 文責: qh73xe
- 作成日: 2020-04-04


.. contents::
    :depth: 2

ここからは応用, つまり, python を使ったアプリ開発を説明します.
アプリ開発の最初のお題は WEB-API です.

近年のアプリケーションは所謂、サバクラ(サーバー&クライアント) を前提としたものが大多数を占めています.
例えば, facebook とか line とか Instagram, slack のようなチャット, SNS サービスもそうですし,
google のサービスも大抵がサバクラシステムです.

こういうシステムは大抵ブラウザ(例えば chrome とか)で動きます.

ところで、皆様はサーバーって何か、ご存知でしょうか?
普通のPC（皆様の目の前にあるMAC） とは何が違うのでしょうか?

実は、(誤解を恐れず言うのなら)そんなに違いはありません.
サーバー機といっても実は単なるPCです(今、丁度研究室で動いでいるので, 実機が見たければ, 見ることができますよ).
少しだけ、違う部分を挙げるなら、サーバー機は色々な人が情報にアクセスすることができます(皆様のPCが色々な人に見られたら結構いやですよね)。
一方、皆様のPCは色々なサーバーの情報をみることができます.

つまり, 皆が見て色々作業をするPCをサーバーと読んで、
そのサーバーから情報を貰うPC(皆様のPC)のことをクライアントと呼ぶのです.
で皆で見るために使用されているルールが例えば http プロトコルであったり,
WEB とか言われているやつです.

最初のアプリ
--------------------------------------

まあ, 前置きはこの程度にしておいて,
早速アプリを作ってみましょう.

今回は, tornado というツールを使います(これは facebook が作成したツールです).

.. note:: Django

   python で WEB-API を作ろうとした場合,
   一番の大御所は, Django というライブラリです.
   これは開発の初期段階では google が大きく関わっていて,
   現在でも Instagram に利用されていたりするライブラリです.

   このライブラリはとても素晴らしいものですが,
   覚えることが多いです.

   一方 tornado は覚えることは少く使用できるので,
   簡単なものをチョロッと作る場合には, tornado を使います.

   django  に興味がある方は, 公式のチュートリアルを試してみてください.
   あれは読む度に発見のあるとてもよいドキュメントです.

まずは, tornado を使用できるようにしましょう.
tornado を導入するには以下のコマンドを使います::

    $ pip3 install tornado


今回のテーマはサバクラシステムで、クライアントはもう既に存在する(皆様のPCのブラウザがクライアントです)ので,
作っていくものはサーバーになります.


そのまま, :code:`server.py` としましょう.
内容は以下の通りにしてください::

    import tornado.web

    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello, world")

    def make_app():
        return tornado.web.Application([
            (r"/", MainHandler),
        ])

    if __name__ == "__main__":
        app = make_app()
        app.listen(8888)
        tornado.ioloop.IOLoop.current().start()

かけましたでしょうか？
かけたら、これを実行します::

    $ python3 server.py

さあ、どうでしょう.
何も起きませんね.
何故ですか？

クライアントを使っていないからです.

ブラウザを立ち上げ, 以下の URL にアクセスしてみてください.

- http://localhost:8888

わー, すごい, なんと文字が出てきましたね.

なんとも面白くもない例ですが,
実は凄いことをしています.

なぜ, "Hello, world" と出て来たのかわかりますか？
別の文字に変えることはできますか?

やってみてください.

- なお, :code:`server.py` を止めるには Ctrl + C を押します.

この例はとてもシンプルな例ですが,
サーバーとしての機能を充分に果たしています（クライアントに伝えるべき情報を伝えているので）.

:code:`server.py` には一つのクラスと, 一つの関数,
そして :code:`if __name__ == "__main__":` で書かれた実行部分が書かれています.
このなかで, サーバー, つまりクライアントに情報を渡している部分はどれでしょう.

そう, :code:`MainHandler` クラスですね.
より正確に言えば :code:`MainHandler` クラスの :code:`get` 関数です.
さらにデータを送っている部分だけでいれば, :code:`self.write` 関数になります.

ここでなんで :code:`self.write` 関数が動くのか説明できる方はいますか？
だって, そんな関数どこにも書いていないじゃないですか.

- この問の意味が分からない方は :doc:`/2019/python/first` のクラスの説明をよく読み直してください.

その答えのヒントは :code:`MainHandler` クラスの最初の行にあります.
ここには以下のように書かれています::

    class MainHandler(tornado.web.RequestHandler):

:doc:`/2019/python/first`  でやったクラスとは :code:`()` の中身が異なりますね.
これは, :code:`tornado.web.RequestHandler` に書かれている関数をすべて使えるようにするという意味になります.
こういう風に、別の誰かが書いたクラスの持つ関数を使える新しいクラスを作ることを継承といいます.

つまり, なんで自分では書いていない :code:`self.write` という関数が使えるのかというと,
:code:`tornado.web.RequestHandler` というクラスの中に誰かが先に書いておいてくれたからな訳です.
このようにすることで, 具体的にどうやってブラウザに情報を伝えるのかを知らなくても,
ただ, 伝えたい情報を :code:`self.write` 関数の中にいれてあげればサーバーが作れる訳です.

どうです？ちょっとは凄さが分かっていただけたでしょうか？

ともかく, self.write の中にブラウザに表示をしたい値(文字列)を書けば良いだけです。
あとは, どんなことを書いてもよいです.

例えば一寸計算をしてみましょう::

    import tornado.web

    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            x = 1 + 5
            self.write(str(x))

    def make_app():
        return tornado.web.Application([
            (r"/", MainHandler),
        ])

    if __name__ == "__main__":
        app = make_app()
        app.listen(8888)
        tornado.ioloop.IOLoop.current().start()

さて, このコードを実行した結果ブラウザには何が表示されるでしょうか?

望みの値になったら、一寸ここまでのおさらいをしましょう.

:doc:`/2020/python/computer_science_basics` ではフィボナッチ数列を計算する関数を作ってみました.
これを利用して, n=10 の場合のフィボナッチ数列を計算してくれるサーバーを作成してみてください。
それができたら、最初のアプリ作成は終了にします.

入力を受け取る
-------------------------------------------

んーでも... と思っている方もいるかもしれません.
折角フィボナッチ数列を出せたとしても(出せて何がうれしいのだという話はおいておいて),
n = 10 だけしか出せないのではどうしようもありません.

もっと色々な n で計算させることはできないのでしょうか？

言い換えれば, クライアント側で n を指定することはできないのでしょうか？

当然可能です.

次のコードを書いてみてください(名前は :code:`squared_server.py` にしましょうか)::

    import tornado.web

    class SquaredHandler(tornado.web.RequestHandler):
        def get(self):
            kwargs = self.request.arguments
            x = int(kwargs.get("x", [0])[0])
            self.write(str(x**2))

    def make_app():
        return tornado.web.Application([
            (r"/", SquaredHandler),
        ])

    if __name__ == "__main__":
        app = make_app()
        app.listen(8888)
        tornado.ioloop.IOLoop.current().start()

さて,  http://localhost:8888 にアクセスしてみましょうか.
この結果は 0 になります.

続いて http://localhost:8888?x=2 にアクセスしてみてください.
この結果は 4 になります.

それぞれ何が起きているかわかりますでしょうか？

まず, http://localhost:8888  にアクセスをした場合, 変数 :code:`kwargs` には空の辞書が入ります.
これは辞書型ですので, :code:`get` 関数が使えます.
辞書型の :code:`get` 関数は第一引数の key があった場合, その value を返します.
では無かった場合にはどうなるのでしょうか？

その場合には第二引数に与えた値, つまり :code:`[0]` を返します.
http://localhost:8888  にアクセスした場合には, :code:`{}.get("x", [0])` ということですから、
:code:`x` という key は存在しません.
そのため, :code:`[0]` になります.

これは 0 ではないことに気を付けてください.
0 という値が一つだけ入ったリストです(なぜこんなことをしているのかというと, 値が入っていた場合にもその値が一つだけ入ったリストが返却されるからです).
そのため, その最初の値, つまり :code:`[0][0]` = :code:`int(0)` が変数 :code:`x` に入ります.
最後に関数 :code:`self.write(str(x**2))` をしているので 0 の二乗で 0 が表示される訳です.

では同様に http://localhost:8888?x=2 の場合にそれぞれの変数の中身はどのような値になり、最終的に 4 が出力されるのでしょうか？
少し考えてみてください.

納得できる答えができたら, 上記コードを少し変えてみてください。
例えば, http://localhost:8888?x=2&y=2 とした場合には 4,
http://localhost:8888?x=2&y=3 とした場合には 6, http://localhost:8888?x=3&y=3  とした場合には 9 を返すサーバーを作ることができるでしょうか？

また、先程作成した :code:`fib(10)` の計算結果を返すサーバーを利用して, n をユーザが決めることができるサーバーを作れるでしょうか？


POST METHOD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

さて, 上で説明をした URL を使った入力方法のことを URL クエリと呼びます.
これはよく見てみると例えば Gmail とか, github とか,  Slack とか, amazon とかで見かける方法です.

- 我々プログラマはしばしば URL を観察してこれらのツールを楽に使う方法を発見します.

ですが, よく見る WEB アプリでは, ユーザに態々 URL を変更させたりしません.
なんか入力する画面があってそこに値を入力すると結果が帰ってきます.

こういう入力方法を行うためには :code:`POST method` を知っておく必要があります.

また :code:`MainHadler` クラスを書き換えます::

    import tornado.web

    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write(''.join([
                '<html>',
                '<body>',
                '<form action="/" method="POST">',
                '<input type="text" name="x">',
                '<input type="text" name="y">',
                '<input type="submit" value="Submit">'
                '</form>',
                '</body>',
                '</html>'
            ]))
        def post(self):
            self.set_header("Content-Type", "text/plain")
            x = int(self.get_body_argument("x", 0))
            y = int(self.get_body_argument("y", 0))
            self.write("x + y = {}".format(x + y))

    def make_app():
        return tornado.web.Application([
            (r"/", MainHandler),
        ])

    if __name__ == "__main__":
        app = make_app()
        app.listen(8888)
        tornado.ioloop.IOLoop.current().start()


さて, http://localhost:8888/ にアクセスしてみると,
今度は form (入力する場所とボタン) が表示されます.
適当な数字を入れて, submit ボタンを押すと,
2つの入力が合計された値が出てきます.

では :code:`MainHandler` を見てみましょう.
関数の数が今までと違いますね.
新しく :code:`post()` が定義されています.

コードの中で実際に足し算をしている場所はこの :code:`post` 関数なので, submit ボタンを押した後に呼び出される関数なのだと分かります.
で入力の受取りは :code:`self.get_body_argument()` を使っています.

ここで引数は :code:`"x"` や :code:`"y"` と書いているので, 多分 submit ボタンを押す前には,
x, や y が定義されているのでしょう.

じゃあ, submit ボタンを押す前の表示はどの関数なのでしょうか?
これは多分, 今まで書いてきた :code:`get()` (だって submit って書いてあります).

で, x, y はどこなのかと考えると, :code:`'<input type="text" name="x">'` と書いてあるのが分かります.
つまり,  :code:`'<input type="text" name="x">'`  の :code:`name="x"` の部分でどのような辞書が造られるのかが決まります.
後はこれに習えば, 自由な入力を作ることができるはずです.

更に :code:`input` と書いてある部分は,  :code:`form` と書かれた文字列に囲まれていると
気がつけた人は大変よろしいです.

:code:`'<form action="/" method="POST">'` の意味は, その中身（ここでは 3 つの input）を,
action で書かれた場所に POST メゾットで送りますよという意味です.
だからこそ, URL "/" に紐付いている :code:`MainHandler` クラスの :code:`post()` が機能したのです.

さあ, これで入出力も自由にできるようになりました.

- このチュートリアルでは基本的に CSS/HTML については話しません.
- やや詳しい人に追記しておくと, put その他 HTML method は同様の記法で機能します.

では, :code:`post` メゾットが理解できたのかを確認するために再び :code:`fib` 関数を使いましょう.

まず, input が一つだけの :code:`get` 関数を作ってみてください.
序で, 任意の n のフィボナッチ数列を計算できる :code:`post` 関数を作ってみてください.

ここまでの練習課題
--------------------------------------

さて, ここまでの説明で皆様はユーザの入力を受け取り結果を返すサーバーを作成することができるようになったはずです.
では, 単純な計算だけでなく, 少しアプリケーションっぽいものを作成してみましょう.

元になるものは :doc:`/2019/python/first`  でやった TODO アプリです.
これをサーバーにしましょう.

作りたいものは以下の通りです.

1. 最初の画面では, 新規に作成する TODO のフォームが存在する
2. フォームには, TODO の内容が入力される
3. サブミットボタンをおすと 新規TODO が登録される
4. この画面には,  最初の画面画面に戻るボタンが存在する
5. 上記ボタンを押すと, 新規に作成する TODO のフォームと今迄登録した TODO の一覧が見える

まずはここまで作成してみましょう.
余力のある方は, 以下の状態にまで, アプリを作ってみてください.

6. それぞれの TODO 一覧の横には終了ボタンがある
7. そのボタンをクリックすると、該当のTODOがなくなる(見えなくなる)

どうでしょう？できるでしょうか？
