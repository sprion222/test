import os
import jieba
import ahocorasick #引入ac算法进行多模式匹配
jieba.setLogLevel(jieba.logging.INFO)

#问题分类器
class Questionclassifier:
    def __init__(self):
        #读取实体特征词的路径
        #streamlit和vscode的相对路径不一样？
        # self.plant_path="../GRADUATE_WORK/web_crawler/new_data/plant.txt" #vscode相对路径
        self.plant_path="./plant.txt" #streamlit相对路径
        
        #别名需要回查到植物实体,要单独处理
        self.diff_name_path="./different_name.txt"

        self.color_path="./color.txt"
        self.category_path="./category.txt"
        self.taste_path="./taste.txt"
        self.shape_path="./shape.txt"
        self.light_path="./light.txt"
        self.session_path="./session.txt"
        self.level_path="./level.txt"
        self.temperature_path="./temperature.txt"
        self.ph_path="./ph.txt"

        #通过上述路径,加载特征词、
        self.plant_wds=[i.strip() for i in open(self.plant_path,encoding="utf-8") if i.strip()]

        self.diff_name_wds=[i.strip() for i in open(self.diff_name_path,encoding="utf-8") if i.strip()]

        self.color_wds=[i.strip() for i in open(self.color_path,encoding="utf-8") if i.strip()]
        self.category_wds=[i.strip() for i in open(self.category_path,encoding="utf-8") if i.strip()]
        self.taste_wds=[i.strip() for i in open(self.taste_path,encoding="utf-8") if i.strip()]
        self.shape_wds=[i.strip() for i in open(self.shape_path,encoding="utf-8") if i.strip()]
        self.light_wds=[i.strip() for i in open(self.light_path,encoding="utf-8") if i.strip()]
        self.session_wds=[i.strip() for i in open(self.session_path,encoding="utf-8") if i.strip()]
        self.level_wds=[i.strip() for i in open(self.level_path,encoding="utf-8") if i.strip()]
        self.temperature_wds=[i.strip() for i in open(self.temperature_path,encoding="utf-8") if i.strip()]
        self.ph_wds=[i.strip() for i in open(self.ph_path,encoding="utf-8") if i.strip()]

        self.region_words=set(self.plant_wds + self.diff_name_wds + self.color_wds + self.category_wds + self.taste_wds + self.shape_wds + self.light_wds + self.session_wds + self.level_wds + self.temperature_wds + self.ph_wds)
        
        #构造领域actree,基于树匹配比关键词分割匹配更加高效,ahocorasick是个现成的快速匹配函数
        self.region_tree = self.build_actree(list(self.region_words))

        #构建词典
        self.wdtype_dict = self.build_wdtype_dict()

        #问句
        self.plant_qwds=['植物','作物','物种','农作物','蔬菜','菜']
        self.diff_name_qwds=['别名','别称','另外名字','另外名称','异名','异称','还能叫什么','还能称作什么','还有什么名字','还叫什么']
        self.color_qwds=['颜色','色彩','色']
        self.category_qwds=['类','种类','类型','分类','哪一类','什么类','哪种','哪一种','属于','隶属']
        self.taste_qwds=['味道','尝起来','感觉起来','尝试吃','吃起来','口味','滋味','品味','品尝','口感']
        self.shape_qwds=['形状','外形','外观','样貌','长什么样','长啥样','长得如何','形体','啥样','形态','特征','特点'] #并入feature_qwds
        self.light_qwds=['光','光照','太阳光','阳光','日照','光强','光照强度']
        self.session_qwds=['花','开花','开花时间','开花季节','多久开花','在哪个季节开花','啥时候开花','什么时候开花','啥季节开花','花什么时候开',
                            '花啥时候开','啥前开花','啥时间开花','什么时间开花','花什么时间开'] #并入flowering_form_qwds
        self.level_qwds=['培育难度','难度','难不难','难否','困难','艰难','好养活','什么难度','简单吗','什么水平','好种','好培养',
                            '难易程度','难易','难吗','难不','简单不','简单否','易否','容易吗','容易否','是否容易','是否困难']
        self.temperature_qwds=['温度','摄氏度','华氏度','室温','气温','热','冷','常温']
        self.ph_qwds=['ph','PH','Ph','酸碱度','酸碱范围','酸性','碱性','酸碱','酸碱性']

        self.cultivation_method_qwds=['种','种植','种植方法','怎么种','怎么样种','咋样种','如何种']
        self.reproduction_qwds=['繁殖','繁育','起苗','育种','生殖','繁衍','滋生','生息','孳生','孳乳']
        

        return



    def classify(self,question):
        data={}
        agriculture_dict=self.check_agriculture(question) #对问题进行过滤

        if not agriculture_dict:
            return {}
        
        data['args']=agriculture_dict
        #收集问题中包含的实体的所有的类型
        types=[]
        for type in agriculture_dict.values():
            types+=type

        question_type=None

        #直接用物种别名的要单独处理一下,用diff_flag=1表示用了别名,在后面neo4j图数据库中查找时多加一步
        diff_flag=0
        #用elif默认只能输入一个问题

        #新增功能,可以接收多个问题并返回答案(因为字典的键必须唯一的限制,一次只能询问一个作物的一个或者多个方面的问题)
        question_types=[]
        #询问物种的别名
        if self.check_words(self.diff_name_qwds,question) and (('Plant' in types) or ('Different_name' in types)):
            question_type='plant_diff_name'
            question_types.append(question_type)
            
        
        #询问物种的颜色
        if self.check_words(self.color_qwds,question) and (('Plant' in types) or ('Different_name' in types)):
            # if ('Different_name' in types):
            #     diff_flag=1
            question_type='plant_color'
            question_types.append(question_type)
            
        
        #询问物种的类型
        if self.check_words(self.category_qwds,question) and  (('Plant' in types) or ('Different_name' in types)):
            # if ('Different_name' in types):
            #     diff_flag=1
            question_type='plant_category'
            question_types.append(question_type)
            

        #询问物种的味道
        if self.check_words(self.taste_qwds,question) and  (('Plant' in types) or ('Different_name' in types)):
            # if ('Different_name' in types):
            #     diff_flag=1
            question_type='plant_taste'
            question_types.append(question_type)
            
        
        #询问物种的外形,作物特征
        if self.check_words(self.shape_qwds,question) and  (('Plant' in types) or ('Different_name' in types)):
            # if ('Different_name' in types):
            #     diff_flag=1
            question_type='plant_shape'
            question_types.append(question_type)
            
        
        #询问物种的光照需求
        if self.check_words(self.light_qwds,question) and  (('Plant' in types) or ('Different_name' in types)):
            # if ('Different_name' in types):
            #     diff_flag=1
            question_type='plant_light'
            question_types.append(question_type)
            

        #询问物种的开花时间和开花形态
        if self.check_words(self.session_qwds,question) and  (('Plant' in types) or ('Different_name' in types)):
            # if ('Different_name' in types):
            #     diff_flag=1
            question_type='plant_session'
            question_types.append(question_type)
            

        #询问物种的培育难度
        if self.check_words(self.level_qwds,question) and  (('Plant' in types) or ('Different_name' in types)):
            # if ('Different_name' in types):
            #     diff_flag=1
            question_type='plant_level'
            question_types.append(question_type)
            
        
        #询问物种的培育温度
        if self.check_words(self.temperature_qwds,question) and  (('Plant' in types) or ('Different_name' in types)):
            # if ('Different_name' in types):
            #     diff_flag=1
            question_type='plant_temperature'
            question_types.append(question_type)
            
        
        #询问物种的酸碱范围
        if self.check_words(self.ph_qwds,question) and  (('Plant' in types) or ('Different_name' in types)):
            # if ('Different_name' in types):
            #     diff_flag=1
            question_type='plant_ph'
            question_types.append(question_type)
        
        #询问物种的种植方法
        if self.check_words(self.cultivation_method_qwds,question) and  (('Plant' in types) or ('Different_name' in types)):
            # if ('Different_name' in types):
            #     diff_flag=1
            question_type='plant_cultivation_method'
            question_types.append(question_type)
        
        #询问物种的繁殖方式
        if self.check_words(self.reproduction_qwds,question) and  (('Plant' in types) or ('Different_name' in types)):
            # if ('Different_name' in types):
            #     diff_flag=1
            question_type='plant_reproduction'
            question_types.append(question_type)

        #没有理解问题,可能识别出了实体 介绍作物
        if question_type== None and (('Plant' in types) or ('Different_name' in types)):
            # if ('Different_name' in types):
            #     diff_flag=1
            question_type='plant_desc'
            question_types.append(question_type)
        
        #没有理解问题,也没有识别出实体
        if question_types == []:
            return {}
        
        #将问题类型存入字典
        data['question_types']=question_types
        # data['diff_flag']=diff_flag

        return data
            

        
    #用jieba实现中文分词并对特征词进行匹配进行分类
    def check_words(self,wds,sent):
        sent_cut=jieba.lcut(sent)
        # print(wds)
        for wd in wds:
            # print(wd)
            if wd in sent_cut:
                return True
        return False


    #利用ahocorasick库,问题过滤子函数
    def check_agriculture(self,question):
        region_wds=[]
        for i in self.region_tree.iter(question): # ahocorasick库 匹配问题  iter返回一个元组，i的形式如(3, (23192, '芥菜'))
            wd=i[1][1] #是匹配到的词 如'芥菜'
            region_wds.append(wd)
        stop_wds=[]
        # 取重复的短的词
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1) #如'强光','强光照',则取出强光
        
        final_wds = [i for i in region_wds if i not in stop_wds]     # final_wds取长词
        final_dict = {i:self.wdtype_dict.get(i) for i in final_wds}#来自于构造词典 # 获取词所对应的实体类型
        # print("实体提取: "+str(final_dict))
        return final_dict

    #ac自动机,加速过滤
    def build_actree(self,wordlist):
        actree=ahocorasick.Automaton()  #初始化,ac自动机,自动过滤违禁数据
        for index,word in enumerate(wordlist):
            actree.add_word(word,(index,word))  #向trie树中添加单词
        actree.make_automaton()     #将trie树转化为Aho-Corasick自动机
        return actree

    #构造词对应的类型
    def build_wdtype_dict(self):
        wd_dict=dict()
        for wd in self.region_words: #对用户输入的问题中提取的关键词构造类型认定的词典
            wd_dict[wd]=[]
            if wd in self.plant_wds:
                wd_dict[wd].append('Plant')
            if wd in self.diff_name_wds:
                wd_dict[wd].append('Different_name')
            if wd in self.color_wds:
                wd_dict[wd].append('Color')
            if wd in self.category_wds:
                wd_dict[wd].append('Category')
            if wd in self.taste_wds:
                wd_dict[wd].append('Taste')
            if wd in self.shape_wds:
                wd_dict[wd].append('Shape')
            if wd in self.light_wds:
                wd_dict[wd].append('Light')
            if wd in self.session_wds:
                wd_dict[wd].append('Session')
            if wd in self.level_wds:
                wd_dict[wd].append('Level')
            if wd in self.temperature_wds:
                wd_dict[wd].append('Temperature')
            if wd in self.ph_wds:
                wd_dict[wd].append('Ph')
        return wd_dict


if __name__=='__main__':
    a=Questionclassifier()
    # question="田七是哪一类作物"
    # question="三七在春季和中光条件下需要什么样的ph值和培育难度怎么样"
    # question="鸡矢果的别名有什么"
    # question="培育鸡矢果的酸碱范围是多少"
    while(1):
        question=input("问题: ")
        data=a.classify(question)
        # args=data['args']
        # entity_dict={}
        # for arg,types in args.items():
        #     for type in types:
        #         if type not in entity_dict:
        #             #新增:用列表存储arg,防止有多个实体的问题
        #             entity_dict[type]=[arg]
        #         else:
        #             entity_dict[type].append(arg)
        print(data)
        # print(args)
        # print(entity_dict)




