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
        is_finished (bool): todo が修了したか否か
    """

    text = ""
    is_finished = False

    def __init__(self, text):
        """インスタンス化の挙動を定義します.

        Args:
            text (str): todo の内容
            id (int): todo の id
        """
        self.text = text

    def set_is_finished(self, y):
        """インスタンスを修了状態にします."""
        self.is_finished = y


def save(todos):
    texts = []
    for todo in todos:
        texts.append("{} {}".format(todo.text, todo.is_finished))
    with open("./tmp.txt", "w") as file:
       file.write("\n".join(texts))

def show(todos):
    for i, todo in enumerate(todos):
        print("- [{}]: {} ({})".format(todo.is_finished, todo.text, i))


def load():
    from os import path
    todos = []
    if path.exists("./tmp.txt"):
        with open("tmp.txt", "r") as file:
            text = file.read()
        lines = text.split("\n")
        for line in lines:
            datas = line.split()
            todo = Todo(datas[0])
            todo.set_is_finished(datas[1])
            todos.append(todo)
    return todos


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("--add", type=str)
    parser.add_argument("--finish", type=int)
    parser.add_argument("--delete", type=int)
    args = parser.parse_args()

    todos = load()
    if args.add:
        todos.append(Todo(args.add))
        save(todos)
    if args.delete is not None:
        todos.pop(args.delete)
        save(todos)
    if args.finish is not None:
        todos[args.finish].set_is_finished(True)
        save(todos)
    show(todos)
