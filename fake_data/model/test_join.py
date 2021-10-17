from model import user, user_address, user_sex
from database.database import DbEngine

tableUser = user.User
tableAddress = user_address.UserAddress
tableUserSex = user_sex.UserSex


# 查询2表匹配的重合的记录
def get_user_addr():
    return DbEngine().get_session().query(tableUser, tableAddress). \
        join(tableAddress, tableUser.name == tableAddress.name).all()


# 查询3表:user表中名字和user_sex表中性别对应，关联是user表的name和user_address表的name对应；
# user_address表的address和user_sex表中address对应，


# 不带条件查询
def get_user_addr_sex():
    return DbEngine().get_session().query(tableUser, tableAddress, tableUserSex). \
        join(tableAddress, tableAddress.name == tableUser.name). \
        join(tableUserSex, tableUserSex.address == tableAddress.address).first()


# 不带条件查询
def list_user_addr_sex():
    return DbEngine().get_session().query(tableUser, tableAddress, tableUserSex). \
        join(tableAddress, tableAddress.name == tableUser.name). \
        join(tableUserSex, tableUserSex.address == tableAddress.address).all()


# 带条件查询：
def get_user_addr_sex_by_addr(addr: str):
    return DbEngine().get_session().query(tableUser, tableAddress, tableUserSex). \
        join(tableAddress, tableAddress.name == tableUser.name). \
        join(tableUserSex, tableUserSex.address == tableAddress.address). \
        filter(tableAddress.address == addr).all()
    #  filter 变量名和类的属性做比较，使用==，filter(属性名=变量)，支持组合查询；
    #  filter_by 把变量名赋值给类的属性，使用=，filter_by(类名.属性名==变量)，不支持组合条件查询



