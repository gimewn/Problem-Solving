function solution(id_list, report, k) {
    var answer = [];
    let reported = {};
    let get_mail = {};
    
    /* 메일 받을 횟수를 객체로 생성 */
    id_list.map((user) => get_mail[user] = 0);
    
    /* 중복 신고 제거 */
    let set_report = [...new Set(report)];
    
    set_report.map((item) => {
    let [user, user_report] = [...item.split(" ")]
    /* user별로 신고 당한 횟수 카운트 */
    reported[user_report] ? reported[user_report].push(user) :
    reported[user_report] = [user];
    })
    
    /* 신고 당한 횟수가 k 이상이면 신고한 유저들의 메일 갯수 +1 */
    for(let user in reported){
        if(reported[user].length >= k){
            reported[user].map((who) => get_mail[who]++);
        }
    }
    
    /* 유저별로 받는 메일 갯수 오브젝트의 value를 배열로 변환 */
    answer = Object.values(get_mail);
    
    return answer;
}