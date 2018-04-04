from urllib import request
from lxml import etree
import xlwt
import ssl

#处理https这种情况
ssl._create_default_https_context = ssl._create_unverified_context
URL = 'http://baike.pcbaby.com.cn/yunqian.html'

wb = xlwt.Workbook()
# 新增一个表单
sh = wb.add_sheet('PCbabywebsite')
sh.write(0, 0, 'URL')
sh.write(0, 1, '标题')
sh.write(0, 2, '内容')
index = 1

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = {'User-Agent' : user_agent ,'Referer' : 'https://baike.pcbaby.com.cn/yunqian.html'}
temp = request.Request(URL, None, headers=headers)
html = request.urlopen(temp)
html = html.read().decode('gb2312')
select = etree.HTML(html)
URL1 = select.xpath('//*[@id="Jbaike"]/div/div[@class="baike-tb-dl"]/dl/dd/span/a/@href')

for url1 in URL1:
    #//*[@id="Jbody"]/div[8]/div[1]/div[6]/div[4]/p[1]/ac
    user_agent2 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    heads2 = {'User-Agent' : user_agent2 , 'Referer' : 'https:'+url1}
    temp2 = request.Request('https:'+url1, None, headers=heads2)
    try:
        html2 = request.urlopen(temp2)
    except Exception as e:
        continue
    html2 = html2.read().decode('GB18030')
    select = etree.HTML(html2)
    url2 = select.xpath(u'//*[@id="Jbody"]/div/div/div/div/p[@class="m-th pt22"]/a/@href')
    for url3 in url2:
        print(url3)
        html3 = request.urlopen("https:"+url3)
        html3 = html3.read().decode('GB18030')
        select3 = etree.HTML(html3)
        print(select3)
        h3 = select.xpath(u'/html/body/div/div/div/div/p[@class="fl"]/text()')
        text3 = select.xpath(u'/html/body/div/div/div/div/div[@class="art-text"]/p/text()')
        print(h3)
        print(text3)