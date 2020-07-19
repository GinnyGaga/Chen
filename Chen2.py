
def main():
    su = {
        "男": ["A1", "A2"],
        "女": ["B1", "B2"]
    }
    chen = {
        "男": ["C1", "C2", "C3"],
        "女": ["D1", "D2", "D3"]
    }

    a = {
        "bbb": {
            "ccc": 111,
            "ddd": 222
        }
    }
    for k, v in a.items():
        for i, j in v.items():
            print(j)

    su_len = 0
    for _, v in su.items():
        su_len += len(v)

    chen_len = 0
    for j in chen:
        chen_len += len(chen[j])

    print("学生总数：", su_len + chen_len)


if __name__ == '__main__':
    main()
