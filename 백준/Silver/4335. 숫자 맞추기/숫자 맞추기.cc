#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<int> num(11, 0);
    while (true) {
        int n;
        cin >> n;
        if (n == 0)
            break;
        
        string a, b;
        cin >> a >> b;

        if (b == "high") {
            for (int i = n; i < 11; ++i)
                num[i] = 1;
        } else if (b == "low") {
            for (int i = 1; i <= n; ++i)
                num[i] = 1;
        } else {
            if (!num[n])
                cout << "Stan may be honest" << endl;
            else
                cout << "Stan is dishonest" << endl;
            num = vector<int>(11, 0);
        }
    }
    return 0;
}
