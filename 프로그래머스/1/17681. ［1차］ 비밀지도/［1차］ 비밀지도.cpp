#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    vector<int> arr3(n);
    vector<string> added = {" ", "#"};
    for (int i = 0; i < n; ++i) {
        arr3[i] = arr1[i] | arr2[i];
        string temp = "";
        for (int j = 0; j < n; ++j) {
            temp = added[arr3[i] % 2] + temp;
            arr3[i] /= 2;
        }
        answer.push_back(temp);
    }
    
    return answer;
}