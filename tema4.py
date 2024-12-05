purchases = {}

with open('purchase_log.txt',encoding='utf=8') as f:
    for i,string in enumerate(f):
        lines = eval(string)
        user_id,category = lines['user_id'],lines['category']
        purchases[user_id]=category

with open('visit_log.csv',encoding='utf=8') as b:
    with open('finnel.csv', 'w', encoding='utf=8') as d:
        for i2, string2 in enumerate(b):
            user_id2 = string2.split(",")[0]
            if user_id2 in purchases:
                d.write(string2[:-1] + ',' + purchases[user_id2] + '\n')