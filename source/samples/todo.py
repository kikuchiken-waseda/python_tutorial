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

    def add(self, todo):
        """todo を追加する.

        Args:
            todo (Todo): 追加する TODO.
        """
        self.todos.append(todo)

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
    todo_list = TodoList()

    # TODO を沢山加える
    todo_list.add(Todo("TODO1"))
    todo_list.add(Todo("TODO2"))
    todo_list.add(Todo("TODO3"))

    # TODO を表示する
    todo_list.show()
    print()

    # 最初の TODO を削除する
    todo_list.delete(0)
    todo_list.show()
    print()

    todo_list.finish(0)
    todo_list.show()
    print()
