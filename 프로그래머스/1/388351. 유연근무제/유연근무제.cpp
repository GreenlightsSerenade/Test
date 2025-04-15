#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> schedules, vector<vector<int>> timelogs, int startday) {
    int answer = 0;
    int n = schedules.size();
    int lmt = 0;
    bool flag = true;
    
    for (int i = 0; i < n; ++i) {
        flag = true;
        lmt = schedules[i];
        if (lmt % 100 >= 50)
            lmt = (lmt / 100 + 1) * 100 + (lmt % 100 + 10) % 60;
        else
            lmt += 10;
        for (int j = 0; j < 7; ++j) {
            if (((startday + j) % 7 == 6) || ((startday + j) % 7 == 0))
                continue;
            if (lmt < timelogs[i][j]) {
                flag = false;
                break;
            }
        }
        
        if (flag)
            answer++;
    }
    return answer;
}