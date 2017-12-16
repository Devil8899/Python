#_author: liuz
#date: 2017/12/15

#学习xml 序列化的处理

#1.引用模块xml.etree.cElementTree
import xml.etree.cElementTree as et

#2.解析xml
tree=et.parse('test.xml')
#3.获取根
root=tree.getroot()

#遍历xml文档
#for child in root:
    #print(child.tag,child.attrib) #获取第一层的标签名和属性名
   # for i in child:
       # print(i.tag,i.text) #获取标签名和属性值
'''
tag     标签名
text    文本
attrib  属性
'''
#只循环单独节点
#for node in root.iter('billid'):
 #   print(node.text,node.tag)


#修改
for node in root.iter('billid'):
    new_year=int(node.text) + 2
    node.text=str(new_year)      #修改文本
    node.set('updated','no')     #增加属性

tree.write('test.xml')

#删除remove()方法
# for child in root:
#     for i in child:
#          if i.tag=='custcode':
#              child.remove(i)
# tree.write('test.xml')


#创建一个xml文件
new_xml=et.Element('namelist')  #创建根
name=et.SubElement(new_xml,'name',attrib={'id':'name1'}) #创建子节点name节点
age=et.SubElement(new_xml,'age',attrib={'checked':'false'}) #创建一个age节点
name.text='jerry'
age.text='20'
name2=et.SubElement(name,'childname') #给name节点添加子节点

et2=et.ElementTree(new_xml)  #设置根节点
et2.write('test2.xml',encoding='utf-8',xml_declaration=True) #写入文本
et.dump(new_xml) #


'''
python对XML的解析
常见的XML编程接口有DOM和SAX，这两种接口处理XML文件的方式不同，当然使用场合也不同。
python有三种方法解析XML，SAX，DOM，以及ElementTree:
1.SAX (simple API for XML )
python 标准库包含SAX解析器，SAX用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。
2.DOM(Document Object Model)
将XML数据在内存中解析成一个树，通过对树的操作来操作XML。
3.ElementTree(元素树)
ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少。
注：因DOM需要将XML数据映射到内存中的树，一是比较慢，二是比较耗内存，而SAX流式读取XML文件，比较快，占用内存少，但需要用户实现回调函数（handler）。


'''
