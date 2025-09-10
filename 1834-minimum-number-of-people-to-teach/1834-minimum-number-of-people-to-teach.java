import java.util.*;
class Solution {
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
        int m = languages.length;

        // Convert languages array to sets for faster lookups
        Set<Integer>[] userLanguages = new Set[m + 1];
        for (int i = 0; i < m; i++) {
            userLanguages[i + 1] = new HashSet<>();
            for (int lang : languages[i]) {
                userLanguages[i + 1].add(lang);
            }
        }

        // Find all pairs of friends who cannot communicate
        List<int[]> cannotCommunicate = new ArrayList<>();
        for (int[] friendship : friendships) {
            int u = friendship[0];
            int v = friendship[1];
            boolean canCommunicate = false;
            for (int lang : userLanguages[u]) {
                if (userLanguages[v].contains(lang)) {
                    canCommunicate = true;
                    break;
                }
            }
            if (!canCommunicate) {
                cannotCommunicate.add(friendship);
            }
        }

        // If all friends can already communicate, return 0
        if (cannotCommunicate.isEmpty()) {
            return 0;
        }

        // Count how many non-communicating users speak each language
        int[] languageCounts = new int[n + 1];
        Set<Integer> usersToTeach = new HashSet<>();

        for (int[] friendship : cannotCommunicate) {
            usersToTeach.add(friendship[0]);
            usersToTeach.add(friendship[1]);
        }

        for (int lang = 1; lang <= n; lang++) {
            for (int user : usersToTeach) {
                if (userLanguages[user].contains(lang)) {
                    languageCounts[lang]++;
                }
            }
        }

        // Find the language that is known by the maximum number of users in the 'usersToTeach' set
        int maxCommonLanguageCount = 0;
        for (int count : languageCounts) {
            maxCommonLanguageCount = Math.max(maxCommonLanguageCount, count);
        }

        // The minimum number of users to teach is the total number of users who need to be taught
        // minus the maximum number of users who already know the chosen language.
        return usersToTeach.size() - maxCommonLanguageCount;
    }
}