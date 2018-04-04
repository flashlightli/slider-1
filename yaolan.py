from urllib import request
from lxml import etree
import xlwt

wb = xlwt.Workbook()
# 新增一个表单
sh = wb.add_sheet('摇篮website')
sh.write(0, 0, '标签序号')
sh.write(0, 1, 'URL')
sh.write(0, 2, '标题')
sh.write(0, 3, '内容')
index = 1

html = request.urlopen('http://www.yaolan.com/zhishi/preconception/')
html = html.read().decode('utf-8')
select = etree.HTML(html)
URL1 = select.xpath(u'//*[@id="page"]/div[4]/div/div[@class="tb_all clear"]/div/div/div/span/a/@href')
URL2 = select.xpath(u'//*[@id="page"]/div[4]/div/div[@class="tb_all clear"]/div/div/div/a/@href')
URL = URL1+URL2
#获取了所有的url标签地址

for url in URL:
    html = request.urlopen(url)
    html = html.read().decode('utf-8')
    select = etree.HTML(html)
    text = select.xpath(u'/html/body/div/div/div/div/div[@class="bka-article"]/h5/a/@title')
    tempP = select.xpath('/html/body/div/div/div/div/div[@class="bka-article"]/div[@class="wenzi"]')
    for i in tempP:
        h2 = text[tempP.index(i)]
        text1 = i.xpath('string(.)')
        sh.write(index, 0, int(URL.index(url)+1))
        sh.write(index, 1, url)
        sh.write(index, 2, h2)
        sh.write(index, 3, text1)
        index = index + 1
        print(index)

wb.save('yaolanWeb.xls')