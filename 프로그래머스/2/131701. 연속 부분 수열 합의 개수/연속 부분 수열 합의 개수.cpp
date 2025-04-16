#include <string>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

int solution(vector<int> elements) {
    set<int> s;
    int n =elements.size();
    int answer = 0;
    for (int i = 0; i < n; ++i) {
        int val = elements[i];
        s.insert(val);
        for (int j =1;j<n;++j) {
            val += elements[(i + j) % n];
            s.insert(val);
        }
    }
    return s.size();
}