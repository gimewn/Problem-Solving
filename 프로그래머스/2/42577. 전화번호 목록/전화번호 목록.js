function solution(phone_book) {
    let answer = true;
    phone_book.sort();
    
    phone_book.slice(0, phone_book.length-1).forEach((item, index) => {
        if(item === phone_book[index+1].slice(0, item.length)){
            answer = false;
            return;
        }
    })

    return answer;
}