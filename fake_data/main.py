from model import user


def test1():
    res = user.get_by_id(1)
    print(res.id, res.name, res.phone)


def test2():
    array = [user.User(name='lmaber', phone='13005497255'),
             user.User(name='xxxx', phone='123456789')]
    res = user.batch_create(array)
    print(res)


def test3():
    array = []

    for i in range(1, 1101):
        array.append(user.User(name='测试用户%d' % i, phone='1234567890%d' % i))
        if i % 200 == 0:  # 每200条数据拼装成1条SQL语句插入后，清除列表中已经插入的数据
            print(i)
            user.batch_create(array)
            array.clear()

    if len(array) > 0:
        print(len(array))
        user.batch_create(array)


def test4():
    res = user.update_by_id(1, "更新11")
    print(res)
    res = user.update_by_id(2, "更新12", "1234")
    print(res)
    res = user.update_by_id(3, phone="3456")
    print(res)
    res = user.update_by_id(4)
    print(res)


def test5():
    res = user.get_by_name("更新11")
    for u in res:
        print(u.id, u.name, u.phone)


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    test5()
