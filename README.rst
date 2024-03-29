================================
2020 年度春季新歓セミナー資料
================================

このレポジトリには, 春季新歓セミナーの資料をまとめます.

資料作成者へ
================================

記述形式
--------------------------------------------

各種資料の作成には, :code:`python/sphinx` を利用します.

- https://www.sphinx-doc.org/ja/master/

このライブラリは, :code:`python` のライブラリ用ドキュメントを
記述する際に, 最も一般的に使用されているツールです.

- 公式ドキュメントからしてこのツールを使用しています

各種記述に関しては :code:`reStructuredText` 形式で記述するべきです.

- :code:`markdown` と比較して圧倒的に表現力に優れています
    - 厳密には :code:`markdown` に対応することはできなくはないですが **敢えて対応していない** ことを考慮してください.

使用する python 環境
--------------------------------------------

このドキュメント自身のライブラリ管理は :code:`venv` を前提にしています.
記述される :code:`python` のバージョンは :code:`python 3.8.2` です.
および各種ライブラリのバージョンを統一するために必ず上記環境を利用してください.

各種開発環境の導入には以下のコマンドを利用してください::

    $ python3 -m venv venv

ここで利用する :code:`venv` は python 3.7 以上であればデフォルトで利用可能です.

- 7 系の大いなる進捗です.

勿論, 仮想環境を自由に利用できるなら、お好きなものを使用していただいて構いません.

ドキュメント環境の作成
--------------------------------------------

ドキュメント環境を入手するには
このレポジトリルートから以下のコマンドを実行してください::

    $ . venv/bin/activate
    $ pip install -r ./requirements.txt


コード規約
--------------------------------------------

各種コードに関しては
最低でも :code:`PEP8` に準拠するようにしてください.

それと矛盾しない形で :code:`google` の
コードスタイルに準拠してください.

各種記述に関しては :code:`flake8` というツールで
チェックを行います。

これに引っ掛る場合, そのプルリクエストはリジェクトするので,
各人コードチェックはしっかりと行ってください.

記述ツール
--------------------------------------------

Document そのものには sphinx を利用しています.

- https://www.sphinx-doc.org/ja/master/

各種環境設定が終了している場合以下のコマンドを入力すると
html ドキュメントが作成されます::

    $ make html

- なお, HTML が作成されるディレクトリは, レポジトリroot 直下 build/html 以下です.
- また, master の上記ディレクトリが更新されると以下のURLが更新されることに注意してください.

- https://kikuchiken-waseda.github.io/python_tutorial/build/html/

加えて, このリポジトリディレクトリ直下で以下のコマンドを入力すると,
各種 source ファイルを監視し, 変更があった場合に自動ビルド, 簡易サーバーを立ててドキュメント確認をすることが可能です::

    $ make livehtml

- これはフォアグラウンド処理なので、Tmux 等で画面分割をすると楽です.
- この場合,デフォルトでは http://localhost:8000/ にアクセスするとビルド結果をみることができます.


ドキュメントの公開
--------------------------------------------

ドキュメントは github page にて公開することにします.
html にビルド済みのドキュメントは以下のコマンドから公開可能です.

.. code-block:: bash

    $ sh ./deploy.sh

公開後は以下の URL から更新を確認してください.

https://kikuchiken-waseda.github.io/python_tutorial/
