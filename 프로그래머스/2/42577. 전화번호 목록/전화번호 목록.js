function solution(phone_book) {
    let answer = true;
    const sortedPhoneBook = phone_book.sort();
    
    sortedPhoneBook.slice(0, sortedPhoneBook.length-1).forEach((item, index) => {
        if(item === sortedPhoneBook[index+1].slice(0, item.length)){
            answer = false;
            return;
        }
    })

    return answer;
}