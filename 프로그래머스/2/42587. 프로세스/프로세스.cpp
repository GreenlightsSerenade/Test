#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(vector<int> priorities, int location) {
    int n = priorities.size();
    queue<int> q;
    priority_queue<int> pq;
    for (int i =0;i <n;++i) {
        q.push(i);
        pq.push(priorities[i]);
    }
    int tmp=0;
    int cnt = 1;
    vector<int> a(n);
    while (!q.empty()) {
        tmp = q.front();
        if (priorities[tmp] == pq.top()) {
            a[tmp] = cnt++;
            q.pop();
            pq.pop();
        }
        else {
            q.push(tmp);
            q.pop();
        }
    }
    return a[location];
}