===========================
JOB QUEING 入門
===========================

- 文責: takuya.waseda.1119@gmail.com
- 作成日: 2020-04-28


.. contents::
    :depth: 2

ここでは JOB QUEING と呼ばれる処理について説明をします.
JOB QUEING とは非同期処理や定期実行のように,
処理を行う予定だけを立てて, あとでその結果を使うような処理のことを指します.

JOB QUEING という言い方には耳慣れないものがあるでしょうが、
これは我々が普段やっている処理です.
例えば、買い物をすることを考えてください.

昔からあるタイプのお店では、
まずお客さんは店員さんに話しかけます。
そこから店員さんに色々な要望を伝え、欲しいものが見つかったら買い物を行います
(そういうお店行ったことあります？吉祥寺には多いのですよ)。
このような古いタイプのお店では、一度に処理できる仕事（お客さん）の数は
店員さんの数だけです.
たとえば, 店員さんが一人しかいない時に 10 人のお客が来たとします.
一人の客は何を買うのかを決めるのに 5 分程度掛かるとして、
お金のやり取りをするのに 1 分程度掛かるとしましょう.
この場合、10人目のお客さんが買い物を済ませるためには, 60 分かかってしまいます(だ
から流行っていないんだよな、あの店...).

一方, 一般的なお店では, お客は勝手に店内を見回りますよね。
こうすると、１人ずつ相手している時と比較して大きく時間を短縮することができます.
ただし、それぞれのお客さんは少し待つ作業も必要です。
そうレジに並ぶタイミングです.
で、店員さんが空いた時（自分の順番になったとき）にお金を払います.
このようにすると, 先程の例だとしても,
10 人目のお客さんの待ち時間は, 10 分で済みます.

この方法をプログラミングに利用した手法のことを
JOB QUEING と(あるいは単にキューイングとも)いいます.
キューイングでは, キューにタスクを貯めて行きますを貯めて行きます
(お店の例では買いたいものを探すこと).
そしてワーカー(お店の例ではお客さん)が適宜タスクを受け取り(勝手に買い物を始め),
終わったタイミングで通知をします(レジに並びます).

このチュートリアルではこのキューイングの作業を python で行っていく方法について説
明をします.

環境設定
==========================================

:code:`python` でキューイングを行う際に便利なライブラリは :code:`celery` です.
ただし、これを利用するには, :code:`redis` というデータベースが必要になります.

Mac OS の場合 :code:`redis` は :code:`brew` から導入することができます::

    $ brew install redis

.. note:: celery と redis

   :code:`redis` は何に使われるのでしょうか?

   :code:`redis` はキュー、つまりタスクを記録しておく
   TODO リストのようなものとして利用されます.

   :code:`celery` はこのキューとして使えるものがあれば何でもよいので,
   :code:`redis` が必須というのは本当はちょっと言い過ぎです.
   しかし (特に日本では) :code:`redis` を利用した説明が一番多いので,
   このチュートリアルでも :code:`redis` を利用します.

また, :code:`celery` は :code:`pip` コマンドから導入可能です::


    $ pip install celery redis
