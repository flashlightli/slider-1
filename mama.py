from urllib import request
from lxml import etree
import xlwt

URL = ['http://www.mama.cn/z/t674/','http://www.mama.cn/z/t675/','http://www.mama.cn/z/t1181/','http://www.mama.cn/z/t1182/','http://www.mama.cn/z/t1183/']

wb = xlwt.Workbook()
# 新增一个表单
sh = wb.add_sheet('妈妈website')
sh.write(0, 0, 'URL')
sh.write(0, 1, '标题')
sh.write(0, 2, '内容')
index = 1


for url1 in URL:
    html = request.urlopen(url1)
    html = html.read().decode('utf-8')
    select = etree.HTML(html)
    URL2 = select.xpath(u'//*[@id="200302"]/div/div/ul/li/a/@href')

    for url2 in URL2:
        html = request.urlopen(url2)
        html = html.read().decode('utf-8')
        select = etree.HTML(html)
        URL3 = select.xpath(u'/html/body/div/div/div/div/div/div[@class="mod-title"]/a/@href')

        for url3 in URL3:
            try:
                html = request.urlopen(url3)
            except Exception as e:
                continue
            html = html.read().decode('utf-8')
            select = etree.HTML(html)
            Mh1 = select.xpath(u'/html/body/div[5]/div[2]/div[1]/div/div[1]/h1/text()')
            Mp = select.xpath(u'/html/body/div[5]/div[2]/div[1]/div/div[2]/div/p/text()')
            Mstr , MlinkStr = "" , ""
            for i in Mp:
                Mstr += i

            Mh1 = Mh1[0]

            # 按位置添加数据
            sh.write(index, 0, url3)
            sh.write(index, 1, Mh1)
            sh.write(index, 2, Mstr)
            index = index+1
            print(index)

wb.save('mamaWeb.xls')