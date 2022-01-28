# 對話紀錄

# 讀取檔案
def read_file(filename):
    data = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            data.append(line.strip())
    return data

# 改寫對話紀錄形式
def convert(data, person):
    chat = []
    name = None
    for c in data:
        if c in person:
            name = c
            continue
        if name:
            chat.append(name + ': ' + c)
    return chat

# 寫入檔案
def write_file(filename, data):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for c in data:
            f.write(c + '\n')

# 執行
def main():
    data = read_file('input.txt')
    person = ['Allen', 'Tom']
    chat = convert(data, person)
    write_file('output.txt', chat)

main()