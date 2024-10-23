#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int H, X, Y;
        cin >> H >> X >> Y;
        
        if (Y >= H) {
            cout << 1 << endl;
        } else {
            int remaining_health = H - Y;
            int normal_attacks = (remaining_health + X - 1) / X;
            cout << 1 + normal_attacks << endl;
        }
    }

    return 0;
}


