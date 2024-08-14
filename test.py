import pyperclip

my_dict = {'蔡松伶':'202110411418',
           '廖航生': '202110411318', 
           '林锐': '202110411401', 
           '许志强': '202110411404',
           '刘欣雨':'202110411209',
           '刘兴蕊':'202110411116',
           '姜文鑫':'202110411413',
            '牟壕': '202110411415',
            '石东东': '202110411411',
            '杨峻诚': '202110411417',
            '徐良禹': '202110411422',
            '许金': '202210411413',
            '张吉': '202210414225'
}
output=""
for key, value in my_dict.items():
    output=output+(f"<tr><td><span>{key}</span></td><td><a href='http://app.rennengda.com/emp/reportContent.html?token=89988ced-1b95-4934-b031-5b2c2e74de0e_202110411318&file=http://cos.rennengda.com/emp/24cdu/2025届毕业生-计算机学院-计算机科学与技术(本)-{value}-{key}.pdf'><span>2025届毕业生-计算机学院-计算机科学与技术(本)-{value}-{key}.pdf (rennengda.com)</span></a></td></tr>")

pyperclip.copy(output)