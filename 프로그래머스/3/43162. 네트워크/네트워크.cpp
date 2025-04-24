#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> flag(n, false);
    for (int i =0; i<n;++i) {
        if (!flag[i]) {
            answer += 1;
            queue<int> q;
            q.push(i);
            flag[i]=true;
            while (!q.empty()) {
                int r = q.front();
                q.pop();
                for (int j =0; j<n;++j) {
                    if(computers[r][j] == 1 && (!flag[j])) {
                        q.push(j);
                        flag[j]=true;
                    }
                }
            }
        }
    }
    return answer;
}