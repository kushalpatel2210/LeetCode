// My Own Solution 
// class Solution {
//     public boolean canPlaceFlowers(int[] flowerbed, int n) {
//         int[] bedOfFlowers = flowerbed;
//         int flowerbedLength = flowerbed.length;
//         int i = 0;
        
//         // Default case 
//         if (n == 0) {
//             return true;
//         }

//         // Single element case 
//         if (flowerbedLength == 1) {
//             if (bedOfFlowers[0] == 0 && n == 1) {
//                 return true;
//             } else {
//                 return false;
//             }
//         } 

//         for (int flower: flowerbed) {
//             if (n == 0) {
//                 return true;
//             }

//             if (i == 0) {
//                 // First element
//                 if (flower == 0 && bedOfFlowers[i +1] == 0) {
//                     bedOfFlowers[i] = 1; 
//                     n--; 
//                 }
//             } else if (i == flowerbedLength - 1) {
//                 // Last element
//                 if (flower == 0 && bedOfFlowers[i - 1] == 0) {
//                     bedOfFlowers[i] = 1; 
//                     n--; 
//                 }
//             } else {
//                 // Else case
//                 if (flower == 0 && bedOfFlowers[i +1] == 0 && bedOfFlowers[i - 1] == 0) {
//                     bedOfFlowers[i] = 1; 
//                     n--;
//                 }
//             }
            
//             i++;
//         }

//         if (n == 0) {
//             return true;
//         }
//         return false;
//     }
// }

// More Clean Solution 
public class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        for (int i = 0; i < flowerbed.length; i++) {
            // Check if the current plot is empty.
            if (flowerbed[i] == 0) {
                // Check if the left and right plots are empty.
                boolean emptyLeftPlot = (i == 0) || (flowerbed[i - 1] == 0);
                boolean emptyRightPlot = (i == flowerbed.length - 1) || (flowerbed[i + 1] == 0);
                
                // If both plots are empty, we can plant a flower here.
                if (emptyLeftPlot && emptyRightPlot) {
                    flowerbed[i] = 1;
                    count++;
                }
            }
        }
        return count >= n;
    }
}