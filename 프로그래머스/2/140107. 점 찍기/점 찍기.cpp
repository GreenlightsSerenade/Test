#include <string>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

long long solution(int k, int d) {
    long long answer = 0;
    long long n=0,r=0;
    long long a = (long long)d*(long long)d;
    for (int i =0;i<=d;i+=k) {
        r = (long long)i * (long long)i;
        n = sqrt(a-r);
        answer += ((n / (long long)k) + 1);
    }
    return answer;
}