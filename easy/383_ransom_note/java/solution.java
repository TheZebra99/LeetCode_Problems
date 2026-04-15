class Solution {

    public boolean canConstruct(String ransomNote, String magazine) {
        int[] counter = new int[26]; // 26 letters from a to z

        for (char letter : magazine.toCharArray()) {
            counter[letter - 'a']++;  // increment the count for this letter
        }

        for (char letter : ransomNote.toCharArray()) {
            counter[letter - 'a']--;  // use up a letter
            if (counter[letter - 'a'] < 0) {
                return false;  // no letters left
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.canConstruct("aa", "aab"));
        System.out.println(solution.canConstruct("aa", "ab"));
        System.out.println(solution.canConstruct("aab", "baa"));
    }
}
