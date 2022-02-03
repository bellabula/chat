# LINE 對話紀錄3

# 讀取檔案
def read_file(filename):
    data = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            data.append(line.strip())
    return data


# 改寫對話紀錄形式
def chat_split(data):
    chat = []
    for c in data:
        s = c.split(' ', 1)
        time = s[0][:5]
        name = s[0][5:]
        message = s[1]
        chat.append(name + ': ' + message)
    return chat

# 執行
def main():
    data = read_file('chat3.txt')
    chat = chat_split(data)
    print(chat)

main()