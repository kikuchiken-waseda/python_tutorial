if __name__ == "__main__":
    import tasks
    print('<first task>')
    # ここでタスク起動　(runタスク)
    worker = tasks.run.delay()
    while not worker.ready():
        pass
    else:
        print(worker.result)

    print('<second task>')
    # ここでタスク起動　(calcタスク)
    worker = tasks.calc.delay(100, 200)
    while not worker.ready():
        pass
    else:
        print(worker.result)
