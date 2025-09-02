class Solution {
    public int lengthOfLastWord(String s) {
        int count = 0;
        
        // Trim any leading or trailing spaces from the string.
        String trimmedString = s.trim();
        
        // Iterate backwards from the end of the trimmed string.
        for (int i = trimmedString.length() - 1; i >= 0; i--) {
            // Check for the character at the current index.
            if (trimmedString.charAt(i) != ' ') {
                count++;
            } else {
                // If a space is found, we've reached the end of the last word.
                break;
            }
        }
        return count;
    }
}