const fs = require("fs");
const [N, ...inputs] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const days = inputs.map((input) => input.split(" ").map(Number));

days.unshift([0, 0]);

const dp = new Array(Number(N) + 1).fill(0);

dp.forEach((value, index) => {
  if (!index) return;

  // 전날까지의 최대 수입 vs 현재 날짜의 최대 수입
  dp[index] = Math.max(dp[index - 1], dp[index]);

  // finishDay = 일을 마친 날
  const finishDay = days[index][0] + index - 1;

  // 일을 N일 안에 마칠 수 없으면 수익 얻을 수 없음
  if (finishDay > N) return;

  // 일을 마친 날의 기존 수익 vs 일을 시작 전날까지의 최대 수입 + 이번 일을 마쳤을 때의 수입
  dp[finishDay] = Math.max(dp[finishDay], dp[index - 1] + days[index][1]);
});

console.log(dp[Number(N)]);
