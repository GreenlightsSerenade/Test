#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int solution(vector<vector<int> > land)
{
    int answer = 0;
    int n = land.size();
    vector<vector<int>> DP(n, vector<int>(4));
    int i = 0;
    for (i = 0;i < 4; ++i)
        DP[0][i] = land[0][i];
    for (i = 1; i < n; ++i) {
        for (int j = 0; j<4;++j) {
            DP[i][j] = max(max(DP[i-1][(j + 1) % 4], DP[i-1][(j + 2) % 4]), DP[i-1][(j + 3) % 4]) + land[i][j];
        }
    }

    return max(max(max(DP[n-1][0], DP[n-1][1]), DP[n-1][2]), DP[n-1][3]);
}