class Solution {
    public int Sum(int num1, int num2) {
        return num1 + num2;
    }
}

class Program {
    static void Main(string[] args) {
        Solution test = new Solution();
        Console.WriteLine(test.Sum(15, 20));
    }
}