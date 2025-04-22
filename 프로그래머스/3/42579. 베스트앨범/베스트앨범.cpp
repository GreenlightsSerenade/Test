#include <string>
#include <vector>
#include <map>
#include <tuple>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare1 (const pair<string, int> &a, const pair<string, int> &b) {
    return a.second > b.second;
}

bool compare2 (const pair<int, int> &a, const pair<int, int> &b) {
    if (a.first == b.first)
        return a.second < b.second;
    return a.first > b.first;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    map<string, int> recap;
    map<string, vector<pair<int, int>>> decap;
    int length = genres.size();
    for (int i = 0; i < length; ++i) {
        recap[genres[i]] += plays[i];
        decap[genres[i]].push_back(make_pair(plays[i], i));
    }
    vector<pair<string, int>> recap_s;
    for (auto it: recap) {
        recap_s.push_back(make_pair(it.first, it.second));
    }
    sort(recap_s.begin(), recap_s.end(), compare1);
    for (auto it: recap_s) {
        vector<pair<int, int>> tmp;
        for (auto it2: decap[it.first]) {
            tmp.push_back(make_pair(it2.first, it2.second));
        }
        sort(tmp.begin(), tmp.end(), compare2);
        int n = tmp.size();
        for (int i = 0; (i < n) && (i < 2); ++i) {
            answer.push_back(tmp[i].second);
        }
    }
    return answer;
}