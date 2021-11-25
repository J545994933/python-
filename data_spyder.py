from bs4 import BeautifulSoup
import requests
import time


def get_data(data_url):
    print(data_url)
    wb1_data = requests.get(data_url)
    wb1_data.encoding = 'gb2312'
    soup = BeautifulSoup(wb1_data.text, 'lxml')
    # f.write('\n'+ title + '\n')
    passages = soup.select(' div.content  > p')
    # print(passages[3].get_text())
    passages_num = len(passages)
    passages_index = 0
    data_text = ''
    file_path = r'./data1/'
    data_num = 0


    while True:
        if passages[passages_index].find('strong') != None and data_num == 0:

            file_title = passages[passages_index].get_text()
            data_text = ''
            data_num +=1
            passages_index +=1

        elif passages[passages_index].find('strong') != None and data_num != 0:

            if data_text == '':
                pass
            else:
                file_title = file_title.strip()
                file_name = file_path + file_title + '.txt'
                print(file_name)
                with open(file_name,'w',encoding='utf-8') as file:

                    file.write(data_text)


            file_title = passages[passages_index].get_text()
            data_text = ''
            data_num +=1
            passages_index += 1

        data_text = data_text + passages[passages_index].get_text() + '\n'
        passages_index += 1
        # print(passages_index,passages_num)

        if passages_index >= passages_num-1 or '相关文章' in passages[passages_index].get_text():
            file_title = file_title.strip()
            file_name = file_path + file_title + '.txt'
            print(file_name)
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(data_text)
            return



# 获取目标网址下所有资料链接
def get_urls(single_url):
    print(1)
    url_head = 'http://www.ruiwen.com/'
    wb_data = requests.get(single_url)
    wb_data.encoding = 'gb2312'
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # print(soup)
    infos = soup.select('div.main > div.list_lan.col_box > ul > li > a')
    # print(infos)
    # time.sleep(4)
    for info in infos:
        try:
            data_url = info.get("href")
            time.sleep(4)
            print(data_url)
            data_url = url_head + data_url
            get_data(data_url)
        except :
            pass


# 将目标网址写入一个list中

start_url = 'http://www.ruiwen.com/wenxue/shici/'
get_urls(start_url)


