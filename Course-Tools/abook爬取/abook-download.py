# 电工电子学（雷勇）abook 课件及答案下载
# by scu-xy 
# contact at xy.hi@qq.com

import os
import requests



# **************
# *            *
# *  用户输入  *
# *            *
# **************

# 需要 课件 还是 答案 （单选）
document_type = '答案'

# 需要第几章的（可多选）
document_chapter = ['上12','下3']




# **************
# *            *
# *  程序核心  *
# *            *
# **************


data_ppt=r'''
上1 缺失
上2 134 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617377801905/1617377801905.files/1.png
上3 87 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/6/7/1623004424455/1623004424455.files/1.png
上4 缺失
上5 49 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617427747338/1617427747338.files/1.png
上6 63 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617421490593/1617421490593.files/1.png
上7 96 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/6/3/1622682596676/1622682596676.files/1.png
上8 缺失
上9 150 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/6/3/1622699460517/1622699460517.files/1.png
上10 52 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617373717863/1617373717863.files/1.png
上11 59 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617372659337/1617372659337.files/1.png
上12 缺失
上13 28 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617427978438/1617427978438.files/1.png
下1 29 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617428161454/1617428161454.files/1.png
下2 58 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617428301000/1617428301000.files/1.png
下3 213 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617428668188/1617428668188.files/1.png
下4 33 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617429300867/1617429300867.files/1.png
下5 122 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617429407264/1617429407264.files/1.png
下6 51 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617429839055/1617429839055.files/1.png
下7 65 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617430054749/1617430054749.files/1.png
下8 117 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617430275101/1617430275101.files/1.png
下9 93 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617430681879/1617430681879.files/1.png
下10 44 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431139050/1617431139050.files/1.png
下11 53 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431272813/1617431272813.files/1.png
'''
data_ppt_list = [line.split() for line in data_ppt.split("\n") if line.strip()]

data_answer = r'''
上1 无
上2 9 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617327609324/1617327609324.files/1.png
上3 39 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617327683863/1617327683863.files/1.png
上4 16 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617327949762/1617327949762.files/2.png
上5 18 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328080528/1617328080528.files/1.png
上6 缺失
上7 4 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328218283/1617328218283.files/1.png
上8 6 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617326013657/1617326013657.files/1.png
上9 7 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328287119/1617328287119.files/1.png
上10 3 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328355340/1617328355340.files/2.png
上11 2 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328394941/1617328394941.files/1.png
上12 4 https://abook.hep.com.cn/ICourseFiles/5000002911/swfresourses/2021/7/13/1626149896278/1626149896278.files/2.png
上13 8 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328451120/1617328451120.files/1.png
下1 无
下2 3 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431461271/1617431461271.files/1.png
下3 18 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431474802/1617431474802.files/1.png
下4 5 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431511575/1617431511575.files/1.png
下5 4 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431539826/1617431539826.files/1.png
下6 2 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431551387/1617431551387.files/1.png
下7 3 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431556201/1617431556201.files/1.png
下8 15 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431567600/1617431567600.files/1.png
下9 8 https://abook.hep.com.cn/ICourseFiles/5000002911/swfresourses/2021/4/3/1617436590233/1617436590233.files/1.png
下10 5 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431593818/1617431593818.files/1.png
下11 2 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328394941/1617328394941.files/1.png
'''
data_answer_list = [line.split() for line in data_answer.split("\n") if line.strip()]


document_list = data_ppt_list if (document_type == '课件') else data_answer_list

for each_chapter in document_chapter:
    print('\n')

    list_number = (each_chapter[0] == '下') * 13 + (int(each_chapter[1:]) - 1)

    if not document_list[list_number][1].isdigit():
        print(f'{each_chapter} 没有{document_type}')
        continue

    folder_name = document_type + '/'+ each_chapter   

    urlstr = document_list[list_number][2]
    page = document_list[list_number][1]

    for i in range(1, int(page) + 1):
        # index_2021 = urlstr.find("2021")
        # first_slash_index = urlstr.find("/", index_2021 + 1)
        # second_slash_index = urlstr.find("/", first_slash_index + 1)
        # third_slash_index = urlstr.find("/", second_slash_index + 1)
        # fourth_slash_index = urlstr.find("/", third_slash_index + 1)
        # iden = urlstr[third_slash_index+1:fourth_slash_index]        
        # date = urlstr[second_slash_index+1]                 
        # url = f"https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/6/{date}/{iden}/{iden}.files/{i}.png"  
        url = urlstr.strip()[:-5] + f"{i}.png"   
        response = requests.get(url)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(current_dir, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_path = os.path.join(folder_path, f"{i}.png")
        with open(file_path, "wb") as file:
            file.write(response.content)

        # os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[F\033[K", end='')
        print(f"图片 {i} / {page} 已保存在 '{folder_name}' 文件夹内")

    print('\n')
    
