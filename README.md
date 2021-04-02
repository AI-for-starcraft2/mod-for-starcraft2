# mod-for-starcraft2
# 玩家社区
## 地精研究院
https://bbs.islga.org/

老牌黑帮社区了，嘻嘻
## 艾尔星盟
https://wp.aiurcovenant.net/

缺乏维修，梦罗快上

## 国外作图社区

https://discord.gg/fpNFhb4C

# 精品mod
## 沙漠风暴S3,S4
蒙斯克，冰光刃，S4，尖山黄泉，Artanis（不分先后，也可能漏了）
## 时空枢纽
菲本家族
## 魔兽3mod系列
麦德三世是骨灰级元老
# 数据库
星际争霸2的引擎是银河引擎

星际争霸2的数据库是xml格式的面向对象数据库

通用数据存储在游戏文件，每张地图额外的数据存在每张地图。只有变化部分会被记录在xml中，其余不变部分被忽略。

MPQEditor.exe工具可以打开地图
# AI
动视暴雪提供API接口给研究者使用后台读取游戏中单位和控制其中的单位。通过API接口玩家可以制作人工智能AI在机器人天梯，远程连接进行对战。

详情参考guide for AI

https://github.com/fengmao31/mod-for-starcraft2/tree/main/guide%20for%20AI
# 地图数据修改
## 地图编辑器
提供了可视化的修改界面，但是由于编辑器缺乏维护，打开缓慢，点开关闭窗口自动初始化等智障操作，反而不如EA家族游戏直接编辑源文件方便。

xml只能导出变化的xml文件，无法导出所有xml文件.
## xml文件
使用MPQEditor.exe工具导出xml文件进行修改，可以编程小工具来批量化处理。
## script文件
使用MPQEditor.exe工具导出Mapscript.galaxy文件进行修改，可以使用编程IDE修改。

https://s2editor-guides.readthedocs.io/New_Tutorials/03_Trigger_Editor/058_GalaxyScript/

https://github.com/Talv/vscode-sc2-galaxy
# 地图版权
由于魔兽争霸3RPG地图dota和暴雪的官司胜诉，所以动视暴雪有了前车之鉴。编辑器完成的地图版权归动视暴雪所有。

有没有和起点一样霸道的感觉。最近看赘婿电视剧，似乎赘婿的作者变成了阅文集团。我记得赘婿是本老书，应该在更改签约合同之前完成的作品。

玩家社区共识作为约束现在的社区玩家。
## 以下行为是可以的

- “搬运”，“汉化”地图说明来源作者，最好得到原作者授权。但是有时候老图完全找不到原作者消息

- “盗图”私下里自己离线游玩

- “作图”出售VIP
## 以下行为是被玩家社区深恶痛绝的
- “盗图”并声称自己是作者

- “盗图”并胡乱修改

- “盗图”留下不平衡作弊接口供自己作弊

- “作图”出售VIP并留下不平衡作弊接口
