import argparse

def add_line_to_html(htmlPath, issueTitle, issueNum, keyword):
    try:
        # 读取原始 HTML 文件
        with open(htmlPath, 'r', encoding='utf-8') as file:
            htmlContent = file.readlines()

        # 寻找包含关键字的行的位置
        insertIdx = -1
        cateLine = -1
        foundCategory = False
        for i, line in enumerate(htmlContent):
            if "category" in line and keyword in line:
                foundCategory = True
                cateLine = i + 1
                break
        if foundCategory:
            for j in range(cateLine, len(htmlContent)):
                if "button-group" in htmlContent[j]:
                    insertIdx = j + 1
                    break
        else:
            print("fail")

        # 如果找不到关键字，将内容添加到文件末尾
        if insertIdx == -1:
            insertIdx = len(htmlContent)
            
        lineToAdd = "<button onclick=\"openLink(\'https://github.com/cosdt/cosdt.github.io/issues/" + str(issueNum) + "\')\" class=\"button: orange-button\">"+ issueTitle +"</button>"

        # 在指定位置插入新的内容
        htmlContent.insert(insertIdx, lineToAdd + '\n')
        
        with open(htmlPath, 'w', encoding='utf-8') as file:
            file.writelines(htmlContent)

        print(f"成功在 {htmlPath} 中添加了新的内容。")

    except Exception as e:
        print(f"发生错误：{e}")



def main():
    # 使用 argparse 处理命令行参数
    parser = argparse.ArgumentParser(description='在 HTML 文件中添加一行内容')
    parser.add_argument('htmlPath', type=str, default="./knowledgeMap/templates/index.html", help='HTML 文件路径')
    parser.add_argument('issueTitle', type=str,default="./knowledgeMap/templates/index.html", help='新增issue题目')
    parser.add_argument('issueNum', type=int,default=1, help='新增issue号码')
    parser.add_argument('keyword', type=str, default="llm", help='关键字')

    args = parser.parse_args()

    # 调用函数并传递命令行参数
    add_line_to_html(args.htmlPath, args.issueTitle, args.issueNum, args.keyword)

if __name__ == "__main__":
    main()
