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

    def finish(self):
        """インスタンスを修了状態にします."""
        self.is_finished = True


class TodoList(object):
    """Todo list クラス.

    複数の todo を管理します.

    Attributes:
        todos (list) : Todo インスタンスを入れておくリストです

    """

    todos = []

    def __init__(self):
        from os import path
        if path.exists("./data.txt"):
            with open("./data.txt", "r") as f:
                for line in f:
                    self.add(line.strip())

    def save(self):
        text = "\n".join([
            todo.text
            for todo in self.todos
        ])
        with open("./data.txt", mode='w') as f:
            f.write(text)

    def add(self, todo):
        """todo を追加する.

        Args:
            todo (Todo): 追加する TODO.
        """
        self.todos.append(Todo(todo))

    def show(self):
        """todo list を表示する."""
        for i, todo in enumerate(self.todos):
            if todo.is_finished:
                check = "X"
            else:
                check = ""
            print("- [{}] {} ({})".format(check, todo.text, str(i)))

    def delete(self, i):
        """todo を削除する.

        Args:
            i (int): 削除する Todo のインデックス
        """
        self.todos.pop(i)

    def finish(self, i):
        """todo を修了する.

        Args:
            i (int): 修了する Todo のインデックス
        """
        self.todos[i].finish()


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("--add", type=str, default="")
    parser.add_argument("--fin", type=str, default="")
    parser.add_argument("--delete", type=str, default="")
    args = parser.parse_args()

    todo_list = TodoList()
    if args.add:
        todo_list.add(args.add)
        todo_list.save()

    if args.delete:
        todo_list.delete(int(args.delete))
        todo_list.save()

    if args.fin:
        todo_list.finish(int(args.fin))
        todo_list.save()

    todo_list.show()
