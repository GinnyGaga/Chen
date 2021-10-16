#不一定两张表有外键关系才可以一起关联查询，只要给出关联条件就可以
rows = session.query(User.id,User.name,Column_test.id,Column_test.name).filter(User.id==Column_test.id).all()

#也可以使用join
rows = session.query(Student.name,User.number).join(User,Student.name==User.name).all()
print(rows)

#outerjoin代表left join ，在SQLAlchemy中没有右连接
rows = session.query(Student.name,User.number).outerjoin(User,Student.name==User.name).all()

#对于union也是可以使用的
q1 = session.query(Student.name)
q2 = session.query(User.name)
rows = q1.union(q2).all()

#子表查询
from sqlalchemy import func
q3 = session.query(Student.dep_id,func.count('*').label('dep_count')).group_by(Student.dep_id).subquery()
print(q3)
rows = session.query(Department,q3.c.dep_count).outerjoin(q3,q3.c.dep_id==Department.id).all()
print(rows)
#这里注意，使用查询子表查询的时候使用  q3.c.dep_count  这种方式去取得对应的属性
#subquery 就是子查询的意思
#group_by  having  order_by 等这些都是可用的
#label 是标签的意思，这里的作用类似与MySQL中的as
#如果要使用聚合函数，需要导入func模块，导入之后就可以是使用各种函数，只要连接的数据库支持
#这个查询，几乎把我们常会用到的各种情况给演示出来，加上之前我们讲过的一些查询，我们在工作中可能会遇到的查询，基本上都已经讲解
