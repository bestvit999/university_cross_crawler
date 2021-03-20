from urllib import request
from lxml import etree
import pandas as pd
import decoder

def get_table_element(url="file:///Users/zhe/Documents/vscode/crawler/7.html"):
    # get html by local file ------------------------- #
    page = request.urlopen(url).read()
    tree = etree.HTML(page)
    # xpath ------------------------------------------ #
    rows = tree.xpath('//*[@id="mainContent"]/table[1]/tbody')
    admits_xpath = './tr/td[2]/div' #[1:]
    imgs_xpath = './tr/td[3]/div/img'
    names_xpath = './tr/td[4]' #[1:]
    collections_xpath = './tr/td[5]/div[1]/div/table/tbody'
    tmp = '//*[@id="mainContent"]/table[1]/tbody/tr[4]/td[5]/div[1]/div/table/tbody/tr[1]/td[3]/div/div[1]'
    tmp = '//*[@id="mainContent"]/table[1]/tbody/tr[4]/td[5]/div[1]/div/table/tbody/tr[2]/td[3]/div/div/div[1]'
    tmp = '//*[@id="mainContent"]/table[1]/tbody/tr[4]/td[5]/div[1]/div/table/tbody/tr[6]/td[3]/div/div/div[1]'
    # get elements by xpath -------------------------- #
    title = [e.replace('\xa0','').replace('\n', '') for e in rows[0].xpath('./tr/td/div/text()[2]')][0]
    ## crawler start -------------------------------- #
    print("start crawler on {title}, decoding the identifications...".format(title=title))
    index = ['一階甄試', '准考證號碼', '姓名', '校系名稱', '二階甄試']
    col_1 = [e.text for e in rows[0].xpath(admits_xpath)][1:] # 一階甄試
    col_2 = [e.get('src') for e in rows[0].xpath(imgs_xpath)] # 准考證號碼 # image_base64
    col_2 = [decoder.base64_to_text(e) for e in col_2]
    col_3 = [e.text for e in rows[0].xpath(names_xpath)][1:] # 姓名
    collections = rows[0].xpath(collections_xpath) # iterator
    col_4 = [', '.join([s.replace('\n', ' ') for s in schools.xpath('tr/td[2]/div/a/text()')]) for schools in collections] # 校系名稱
    col_5 = [second_admits.xpath('tr/td[3]/div/div[1]/text()') for second_admits in collections] # need to be cleaned
    col_5 = [list(filter(lambda a: a != '\n' and a != '\n\n' and a != ' \n' and a != '\n ', l)) for l in col_5] # cleaned
    col_6 = [second_admits.xpath('tr/td[3]/div/div/div[1]/text()') for second_admits in collections] # need to be combined
    for i in range(len(col_5)):
        col_5[i].extend(col_6[i])
    col_5 = [', '.join(l) for l in col_5] # 二階甄試
    # output elements to DataFrame ------------------- #
    data = {
        index[0] : col_1,
        index[1] : col_2,
        index[2] : col_3,
        index[3] : col_4,
        index[4] : col_5,
    }
    df = pd.DataFrame(data)
    # export to CSV ----------------------------------- #
    df.to_csv('./csv/{}.csv'.format(title), index=False, encoding='utf-8-sig')