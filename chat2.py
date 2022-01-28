# LINE 對話紀錄

# 讀取檔案
def read_file(filename):
    data = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            data.append(line.strip())
    return data

# 改寫對話紀錄形式
def caht_split(data):
    chat = []
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for c in data:
        s = c.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
        chat.append(name + ': ' + ' '.join(s[2:]))
    return chat, allen_word_count, allen_sticker_count, allen_image_count, viki_word_count, viki_sticker_count, viki_image_count

# 寫入檔案
def write_file(filename, data):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for c in data:
            f.write(c + '\n')

# 執行
def main():
    data = read_file('LINE-Viki.txt')
    chat, allen_word_count, allen_sticker_count, allen_image_count, viki_word_count, viki_sticker_count, viki_image_count = caht_split(data)
    print('allen 說了', allen_word_count, '個字，傳了', allen_sticker_count, '個貼圖', allen_image_count, '張圖片')
    print('viki 說了', viki_word_count, '個字，傳了', viki_sticker_count, '個貼圖', viki_image_count, '張圖片')
    write_file('LINE-output.txt', chat)

main()