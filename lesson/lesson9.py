# orm工具sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建数据库引擎
engine = create_engine('mysql+pymysql://root:123456@localhost/ry')

# 定义模型基类
Base = declarative_base()


# 定义模型
class User(Base):
    __tablename__ = 'users'
    userId = Column(Integer, primary_key=True,name="user_id")
    userName = Column(String(50), name="user_name")
    sex = Column(Integer)


# 创建表
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 添加数据
new_user = User(userName='Alice', sex=1)
session.add(new_user)
session.commit()  # 提交事务

# 查询数据
users = session.query(User).all()
for user in users:
    print(user.userName, user.sex)

# 关闭会话
session.close()
