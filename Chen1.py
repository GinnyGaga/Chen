# -*- coding: utf-8 -*-


class Tech:
    def __init__(self, name: str, stus: list):
        self.name = name
        self.stus = stus

    def get_stus_len(self):
        if self.stus is None:
            return 0
        return len(self.stus)


class Stu:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


def main():
    l = []
    l.extend([
        Tech("su", [
            Stu("A1", "男"),
            Stu("A2", "男"),
            Stu("B1", "女"),
            Stu("B2", "女"),
        ]),
        Tech("chen", [
            Stu("C1", "男"),
            Stu("C2", "男"),
            Stu("C3", "男"),
            Stu("D1", "女"),
            Stu("D2", "女"),
            Stu("D3", "女"),
        ])
    ])

    stus_len = 0
    for i in l:
        stus_len += i.get_stus_len()
    print(stus_len)


if __name__ == '__main__':
    main()

