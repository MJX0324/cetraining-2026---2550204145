# cetraining-2026---2550204145

#项目名称

项目 ：单词词频统计与排序工具

##信息

姓名：马嘉欣

学号：2550204145

班级：计算机科学与技术1班

##项目简介

这是云端GitHub冲突的第一次实验


•	一、功能演示
•	核心流程（5步流水线）
plain
[输入] 英文文本文件（支持多文件合并）
   ↓
[分词] 正则提取 + 小写统一 + 标点过滤
   ↓
[清洗] 停用词过滤 + 短词过滤（--min-len）
   ↓
[统计] Counter 高效计数（O(n) 时间复杂度）
   ↓
[排序] 频率降序 + 同频字母升序
   ↓
[输出] 终端表格 / JSON文件 / 词云数据
•	6种使用场景
表格
场景	命令	效果
基础统计	python wordfreq.py sample.txt	显示完整词频表
TopN过滤	python wordfreq.py sample.txt -n 20	只显示前20个高频词
多文件合并	python wordfreq.py file1.txt file2.txt	合并统计多个文件
停用词过滤	python wordfreq.py sample.txt --stopwords stopwords.txt	排除常见无意义词
JSON输出	python wordfreq.py sample.txt -o result.json	保存完整统计结果
词云数据	python wordfreq.py sample.txt --wordcloud wc.json	生成词云可视化数据
•	输入输出示例
输入：
plain
Hello world! This is a simple test.
Hello again, world. This test is simple and fun.
输出（终端表格）：
plain
排名   单词                 频率
------------------------------------
1      the                  4
2      is                   3
3      and                  3
4      python               2
...
总单词数（去重）: 18
总单词数（含重复）: 29
________________________________________
•	二、技术方案简介
•	技术栈（零外部依赖）
表格
模块	用途	关键代码
argparse	命令行参数解析	-n, -o, --wordcloud, --stopwords
re（正则）	分词引擎	r'\b[a-z]+\b'
Counter	词频统计核心	Counter(words)，O(n) 复杂度
JSON	结果序列化 + 词云数据生成	json.dump(data, f)
os/sys	文件操作 + 跨平台兼容	os.path.exists(), sys.exit()
•	设计亮点
•	类型注解：全函数使用 -> List[str]、-> Counter 等类型提示
•	异常处理：try-except 包裹文件读取与处理逻辑
•	编码兼容：errors='replace' 防止非UTF-8文件崩溃
•	模块化：输入、分词、统计、排序、输出各功能独立封装
•	架构图（文字版）
plain
┌─────────────────────────────────────────┐
│           核心架构（5大模块）              │
├─────────────┬───────────────────────────┤
│  argparse   │  命令行参数解析              │
├─────────────┼───────────────────────────┤
│  re (正则)  │  分词引擎 r"\b[a-z]+\b"    │
├─────────────┼───────────────────────────┤
│  Counter    │  词频统计核心 O(n)          │
├─────────────┼───────────────────────────┤
│  JSON       │  结果序列化 + 词云数据       │
├─────────────┼───────────────────────────┤
│  os/sys     │  文件操作 + 跨平台兼容        │
└─────────────┴───────────────────────────┘
________________________________________
•	三、AI 使用反思
•	AI 辅助的3个环节
表格
环节	AI贡献	实际应用
正则表达式设计	提供 \b[a-z]+\b 模式建议	精确提取英文单词，过滤标点数字
多级排序算法	建议 key=lambda x: (-x[1], x[0])	频率降序 + 同频字母升序
命令行参数结构	规划参数组合与帮助文档	位置参数 + 可选参数 + 默认值


