import wx
from sympy import Matrix, Mod

#-------------------------UI部分-------------------------------

class ArgumentSelect(wx.Frame):
    def __init__(self):
        super().__init__(None, title="参数选择", size=(250, 270))
        
        # 创建菜单栏
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        open_item = file_menu.Append(wx.ID_OPEN, "说明", "Open a file")
        exit_item = file_menu.Append(wx.ID_EXIT, "Exit", "Exit the application")
        menu_bar.Append(file_menu, "帮助")      # 将菜单添加到菜单栏
        self.SetMenuBar(menu_bar)               # 将菜单栏设置为窗口的菜单栏
        self.Bind(wx.EVT_MENU, self.on_open, open_item)
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)
        

        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.param1_label = wx.StaticText(self.panel, label="雷立方个数：")
        self.cube_num = wx.Choice(self.panel, choices=[str(i) for i in range(2, 9)])
        
        self.param2_label = wx.StaticText(self.panel, label="状态种数:")
        self.state_num = wx.Choice(self.panel, choices=[str(i) for i in range(2, 7)])
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.ok_button = wx.Button(self.panel, label="确定")
        self.ok_button.Bind(wx.EVT_BUTTON, self.on_ok)

        self.shut_button = wx.Button(self.panel, label="关闭其他窗口")
        self.shut_button.Bind(wx.EVT_BUTTON, self.on_close_button)
        
        self.sizer.Add(self.param1_label, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.cube_num, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.param2_label, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.state_num, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.ok_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.sizer.Add(self.shut_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.panel.SetSizer(self.sizer)
        
    def on_ok(self, event):
        
        cube_num = int(self.cube_num.GetStringSelection())
        rotate_state = int(self.state_num.GetStringSelection())
        
        Matrix_Frame = MatrixFrame(cube_num, rotate_state)
        Matrix_Frame.Show()
    
    def on_open(self, event):        # 处理打开菜单项的事件
        new_window = wx.Frame(None, title="Introduction", size=(425, 500), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        text = """		    【帮助】\n\n
一、适用范围\n
    本程序用于游戏《原神》稻妻地区 *雷立方解密* 或相似应用场景。
    已知有 n 个雷立方，每击打某个雷立方一次，会有若干个雷立方跟随转动。最终要通过若干次击打，让它们朝向一致，需解出每一个雷立方各需要击打多少次。\n\n
二、算法说明\n
    本程序采用两种算法。\n
    1. 矩阵解法：同余线性方程组\n
    由于每一个雷立方与其他 (n-1) 个雷立方均有关联，引入关联变换矩阵 V 。设待解击打次数为 X ，当前状态为 N ，目标状态为 S 。则待解线性方程组可写作 V * X ≡ (N - S) mod r ，其中 r 为状态变换种类。于是可解出 X = V' * (N - S) mod r 。本程序使用 sympy 库实现上述矩阵运算。
    值得注意的是，当 |V| = 0 时，矩阵 V 是奇异的，无法使用此方法求解。在这种情况下，本程序采用下列穷举方法。\n
    2. 穷举解法：函数迭代\n
    由于总存在至少一种解法，且状态变换存在循环，于是对每一个雷立方的击打次数进行穷举。然后判断在这种击打组合下，最后的朝向是否一致，如果一致，则存储在列表中，最后输出其中一组解即可。\n
    更详细的算法说明请查看 PDF 文档。\n\n
三、使用方法\n
    选择当前雷立方个数、变换状态种类数，点击确定。
    在新窗口依次按列选择每一个雷立方所关联的雷立方（例如击打 A 时，A、B、C均旋转：则将第一列第1、2、3排均点亮），输入当前状态（选取特定方向为 1 ，其余的按顺序排列即可。建议将朝向自己的方向假定成最大的状态数），点击“击打次数：”按钮，即显示每一个雷立方击打次数的运算结果。\n\n
四、结果说明\n
    最终可能产生三种结果：
    1. 数字（如“1 2 3 1”），说明这是由矩阵解法解得；
    2. 括号数字（如“[1] [2] [3] [1]”），说明这是由穷举解法解得，故速度会稍慢；
    3. None None None None，说明无解或程序出错，请重新尝试。\n\n\n
                                    xy\n
                                2024年2月2日
        """
        text_ctrl = wx.TextCtrl(new_window, style=wx.TE_MULTILINE | wx.TE_READONLY)
        text_ctrl.SetValue(text)
        font = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, faceName="黑体")
        text_ctrl.SetFont(font)
        new_window.Show()
        
    def on_exit(self, event):        # 处理退出菜单项的事件
        self.Close()

    def on_close_button(self, event): # 关闭其他窗口
        top_windows = wx.GetTopLevelWindows()
        current_window = self
        for window in top_windows:
            if window != current_window:
                window.Close()

class MatrixFrame(wx.Frame):
    def __init__(self, cube_num, rotate_state):
        super().__init__(None, title=f"{cube_num}个雷立方，{rotate_state}种状态", size=(400, 300))
        
        # 获取屏幕的尺寸
        screen_width, screen_height = wx.GetDisplaySize()
        # 计算窗口的左上角坐标，使其位于屏幕正中间
        window_width, window_height = self.GetSize()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        # 设置窗口的位置
        self.SetPosition((x, y))

        self.matrix_size = cube_num  # 矩阵大小
        self.rotate_state = rotate_state
        self.matrix = [[False for _ in range(self.matrix_size)] for _ in range(self.matrix_size)]  # 创建一个默认大小的矩阵
        self.cell_size = 50  # 每个单元格的大小
        
        self.panel = wx.Panel(self)
        self.sizer = wx.GridSizer(self.matrix_size + 4, self.matrix_size + 1, 0, 0)
        
        # 添加列名称
        self.sizer.Add(wx.StaticText(self.panel), 0, wx.EXPAND)
        for i in range(self.matrix_size):
            col_label = chr(ord('A') + i)
            self.sizer.Add(wx.StaticText(self.panel, label=col_label, style=wx.ALIGN_CENTER), 0, wx.EXPAND)
        
        # 添加行名称和单元格
        for i in range(self.matrix_size):
            row_label = '联动'+chr(ord('A') + i)
            self.sizer.Add(wx.StaticText(self.panel, label=row_label, style=wx.ALIGN_CENTER), 0, wx.EXPAND)
            for j in range(self.matrix_size):
                toggle_btn = wx.ToggleButton(self.panel, id=wx.ID_ANY, label="", size=(self.cell_size, self.cell_size))
                toggle_btn.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle)
                toggle_btn.row = i  # 将行索引保存在toggle_btn的属性中
                toggle_btn.col = j  # 将列索引保存在toggle_btn的属性中
                self.sizer.Add(toggle_btn, 0, wx.EXPAND)

        # 添加目前状态	
        self.state_choices = []  # 用于存储所有选择控件的列表
        row_label = '目前状态'
        self.sizer.Add(wx.StaticText(self.panel, label=row_label, style=wx.ALIGN_CENTER), 0, wx.EXPAND)
        for j in range(self.matrix_size):
            state_choice = wx.Choice(self.panel, choices=[str(i) for i in range(1, rotate_state+1)])
            state_choice.SetSelection(0)
            self.sizer.Add(state_choice, 0, wx.EXPAND | wx.ALL, 5)
            self.state_choices.append(state_choice)  # 将选择控件添加到列表中

        # 添加确定按钮
        self.confirm_button = wx.Button(self.panel, label="矩阵法：")
        self.confirm_button.Bind(wx.EVT_BUTTON, self.on_ok)
        self.sizer.Add(self.confirm_button, 2, wx.EXPAND)
        # 添加文本框
        for i in range(0, cube_num):
            exec(f'self.text_ctrl_{i} = wx.StaticText(self.panel, label="", style=wx.ALIGN_CENTER)')
            exec(f"self.sizer.Add(self.text_ctrl_{i}, 0, wx.ALIGN_CENTER)")

        # 添加穷举法按钮
        self.solution_change_button = wx.Button(self.panel, label="穷举法：")
        self.solution_change_button.Bind(wx.EVT_BUTTON, self.on_solution_change)
        self.sizer.Add(self.solution_change_button, 2, wx.EXPAND)
        # 添加文本框
        for i in range(0, cube_num):
            exec(f'self.text_ctrl_all_{i} = wx.StaticText(self.panel, label="", style=wx.ALIGN_CENTER)')
            exec(f"self.sizer.Add(self.text_ctrl_all_{i}, 0, wx.ALIGN_CENTER)")

        self.panel.SetSizer(self.sizer)
        
    def on_toggle(self, event): 
        toggle_btn = event.GetEventObject()
        row = toggle_btn.row
        col = toggle_btn.col
        self.matrix[row][col] = toggle_btn.GetValue()
        
        self.vary_matrix = [[0 for _ in range(self.matrix_size)] for _ in range(self.matrix_size)]  # 创建一个新的矩阵
        
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                if self.matrix[i][j]:
                    self.vary_matrix[i][j] = 1

        self.vary_matrix = Matrix(self.vary_matrix)

        self.panel.Layout()  # 更新面板布局，实现实时反馈

    def on_ok(self, event):
        # 获取当前所有选择的值
        now_state = [int(choice.GetStringSelection()) for choice in self.state_choices]
        self.now_state = Matrix(now_state)
        try:
            result = calculation(self.matrix_size, self.rotate_state, self.vary_matrix, self.now_state, 1)
            if result[0] == '矩阵奇异':
                self.on_solution_change(self)
        except:
            result = ['None']*self.matrix_size
        for i in range(0, self.matrix_size):
            exec(f"self.text_ctrl_{i}.SetLabel('')")
            exec(f"self.text_ctrl_{i}.SetLabel(str((result[i])))")

    def on_solution_change(self, event):
        # 获取当前所有选择的值
        now_state = [int(choice.GetStringSelection()) for choice in self.state_choices]
        self.now_state = Matrix(now_state)
        try:
            result = calculation(self.matrix_size, self.rotate_state, self.vary_matrix, self.now_state, 0)
        except:
            result = ['None']*self.matrix_size
        for i in range(0, self.matrix_size):
            exec(f"self.text_ctrl_all_{i}.SetLabel('')")
            exec(f"self.text_ctrl_all_{i}.SetLabel(str((result[i])))")


#------------------------计算部分----------------------------
            
def calculation(cube_num, state_num, vary_matrix, now_state, solution_choice):
    solution_state = Matrix([state_num] * cube_num)
    
    if solution_choice:      # 矩阵解法
        if (vary_matrix.det() != 0) :
            result = vary_matrix.inv() * (solution_state - now_state)
            result = result.T
            result = result.applyfunc(lambda x: Mod(x, state_num))
        else:
            result = ['矩阵奇异']+['']*(cube_num-1)

    else:                           # 穷举解法
        result = []
        prime_result = Matrix([1]*cube_num)
        result = all_result(cube_num, state_num, vary_matrix, now_state, solution_state, prime_result, result)
        result = result[0]
    return result

def all_result(cube_num, state_num, vary_matrix, now_state, solution_state, prime_result, result): # 穷举法
    if cube_num == 0:
        final = vary_matrix * prime_result + now_state
        final = final.applyfunc(lambda x: Mod(x, state_num))
        final_equal = all(final.row(i).equals(final.row(0)) for i in range(1, final.rows))
        if final_equal:
            result.append(prime_result.tolist())
            result.append(final[0])  # 将结果添加到列表中
    else:
        for i in range(state_num):
            prime_result[cube_num-1] = i
            all_result(cube_num - 1, state_num, vary_matrix, now_state, solution_state, prime_result, result)
    return result

app = wx.App()
frame = ArgumentSelect()
frame.Show()
app.MainLoop()
