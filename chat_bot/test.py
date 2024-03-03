# # plant_path="../GRADUATE_WORK/web_crawler/new_data/shape.txt"
# plant_path="../GRADUATE_WORK/web_crawler/new_data/different_name.txt"

# disease_wds= [i.strip() for i in open(plant_path,encoding="utf-8") if i.strip()]

# print(disease_wds)
# if not None:
#     print("ok")
# entity_dict={'Different_name': ['三七'], 'Different_name': ['挂菜']}

# print(entity_dict.get('Different_name'))

# import os
# import json
# from re import A
# from turtle import color
# from unicodedata import name
# from py2neo import Graph,Node

# class AgricultureGraph:
#     def __init__(self):
#         self.data_path="D:/graduate_workspace/graduate_work/web_crawler/new_data/data.json"
#         self.g=Graph("http://localhost:7474/",username="neo4j",password="Cdslqyqxhz31203")

#     #读取文件
#     def read_nodes(self):
#         #共12类节点
#         plant=[] #植物
#         diff_name=[] #别名
#         color=[] #颜色分类
#         category=[] #作物分类
#         taste=[] #味道分类
#         shape=[] #形状分类
#         light=[] #光照需求
#         session=[] #开花季节
#         level=[] #培育难度
#         temperature=[] #适宜温度
#         ph=[] #酸碱范围

#         agriculture_info=[] #植物基础信息 用于创建植物基础信息表

#         #构建节点实体关系
#         rels_other_name=[] #植物-别名
#         rels_color_type=[] #植物-颜色分类
#         rels_category_type=[] #植物-作物分类
#         rels_taste_type=[] #植物-味道分类
#         rels_shape_type=[] #植物-形状分类
#         rels_light_type=[] #植物-光照需求
#         rels_session_type=[] #植物-开花季节
#         rels_level_type=[] #植物-培育难度
#         rels_temperature_type=[] #植物-适宜温度
#         rels_ph_type=[] #植物-酸碱范围

#         # count=0
#         with open(self.data_path,encoding='utf-8') as f:
#             data_json=json.load(f)
#             # print(data_json)
#         for key,data in data_json.items():
#             agriculture_dict={}
#             # count=count+1
#             # print(count)
#             # print(key,data)
#             # print("_"*30)
            
#             agriculture_dict['name']=key #植物名称
#             plant.append(key) #加到植物节点中

#             agriculture_dict['desc']=''#作物描述
#             # agriculture_dict['diff_name']=''
#             # agriculture_dict['color']=''
#             # agriculture_dict['category']=''
#             # agriculture_dict['taste']=''
#             # agriculture_dict['shape']=''
#             # agriculture_dict['light']=''
#             # agriculture_dict['session']=''
#             # agriculture_dict['level']=''
#             # agriculture_dict['temperature']=''
#             # agriculture_dict['ph']=''

#             #提取实体,构建关系
#             #植物-别名
#             if "别名" in data:
                
#                 for other_name in data["别名"]: #一个作物可能有多个别名
                    
#                     if other_name in diff_name:
#                         print(other_name)
#                 diff_name += data["别名"] #+用于组合列表
                    
#                 rels_other_name=[]#对于每个别名,构建一个植物-别名的关系
#             # print(rels_other_name)

#             #植物描述的属性
#             if "基础信息" in data:
#                 agriculture_dict['desc']=data['基础信息']
#             # print(agriculture_dict['desc'])

#             #继续构建关系
#             #植物-颜色分类
#             if "颜色分类" in data:
#                 color.append(data["颜色分类"])
#                 rels_color_type.append([key,data["颜色分类"]])
#             # print(rels_color_type)

#             #植物-作物分类
#             if "作物分类" in data:
#                 category.append(data["作物分类"])
#                 rels_category_type.append([key,data["作物分类"]])
#             # print(rels_category_type)

#             #植物-味道分类
#             if "味道分类" in data:
#                 taste.append(data["味道分类"])
#                 rels_taste_type.append([key,data["味道分类"]])
#             # print(rels_taste_type)

#             #植物-形状分类
#             if "形状分类" in data:
#                 shape.append(data["形状分类"])
#                 rels_shape_type.append([key,data["形状分类"]])
#             # print(rels_shape_type)

#             #植物-光照需求
#             if "光照需求" in data:
#                 light.append(data["光照需求"])
#                 rels_light_type.append([key,data["光照需求"]])
#             # print(rels_light_type)

#             #植物-开花季节
#             if "开花季节" in data:
#                 session.append(data["开花季节"])
#                 rels_session_type.append([key,data["开花季节"]])
#             # print(rels_session_type)

#             #植物-培育难度
#             if "培育难度" in data:
#                 level.append(data["培育难度"])
#                 rels_level_type.append([key,data["培育难度"]])
#             # print(rels_level_type)

#             #植物-适宜温度
#             if "适宜温度" in data:
#                 temperature.append(data["适宜温度"])
#                 rels_temperature_type.append([key,data["适宜温度"]])
#             # print(rels_temperature_type)

#             #植物-酸碱范围
#             if "酸碱范围" in data:
#                 ph.append(data["酸碱范围"])
#                 rels_ph_type.append([key,data["酸碱范围"]])
#             # print(rels_ph_type)
            
#             # if count==3:
#             #     break

#             #将信息全部整合到字典中
#             agriculture_info.append(agriculture_dict)
#         # print(agriculture_info)
#         # print("ok")

#         return set(plant),set(diff_name),set(color),set(category),set(taste),set(shape),set(light),set(session),set(level),set(temperature),\
#             set(ph),agriculture_info,\
#             rels_other_name, rels_color_type, rels_category_type, rels_taste_type,rels_shape_type, rels_light_type, rels_session_type,\
#             rels_level_type, rels_temperature_type, rels_ph_type

#     #建立节点
#     def create_node(self, label,nodes):
#         count=0
#         for node_name in nodes:
#             node=Node(label,name=node_name)
#             self.g.create(node)
#             count+=1
#             print(count,len(nodes))
#         return

#     #创建知识图谱中心植物的节点
#     def create_plant_nodes(self, agriculture_info):
#         count=0
#         for agriculture_dict in agriculture_info:
#             node=Node("Plant",name=agriculture_dict['name'],desc=agriculture_dict['desc'])
#             self.g.create(node)
#             count+=1
#             print(count)
#         return

#     #创建知识图谱实体节点类型schema
#     def create_graph_nodes(self):
#         Plant, Different_name, Color, Category, Taste, Shape, Light, Session, Level, Temperature, Ph, agriculture_info, rels_other_name, rels_color_type, rels_category_type, rels_taste_type, rels_shape_type, rels_light_type, rels_session_type, rels_level_type, rels_temperature_type, rels_ph_type= self.read_nodes()
#         self.create_plant_nodes(agriculture_info) #创建作物节点
#         # self.create_node('Plant',Plant)
#         self.create_node('Different_name',Different_name) #别名
#         self.create_node('Color',Color) #颜色分类
#         self.create_node('Category',Category) #作物分类
#         self.create_node('Taste',Taste) #味道分类
#         self.create_node('Shape',Shape) #形状分类
#         self.create_node('Light',Light) #光照需求
#         self.create_node('Session',Session) #开花季节
#         self.create_node('Level',Level) #培育难度
#         self.create_node('Temperature',Temperature) #适宜温度
#         self.create_node('Ph',Ph) #酸碱范围
        

#     #创建实体关系边
#     def create_graph_hrels(self):
#         Plant, Different_name, Color, Category, Taste, Shape, Light, Session, Level, Temperature, Ph, agriculture_info, rels_other_name, rels_color_type, rels_category_type, rels_taste_type, rels_shape_type, rels_light_type, rels_session_type, rels_level_type, rels_temperature_type, rels_ph_type= self.read_nodes()
#         self.create_relationship('Plant','Different_name',rels_other_name,'other_name','别名')
#         self.create_relationship('Plant','Color',rels_color_type,'color','颜色')
#         self.create_relationship('Plant','Category',rels_category_type,'category','作物类型')
#         self.create_relationship('Plant','Taste',rels_taste_type,'taste','味道')
#         self.create_relationship('Plant','Shape',rels_shape_type,'shape','形状')
#         self.create_relationship('Plant','Light',rels_light_type,'light_requirement','光照需求')
#         self.create_relationship('Plant','Session',rels_session_type,'flower_session','开花季节')
#         self.create_relationship('Plant','Level',rels_level_type,'level','培育难度')
#         self.create_relationship('Plant','Temperature',rels_temperature_type,'need_temperature','适宜温度')
#         self.create_relationship('Plant','Ph',rels_ph_type,'need_ph','酸碱范围')


#     #创建实体关联边
#     def create_relationship(self,start_node,end_node,edges,rel_type,rel_name):
#         count=0
#         #去重处理,加上特殊符,方便之后进行拆分
#         set_edges=[]
#         for edge in edges:
#             set_edges.append('###'.join(edge))
#         all=len(set(set_edges))
#         for edge in set(set_edges):
#             edge=edge.split('###')
#             p=edge[0]
#             q=edge[1]
#             query="match(p:%s),(q:%s) where p.name='%s'and q.name='%s' create (p)-[rel:%s{name:'%s'}]->(q)" % (
#                 start_node, end_node, p, q, rel_type, rel_name)#match语法，p，q分别为标签，rel_type关系类别，rel_name 关系名字
#             try:
#                 self.g.run(query)
#                 count+=1
#                 print(rel_type,count,all)
#             except Exception as e:
#                 print(e)
            


#     #导出数据
#     def export_data(self):
#         Plant, Different_name, Color, Category, Taste, Shape, Light, Session, Level, Temperature, Ph, agriculture_info, rels_other_name, rels_color_type, rels_category_type, rels_taste_type, rels_shape_type, rels_light_type, rels_session_type, rels_level_type, rels_temperature_type, rels_ph_type= self.read_nodes()
#         f_plant=open("../GRADUATE_WORK/web_crawler/new_data/plant.txt",'w+',encoding='utf-8')
#         f_different_name=open("../GRADUATE_WORK/web_crawler/new_data/different_name.txt",'w+',encoding='utf-8')
#         f_color=open("../GRADUATE_WORK/web_crawler/new_data/color.txt",'w+',encoding='utf-8')
#         f_category=open("../GRADUATE_WORK/web_crawler/new_data/category.txt",'w+',encoding='utf-8')
#         f_taste=open("../GRADUATE_WORK/web_crawler/new_data/taste.txt",'w+',encoding='utf-8')
#         f_shape=open("../GRADUATE_WORK/web_crawler/new_data/shape.txt",'w+',encoding='utf-8')
#         f_light=open("../GRADUATE_WORK/web_crawler/new_data/light.txt",'w+',encoding='utf-8')
#         f_session=open("../GRADUATE_WORK/web_crawler/new_data/session.txt",'w+',encoding='utf-8')
#         f_level=open("../GRADUATE_WORK/web_crawler/new_data/level.txt",'w+',encoding='utf-8')
#         f_temperature=open("../GRADUATE_WORK/web_crawler/new_data/temperature.txt",'w+',encoding='utf-8')
#         f_ph=open("../GRADUATE_WORK/web_crawler/new_data/ph.txt",'w+',encoding='utf-8')

#         f_plant.write('\n'.join(list(Plant)))
#         # print(Color)
#         # print(Different_name)
#         f_different_name.write('\n'.join(list(Different_name)))
#         f_color.write('\n'.join(list(Color)))
#         f_category.write('\n'.join(list(Category)))
#         f_taste.write('\n'.join(list(Taste)))
#         f_shape.write('\n'.join(list(Shape)))
#         f_light.write('\n'.join(list(Light)))
#         f_session.write('\n'.join(list(Session)))
#         f_level.write('\n'.join(list(Level)))
#         f_temperature.write('\n'.join(list(Temperature)))
#         f_ph.write('\n'.join(list(Ph)))

#         f_plant.close()
#         f_different_name.close()
#         f_color.close()
#         f_category.close()
#         f_taste.close()
#         f_shape.close()
#         f_light.close()
#         f_session.close()
#         f_level.close()
#         f_temperature.close()
#         f_ph.close()

#         return


# if __name__=='__main__':
#     a=AgricultureGraph()
#     # a.create_graph_nodes()
#     a.read_nodes()
#     # a.export_data()
#     # a.create_graph_hrels()

#问题解析器
# import sqlite3


# class Questionparser:
#     def __init__(self):
#         pass
    
#     def parser_main(self,res_classify):
#         args=res_classify['args']
#         #实体字典
#         entity_dict={}
#         for arg,types in args.items():
#             for type in types:
#                 if type not in entity_dict:
#                     #新增:用列表存储arg,防止有多个实体的问题: {'Plant': ['三七'], 'Session': ['春季'], 'Light': ['中光']}
#                     entity_dict[type]=[arg]
#                 else:
#                     entity_dict[type].append(arg)
        
#         question_types=res_classify['question_types']
        
#         #新增: 对于多个问题,保存问题的序列
#         sqls=[]
#         #一次处理一个问题
#         for question_type in question_types:
#             sql_get={}

#             sql_get['question_type']=question_type
            

#             sql=self.get_sql(question_type,entity_dict)

#             if sql:
#                 sql_get['sql']=sql
#                 sqls.append(sql_get)
        
#         #可以是多个问题,所以可以有多个sql查询语句
        
#         return sqls
            
    

#     def get_sql(self,question_type,entity_dict):
#         sql=[]
#         #flag=1表示使用了别名,要多一步处理
#         flag=0
#         #未使用别名
#         if not entity_dict.get('Different_name'):
#             #询问物种的别名
#             if question_type=='plant_diff_name':
#                 sql=self.sql_transfer(question_type,entity_dict.get('Plant'),flag)
            
#             #可能使用了别名对使用了别名的进行单独处理
#             #询问物种的颜色
#             elif question_type=='plant_color':
#                 sql=self.sql_transfer(question_type,entity_dict.get('Plant'),flag)

#             #询问物种的类型
#             elif question_type=='plant_category':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Plant'),flag)
            
#             #询问物种的味道
#             elif question_type=='plant_taste':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Plant'),flag)

#             #询问物种的外形
#             elif question_type=='plant_shape':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Plant'),flag)

#             #询问物种的光照需求
#             elif question_type=='plant_light':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Plant'),flag)
            
#             #询问物种的开花时间
#             elif question_type=='plant_session':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Plant'),flag)
            
#             #询问物种的培育难度
#             elif question_type=='plant_level':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Plant'),flag)
            
#             #询问物种的培育温度
#             elif question_type=='plant_temperature':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Plant'),flag)
            
#             #询问物种的酸碱范围
#             elif question_type=='plant_ph':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Plant'),flag)
            
#             #介绍作物
#             elif question_type=='plant_desc':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Plant'),flag)

#         #使用了别名
#         else:
#             flag=1
#             #询问物种的别名
#             if question_type=='plant_diff_name':
#                 sql=self.sql_transfer(question_type,entity_dict.get('Different_name'),flag)

#             #询问物种的颜色
#             elif question_type=='plant_color':
#                 sql=self.sql_transfer(question_type,entity_dict.get('Different_name'),flag)

#             #询问物种的类型
#             elif question_type=='plant_category':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Different_name'),flag)
            
#             #询问物种的味道
#             elif question_type=='plant_taste':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Different_name'),flag)

#             #询问物种的外形
#             elif question_type=='plant_shape':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Different_name'),flag)

#             #询问物种的光照需求
#             elif question_type=='plant_light':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Different_name'),flag)
            
#             #询问物种的开花时间
#             elif question_type=='plant_session':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Different_name'),flag)
            
#             #询问物种的培育难度
#             elif question_type=='plant_level':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Different_name'),flag)
            
#             #询问物种的培育温度
#             elif question_type=='plant_temperature':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Different_name'),flag)
            
#             #询问物种的酸碱范围
#             elif question_type=='plant_ph':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Different_name'),flag)
            
#             #介绍作物
#             elif question_type=='plant_desc':
#                 sql = self.sql_transfer(question_type, entity_dict.get('Different_name'),flag)

#         return sql

#     #对问题分别进行处理
#     def sql_transfer(self,question_type,entities,flag):
#         if not entities:
#             return []
        
#         #设定查询语句
#         sql=[]
#         #entities = ['三七']
#         #未使用别名
#         if flag==0:
#             #询问作物的别称
#             if question_type=='plant_diff_name':
#                 sql=["MATCH (n:Plant) where n.name='{0}'  MATCH (n)-[:other_name]->(m:Different_name) RETURN n.name,m.name".format(i) for i in entities] #多个实体一个问题用for处理
            
#             #询问物种的颜色
#             elif question_type=='plant_color':
#                 sql=["MATCH (n:Plant) where n.name='{0}'  MATCH (n)-[:color]->(m:Color) RETURN n.name,m.name".format(i) for i in entities]

#             #询问物种的类型
#             elif question_type=='plant_category':
#                 sql=["MATCH (n:Plant) where n.name='{0}'  MATCH (n)-[:category]->(m:Category) RETURN n.name,m.name".format(i) for i in entities]

#             #询问物种的味道
#             elif question_type=='plant_taste':
#                 sql=["MATCH (n:Plant) where n.name='{0}'  MATCH (n)-[:taste]->(m:Taste) RETURN n.name,m.name".format(i) for i in entities]

#             #询问物种的外形
#             elif question_type=='plant_shape':
#                 sql=["MATCH (n:Plant) where n.name='{0}'  MATCH (n)-[:shape]->(m:Shape) RETURN n.name,m.name".format(i) for i in entities]

#             #询问物种的光照需求
#             elif question_type=='plant_light':
#                 sql=["MATCH (n:Plant) where n.name='{0}'  MATCH (n)-[:light_requirement]->(m:Light) RETURN n.name,m.name".format(i) for i in entities]
            
#             #询问物种的开花时间
#             elif question_type=='plant_session':
#                 sql=["MATCH (n:Plant) where n.name='{0}'  MATCH (n)-[:flower_session]->(m:Session) RETURN n.name,m.name".format(i) for i in entities]
            
#             #询问物种的培育难度
#             elif question_type=='plant_level':
#                 sql=["MATCH (n:Plant) where n.name='{0}'  MATCH (n)-[:level]->(m:Level) RETURN n.name,m.name".format(i) for i in entities]
            
#             #询问物种的培育温度
#             elif question_type=='plant_temperature':
#                 sql=["MATCH (n:Plant) where n.name='{0}'  MATCH (n)-[:need_temperature]->(m:Temperature) RETURN n.name,m.name".format(i) for i in entities]
            
#             #询问物种的酸碱范围
#             elif question_type=='plant_ph':
#                 sql=["MATCH (n:Plant) where n.name='{0}'  MATCH (n)-[:need_ph]->(m:Ph) RETURN n.name,m.name".format(i) for i in entities]
            
#             #介绍作物
#             elif question_type=='plant_desc':
#                 sql=["MATCH (n:Plant) where n.name='{0}' return n.name,n.desc".format(i) for i in entities]
        
#         #使用了别名
#         else:
#             #先找出别名对应的实体(Plant)(默认是一个别名就偷懒没写)
#             #会存在一个别名对应多个作物的情况
#             sql_find_plant=["MATCH (n:Different_name) where n.name='{0}'  MATCH (n)<-[:other_name]-(m:Plant)".format(entities)]


#             #询问作物的别称
#             if question_type=='plant_diff_name':
#                 sql_1=["MATCH (m)-[:other_name]->(t:Different_name)  RETURN n.name,m.name,t.name"] #多个实体一个问题用for处理
            
#             #询问物种的颜色
#             elif question_type=='plant_color':
#                 sql_1=["MATCH (m)-[:color]->(t:Color)   RETURN n.name,m.name,t.name"]

#             #询问物种的类型
#             elif question_type=='plant_category':
#                 sql_1=["MATCH (m)-[:category]->(t:Category)  RETURN n.name,m.name,t.name"]
#             #询问物种的味道
#             elif question_type=='plant_taste':
#                 sql_1=["MATCH (m)-[:taste]->(t:Taste)  RETURN n.name,m.name,t.name"]

#             #询问物种的外形
#             elif question_type=='plant_shape':
#                 sql_1=["MATCH (m)-[:shape]->(t:Shape) RETURN n.name,m.name,t.name"]

#             #询问物种的光照需求
#             elif question_type=='plant_light':
#                 sql_1=["MATCH (m)-[:light_requirement]->(t:Light) RETURN n.name,m.name,t.name"]
            
#             #询问物种的开花时间
#             elif question_type=='plant_session':
#                 sql_1=["MATCH (m)-[:flower_session]->(t:Session) RETURN n.name,m.name,t.name"]
            
#             #询问物种的培育难度
#             elif question_type=='plant_level':
#                 sql_1=["MATCH (m)-[:level]->(t:Level) RETURN n.name,m.name,t.name"]
            
#             #询问物种的培育温度
#             elif question_type=='plant_temperature':
#                 sql_1=["MATCH (m)-[:need_temperature]->(t:Temperature) RETURN n.name,m.name,t.name"]
            
#             #询问物种的酸碱范围
#             elif question_type=='plant_ph':
#                 sql_1=["MATCH (m)-[:need_ph]->(t:Ph) RETURN n.name,m.name,t.name"]
            
#             #介绍作物
#             elif question_type=='plant_desc':
#                 sql_1=["return n.name,m.name,m.desc".format(i) for i in entities]
            
#             #对查询语句进行拼接
#             sql= sql_find_plant + sql_1
        
#         return sql
        
# if __name__=='__main__':
#     a=Questionparser()
#     res_classify={'args': {'三七': ['Plant'], '春季': ['Session'], '中光': ['Light']}, 'question_types': ['plant_level', 'plant_ph']}
#     sql=a.parser_main(res_classify)
#     print(sql)




# sqls=[{'question_type': 'plant_level', 'sql': ["MATCH (n:Plant) where n.name='三七'  MATCH (n)-[:level]->(m:Level) RETURN n.name,m.name"]}, {'question_type': 'plant_ph', 'sql': ["MATCH (n:Plant) where n.name='三七'  MATCH (n)-[:need_ph]->(m:Ph) RETURN n.name,m.name"]}]
# for sql in sqls:
#     print(sql)
#     query=sql['sql']
#     print(query)
            

        
a=[{'n.name': '三七', 'm.name': '较难'}]
print(len(a[0]))

