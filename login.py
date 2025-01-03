def solution(id_pw, db):
    answer = 'fail'
    if id_pw in db:
        answer = 'login'
    else:
        for i in db:
            if id_pw[0] in i:
                answer = 'wrong pw'

    print(answer)
    return answer

solution(["meosseugi", "1234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]])