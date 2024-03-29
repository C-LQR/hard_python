import random
import time

#产生一个4位数字
def generate_ansewr():
    # return random.randint(1000,9999)
    return 9527

def make_guess():
    return input('请输入猜测:')


#返回一个2A2B这样的字符串，有可能抛出异常
def check_guess(answer,guess):
    guess = int(guess)
    a_num = check_guess_A(answer,guess)
    b_num = check_guess_B(answer,guess)
    result = f'{a_num}A{b_num}B'
    return result

#返回数字和位置都正确的个数
#例如9527，9572返回2A2B
def check_guess_A(answer,guess):
    count = 0
    answer_str = str(answer)
    guess_str = str(guess)
    for index,char in enumerate(answer_str):
        if (guess_str[index] == char):
            count +=1
    return count


#数字和位置都正确是A
#数字正确但位置不对算B，不过只能和不是A的位置相比
# 例如：5923，9527应该返回2  
def check_guess_B(answer,guess):
    count = 0
    answer_str = str(answer)
    guess_str = str(guess)
    a_indexes = [] #保存A的下标
    for index,char in enumerate(answer_str):
        if (guess_str[index] == char):
            a_indexes.append(index)

    for char in guess_str:
        if (char in answer_str):
            index2 = answer_str.index(char)
            if(index2 not in a_indexes):
                count +=1
    return count


    

#如果赢了返回True，否则返回False
def process_result(guess_count, guess, result):
    print(guess_count, guess, result)
    if(result == '4A0B'):
        print('Yeah! You win!')
        return True
    return False
    

def show_scores(scores):
    print('==========================')
    print('轮次'.ljust(5),'猜测次数'.ljust(8),'用时'.ljust(5))
    for sc in scores:
        cycle = str(sc[0]).ljust(7)
        guess = str(sc[1]).ljust(12)
        used_time = str(sc[2]).ljust(5)
        print(cycle, guess, used_time)
    print('==========================')
    
def should_continue():
    con = input('要继续玩吗?继续请输入y或者Y,否则任意键推出:')
    if(con == 'y' or con == 'Y'):
        return True
    else:
        print('再见了,886')
        return False

#自动化测试
if (__name__ == '__main__'):
    print('testing')
    assert(check_guess_A(9527,9572) == 2) #断言
    assert(check_guess_A(9527,9522) == 3) #断言
    assert(check_guess_A(9527,9527) == 4) #断言
    assert(check_guess_A(9527,9342) == 1) #断言
    assert(check_guess_B(9527,5923) == 2) #断言
    assert(check_guess_B(9527,5972) == 4) #断言
    assert(check_guess_B(9527,9522) == 0) #断言


