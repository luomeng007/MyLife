# MyLife
This is a game project  
  
We are aiming at improving players themselves in their real life.  
  
We hope by playing this game, every player can live a better life in the future.   
  
At the beginning, this game is only designed for Chinese player, later when we have time, we may develope it for players from other countries.

主要逻辑：
	1.所有的限制每日进行更新
	2.所有的目标只要达到则对应目标值对应的分数
	3.目前所有的数据先用.txt文档存储起来
次要逻辑：
	1.每日慢跑：
		1).一次20分钟，健康值+1
		2).两次慢跑之间间隔不少于6个小时
		3).每日慢跑次数不得超过三次
	2.每日学习：
		1).2个选项，
			学习30分钟，学术值+0.25
			学习1分钟，学术值+0.5
		2).每日学习时常不得超过8个小时
	3.冥想：
		1).一次10分钟，精神力+1
	4.打扫卫生：
		1).无论做什么，20分钟，清洁值+1
日常任务:
	1).每日慢跑至少一次，未完成，健康值-1
	2).三天至少进行一次打扫，未完成清洁值-1，健康值-1
	3).一周至少进行一次学习，未完成学术值-1, 每日学术值最高上限4（学术值2个小时+1）
	4).冥想任务未完成不扣分，独立于所有任务之外，连续完成一周额外+1
目前缺失功能：
	1.每日限制条件
	2.每日进行对限制条件的更新
