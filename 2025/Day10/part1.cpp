#include <fstream>
#include <iostream>
#include <ranges>
#include <vector>
#include <string>
using namespace std;


vector<string> split(const std::string &s, const string &delimiter) {
    vector<string> result;
    size_t start = 0;
    size_t pos;
    if (delimiter.empty()) {
        while (start < s.size()) {
            auto sub = s.substr(start, 1);
            result.push_back(sub);
            start++;
        }
        return result;
    }
    while ((pos = s.find(delimiter, start)) != string::npos) {
        result.push_back(s.substr(start, pos - start));
        start = pos + delimiter.length();
    }
    result.push_back(s.substr(start));
    return result;
}


void combineUtil(vector<vector<int> > &res, vector<int> &temp, int n, int start, int k) {
    if (k == 0) {
        res.push_back(temp);
        return;
    }

    for (int i = start; i <= n; ++i) {
        temp.push_back(i);
        combineUtil(res, temp, n, i + 1, k - 1);
        temp.pop_back();
    }
}

vector<vector<int> > getCombinations(int n, int k) {
    vector<vector<int> > res;
    vector<int> temp;
    combineUtil(res, temp, n, 1, k);
    return res;
}


void applyButton(vector<bool> &lights, const vector<int> &button) {
    for (auto light: button) {
        lights[light] = !lights[light];
    }
}

bool testSequence(vector<bool> &lights, const vector<bool> &goal, const vector<vector<int> > &buttons,
                  const vector<int> sequence) {
    for (auto x: sequence) {
        applyButton(lights, buttons.at(x - 1));
    }

    for (auto i = 0; i < goal.size(); i++) {
        if (goal.at(i) != lights.at(i)) {
            return false;
        }
    }
    return true;
}

int bruteForce(vector<bool> &lights, const vector<bool> &goal, const vector<vector<int> > &buttons) {
    int sequenceLength = 1;
    while (sequenceLength < 10) {
        for (const auto seq: getCombinations(buttons.size(), sequenceLength)) {
            if (testSequence(lights, goal, buttons, seq)) {
                return seq.size();
            }
            lights = vector(lights.size(), false);
        }

        sequenceLength++;
    }
}


int main() {
    ifstream file("input.txt");
    string line;
    vector<std::string> lines;

    while (std::getline(file, line)) { lines.push_back(line); }
    auto sum = 0;
    for (const string &line: lines) {
        vector<bool> lights = {};
        auto parts = split(line, " ");
        vector<bool> goal = {};

        for (const string &l: split(parts.at(0), "")) {
            if (l.compare(0, l.length(), "]") == 0 || l.compare(0, l.length(), "[") == 0) { continue; }
            bool on = l.compare(0, l.length(), "#") == 0;
            goal.push_back(on);
            lights.push_back(false);
        }

        vector<vector<int> > buttons = {};
        auto i = 0;
        for (const string &buttonStr: parts) {
            if (i == 0 || i == parts.size() - 1) {
                i++;
                continue;
            }

            vector<int> buttonLights;
            for (auto light: split(buttonStr, ",")) {
                if (light.starts_with('(')) {
                    light.erase(0, 1);
                }
                buttonLights.push_back(stoi(light));
            }

            buttons.push_back(buttonLights);

            i++;
        }

        auto x = bruteForce(lights, goal, buttons);
        //cout << x << endl;
        sum += x;
    }
    cout << sum << endl;
    return 0;
}
