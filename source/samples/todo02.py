# -*- coding: utf-8 -*
"""Todo リストアプリ.

このモジュールは, 2019 年菊池研究室春季セミナー合宿，プログラミング入門において
クラスの概念を説明するために作成されたものです．

このモジュールではクラスの概念を説明するために TODO LIST の作成を行っています．

Example:
    この TODO アプリでできることは以下の通りです:
        - Todo の確認
        - Todo の登録
        - Todo の修了
        - Todo の削除

    何も引数を与えずに実行すると今までに登録された全ての todo を表示します::

        $ python todo.py
        - [] TODO 1 (0)
        - [] TODO 2 (1)
        - [] TODO 3 (2)

    --add "内容" を加えると新規 todo を追加します::
        $ python todo.py --add "やること"
        - [] TODO 1 (0)
        - [] TODO 2 (1)
        - [] TODO 3 (2)
        - [] やること (3)
    --fin id を加えるとその ID の TODO を修了します::
        $ python todo.py --fin 1
        - [x] TODO 1 (0)
        - [] TODO 2 (1)
        - [] TODO 3 (2)
        - [] やること (3)
    --del id を加えるとその ID の TODO を削除します::
        $ python todo.py --del 1
        - [] TODO 2 (2)
        - [] TODO 3 (3)
        - [] やること (4)

"""


class Todo(object):
    """Todo class.

    ユーザのやることを管理します．

    Attributes:
        text (str): todo の内容
        text (id): todo の id
    """

    text = ""

    def __init__(text):
        """インスタンス化の挙動を定義します.

        Args:
            text (str): todo の内容
            id (int): todo の id
        """
        self.text = text


if __name__ == "__main__":

    todo = Todo("TODO")
    print(todo.text)
