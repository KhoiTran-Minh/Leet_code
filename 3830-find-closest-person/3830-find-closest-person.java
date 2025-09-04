class Solution {
    public int findClosest(int x, int y, int z) {
        int distance1,distance2;
        if (z>x){
            distance1 = z-x;
        }
        else{
            distance1 = x-z;
        }
        if (z>y){
            distance2 = z-y;
        }
        else{
            distance2= y-z;
        }
        if (distance1<distance2){
            return 1;
        } else{ 
        if (distance1==distance2){return 0;} else {return 2;}
            }

    
    }
}