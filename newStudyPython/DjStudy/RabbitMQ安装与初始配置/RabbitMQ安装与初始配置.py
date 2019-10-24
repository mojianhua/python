'''
	1、yum -y install socat
	2、安装erlang软件包
	wget http://www.rabbitmq.com/releases/erlang/erlang-19.0.4-1.el7.centos.x86_64.rpm
	安装erlang
	rpm -ivh erlang-19.0.4-1.el7.centos.x86_64.rpm
	3、安装rabbitmq
	wget  http://www.rabbitmq.com/releases/rabbitmq-server/v3.6.10/rabbitmq-server-3.6.10-1.el7.noarch.rpm
	安装mq
	rpm -ivh rabbitmq-server-3.6.10-1.el7.noarch.rpm
	注意：如果是重装请记得删除/var/lib/rabbitmq目录和/etc/rabbitmq目录，否则可能服务会起不来
	4、查询mq安装路径
	whereis rabbitmq
	5、进入cd /usr/lib/rabbitmq/bin
	6、开启服务
	rabbitmq-server -detached
	7、查看状态
	rabbitmqctl status
	8、关闭服务
	rabbitmqctl stop
	9、添加用户
	rabbitmqctl add_user [用户名] [密码]
	10、设置成超级管理员
	rabbitmqctl set_user_tags [用户名] administrator 
	11、分配访问权限，注意'/'标识任何host,如需要修改指定的哪个vhost
	rabbitmqctl set_permissions -p / jim2 ".*" ".*" ".*"
'''