import os
import requests

# 课件
# 上2 134 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617377801905/1617377801905.files/
# 下1 29 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617428161454/1617428161454.files/1.png
# 下2 58 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617428301000/1617428301000.files/1.png

# 答案
# 上2 9 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617327609324/1617327609324.files/1.png
# 上3 39 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617327683863/1617327683863.files/1.png
# 上4 16 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617327949762/1617327949762.files/2.png
# 上5 18 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328080528/1617328080528.files/1.png
# 上6 缺失
# 上7 4 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328218283/1617328218283.files/1.png
# 上8 6 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617326013657/1617326013657.files/1.png
# 上9 7 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328287119/1617328287119.files/1.png
# 上10 3 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328355340/1617328355340.files/2.png
# 上11 2 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328394941/1617328394941.files/1.png
# 上12 4 https://abook.hep.com.cn/ICourseFiles/5000002911/swfresourses/2021/7/13/1626149896278/1626149896278.files/2.png
# 上13 8 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328451120/1617328451120.files/1.png
# 下2 3 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431461271/1617431461271.files/1.png
# 下3 18 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431474802/1617431474802.files/1.png
# 下4 5 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431511575/1617431511575.files/1.png
# 下5 4 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431539826/1617431539826.files/1.png
# 下6 2 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431551387/1617431551387.files/1.png
# 下7 3 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431556201/1617431556201.files/1.png
# 下8 15 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431567600/1617431567600.files/1.png
# 下9 8 https://abook.hep.com.cn/ICourseFiles/5000002911/swfresourses/2021/4/3/1617436590233/1617436590233.files/1.png
# 下10 5 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/3/1617431593818/1617431593818.files/1.png
# 下11 2 https://abook.hep.com.cn/ICourseFiles/5000002567/swfresourses/2021/4/2/1617328394941/1617328394941.files/1.png

folder_name = "答案/上12"    #1
urlstr = '''
https://abook.hep.com.cn/ICourseFiles/5000002911/swfresourses/2021/7/13/1626149896278/1626149896278.files/2.png
'''                        #2
page = 4


for i in range(1,page+1):
    index_2021 = urlstr.find("2021")
    first_slash_index = urlstr.find("/", index_2021 + 1)
    second_slash_index = urlstr.find("/", first_slash_index + 1)
    third_slash_index = urlstr.find("/", second_slash_index + 1)
    fourth_slash_index = urlstr.find("/", third_slash_index + 1)
    iden = urlstr[third_slash_index+1:fourth_slash_index]        
    date = urlstr[second_slash_index+1]                 
    url = f"https://abook.hep.com.cn/ICourseFiles/5000002911/swfresourses/2021/4/{date}/{iden}/{iden}.files/{i}.png"   
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
    print(f"图片{i}已保存在'{folder_name}'文件夹内")
    
