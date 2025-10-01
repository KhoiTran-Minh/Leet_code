class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int total= numBottles;
        int empty= numBottles;

        while (empty >= numExchange){
            int newfull= empty/numExchange;
            total += newfull;
            empty = empty % numExchange + newfull;
        }

        return total;
    }
}