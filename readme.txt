玻璃加工生产线管理系统
此系统是为玻璃加工生产线设计的，旨在实时跟踪并管理每个工作站上工件的处理状态。

主要功能：
实时记录工件在每个工作站的到达和离开时间。
将所有实时信息集中存储到数据库中。
统计每个工件在每个工作站的停留时间。
提供筛选功能，能够筛选出当天的工作站信息。
为用户提供一个基本的显示界面，查看和分析数据。
系统要求：
Python 3.7+
Django 3.2+
PostgreSQL 12+ (或您选择的其他关系型数据库)
安装与配置：
虚拟环境设置:

建议为项目设置一个Python虚拟环境。可以使用以下命令：

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
依赖项安装:

安装项目所需的所有依赖项：

bash
Copy code
pip install django psycopg2-binary
数据库配置:

在PostgreSQL中创建一个新的数据库，并在settings.py中进行相应配置：

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
迁移与启动:

运行以下命令应用模型更改：

bash
Copy code
python manage.py makemigrations
python manage.py migrate
启动Django开发服务器：

bash
Copy code
python manage.py runserver
使用方法：
打开浏览器，访问 http://localhost:8000/ 查看所有事件。
使用提供的API端点（例如 http://localhost:8000/capture_event）从工作站传感器发送数据。
使用网页界面的筛选功能查找特定数据。
贡献与支持：
如有任何问题或建议，请通过Github Issues提交或联系项目维护者。


ENGLISH///

Glass Processing Production Line Management System
This system is designed for the glass processing production line, aiming to track and manage the processing status of workpieces on each workstation in real-time.

Main Features:
Real-time recording of the arrival and departure times of workpieces at each station.
Centralize all real-time information into a database.
Calculate the dwell time of each workpiece at each station.
Provides a filtering feature to display station information for the day.
Provides users with a basic display interface to view and analyze data.
System Requirements:
Python 3.7+
Django 3.2+
PostgreSQL 12+ (or any other relational database of your choice)
Installation & Configuration:
Setting up a virtual environment:

It is recommended to set up a Python virtual environment for the project. This can be done using the following commands:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Installing dependencies:

Install all required dependencies for the project:

bash
Copy code
pip install django psycopg2-binary
Database Configuration:

Create a new database in PostgreSQL and configure it accordingly in settings.py:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Migrations and Launch:

Run the following commands to apply model changes:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Start the Django development server:

bash
Copy code
python manage.py runserver
How to Use:
Open a browser and visit http://localhost:8000/ to view all events.
Use the provided API endpoint (e.g., http://localhost:8000/capture_event) to send data from workstation sensors.
Use the web interface's filtering feature to search for specific data.
