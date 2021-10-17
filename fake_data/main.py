from model import user, user_address, test_join


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

    for i in range(1, 1101):  # 左闭右开，插入1100条数据0
        array.append(user.User(name='测试用户%d' % i, phone='1234567890%d' % i))  # id 自动递增
        if i % 200 == 0:  # 每200条数据拼装成1条SQL语句插入后，清除列表中已经插入的数据
            print(i)
            user.batch_create(array)
            array.clear()

    if len(array) > 0:
        print(len(array))
        user.batch_create(array)


def test4():
    res = user.update_by_id(1, "更新22311")
    print(res)
    # res = user.update_by_id(2, "更新122", "123114")
    # print(res)
    # res = user.update_by_id(5, phone="3456ee")
    # print(res)
    # res = user.update_by_id(4)
    # print(res)


def test5():
    res = user.get_by_name("更新11")
    for u in res:
        print(u.id, u.name, u.phone)


def test6():
    res = user_address.get_by_id(1)
    print(res.id, res.name, res.address)


# 2表联查
def test7():
    res = test_join.get_user_addr()
    print(res)
    for v in res:
        u = v["User"]
        addr = v["UserAddress"]
        print(u.id, u.name, addr.address)


# 3表联查
def test8():
    res = test_join.list_user_addr_sex()
    print(res)  # 返回值为列表，即返回列表为3个元组，每个元组含有3张表。
    for (user, addr, sex) in res:
        print(user.name, addr.address, sex.sex)
    # for v in res:
    #     user, addr, sex = v["User"], v["UserAddress"], v["UserSex"]
    #     print(user.name, addr.address, sex.sex)


# 3表联查带条件
def test9():
    res = test_join.get_user_addr_sex_by_addr("NN")
    print(res)
    for (user, addr, sex) in res:
        # user, addr, sex = v["User"], v["UserAddress"], v["UserSex"]
        print(user.name, addr.address, sex.sex)


# 3表联查带条件
def test10():
    # 法1：报错的话，打断点，看data和fileds字段
    # user, addr, sex = test_join.get_user_addr_sex()
    # print(user.name, addr.address, sex.sex)
    # 法2：
    # res = test_join.get_user_addr_sex()
    # print(res)
    # print(res.User.name, res.UserAddress.address, res.UserSex.sex)
    # 法3：
    res = test_join.get_user_addr_sex()
    print(res)
    print(res[0].name, res[1].address, res[2].sex)


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    # test7()
    # test8()
    # test9()
    test10()
