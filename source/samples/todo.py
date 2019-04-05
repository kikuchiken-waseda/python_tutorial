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
