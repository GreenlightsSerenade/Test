#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 1;
    queue<int> trucks;
    queue<int> bridge;
    for (int i =0;i<truck_weights.size();++i)
        trucks.push(truck_weights[i]);
    bridge.push(trucks.front());
    int now_weight = trucks.front();
    trucks.pop();
    while (!trucks.empty() && !bridge.empty()) {
        if (bridge.size() == bridge_length) {
            now_weight -= bridge.front();
            bridge.pop();
        }
        if (now_weight + trucks.front() <= weight) {
            now_weight += trucks.front();
            bridge.push(trucks.front());
            trucks.pop();
        }
        else {
            bridge.push(0);
        }
        answer += 1;
    }
    return answer + bridge_length;
}