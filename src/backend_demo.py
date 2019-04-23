import time

header = "<span style=\" font-face:; font-size:24pt; font-weight:600; color:#ff0000;\" >"
tail = "</span>"


def build_tree():
    print("build tree")
    time.sleep(3)
    return "Trie Tree generated"

demo = "This is a demo for trie tree."

def check_error(txt_data):
    str = txt_data.split(" ")
    error_marker = True
    recommendation = ""
    error_list = detector(str)
    if not error_list:
        error_marker = False
    for error in error_list:
        recommendation +=get_recom(str[error])
        str[error] = redMark(str[error])

    s = ' '
    marked_txt = s.join(str)

    return error_marker, marked_txt, recommendation

def detector(str):
    error_list = [4,5,16,35,50,72]
    return error_list

def redMark(str):
    return header + str + tail

def get_recom(str_error):
    #find 5 nearest recommendation through trietree
    recom_5 = ['recom1', 'recom2', 'recom3', 'recom4', 'recom5']
    s_tmp = ','
    tmp_2 = str_error +":    " +s_tmp.join(recom_5)+'\n'
    return tmp_2
