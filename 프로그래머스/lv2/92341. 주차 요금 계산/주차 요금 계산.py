def solution(fees, records):
    answer = []
    new_records = []
    result = {}
    default_time, default_fee, minute_time, minute_fee = fees
    close_time = 23*60+59
    for rec in records:
        time, num, inOrOut = rec.split(" ")
        hour, minute = map(int, time.split(":"))
        new_records.append([60*hour+minute, num, inOrOut])
    new_records.sort(key=lambda x: x[1])

    index = 0

    while new_records:
        flag = 0
        if len(new_records) >= 2:
            if new_records[1][2] == 'OUT':
                flag = 1
                
        if flag:
            cars_time = new_records[1][0] - new_records[0][0]
        else:
            cars_time = close_time - new_records[0][0]
            
        if new_records[0][1] in result:
            result[new_records[0][1]] += cars_time
        else:
            result[new_records[0][1]] = cars_time

        if flag:
            new_records = new_records[2:]
        else:
            new_records = new_records[1:]

    for car in result:
        if result[car] > default_time:
            result[car] -= default_time
            cars_fee = default_fee + ((result[car]) // minute_time) * minute_fee
            if result[car] % minute_time:
                cars_fee += minute_fee
        else:
            cars_fee = default_fee
        answer.append(cars_fee)
    return answer