#                                       HTML Basics / HTML 基础

##                                  1. 列表 / List
* 列表的应用场景: 
    - 场景: 在网页中按照"行"展示关联性的内容, 如: 新闻列表, 排行榜, 账单等
    - 特点: 按照行的方式, 整齐显示内容
    - 种类: 1.无序列表  2.有序列表  3.自定义列表

###         1) 无序列表
* 场景: 在网页中表示一组无顺序之分的列表, 如: 新闻列表
* 标签组成: 
        标签名                      说明
          ul             表示无序列表的整体, 用于包裹li标签
          li             表示无序列表的每一项, 用于包含每一行的内容
* 显示特点: 
    · 列表的每一项前默认显示圆点标识
* 注意点: 
    - ul标签只允许包含li标签
    - li标签可以包含任意内容
* 例子:     
        水果列表
    · 榴莲
    · 香蕉
    · 苹果

###         2) 有序列表
* 场景: 在网页中表示一组有顺序之分的列表, 如: 排行榜    
* 标签组成: 
        标签名                      说明
          ol             表示有序列表的整体, 用于包裹li标签
          li             表示有序列表的每一项, 用于包含每一行的内容
* 显示特点: 
    · 列表的每一项前默认显示序号标识
* 注意点: 
    - ol标签只允许包含li标签
    - li标签可以包含任意内容
* 例子:     
        成绩排行榜
    1. 马云: 100分
    2. 马化腾: 95分
    3. 蔡徐坤: 50分

###         3) 自定义列表
* 场景: 在网页的底部导航中通常会使用自定义列表实现
* 标签组成: 
        标签名                      说明
          dl             表示自定义列表的整体, 用于包裹dt/dd标签
          dt             表示自定义列表的主题
          dd             表示自定义列表的针对主题的每一项内容
* 显示特点: 
    - dd前会默认显示缩进效果
* 注意点:
    - dl标签只允许包含dt/dd标签
    - dt/dd标签可以包含任意内容

##                                  2. 表格标签 / table tag

###         1) 基本标签
* 场景: 在网页中以行+列的单元格的方式整齐展示数据, 如: 学生成绩表
* 基本标签: 
        标签名                              说明
        table                     表格整体, 可用于包裹多个tr
        tr(table row)              表格每行, 可用于包裹td
        td(table data)             表格单元格, 可用于包裹内容
* 注意点: 
    - 标签的嵌套关系: table > tr > td

###         2) 表格相关属性
* 场景: 设置表格基本使用效果
* 常见相关属性: 
        属性名             属性值                     效果
        border              数字                    边框宽度
        width               数字                    表格宽度
        height              数字                    表格高度
* 注意点: 实际开发时针对与样式效果推荐使用CSS设置

###         3) 表格标题和表头单元格标签
* 场景: 在表格中表示整体大标题和一列小标题
* 标签组成: 
    标签名                     名称                            说明
    caption                 表格大标题                表示表格整体大标题, 默认在表格整体顶部居中位置显示
    th(tableheadercell)     表头单元格                表示一列小标题, 通常用于表格第一行, 默认内部文字加粗并居中显示
* 注意点: 
    - caption标签写在table标签内部
    - th标签写在tr标签内部(用于替换td标签)

###         4) 表格的结构标签(了解)
* 场景: 让表格的内容结构分组, 突出表格的不同部分(头部, 主体, 底部), 使语义更加清晰
* 结构标签:
        标签名               说明
        thead              表格头部
        tbody              表格主体
        tfoot              表格底部
* 注意点: 
    - 表格结构标签内部用于包裹tr标签
    - 表格的结构标签可以省略

###         5) 合并单元格
* 场景: 将水平或垂直多个单元格合并成一个单元格
* 代码实现: 
    1. 明确合并哪几个单元格
    2. 通过左上原则, 确定保留谁删除谁
        - 上下合并 -> 只保留最上的, 删除其他
        - 左右合并 -> 只保留最左的, 删除其他
    3. 给保留的单元格设置: 跨行合并(rowspan) 或者 跨列合并(colspan)
        属性名             属性值                     说明
        rowspan        合并单元格的个数              跨行合并, 将多行的单元格垂直合并
        colspan        合并单元格的个数              跨列合并, 将多列的单元格水平合并
* 注意点: 
    - 只有同一个结构标签中的单元格才能合并, 不能跨结构标签合并

##                                  3. 表单标签
1. input系列标签
2. button按钮标签
3. select下拉菜单标签
4. textarea文本域标签
5. label标签

* HTML 表单用于收集用户的输入信息
* HTML 表单表示文档中的一个区域，此区域包含交互控件，将用户收集到的信息发送到 Web 服务器。
* 表单标签是允许用户在表单中输入内容, 比如：文本域（textarea）、下拉列表（select）、单选框（radio-buttons）、复选框（checkbox） 等等

###                     0) Form 标签
<form method="get" action="/index">  method 是请求方式(get或post)  action是提交的地址 
    表单标签....
</form>


###                     1) Input系列标签
* 场景: 在网页中显示收集用户信息的表单效果, 如: 登录页, 注册页
* 标签名: input
    - input标签可以通过type属性值的不同, 展示不同效果
* type属性值:
        标签名               type属性值                     说明
        input                   text                文本框,用于输入单行文本
        input                 password              密码框, 用于输入密码
        input                   radio                  单选框, 用于多选一
        input                  checkbox                多选框, 用于多选多
        input                   file               文件选择, 用于之后上传文件  
        input                   submit                  提交按钮, 用于提交
        input                   reset                   重置按钮, 用于重置
        input                   button           普通按钮, 默认无功能,之后配合js添加功能     

###         1.1) Input系列标签-文本框和密码框 / text & password
* 场景: 在网页中显示 输入单行文本 的表单控件
* type属性值: text
* 常用属性: 
    placeholder                 占位符, 提示用户输入内容的文本

###         1.2) Input系列标签-单选框和多选框 / radio & checkbox
* 场景: 在网页中显示 多选一 的单选表单控件
* type属性值: radio
* 常用属性: 
    name                 分组, 有相同name属性值的单选框为一组, 一组中同时只能有一个被选中
    checked                                 默认选中

###        1.3) Input系列标签-文件选择 / file
* 场景: 在网页中显示 文件选择 的表单控件
* type属性值: file
* 常用属性: 
    multiple                多文件选择

###         1.4) Input系列标签-按钮 / input button
* 场景: 在网页中显示 不同功能的按钮 表单控件
* type属性值:
        标签名               type属性值                     说明 
        input                   submit                  提交按钮, 点击之后提交数据给后端服务器
        input                   reset                   重置按钮, 点击之后恢复表单默认值
        input                   button           普通按钮, 默认无功能,之后配合js添加功能
* 注意点:
    - 如果需要实现以上按钮功能, 需要配合form标签使用
    - form使用方法: 用form标签把表单标签一起包裹起来即可

###                     2) button按钮标签
* 场景: 在网页中显示 用户点击的按钮
* 标签名: button
* type属性值(同input的按钮系列):
        标签名               type属性值                     说明 
        input                   submit                  提交按钮, 点击之后提交数据给后端服务器
        input                   reset                   重置按钮, 点击之后恢复表单默认值
        input                   button           普通按钮, 默认无功能,之后配合js添加功能
* 注意点:
    - 谷歌浏览器中button默认是提交按钮
    - button标签是双标签, 更便于包裹其他内容: 文字, 图片等

###                     3) select下拉菜单标签
* 场景: 在网页中 提供多个选择项的下拉菜单表单控件
* 标签组成: 
    - select标签: 下拉菜单的整体
    - option标签: 下拉菜单的每一项
* 常见属性: 
    - selected: 下拉菜单的默认选中       

###                     4) textarea文本域标签
* 场景: 在网页中提供 可输入多行文本的表单控件
* 标签名: textare
* 常见属性: 
    - cols: 规定了文本域内可见宽度
    - rows: 规定了文本域内可见行数
* 注意点: 
    - 右下角可以拖拽改变大小
    - 实际开发时针对样式效果推荐使用CSS设置
   
###                     5) label标签
* 场景: 常用于绑定内容与表单标签的关系
* 标签名: label
* 使用方法(1):
    1.使用label标签把内容(如: 文本)包裹起来
    2.在表单标签上添加id属性
    3.在label标签的for属性中设置对应的id属性值
* 使用方法(2):
    1.直接使用label标签把内容(如: 文本) 和表单标签一起包裹起来
    2.需要把label标签的for属性删除即可

##                                  4. 语义化标签
###                     1) 没有语义的布局标签: div & span
* 场景: 实际开发网页时会大量频繁的使用到 div 和 span 这两个没有语义的布局标签
* div '块级'标签: 一行只显示一个(独占一行)
* span '行内'标签: 一行可以显示多个

###                     2) 有语义的布局标签(了解) - 做手机端网页时用的
* 场景: 在HTML5新版本中, 推出了一些有语义的布局标签供开发者使用
* 标签: 
            标签名                            语义
            header                          网页头部
            nav                             网页导航
            footer                          网页底部
            aside                           网页侧边栏
            section                         网页区块
            article                         网页文章
* 注意点: 
    - 以上标签显示特点和div一致, 但是比div多了不同的语义

##                                  5. 字符实体 / Character Entity
* 场景: 在网页中展示特殊符号效果时, 需要使用字符实体替代
* 结构: &英文;
* 常见字符实体: 
        显示结果:           描述:                实体名称:
                            空格                  &nbsp;
           <               小于号                 &lt;
           >               大于号                 &gt;
           &                和号                  &amp;
           "                引号                  &quot;
           '                撇号                  &apos;(IE不支持)
           &	                                  &amp;
            
##                                  6. 块级 和 行内标签
###     1) 块级标签
    <h1></h1>
    <div></div>

###     2) 行内标签 
    <span></span>
    <a></a>
    <img />